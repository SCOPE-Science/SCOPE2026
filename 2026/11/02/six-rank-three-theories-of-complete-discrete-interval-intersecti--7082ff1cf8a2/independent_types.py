"""Independent exhaustive definition-level EF signatures of interval intersection graphs."""
from functools import lru_cache
from hashlib import sha256
import sys

def canonical(obj):
    if isinstance(obj,int):
        return str(obj)
    return '['+','.join(sorted(canonical(v) for v in obj))+']'

def rank_three(n):
    intervals = tuple((l,r) for r in range(1,n+1) for l in range(1,r+1))
    N = len(intervals)
    edges = [[False]*N for _ in range(N)]
    for p,(l,r) in enumerate(intervals):
        for q,(s,t) in enumerate(intervals):
            edges[p][q] = (p!=q and max(l,s)<=min(r,t))

    @lru_cache(maxsize=None)
    def atom(chosen):
        bits=[]
        for p in range(len(chosen)):
            for q in range(p,len(chosen)):
                bits.extend((int(chosen[p] == chosen[q]), int(edges[chosen[p]][chosen[q]])))
        return sum(bit<<i for i,bit in enumerate(bits))

    @lru_cache(maxsize=None)
    def rank_type(chosen,rank):
        if rank==0:
            return atom(chosen)
        return frozenset(rank_type(chosen+(point,),rank-1) for point in range(N))
    signature=rank_type((),3)
    return signature, len(signature)

def main():
    top=int(sys.argv[1]) if len(sys.argv)>1 else 12
    types=[]
    for n in range(1,top+1):
        typ, num=rank_three(n)
        if typ not in types:types.append(typ)
        hexdigest=sha256(canonical(typ).encode()).hexdigest()[:20]
        print(f'n={n} rank3_class={types.index(typ)+1} singleton_types={num} digest={hexdigest}',flush=True)
    print('classes',len(types))
if __name__=='__main__':main()
