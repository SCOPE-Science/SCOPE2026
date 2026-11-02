#!/usr/bin/env python3
"""Exact independent finite checks for cycle-corona resolving robot theorem.

Every claim for all even circumferences relies on the accompanying proof,
not on finite extrapolation from this test program.
"""
from itertools import combinations
from collections import deque


def graph(n):
    assert n >= 4 and n % 2 == 0
    adj = [set() for _ in range(2*n)]
    for v in range(n):
        for w in ((v+1) % n, v+n):
            adj[v].add(w); adj[w].add(v)
    d = []
    for s in range(2*n):
        ds = [-1]*(2*n); ds[s]=0
        q=deque([s])
        while q:
            v=q.popleft()
            for w in adj[v]:
                if ds[w]<0:
                    ds[w]=ds[v]+1; q.append(w)
        d.append(ds)
    return adj,d


def resolves(d, S):
    n=len(d)
    return len({tuple(d[v][s] for s in S) for v in range(n)}) == n


def gap_ok(n,S):
    ss=sorted(S)
    return all((ss[(j+1)%3]-ss[j])%n <= n//2 for j in range(3))


def labeled_core_reach(n, eligible, start):
    adj,_=graph(n)
    q=deque([start]); seen={start}; visiting=[set() for _ in range(3)]
    while q:
        state=q.popleft()
        for j,x in enumerate(state): visiting[j].add(x)
        for j,v in enumerate(state):
            for w in adj[v]:
                if w>=n or w in state: continue
                t=list(state);t[j]=w;t=tuple(t)
                if t not in seen and frozenset(t) in eligible:
                    seen.add(t);q.append(t)
    return visiting,len(seen)


def main():
    for n in range(4,18,2):
        m=n//2;adj,d=graph(n)
        two=[S for S in combinations(range(2*n),2) if resolves(d,S)]
        assert len(two)==(4 if n==4 else 0),(n,two)
        if n==4:
            assert set(map(frozenset,two)) == {
                frozenset((n+i,n+(i+1)%n)) for i in range(n)
            }
            for S in two:
                for v in S:
                    assert not any(w not in S and resolves(d,tuple((set(S)-{v})|{w})) for w in adj[v])
        eligible={frozenset(S) for S in combinations(range(n),3) if resolves(d,S)}
        expected={frozenset(S) for S in combinations(range(n),3) if gap_ok(n,S)}
        assert eligible==expected,(n,'gap equivalence failed')
        want=m*(m-1)*(m+4)//3
        assert len(eligible)==want,(n,len(eligible),want)
        # Every independently enumerated core triple remains completely mobile:
        # each of its three named robots visits every core vertex using core-only moves.
        for S in eligible:
            visited,_=labeled_core_reach(n,eligible,tuple(sorted(S)))
            assert all(s==set(range(n)) for s in visited),(n,S,visited)
            # The exact pendant detour preserves resolvingness for each robot.
            for v in S:
                replace=tuple((set(S)-{v})|{n+v})
                assert resolves(d,replace),(n,S,v)
        print('EVEN_SUNLET_OK n={} two_resolving={} core_triples={} triple_each_robot_all_core=YES'.format(n,len(two),len(eligible)))
    print('VERIFY_OK complete-mobile lower bound and core-gap classification checks n=4..16')

if __name__=='__main__': main()
