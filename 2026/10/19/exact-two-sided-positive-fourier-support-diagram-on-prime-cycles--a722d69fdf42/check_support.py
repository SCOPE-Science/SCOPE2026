"""Independent finite-grid tests for a doubly nonnegative Fourier-support theorem.

Requires Python 3.10+ and mpmath 1.3+. These tests verify sampled cases;
the theorem for every odd prime is proved analytically in RESULT.md.
"""
from mpmath import mp

mp.dps = 90
PRIMES = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
EPS = mp.mpf('1e-56')


def convolution(a, b):
    out = {}
    for j, u in a.items():
        for k, v in b.items():
            out[j + k] = out.get(j + k, mp.mpf(0)) + u * v
    return out


def coefficients(p, k, ell):
    """Unnormalized DFT convention; produce the non-swapped construction."""
    m = (p - 1) // 2
    r = (k - 1) // 2
    s = (p - ell) // 2
    assert 0 <= s <= r <= m and 2 * r + 1 <= ell
    factors = []
    for j in range(m - s + 1, m + 1):
        c = mp.cos(2 * mp.pi * j / p)
        assert c < 0
        factors.append({-1: mp.mpf('0.5'), 0: -c, 1: mp.mpf('0.5')})
    for _ in range(r - s):
        factors.append({-1: mp.mpf('0.5'), 0: mp.mpf(2), 1: mp.mpf('0.5')})
    a = {0: mp.mpf(1)}
    for fac in factors:
        a = convolution(a, fac)
    assert set(a) == set(range(-r, r + 1))
    assert all(t > 0 for t in a.values())
    f = [a.get(x if x <= m else x - p, mp.mpf(0)) for x in range(p)]
    fhat = [sum(f[x] * mp.cos(2 * mp.pi * x * j / p)
                for x in range(p)) for j in range(p)]
    for j in range(p):
        c = mp.cos(2 * mp.pi * min(j, p - j) / p)
        expected = mp.mpf(1)
        for t in range(m - s + 1, m + 1):
            expected *= c - mp.cos(2 * mp.pi * t / p)
        expected *= (c + 2) ** (r - s)
        assert abs(fhat[j] - expected) < EPS, (p,k,ell,j)
        if min(j, p-j) > m - s:
            assert abs(fhat[j]) < EPS
        else:
            assert fhat[j] > 0
    assert sum(a_ > 0 for a_ in f) == k
    assert sum(abs(v) > EPS for v in fhat) == ell
    return f, fhat


def run():
    total = 0
    for p in PRIMES:
        for k in range(1, p + 1, 2):
            for ell in range(1, p + 1, 2):
                if k + ell < p + 1:
                    continue
                if k <= ell:
                    coefficients(p, k, ell)
                else:
                    # Apply Fourier duality: the support counts swap and
                    # the second transform is p times spatial reflection.
                    a, ahat = coefficients(p, ell, k)
                    assert sum(z > EPS for z in ahat) == k
                    assert sum(z > 0 for z in a) == ell
                    for j in range(p):
                        transformed_twice = sum(
                            ahat[x] * mp.cos(2 * mp.pi * x * j / p)
                            for x in range(p))
                        assert abs(transformed_twice - p*a[(-j) % p]) < EPS
                total += 1
    print('PASS:', len(PRIMES), 'odd primes;', total,
          'admissible support pairs checked.')


if __name__ == '__main__':
    run()
