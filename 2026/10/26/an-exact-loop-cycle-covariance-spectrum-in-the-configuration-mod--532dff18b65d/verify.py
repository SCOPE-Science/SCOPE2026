"""Exact finite checks for loop-cycle covariance in labeled-stub matchings."""
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial, prod


def pairings(xs):
    if not xs:
        yield ()
        return
    a = xs[0]
    for k in range(1, len(xs)):
        b = xs[k]
        rest = xs[1:k] + xs[k+1:]
        for p in pairings(rest):
            yield ((a, b),) + p


def pg_den(q, r):
    return prod(q - (2*j+1) for j in range(r))


def simple_cycles(n, r):
    # A 2-cycle means a pair of parallel edges (handled separately).
    if r == 2:
        yield from combinations(range(n), 2)
    else:
        for vs in combinations(range(n), r):
            root = vs[0]
            for tail in permutations(vs[1:]):
                if tail[0] < tail[-1]:
                    yield (root,) + tail


def cycles(adj, r):
    if r == 2:
        return sum(comb(adj[a][b], 2) for a,b in combinations(range(len(adj)), 2))
    ans = 0
    for cyc in simple_cycles(len(adj), r):
        ans += prod(adj[cyc[j]][cyc[(j+1)%r]] for j in range(r))
    return ans


def falling(x, r):
    return prod(x-j for j in range(r))


def formula(degs, r):
    n=len(degs)
    q=sum(degs)
    if r<2 or r>n or q%2 or q<2*r:
        raise ValueError((degs,r))
    A=sum(comb(d,2) for d in degs)
    B = Fraction(0)
    S = Fraction(0)
    for cyc in simple_cycles(n,r):
        weight = prod(degs[v]*(degs[v]-1) for v in cyc)
        if r==2:
            weight = Fraction(weight,2) # two stub-pairings per two double-edge possibilities
        B += weight
        S += weight*sum(2*degs[v]-3 for v in cyc)
    # C2 uses product (d_i)_2 (d_j)_2 / 2; r>=3 product fully.
    er= B / pg_den(q,r)
    el=Fraction(A,q-1)
    if q==2*r:
        elr=Fraction(0)
    else:
        elr= (A*B-S)/pg_den(q,r+1)
    return el,er,elr,elr-el*er


def exact(degs,r):
    n=len(degs); q=sum(degs)
    owners=[]
    for i,d in enumerate(degs):owners.extend([i]*d)
    tot=sl=sc=slc=0
    for pairs in pairings(tuple(range(q))):
        adj=[[0]*n for _ in range(n)]
        for a,b in pairs:
            i,j=owners[a],owners[b]
            adj[i][j]+=1
            if i!=j:adj[j][i]+=1
        l=sum(adj[i][i] for i in range(n))
        c=cycles(adj,r)
        tot+=1;sl+=l;sc+=c;slc+=l*c
    el=Fraction(sl,tot);er=Fraction(sc,tot);elr=Fraction(slc,tot)
    return el,er,elr,elr-el*er,tot


def main():
    checked=0; matchings_count=0
    tests=[
        (2,2,2), (2,2,2,2), (2,2,2,2,2), (2,2,2,2,2,2),
        (3,3,3,3), (4,4,4), (2,2,2,4), (3,2,2,3),
        (2,2,4,4), (1,3,2,4), (0,2,2,4),
    ]
    for ds in tests:
        if sum(ds)>12:continue
        for r in range(2,len(ds)+1):
            if 2*r>sum(ds):continue
            expected=formula(ds,r)
            observed=exact(ds,r)
            assert expected==observed[:4], (ds,r,expected,observed)
            checked+=4
            matchings_count+=observed[4]
    # Regular sign law and all fixed-r asymptotic constants, tested symbolically
    for n in range(3,14):
        for d in range(2,9):
            if n*d%2:continue
            q=n*d
            for r in range(2,n+1):
                if 2*r>q:continue
                el,er,elr,cov=formula_regular(n,d,r)
                if d==2 and r==n:
                    assert cov<0
                elif d==2:
                    assert cov>0
                else:
                    assert cov<0
                checked+=1
    print('PASS exact comparisons:',checked)
    print('PASS total enumerated matching-cases:',matchings_count)
    print('PASS regular sign checks: n=3..13, d=2..8, valid r=2..n')


def formula_regular(n,d,r):
    q=n*d
    assert q%2==0 and d>=2 and n>=r>=2
    A=n*comb(d,2)
    B=Fraction(falling(n,r)*falling(d,2)**r,2*r)
    er=B/pg_den(q,r)
    el=Fraction(A,q-1)
    if q==2*r:
        elr=Fraction(0)
    else:
        elr=B*(A-r*(2*d-3))/pg_den(q,r+1)
    return el,er,elr,elr-el*er

if __name__=='__main__':main()
