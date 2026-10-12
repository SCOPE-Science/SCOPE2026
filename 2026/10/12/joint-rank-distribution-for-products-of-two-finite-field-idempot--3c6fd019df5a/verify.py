"""Exact finite-field checks of the joint ranks of products of idempotents.

Pure Python, no nonstandard packages. For GF(4), elements are binary
polynomials modulo x^2+x+1, represented by bit pairs.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product


def gaussian(n, k, q):
    if n < 0 or k < 0 or k > n:
        return 0
    out = Fraction(1)
    for i in range(k):
        out *= Fraction(q ** (n-i)-1, q ** (k-i)-1)
    assert out.denominator == 1
    return out.numerator


def gl(k, q):
    out = 1
    for i in range(k):
        out *= q ** k - q ** i
    return out


def rank_count(a, b, j, q):
    return gaussian(a, j, q) * gaussian(b, j, q) * gl(j, q)


def formula(n, r, s, p, t, q):
    if any(x < 0 or x > n for x in (r, s, p, t)):
        return 0
    total = 0
    k = n-r
    for h in range(min(r, s, p, t)+1):
        b = s-p
        c = p-h
        rem = n-s-r+h
        if b < 0 or b > k or c < 0 or c > r-h or c > k-b:
            continue
        if t < h or t-h > min(s-h, r-h) or rem < 0:
            continue
        ways_image = (gaussian(r,h,q)*gaussian(k,b,q)*
                      gaussian(r-h,c,q)*gaussian(k-b,c,q)*gl(c,q))
        ways_kernel = (rank_count(s-h,r-h,t-h,q)*
                       q ** (h*(r-h)+s*rem))
        total += ways_image*ways_kernel
    return gaussian(n,r,q) * q ** (r*(n-r)) * total


def add(a, b, q):
    return a ^ b if q == 4 else (a + b) % q


def mul(a, b, q):
    if q != 4:
        return a*b % q
    z = 0
    for i in range(2):
        for j in range(2):
            if ((a>>i)&1) and ((b>>j)&1):
                power = i+j
                z ^= (1 << power) if power < 2 else 3
    return z


def inverse(a, q):
    if a == 0:
        raise ZeroDivisionError
    return next(b for b in range(1, q) if mul(a,b,q)==1)


def matmul(a, b, q):
    n=len(a)
    return tuple(tuple(
        __import__('functools').reduce(lambda z,k:add(z,mul(a[i][k],b[k][j],q),q),range(n),0)
        for j in range(n)) for i in range(n))


def rank(matrix, q):
    a=[list(x) for x in matrix]
    n=len(a)
    rr=0
    for j in range(n):
        pivot=next((i for i in range(rr,n) if a[i][j]!=0),None)
        if pivot is None:
            continue
        a[rr],a[pivot]=a[pivot],a[rr]
        inv=inverse(a[rr][j],q)
        a[rr]=[mul(z,inv,q) for z in a[rr]]
        for i in range(n):
            if i != rr and a[i][j]:
                f=a[i][j]
                a[i]=[add(a[i][h],mul(f,a[rr][h],q),q) if q==4
                      else (a[i][h]-mul(f,a[rr][h],q))%q
                      for h in range(n)]
        rr+=1
    return rr


def verify_brute(q,n):
    idem=defaultdict(list)
    for flat in product(range(q),repeat=n*n):
        a=tuple(tuple(flat[i*n+j] for j in range(n)) for i in range(n))
        if matmul(a,a,q)==a:
            idem[rank(a,q)].append(a)
    for r in range(n+1):
        expected=gaussian(n,r,q)*q**(r*(n-r))
        assert len(idem[r]) == expected, (q,n,r,len(idem[r]),expected)
    observations=Counter()
    for r,rr in idem.items():
        for s,ss in idem.items():
            for a in rr:
                for b in ss:
                    observations[r,s,rank(matmul(a,b,q),q),rank(matmul(b,a,q),q)] += 1
    for r,s,p,t in product(range(n+1),repeat=4):
        predicted=formula(n,r,s,p,t,q)
        actual=observations[r,s,p,t]
        assert actual == predicted, (q,n,r,s,p,t,actual,predicted)
    print('PASS exhaustive',q,n,'idempotents',sum(map(len,idem.values())),
          'pairs',sum(observations.values()),'nonempty strata',len(observations))


def verify_totals(q,n):
    for r,s in product(range(n+1),repeat=2):
        total=sum(formula(n,r,s,p,t,q) for p,t in product(range(n+1),repeat=2))
        expected=(gaussian(n,r,q)*q**(r*(n-r)) *
                  gaussian(n,s,q)*q**(s*(n-s)))
        assert total == expected, ('total',q,n,r,s,total,expected)
        for p,t in product(range(n+1),repeat=2):
            assert formula(n,r,s,p,t,q)==formula(n,s,r,t,p,q), (q,n,r,s,p,t)
    print('PASS totals/swap',q,n)


if __name__ == '__main__':
    for q,n in ((2,2),(3,2),(4,2),(2,3),(3,3),(2,4)):
        verify_brute(q,n)
    for q,n in ((2,5),(3,5),(4,5),(5,5),(7,5),(8,5)):
        verify_totals(q,n)
    print('VERIFY_OK')
