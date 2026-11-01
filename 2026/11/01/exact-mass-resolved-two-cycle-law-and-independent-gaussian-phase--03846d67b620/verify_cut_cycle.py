#!/usr/bin/env python3
"""Independent exact checks for primitive period-two parallel chip-firing states.

Usage: python verify_cut_cycle.py
Only Python standard-library modules are required.
"""
from collections import Counter
from itertools import product
from math import comb, exp, lgamma, log, sqrt


def graph_poly(adj):
    """Cut formula; coefficients count unoriented period-two state-pairs."""
    n=len(adj)
    degrees=[len(x) for x in adj]
    edges=sum(degrees)//2
    total=Counter()
    for mask in range(1, (1<<n)-1):
        cross=[sum(((mask>>u)&1)!=((mask>>v)&1) for u in adj[v]) for v in range(n)]
        if 0 in cross: continue
        cut=sum(cross)//2
        weights=Counter({2*edges-cut:1})
        for c in cross:
            nxt=Counter()
            for a,va in weights.items():
                for i in range(c):
                    nxt[a+i]+=va
            weights=nxt
        total.update(weights)
    assert all(v%2==0 for v in total.values())
    return Counter({k:v//2 for k,v in total.items()})


def brute_poly(adj):
    n=len(adj)
    degrees=[len(x) for x in adj]
    # This finite box contains EVERY period-two state by the cut lemma.
    boxes=[range(2*d) for d in degrees]
    answer=Counter()
    def step(x):
        fires=tuple(int(x[i]>=degrees[i]) for i in range(n))
        return tuple(x[i]-degrees[i]*fires[i]+sum(fires[j] for j in adj[i]) for i in range(n))
    attempts=0
    for x in product(*boxes):
        y=step(x)
        if y != x and step(y)==x:
            assert all(a>=0 for a in y)
            answer[sum(x)]+=1
        attempts+=1
    assert all(v%2==0 for v in answer.values())
    return Counter({k:v//2 for k,v in answer.items()}),attempts


def clique(n):
    return [tuple(j for j in range(n) if j!=i) for i in range(n)]


def clique_poly(n):
    answer=Counter()
    for a in range(1,n):
        poly=Counter({n*(n-1)-a*(n-a):comb(n,a)})
        for width,multiplicity in ((n-a,a),(a,n-a)):
            for _ in range(multiplicity):
                nxt=Counter()
                for power,coefficient in poly.items():
                    for j in range(width):
                        nxt[power+j]+=coefficient
                poly=nxt
        answer.update(poly)
    assert all(v%2==0 for v in answer.values())
    return Counter({m:c//2 for m,c in answer.items()})

# Exhaustively test every connected simple graph on 2..4 labelled vertices.
tests=0
for n in range(2,5):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    for bits in range(1,1<<len(pairs)):
        adj=[set() for _ in range(n)]
        for b,(i,j) in enumerate(pairs):
            if bits>>b&1:adj[i].add(j);adj[j].add(i)
        reached={0}
        for _ in range(n): reached |= {j for i in tuple(reached) for j in adj[i]}
        if len(reached)!=n: continue
        predicted=graph_poly(adj)
        observed,attempts=brute_poly(adj)
        assert observed==predicted,(n,bits,predicted,observed)
        tests+=attempts
print('ALL_CONNECTED_GRAPHS_N_2_TO_4_OK',tests)

# Exhaustive larger natural graphs, including complete graphs.
for n in range(2,7):
    g=clique(n)
    observed,attempts=brute_poly(g)
    predicted=clique_poly(n)
    assert observed==predicted==graph_poly(g),(n,observed,predicted)
    total=sum(predicted.values())
    direct=sum(comb(n,a)*a**(n-a)*(n-a)**a for a in range(1,n))//2
    assert total==direct
    exponent=n*(2*n-3)
    assert all(predicted.get(m,0)==predicted.get(exponent-m,0) for m in predicted)
    assert sum(m*v for m,v in predicted.items())*2 == total*n*(2*n-3)
    print('CLIQUE',n,'attempts',attempts,'orbits',total,'polynomial',sorted(predicted.items()) if n<=4 else 'hash-free exact coefficients checked')

# All small paths and cycles independently, where the graph admits some period-two states.
for n in range(3,9):
    g=[set() for _ in range(n)]
    for i in range(n-1):g[i].add(i+1);g[i+1].add(i)
    observed,attempts=brute_poly(g)
    assert observed==graph_poly(g)
    g[0].add(n-1);g[-1].add(0)
    observed2,attempts2=brute_poly(g)
    assert observed2==graph_poly(g)
    print('PATH_CYCLE',n,'tests',attempts+attempts2)

# Laplace asymptotic numerical diagnostics (not a proof).
for n in (40,160,640):
    lws=[lgamma(n+1)-lgamma(a+1)-lgamma(n-a+1)+a*log(n-a)+(n-a)*log(a) for a in range(1,n)]
    hi=max(lws)
    vals=[exp(x-hi) for x in lws]
    denom=sum(vals)
    varA=sum((a-n/2)**2*vals[a-1] for a in range(1,n))/denom
    mvar=sum((n*(a*(n-a)-1)/12)*vals[a-1] for a in range(1,n))/denom
    print('ASYMPTOTIC_DIAGNOSTIC',n,'varianceA_over_n',varA/n,'varianceM_over_n3',mvar/n**3,
          'scaled_total',exp(hi-n*log(n))*denom)
print('GRAPH_CUT_TWO_CYCLE_VERIFY_OK')
