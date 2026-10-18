"""Finite necessary checks for ternary face-step circulants, using only stdlib.
These checks supplement, and do not replace, the all-parameter proof.
"""
from itertools import combinations, product, permutations
from collections import defaultdict
from math import factorial

def sign(p): return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
def det(a):
    n=len(a)
    if n==1:return a[0][0]
    return sum((-1)**j*a[0][j]*det([r[:j]+r[j+1:] for r in a[1:]]) for j in range(n))
def run(d,maxfaces):
    L={frozenset()} | {frozenset(c) for F in maxfaces for k in range(1,len(F)+1) for c in combinations(F,k)}
    assert all(frozenset((i,)) in L for i in range(d))
    weights={F:sum(3**i for i in F) for F in L};S=tuple(sorted(weights[F] for F in L if F))
    vectors={weights[F]:tuple(int(i in F) for i in range(d)) for F in L}
    assert len(set(S))==len(S)
    n=2*max(S)+1
    # Every two-term sum has the same integer equality pattern as vector addition.
    pairs=[(0,0)]+[(0,a) for a in S]+[(a,b) for a in S for b in S]
    reps={}
    for a,b in pairs:
        s=a+b;v=tuple(vectors[a][i]+vectors[b][i] for i in range(d))
        if s in reps: assert reps[s]==v
        reps[s]=v
    assert max(reps)<n
    # Each characteristic step reduces under any one-coordinate clamp to a face step or zero.
    for i in range(d):
        for x in product(range(-2,3),repeat=d):
            for k in range(-1,3):
                for s in S:
                    v=vectors[s]
                    y=tuple(x[j]+v[j] for j in range(d))
                    xx=list(x);yy=list(y);xx[i]=max(xx[i],k);yy[i]=max(yy[i],k)
                    delta=tuple(yy[j]-xx[j] for j in range(d))
                    assert delta in vectors.values()
    # A top-dimensional translational alternating integral cycle.
    base=tuple(3**i for i in range(d)); bd=defaultdict(int)
    for a in range(n):
        for perm in permutations(range(d)):
            steps=tuple(base[i] for i in perm);vert=[a]
            for s in steps:vert.append((vert[-1]+s)%n)
            for j in range(d+1):bd[tuple(vert[:j]+vert[j+1:])]+=(-1)**j*sign(perm)
    assert not any(bd.values())
    # Explicit determinant cocycle on all elementary (d+1)-paths (on the full regular path algebra).
    def phi(ss):return det([[reps[s][i] for s in ss] for i in range(d)])
    for ss in product(S,repeat=d+1):
        val=phi(ss[1:])+(-1)**(d+1)*phi(ss[:-1])
        for j in range(d): val+=(-1)**(j+1)*phi(ss[:j]+(ss[j]+ss[j+1],)+ss[j+2:])
        assert val==0
    pairing=n*sum(sign(p)*phi(tuple(base[j] for j in p)) for p in permutations(range(d)))
    assert pairing==n*factorial(d)
    return f'd={d} facets={sorted(tuple(sorted(F)) for F in maxfaces)} n={n} generators={S} pair-sum-types={len(reps)} clamp-and-cocycle-check=PASS cycle-boundary=zero pairing={pairing}'

if __name__=='__main__':
    print(run(3,[{0,1},{1,2}]))
    print(run(3,[{0,1,2}]))
    print(run(4,[{0,1},{1,2},{2,3}]))
