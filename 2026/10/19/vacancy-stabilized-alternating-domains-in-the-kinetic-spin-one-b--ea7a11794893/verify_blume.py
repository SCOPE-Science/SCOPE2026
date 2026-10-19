"""Exact finite-volume checks for strict one-site stability of a spin-one cycle."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb


def direct(n, d):
    ans = Counter()
    for a in product((-1, 0, 1), repeat=n):
        if all(
            d * t * t - t * (a[(i-1) % n] + a[(i+1) % n])
            > d * a[i] * a[i] - a[i] * (a[(i-1) % n] + a[(i+1) % n])
            for i in range(n) for t in (-1, 0, 1) if t != a[i]
        ):
            ans[a.count(0)] += 1
    return ans


def predicted(n, d):
    if d == 0:
        return Counter({0: 2})
    if 0 < d < 1:
        c = Counter({0: 2, n: 1})
        for k in range(2, n//3+1, 2):
            numerator = 2*n*comb(n-2*k-1, k-1)
            assert numerator % k == 0
            c[k] += numerator // k
        return c
    if 1 <= d < 2:
        return Counter({0: 2, n: 1})
    return Counter({n: 1})


def main():
    tests = 0
    for n in range(3, 12):
        for d in map(Fraction, ('0', '1/4', '1/2', '3/4', '1', '3/2', '2', '3')):
            a = direct(n, d)
            b = predicted(n, d)
            assert a == b, (n, d, a, b)
            tests += 1
    # Coefficients of x h'(x)/(1-h(x)), with h=x^6/(1-x)^2.
    limit = 28
    q = [0] * (limit+1)
    q[0] = 1
    for n in range(1, limit+1):
        q[n] = sum((m-5)*q[n-m] for m in range(6, n+1))
    for n in range(3, limit+1):
        coeff = sum(m*(m-5)*q[n-m] for m in range(6, n+1))
        count = sum(v for k,v in predicted(n, Fraction(1,2)).items() if 0<k<n)
        assert coeff == count, (n, coeff, count)
    print(f'PASS: {tests} direct Hamiltonian checks and {limit-2} renewal-polynomial coefficient checks.')

if __name__ == '__main__':
    main()
