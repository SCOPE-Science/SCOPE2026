#!/usr/bin/env python3
"""Direct finite-matrix checks for a p-adic Dirac spinor entanglement ceiling.
Standard library only; checks complement, not replace, the arbitrary-level proof.
"""
import cmath
import math


def h2(q):
    if q <= 0.0 or q >= 1.0:
        return 0.0
    return -q * math.log2(q) - (1.0 - q) * math.log2(1.0 - q)


def valuation(z, p):
    r = 0
    while z % p == 0:
        z //= p
        r += 1
    return r


def matrix(p, ell, g=1.0, weights=None):
    n = p ** ell
    a = [[0.0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if x != y:
                z = (x - y) % n
                a[x][y] = (2.0 * g / n + (g / p if z % (p ** (ell - 1)) == 0 else 0.0)) if weights is None else weights[valuation(z, p)] / n
        a[x][x] = -sum(a[x])
    return a


def apply_h(a, m, state):
    n = len(a)
    up, dn = state[:n], state[n:]
    return ([m * up[x] + sum(a[x][y] * dn[y] for y in range(n)) for x in range(n)] +
            [sum(a[x][y] * up[y] for y in range(n)) - m * dn[x] for x in range(n)])


def evolve(a, m, t):
    n = len(a)
    term = [0j] * (2 * n)
    term[0] = 1.0 + 0j
    state = term.copy()
    for k in range(1, 90):
        ht = apply_h(a, m, term)
        term = [(-1j * t / k) * z for z in ht]
        state = [s + q for s, q in zip(state, term)]
    up, dn = state[:n], state[n:]
    nu = sum(abs(z)**2 for z in up)
    nd = sum(abs(z)**2 for z in dn)
    cross = sum(u.conjugate() * d for u, d in zip(up, dn))
    assert abs(nu + nd - 1.0) < 1e-10, (nu, nd)
    gap = math.sqrt(max(0.0, (nu - nd) ** 2 + 4.0 * abs(cross)**2))
    return h2((1.0 + gap) / 2.0), ((1.0 + gap) / 2.0, (1.0 - gap) / 2.0)


def spectrum(a):
    n = len(a)
    result = []
    for k in range(n):
        z = sum(a[0][j] * cmath.exp(2j * math.pi * k * j / n) for j in range(n))
        assert abs(z.imag) < 1e-9
        result.append(z.real)
    return result


def main():
    checked = 0
    for p, ell in [(2, 1), (2, 2), (2, 4), (3, 1), (3, 2), (3, 3), (5, 1), (5, 2), (7, 1)]:
        a = matrix(p, ell)
        n = p ** ell
        assert all(a[x][y] > 0 for x in range(n) for y in range(n) if x != y)
        eig = spectrum(a)
        for k in range(n):
            expected = 0 if k == 0 else (-3 if k % p else -2)
            assert abs(eig[k] - expected) < 1e-9, (p, ell, k, eig[k], expected)
            checked += 1
        entropy, lambdas = evolve(a, 0.0, math.pi / 2.0)
        assert abs(entropy - h2(1 / p)) < 2e-10, (p, ell, entropy)
        assert abs(lambdas[0] - (p - 1) / p) < 2e-10
        checked += 3
        for m, t in [(0.0, 0.217), (0.6, 0.561), (1.2, 0.91)]:
            entropy, _ = evolve(a, m, t)
            assert entropy <= h2(1 / p) + 1e-9
            checked += 1
        if p in (2, 3, 5):
            fast = matrix(p, ell, g=100.0)
            entropy, _ = evolve(fast, 0.8, math.pi / 200.0)
            assert h2(1 / p) - entropy < 0.002
            checked += 1
        # An independently chosen positive radial generator has a common unit-character eigenvalue.
        weights = [1.1 + 0.37 * r for r in range(ell)]
        ar = matrix(p, ell, weights=weights)
        spec = spectrum(ar)
        assert max(abs(spec[k] - spec[1]) for k in range(1, n) if k % p) < 1e-9
        checked += 1
        # Independently evolved massless spinor agrees with the character-phase formula.
        t = 0.713
        f = sum(cmath.exp(-2j * t * x) for x in spec) / n
        exact = h2((1 + abs(f)) / 2)
        evolved, _ = evolve(ar, 0.0, t)
        assert abs(exact - evolved) < 2e-10
        checked += 1
    print(f'VERIFICATION_OK {checked} finite checks; arbitrary-depth proof is analytic')


if __name__ == '__main__':
    main()
