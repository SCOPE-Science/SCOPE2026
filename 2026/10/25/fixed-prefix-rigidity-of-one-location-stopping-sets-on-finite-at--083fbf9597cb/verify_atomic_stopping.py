"""Exhaustive finite Boolean and ternary checks of one-location stopping sets."""
from itertools import product, combinations, permutations
from math import factorial

def count_exact(n, alphabet=(0,1)):
    states = list(product(alphabet, repeat=n))
    total = len(states)
    candidates=[]
    for mask in range(1<<n):
        idx=[i for i in range(n) if mask>>i & 1]
        for vals in product(alphabet, repeat=len(idx)):
            if sum(v>0 for v in vals)>1: continue
            cells=0
            for k,state in enumerate(states):
                if all(state[i]==v for i,v in zip(idx,vals)):
                    cells |= 1<<k
            candidates.append((mask,cells))
    bystate=[[] for _ in states]
    for i,(_,cells) in enumerate(candidates):
        for s in range(total):
            if cells>>s & 1: bystate[s].append(i)
    allcells=(1<<total)-1
    maps=set()
    cur=[0]*total
    def rec(filled):
        if filled==allcells:
            maps.add(tuple(cur));return
        s=next(k for k in range(total) if not(filled>>k & 1))
        for i in bystate[s]:
            mask,cells=candidates[i]
            if cells & filled:continue
            for k in range(total):
                if cells>>k & 1:cur[k]=mask
            rec(filled|cells)
    rec(0)
    def prefix_map(p):
        out=[]
        for state in states:
            subset=0
            for i in p:
                subset|=1<<i
                if state[i]>0:break
            out.append(subset)
        return tuple(out)
    prefix={prefix_map(p) for r in range(n+1) for p in permutations(range(n),r)}
    assert maps==prefix,(n,len(maps),len(prefix),len(maps-prefix),len(prefix-maps))
    return len(maps),sum(factorial(n)//factorial(n-r) for r in range(n+1)),len(candidates)

if __name__=='__main__':
    for n,alph in [(0,(0,1)),(1,(0,1)),(2,(0,1)),(3,(0,1)),(4,(0,1)),(1,(0,1,2)),(2,(0,1,2)),(3,(0,1,2))]:
        print(n,alph,count_exact(n,alph),flush=True)
