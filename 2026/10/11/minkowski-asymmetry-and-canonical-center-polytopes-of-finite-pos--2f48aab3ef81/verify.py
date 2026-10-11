"""Exact finite checks for the strict-order-map center polytope.

Requires Python 3 standard library only. The accompanying proof applies to
arbitrary finite posets; enumeration here is corroborative, not that proof.
"""
from itertools import combinations, product
from fractions import Fraction
from random import Random


def rational_rank(vectors):
    if not vectors:
        return 0
    a = [[Fraction(x) for x in v] for v in vectors]
    m, n = len(a), len(a[0])
    row = 0
    for col in range(n):
        piv = next((i for i in range(row, m) if a[i][col]), None)
        if piv is None:
            continue
        a[row], a[piv] = a[piv], a[row]
        fac = a[row][col]
        a[row] = [x / fac for x in a[row]]
        for i in range(row + 1, m):
            fac = a[i][col]
            if fac:
                a[i] = [x - fac * y for x, y in zip(a[i], a[row])]
        row += 1
        if row == m:
            break
    return row


def check(n,mask):
    pairs = list(combinations(range(n),2))
    reach = [[False]*n for _ in range(n)]
    for b,(i,j) in enumerate(pairs):
        if (mask >> b)&1:
            reach[i][j]=True
    for k in range(n):
        for i in range(n):
            for j in range(n):
                reach[i][j] |= reach[i][k] and reach[k][j]
    covers = [(i,j) for i in range(n) for j in range(i+1,n)
              if reach[i][j] and not any(reach[i][k] and reach[k][j] for k in range(n))]
    low=[1]*n
    for j in range(n):
        low[j]=1+max((low[i] for i in range(j) if reach[i][j]),default=0)
    high=[1]*n
    for i in range(n-1,-1,-1):
        high[i]=1+max((high[j] for j in range(i+1,n) if reach[i][j]),default=0)
    h=max(low)
    critical=[i for i in range(n) if low[i]+high[i]-1==h]
    # Integer points of the codegree interior hull.
    pts = [z for z in product(range(1,h+1),repeat=n)
           if all(z[j]-z[i]>=1 for i,j in covers)]
    assert pts
    for i in critical:
        assert all(z[i]==low[i] for z in pts)
    assert rational_rank([tuple(z[i]-pts[0][i] for i in range(n)) for z in pts[1:]]) == n-len(critical)
    # The defining Minkowski-center facet constraints hold for each vertex
    # of the order polytope (indicator functions of upper sets).
    uppers=[v for v in product((0,1),repeat=n)
            if all(v[i]<=v[j] for i,j in covers)]
    for z in pts:
        for v in uppers:
            # Equivalent scaled rational test with center z/(h+1):
            # ((h+1)c-v)/h = (z-v)/h.
            assert all(0<=z[i]-v[i]<=h for i in range(n))
            assert all(z[i]-v[i]<=z[j]-v[j] for i,j in covers)
    return len(pts)


def main():
    trials=0; total=0
    for n in range(1,6):
        for mask in range(1<<(n*(n-1)//2)):
            total += check(n,mask)
            trials += 1
    rnd=Random(20261009)
    for _ in range(120):
        n=6
        mask=rnd.randrange(1<<(n*(n-1)//2))
        total += check(n,mask)
        trials += 1
    print(f"PASS {trials} poset presentations, {total} integer center points, exact affine ranks and vertex tests")

if __name__=='__main__':
    main()
