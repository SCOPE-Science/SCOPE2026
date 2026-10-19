"""Reproduce finite dyadic parabola identities and independent sharpness tests.

Run with Python 3. No external packages are required. Finite tests corroborate,
but do not replace, the valuation proof in RESULT.md.
"""
from collections import defaultdict
from cmath import exp
from math import pi


def energy(f):
    n = len(f)
    fibers = defaultdict(complex)
    for a, va in enumerate(f):
        if abs(va) < 1e-14:
            continue
        for b, vb in enumerate(f):
            if abs(vb) < 1e-14:
                continue
            fibers[((a+b) % n, (a*a+b*b) % n)] += va * vb
    return sum(abs(z)**2 for z in fibers.values())


def formula(k, d):
    n = 2**(2*k)
    r = 2*k if d == 0 else ((d & -d).bit_length()-1)
    return 2**(r+2) if r < k else 2**k


def collision(k, d):
    n = 2**(2*k)
    return sum(2*h*(d-h) % n == 0 for h in range(n))


def packet(k, r, j, eta_phase):
    n = 2**(2*k)
    q = 2**k
    f = [0j] * n
    for eta in (0, 1):
        for u in range(q):
            x = r + 2**(k-1)*eta + q*u
            f[x] = exp(2j*pi*(j*u/q + eta*eta_phase))
    return f


def main():
    for k in range(1, 5):
        n = 2**(2*k)
        for d in range(n):
            assert collision(k, d) == formula(k, d), ('collision', k, d)
        constant = 3*2**(k-1)
        cases = 0
        for r in range(2**(k-1)):
            for j in sorted({0, 1, 2**k-1}):
                for eta_phase in (0.0, 0.17, 0.33):
                    f = packet(k, r, j, eta_phase)
                    s = sum(abs(z)**2 for z in f)
                    e = energy(f)
                    assert abs(e/(s*s)-constant) < 1e-9, ('packet', k, r, j, eta_phase)
                    cases += 1
        # Concentration on one daughter is strictly below the bound.
        bad = [0j] * n
        for u in range(2**k):
            bad[u*2**k] = 1
        s = sum(abs(z)**2 for z in bad)
        assert energy(bad)/(s*s) < constant
        print(f'k={k}: N={n}, M(d) verified for all {n} differences, {cases} sharp packets, one strict witness')
    print('CHECK_PASS dyadic-even-family')


if __name__ == '__main__':
    main()
