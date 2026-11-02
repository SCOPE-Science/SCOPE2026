"""Independent recursive EF-type calculation on simple undirected graph families."""
from functools import lru_cache
from collections import defaultdict
import sys

def arms(lengths):
    edges=[]; v=1
    for length in lengths:
        parent=0
        for _ in range(length):
            edges.append((parent,v))
            parent=v
            v+=1
    return v,edges

def chain(n):return n,list(zip(range(n-1),range(1,n)))

registry=[{} for _ in range(5)]
def classify_graph(n,edges):
    edge_set={frozenset(pair) for pair in edges}
    def atomic_signature(tup):
        return tuple((tup[i]==tup[j],frozenset((tup[i],tup[j])) in edge_set)
                     for i in range(len(tup)) for j in range(i))
    def intern(rank,key):
        d=registry[rank]
        if key not in d:d[key]=len(d)+1
        return d[key]
    @lru_cache(None)
    def rec(tup,remaining):
        if remaining==0:return intern(0,atomic_signature(tup))
        sig=frozenset(rec(tup+(a,),remaining-1) for a in range(n))
        return intern(remaining,sig)
    return rec((),4)

def main(max_n=22):
    types=defaultdict(list)
    for n in range(1,max_n+1):
        types[classify_graph(*chain(n))].append(f'A{n}')
        if n>=4:types[classify_graph(*arms([1,1,n-3]))].append(f'D{n}')
        if 6<=n<=8:types[classify_graph(*arms([1,2,n-4]))].append(f'E{n}')
    print('INDEPENDENT_PYTHON_CLASSES',len(types))
    for k,v in types.items():print(k,','.join(v))

if __name__=='__main__':main(int(sys.argv[1]) if len(sys.argv)>1 else 22)
