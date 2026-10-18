"""Exact integer certificate for two Stern diatomic residue-count identities.

No external dependencies. Run: python3 stern_22_27_checker.py
"""
from collections import defaultdict
from math import gcd

COEFF = (1, -3, 4, -6, 9, -13, 14, -18, 12, -16, 0, 32, -64)
N_STATES = 36


def projective_system(m):
    units = [u for u in range(m) if gcd(u, m) == 1]
    canonical = lambda a, b: min(((u*a) % m, (u*b) % m) for u in units)
    states = sorted({canonical(a, b) for a in range(m) for b in range(m)
                     if gcd(gcd(a, b), m) == 1})
    assert len(states) == N_STATES, (m, len(states))
    indices = {state: i for i, state in enumerate(states)}
    left = [indices[canonical(a, a+b)] for a,b in states]
    right = [indices[canonical(a+b, b)] for a,b in states]
    zero = [int(a == 0) for a,b in states]
    assert sum(zero) == 1
    root = indices[canonical(1, 1)]
    return left, right, zero, root


def series(m, steps=96):
    left, right, f, root = projective_system(m)
    res = []
    for k in range(steps):
        res.append(f[root])
        f = [f[left[i]] + f[right[i]] for i in range(N_STATES)]
    return res


def raw_stern_row_zeros(m, k):
    vals = [1,1]
    for _ in range(k):
        out = [vals[0]]
        for a,b in zip(vals, vals[1:]):
            out.extend((a+b,b))
        vals = out
    assert len(vals) == (1 << k)+1
    return sum(v % m == 0 for v in vals[:-1])


def main():
    z22, z27 = series(22), series(27)
    assert z22[:12] == z27[:12] == [0,0,0,0,0,0,0,4,8,16,24,52]
    # A dimension-36 transfer matrix annihilates every sequence after its
    # characteristic polynomial. Therefore 36 consecutive zero residuals
    # certify that the putative order-12 recurrence holds for all later k.
    for m, z in ((22,z22),(27,z27)):
        for k in range(12, 48):
            assert sum(COEFF[j]*z[k-j] for j in range(13)) == 0, (m,k)
        for k in range(12,96):
            assert sum(COEFF[j]*z[k-j] for j in range(13)) == 0, (m,k)
        for k in range(12):
            assert raw_stern_row_zeros(m,k) == z[k], (m,k)
    # Independently, direct-sum Cayley--Hamilton (72 states) makes equality
    # of the first 72 levels a certificate of equality at all levels.
    assert z22[:72] == z27[:72]
    print('PASS: 36 projective states at each modulus, two exact transfer systems')
    print('PASS: order-12 recurrence residuals at k=12..47, both moduli')
    print('PASS: direct-sum 72-level equality certificate')
    print('PASS: independent raw Stern checks at k=0..11')
    print('Initial terms:', z22[:16])
    print('Numerator coefficients:', [sum(COEFF[j]*z22[k-j] for j in range(min(12,k)+1)) for k in range(12)])

if __name__ == '__main__':
    main()
