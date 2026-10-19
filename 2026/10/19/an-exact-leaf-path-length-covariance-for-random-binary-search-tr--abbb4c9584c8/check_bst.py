"""Exact finite checks for the random binary-search-tree leaf/path-length covariance.
Run with Python 3.10 or newer; uses only the standard library.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial


def stats(insertion_order):
    if not insertion_order:
        return 0, 0
    pivot = insertion_order[0]
    left = tuple(x for x in insertion_order[1:] if x < pivot)
    right = tuple(x for x in insertion_order[1:] if x > pivot)
    if not left and not right:
        return 1, 0
    a, b = stats(left)
    c, d = stats(right)
    return a + c, b + d + len(insertion_order) - 1


def recursive_exact(max_n=80):
    a = [Fraction(0) for _ in range(max_n + 1)]
    b = [Fraction(0) for _ in range(max_n + 1)]
    ab = [Fraction(0) for _ in range(max_n + 1)]
    a2 = [Fraction(0) for _ in range(max_n + 1)]
    b2 = [Fraction(0) for _ in range(max_n + 1)]
    a[1] = a2[1] = Fraction(1)
    for n in range(2, max_n + 1):
        for i in range(n):
            j = n-1-i
            a[n] += (a[i] + a[j]) / n
            b[n] += (b[i] + b[j] + n-1) / n
            a2[n] += (a2[i] + a2[j] + 2*a[i]*a[j]) / n
            b2[n] += (b2[i] + b2[j] + 2*b[i]*b[j] + 2*(n-1)*(b[i]+b[j]) + (n-1)**2) / n
            ab[n] += (ab[i] + ab[j] + a[i]*b[j] + a[j]*b[i]
                       + (n-1)*(a[i]+a[j])) / n
        covariance = ab[n] - a[n]*b[n]
        assert covariance == Fraction(-(n*n+n-6), 9*n), (n, covariance)
        if n >= 4:
            assert a2[n] - a[n]**2 == Fraction(2*(n+1), 45)
        assert a[n] == Fraction(n+1,3)
        harmonic = sum(Fraction(1,j) for j in range(1,n+1))
        assert b[n] == 2*(n+1)*harmonic-4*n
        h2 = sum(Fraction(1,j*j) for j in range(1,n+1))
        assert b2[n] - b[n]**2 == n*(7*n+13)-2*(n+1)*harmonic-4*(n+1)**2*h2
    return a,b,ab,a2,b2


def exhaustive(max_n=8):
    for n in range(2,max_n+1):
        s_l=s_p=s_lp=0
        for order in permutations(range(n)):
            l,p=stats(order)
            s_l += l; s_p += p; s_lp += l*p
        f = factorial(n)
        cov = Fraction(s_lp, f) - Fraction(s_l*s_p, f*f)
        assert cov == Fraction(-(n*n+n-6), 9*n), (n,cov)
        print('n =',n,'permutations =',f,'covariance =',cov)


if __name__=='__main__':
    recursive_exact()
    exhaustive()
    print('PASS: exact mixed recurrences for n=2..80 and exhaustive permutations n=2..8')
