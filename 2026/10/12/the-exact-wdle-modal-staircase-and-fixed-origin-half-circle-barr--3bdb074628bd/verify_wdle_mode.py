#!/usr/bin/env python3
"""Independent finite-arithmetic checks for the WDLE modal-sector theorem.

The analytic proof, not these finite checks, establishes the all-parameter claim.
Requires only Python 3 standard library.
"""
import math


def base_mass(n, phi):
    q = math.exp(-phi)
    a = 1 + phi ** 3
    return math.exp(-phi * n) * (a * (1 - q) + phi * n * (1 - q) - phi * q) / a


def wrapped_direct(r, m, phi):
    total = 0.0
    for k in range(100000):
        term = base_mass(r + k * m, phi)
        total += term
        if k > 20 and term < 1e-17:
            return total
    raise ArithmeticError('tail did not converge')


def wrapped_closed(r, m, phi):
    q = math.exp(-phi)
    Q = math.exp(-m * phi)
    a = 1 + phi ** 3
    c = a * (1 - q) - q * phi
    d = phi * (1 - q)
    return q ** r * (c + d * r + d * m * Q / (1 - Q)) / (a * (1 - Q))


def H(m, phi):
    return 2 / math.expm1(phi) - m / math.expm1(m * phi) - 1 / phi - phi ** 2


def threshold(m, j):
    lo, hi = 1e-5, 5.0
    assert H(m, lo) > j > H(m, hi)
    for _ in range(90):
        mid = (lo + hi) / 2
        if H(m, mid) > j:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def predicted_modes(m, phi):
    h = H(m, phi)
    rounded = round(h)
    if 0 <= rounded < m-1 and abs(h-rounded) < 3e-12:
        return [rounded, rounded+1]
    return [max(0, math.ceil(h))]


def main():
    for m in (2, 3, 4, 5, 9, 20):
        for phi in (0.06, 0.1, 0.3, 0.5, 0.9, 1.4):
            closed = [wrapped_closed(r, m, phi) for r in range(m)]
            direct = [wrapped_direct(r, m, phi) for r in range(m)]
            assert abs(sum(closed) - 1) < 1e-12
            assert min(closed) > 0
            assert max(abs(a-b) for a,b in zip(closed,direct)) < 1e-12
            actual = [r for r, p in enumerate(closed) if p >= max(closed)-1e-12]
            assert actual == predicted_modes(m,phi), (m,phi,actual,predicted_modes(m,phi))
    expected = {3:(0.48078153605492535,),
                5:(0.6588947478831645,0.23732245706316243),
                9:(0.7121183949978162,0.43471723426633385,
                   0.23579457294878245,0.07567261369589387)}
    for m, roots in expected.items():
        for j, r in enumerate(roots):
            z = threshold(m,j)
            assert abs(z-r)<5e-13
            assert abs(wrapped_closed(j,m,z)-wrapped_closed(j+1,m,z))<1e-12
            print('threshold',m,j,format(z,'.14f'))
    for m in range(2,41):
        k = (m-1)//2
        for phi in (.01,.075,.17,.35,.7,1.2,2):
            assert predicted_modes(m,phi)[-1] <= k
    print('CHECK_OK: direct wrap, normalization, modes, roots, sector ceiling')

if __name__=='__main__':
    main()
