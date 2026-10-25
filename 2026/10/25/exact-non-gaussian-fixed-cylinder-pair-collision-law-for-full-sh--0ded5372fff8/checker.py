"""Independent finite covariance and exact-mean checks for sliding-word collisions.

Uses rational arithmetic and a direct overlap count, rather than the
orthogonal-polynomial derivation of the limit spectrum.
"""
from fractions import Fraction
from itertools import product
from collections import Counter
from math import comb


def profile(q, k):
    return {k: q-1} if k == 1 else {k-d: (q-1) if d==0 else (q-1)**2 *q**(d-1) for d in range(k)}


def long_run_covariance(q, k):
    words = list(product(range(q), repeat=k))
    m = q**k
    C = [[Fraction(0) for _ in range(m)] for _ in range(m)]
    for a, wa in enumerate(words):
        for b, wb in enumerate(words):
            c = Fraction(int(wa==wb),q**k) - Fraction(1,q**(2*k))
            for lag in range(1,k):
                both_ab = int(wa[lag:] == wb[:k-lag])
                both_ba = int(wb[lag:] == wa[:k-lag])
                c += Fraction(both_ab+both_ba, q**(k+lag)) - Fraction(2,q**(2*k))
            C[a][b] = c
    return C


def check_spectrum(q,k):
    import sympy as sp
    C=long_run_covariance(q,k)
    M=sp.Matrix([[sp.Rational(x.numerator,x.denominator) for x in row] for row in C])
    actual=M.eigenvals()
    predicted={sp.Rational(j,q**k):mult for j,mult in profile(q,k).items()}
    predicted[sp.Integer(0)]=q**(k-1)
    assert actual == predicted, (q,k,actual,predicted)
    e=sum(mult*j*j for j,mult in profile(q,k).items())
    closed=((q+1)*q**k-(q+1)-2*k*(q-1))//(q-1)
    assert e == closed
    return {str(key): int(value) for key,value in actual.items()}, Fraction(e,2*q**(2*k))


def exact_mean(q,k,N):
    sums = Fraction(0)
    total = q**(N+k-1)
    for digits in product(range(q), repeat=N+k-1):
        cnt=Counter(tuple(digits[i:i+k]) for i in range(N))
        U=sum(a*(a-1)//2 for a in cnt.values())
        sums += U
    assert sums/total == Fraction(comb(N,2),q**k), (q,k,N,sums,total)
    return int(total)

if __name__=='__main__':
    print('EXACT LONG-RUN COVARIANCE EIGENVALUES')
    for q,k in [(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3),(4,2)]:
        spectrum,v=check_spectrum(q,k)
        print('q',q,'k',k,'eigenvalues',spectrum,'variance_coefficient',str(v))
    print('EXACT FINITE-COLLISION MEANS')
    for q,k,N in [(2,1,6),(2,2,6),(2,3,6),(3,1,5),(3,2,5),(3,3,4),(4,2,4)]:
        print('q',q,'k',k,'N',N,'strings',exact_mean(q,k,N),'PASS')
    print('CHECKS_PASS')
