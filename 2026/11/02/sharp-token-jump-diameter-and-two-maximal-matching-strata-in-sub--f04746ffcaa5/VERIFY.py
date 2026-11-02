#!/usr/bin/env python3
"""Direct finite checks for the maximal-matching reconfiguration theorem.

The test constructs S(K_n) as a bipartite graph, enumerates matchings
using independent incidence choices, tests the original maximality
predicate, and rebuilds token-jumping adjacency on graph edges.
No theorem about arbitrary n is inferred from these finite tests.
"""
from collections import Counter, deque
from itertools import combinations, product
from math import factorial
from random import Random


def coefficient(n):
    return sum((-1)**k * factorial(n) //
               (factorial(n - 2*k)*2**k*factorial(k)) *
               (n-1)**(n-2*k) for k in range(n//2 + 1))


def original_graph(n):
    pairs=list(combinations(range(n),2))
    edges={(v,n+q) for q,p in enumerate(pairs) for v in p}
    incidents=[[n+q for q,p in enumerate(pairs) if i in p] for i in range(n)]
    return edges,incidents


def independently_enumerated_maximal_matchings(n):
    edges,incident=original_graph(n)
    answer=[]
    for choices in product(*[[None]+x for x in incident]):
        occupied=[x for x in choices if x is not None]
        if len(occupied)!=len(set(occupied)):
            continue
        M=frozenset((i,x) for i,x in enumerate(choices) if x is not None)
        used_left={i for i,_ in M}
        used_right={x for _,x in M}
        # Original characterization, without using the structural theorem:
        maximal=all((i in used_left or x in used_right) for i,x in edges)
        if maximal:
            answer.append(M)
    return answer


def neighbors(M,edges):
    out=set()
    for drop in M:
        base=M-{drop}
        ul={i for i,_ in base}
        ur={j for _,j in base}
        for add in edges-base:
            if add[0] not in ul and add[1] not in ur and add!=drop:
                out.add(frozenset(base | {add}))
    return out


def eccentricity(source, adj):
    dis={source:0}
    q=deque([source])
    while q:
        m=q.popleft()
        for t in adj[m]:
            if t not in dis:
                dis[t]=dis[m]+1
                q.append(t)
    return max(dis.values()),len(dis)


def retarget(f, g):
    """Construct a legal route between two no-1/no-2-cycle functions."""
    n=len(f)
    cur=list(f)
    edits=[]

    def change(i,j):
        assert i!=j and cur[j]!=i and cur[i]!=j
        cur[i]=j
        edits.append((i,j))
        assert all(cur[cur[x]]!=x for x in range(n))

    while tuple(cur)!=tuple(g):
        wrong=[i for i in range(n) if cur[i]!=g[i]]
        available=next((i for i in wrong if cur[g[i]]!=i),None)
        if available is not None:
            change(available,g[available])
            continue
        # All desired changes are blocked.  The wrong indices split into
        # cycles of g, and cur is g-inverse on those indices.
        wset=set(wrong)
        assert {g[i] for i in wrong}==wset
        assert all(cur[g[i]]==i for i in wrong)
        i=wrong[0]
        cycle=[i]
        while g[cycle[-1]]!=i:
            cycle.append(g[cycle[-1]])
        assert len(cycle)>=3
        assert all(x in wset for x in cycle)
        # Choose a movable j on the cycle, with free replacement k.
        j=next(j for j in cycle if sum(cur[x]==j for x in range(n))<=n-3)
        k=next(k for k in range(n) if k!=j and k!=cur[j] and cur[k]!=j)
        pred={g[t]:t for t in cycle}
        change(j,k)
        t=pred[j]
        for _ in range(len(cycle)):
            change(t,g[t])
            t=pred[t]
        assert t==pred[j]
        assert all(cur[x]==g[x] for x in cycle)
    assert len(edits)<=n+n//3
    return len(edits)


def main():
    total=0
    for n in range(3,7):
        edges,_=original_graph(n)
        allM=independently_enumerated_maximal_matchings(n)
        lower={M for M in allM if len(M)==n-1}
        upper={M for M in allM if len(M)==n}
        assert len(allM)==len(set(allM))
        assert len(allM)==len(lower)+len(upper)
        assert len(lower)==n and len(upper)==coefficient(n)
        assert all(len(M) in [n-1,n] for M in allM)
        eligible=set(allM)
        adj={M:(neighbors(M,edges) & eligible) for M in allM}
        assert all(N in adj and M in adj[N] for M,ns in adj.items() for N in ns)
        assert all(not adj[M] for M in lower)
        assert all(len(adj[M])==n*(n-3) for M in upper)
        upper_edges=sum(len(adj[M]) for M in upper)//2
        assert upper_edges==len(upper)*n*(n-3)//2
        if n<6:
            dvals=[]
            for M in upper:
                e,seen=eccentricity(M,adj)
                assert seen==(len(upper) if n>=4 else 1)
                dvals.append(e)
            if n>=4:
                assert max(dvals)==n+n//3
            else:
                assert max(dvals)==0
            diameter_text=str(max(dvals))
        else:
            # One nontrivial source independently tested for connectivity
            # and for the sharp lower-bound witness (two reversed 3-cycles).
            target=(1,2,0,4,5,3)
            left={i:n+list(combinations(range(n),2)).index(tuple(sorted((i,j))))
                  for i,j in enumerate(target)}
            sample=frozenset(left.items())
            assert sample in upper
            ecc,seen=eccentricity(sample,adj)
            assert seen==len(upper)
            assert ecc==n+n//3
            diameter_text='sample eccentricity '+str(ecc)
        total+=len(allM)
        print('n=',n,'maximal=',len(allM),'lower=',len(lower),
              'upper=',len(upper),'upper degree=',n*(n-3),
              'upper edges=',upper_edges,'diameter:',diameter_text)
    # Independent constructive algorithm checks every ordered pair for n=4,5,
    # and reproducible sampled pairs at n=6.  Enumeration never substitutes
    # for the general upper/lower bound argument.
    for n in (4,5,6):
        choices=[[j for j in range(n) if i!=j] for i in range(n)]
        states=[v for v in product(*choices) if all(v[v[i]]!=i for i in range(n))]
        if n<=5:
            tested=((a,b) for a in states for b in states)
            number=len(states)**2
        else:
            rng=Random(1729)
            tested=((rng.choice(states),rng.choice(states)) for _ in range(2000))
            number=2000
        max_route=0
        for a,b in tested:
            max_route=max(max_route,retarget(a,b))
        print('constructive route check: n=',n,'ordered pairs=',number,
              'longest constructed route=',max_route,
              'upper bound=',n+n//3)
    print('PASS: tested',total,'distinct inclusion-maximal matchings,',
          'their original edge predicates, and all token-jumping adjacencies')


if __name__=='__main__':
    main()
