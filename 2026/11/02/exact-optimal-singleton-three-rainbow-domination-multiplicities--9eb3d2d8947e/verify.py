"""Exact finite checks for singleton three-rainbow minima of Möbius ladders.

The universal theorem relies on a combinatorial triangle-chain proof, not
on this bounded enumeration. Requires only the Python standard library.
"""
from collections import Counter
from itertools import product


def neighbors(n):
    m=n//2
    return [((v-1)%n,(v+1)%n,(v+m)%n) for v in range(n)]


def min_weight(n):
    m=n//2
    if m%2==0:return m+1
    if m%3==0:return m
    return m+2


def claimed_count(n):
    r=n%12
    if r==6:return 12
    if r in (0,4,8):return 6*n
    if r==2:return 9*n*(3*n-2)//2
    if r==10:return 9*n*(3*n-10)//2
    raise ValueError(n)


def zero_sets(n,size):
    # Exhaustive selection among graph-independent zero supports.
    m=n//2
    def dfs(i,selected):
        if len(selected)>size or len(selected)+n-i<size:return
        if i==n:
            if len(selected)==size:
                S=set(selected)
                if all((v+m)%n not in S for v in S):yield frozenset(S)
            return
        yield from dfs(i+1,selected)
        if selected and selected[-1]==i-1:return
        if i==n-1 and 0 in selected:return
        if i>=m and i-m in selected:return
        selected.append(i)
        yield from dfs(i+1,selected)
        selected.pop()
    yield from dfs(0,[])


def coloring_count(n,zeros):
    # Independent exact graph-coloring solver for the pairwise inequalities
    # implied by all three-neighbor-zero constraints.
    C=[v for v in range(n) if v not in zeros]
    ix={v:i for i,v in enumerate(C)}
    adj=[set() for _ in C]
    for v in zeros:
        xs=[ix[u] for u in neighbors(n)[v]]
        for a in xs:
            for b in xs:
                if a!=b:adj[a].add(b)
    colors=[-1]*len(C)
    colors[0]=0
    def rec(uncolored):
        if not uncolored:return 1
        choices=[]
        for v in uncolored:
            used={colors[u] for u in adj[v] if colors[u]>=0}
            available=tuple(c for c in range(3) if c not in used)
            choices.append((len(available),-len(adj[v]),v,available))
        count,_,v,options=min(choices)
        if count==0:return 0
        out=0
        for c in options:
            colors[v]=c
            out+=rec(uncolored-{v})
            colors[v]=-1
        return out
    return 3*rec(set(range(1,len(C))))


def direct_small(n):
    adj=neighbors(n); k=min_weight(n); ans=0
    for vals in product((0,1,2,3),repeat=n):
        if sum(v!=0 for v in vals)!=k:continue
        if all(vals[v]!=0 or {vals[u] for u in adj[v]}=={1,2,3}
               for v in range(n)):
            ans+=1
    return ans


def test():
    assert direct_small(6)==12
    assert direct_small(8)==48
    assert direct_small(10)==900
    tests=0
    for n in range(6,43,2):
        zeros=n-min_weight(n)
        total=0
        for S in zero_sets(n,zeros):
            total+=coloring_count(n,S)
        assert total==claimed_count(n),(n,total,claimed_count(n))
        tests+=1
    print('VERIFY_OK direct_labelings_n=6,8,10 all_minimum_counts_n=6..42_even cases='+str(tests))

if __name__=='__main__':test()
