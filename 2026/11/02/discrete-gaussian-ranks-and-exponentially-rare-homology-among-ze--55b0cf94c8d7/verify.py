"""Finite computational checks for uniform zero-product pairs of matrices.

Run: python3 verify.py (requires Python 3.9+, standard library only).
This script verifies finite counts, not the infinite-dimensional limits.
"""
from itertools import product
from math import prod
from fractions import Fraction


def gbin(n, r, q):
    if r < 0 or r > n:
        return 0
    return (prod(q ** (n-i)-1 for i in range(r)) //
            prod(q ** (r-i)-1 for i in range(r)))


def gl(n, q):
    return prod(q**n-q**i for i in range(n))


def expected(n, r, s, q):
    if r+s>n:
        return 0
    return gbin(n,r,q)**2*gl(r,q)*gbin(n-r,s,q)*gbin(n,s,q)*gl(s,q)


def rank(matrix, q):
    m = [list(row) for row in matrix]
    n = len(m)
    piv = 0
    for c in range(n):
        found = next((row for row in range(piv,n) if m[row][c]%q), None)
        if found is None:
            continue
        m[piv],m[found]=m[found],m[piv]
        inverse = pow(m[piv][c], -1, q)
        m[piv] = [(x*inverse)%q for x in m[piv]]
        for i in range(piv+1,n):
            factor=m[i][c]
            if factor:
                m[i] = [(x-factor*y)%q for x,y in zip(m[i],m[piv])]
        piv+=1
        if piv==n:
            break
    return piv


def product_zero(a,b,q):
    n=len(a)
    for i in range(n):
        for j in range(n):
            if sum(a[i][k]*b[k][j] for k in range(n)) % q:
                return False
    return True


def brute(n,q):
    matrices=[tuple(tuple(row[i*n:(i+1)*n]) for i in range(n))
              for row in product(range(q),repeat=n*n)]
    ranks=[rank(a,q) for a in matrices]
    observed={(r,s):0 for r in range(n+1) for s in range(n+1)}
    for i,a in enumerate(matrices):
        for j,b in enumerate(matrices):
            if product_zero(a,b,q):
                observed[ranks[i],ranks[j]]+=1
    for r in range(n+1):
        for s in range(n+1):
            assert observed[r,s]==expected(n,r,s,q), (n,q,r,s,observed[r,s],expected(n,r,s,q))
    return sum(observed.values())


def checks():
    for q,n in [(2,1),(2,2),(2,3),(3,1),(3,2)]:
        brute(n,q)
    # Algebraic count comparison: sum rank refined formula against the
    # independent choice A followed by an arbitrary compatible B.
    count=0
    for q in (2,3,4,5):
        for n in range(1,13):
            bypair=sum(expected(n,r,s,q) for r in range(n+1) for s in range(n+1))
            byfirst=sum(gbin(n,r,q)**2*gl(r,q)*q**(n*(n-r)) for r in range(n+1))
            assert bypair==byfirst, (n,q)
            prob=Fraction(sum(expected(n,r,n-r,q) for r in range(n+1)),bypair)
            assert Fraction(0)<=prob<=Fraction(1)
            count+=1
    print('VERIFY_OK: 5 fully enumerated matrix-pair models, '+str(count)+' exact symbolic counts')


if __name__=='__main__':
    checks()
