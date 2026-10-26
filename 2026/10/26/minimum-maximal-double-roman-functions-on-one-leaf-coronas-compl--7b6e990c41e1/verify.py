"""Reproducible finite checks of maximal double Roman labelings of graph coronas.

Run: python verify.py
"""
from itertools import product,combinations
from math import comb

def edges_for_code(n,code):
    pairs=list(combinations(range(n),2))
    return [(i,j) for k,(i,j) in enumerate(pairs) if code & (1<<k)]

def domination_sets(n,edges):
    nei=[set() for _ in range(n)]
    for i,j in edges: nei[i].add(j);nei[j].add(i)
    ds=[frozenset(D) for r in range(n+1) for D in combinations(range(n),r) if all(v in D or nei[v]&set(D) for v in range(n))]
    gamma=min(map(len,ds))
    mins=[D for D in ds if len(D)==gamma]
    return nei,gamma,mins

def theoretical(n,edges):
    nei,g,ds=domination_sets(n,edges)
    covers=sum(1 for D in ds for bits in product((False,True),repeat=g)
               if all(any(v in nei[u] for v,flag in zip(sorted(D),bits) if flag) for u in range(n) if u not in D))
    return 2*n+g,(2**g-1)*covers,covers,len(ds)

def bruteforce(n,edges):
    adj=[set() for _ in range(2*n)]
    for i,j in edges: adj[i].add(j);adj[j].add(i)
    for i in range(n): adj[i].add(n+i);adj[n+i].add(i)
    upper=theoretical(n,edges)[0]
    mn=None; count=0; explored=0
    for lab in product(range(4), repeat=2*n):
        weight=sum(lab)
        if weight>upper: continue
        explored+=1
        if any((lab[v]==0 and not (any(lab[u]==3 for u in adj[v]) or sum(lab[u]==2 for u in adj[v])>=2)) or
               (lab[v]==1 and not any(lab[u]>=2 for u in adj[v])) for v in range(2*n)):
            continue
        zeros={v for v in range(2*n) if lab[v]==0}
        if all(v in zeros or adj[v]&zeros for v in range(2*n)):
            continue
        if mn is None or weight<mn: mn=weight;count=1
        elif weight==mn: count+=1
    return (mn,count,explored)

def cycle_count(n):
    q=(n+2)//3
    if n%3==0: covered=3
    elif n%3==2: covered=n
    else: covered=n*(n+11)//6
    return 2*n+q, (2**q-1)*covered

def main():
    total=0;explored=0
    for n in range(1,5):
        num=2**comb(n,2)
        for code in range(num):
            E=edges_for_code(n,code)
            target=theoretical(n,E)
            measured=bruteforce(n,E)
            assert measured[:2]==target[:2],(n,code,E,target,measured)
            total+=1; explored+=measured[2]
        print('EXHAUSTIVE_BASE_GRAPH_OK',n,'graphs',num)
    for n,es in [(5,[(i,(i+1)%5) for i in range(5)]),
                 (5,[(i,i+1) for i in range(4)]),
                 (5,[(0,i) for i in range(1,5)]),
                 (5,[]),
                 (5,[(i,j) for i,j in combinations(range(5),2)])]:
        t=theoretical(n,es);b=bruteforce(n,es)
        assert b[:2]==t[:2],(n,es,t,b)
        total+=1;explored+=b[2]
        print('FIVE_VERTEX_OK',es,'weight,count=',t[:2])
    for n in range(3,16):
        E=[(i,(i+1)%n) for i in range(n)]
        t=theoretical(n,E)
        c=cycle_count(n)
        assert t[:2]==c,(n,t,c)
        print('SUNLET_CYCLE_FORMULA_OK',n,c[1])
    print('VERIFICATION_OK base_graphs=',total,'candidate_labelings=',explored)

if __name__=='__main__':main()
