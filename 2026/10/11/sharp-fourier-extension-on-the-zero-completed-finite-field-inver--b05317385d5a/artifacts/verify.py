#!/usr/bin/env python3
"""Direct finite checks of the convolution identities and sharp witnesses.

Run: python3 artifacts/verify.py
The unrestricted theorem relies on the accompanying mathematical proof.
"""
import cmath
import math
import random


class Field:
    def __init__(self, p, d=None):
        self.p = p
        self.d = d
        self.q = p if d is None else p * p
        if d is not None:
            assert all((j * j) % p != d for j in range(p))

    def unpack(self, a):
        return a % self.p, a // self.p

    def add(self, a, b):
        if self.d is None:
            return (a + b) % self.p
        x, y = self.unpack(a)
        u, v = self.unpack(b)
        return (x + u) % self.p + self.p * ((y + v) % self.p)

    def neg(self, a):
        return self.sub(0, a)

    def sub(self, a, b):
        if self.d is None:
            return (a - b) % self.p
        x, y = self.unpack(a)
        u, v = self.unpack(b)
        return (x - u) % self.p + self.p * ((y - v) % self.p)

    def mul(self, a, b):
        if self.d is None:
            return (a * b) % self.p
        x, y = self.unpack(a)
        u, v = self.unpack(b)
        return (x * u + self.d * y * v) % self.p + self.p * ((x * v + y * u) % self.p)

    def power(self, a, n):
        z = 1
        while n:
            if n & 1:
                z = self.mul(z, a)
            a = self.mul(a, a)
            n >>= 1
        return z

    def inv(self, a):
        assert a != 0
        return self.power(a, self.q - 2)

    def hex_root(self):
        roots = [x for x in range(1, self.q)
                 if self.add(self.sub(self.mul(x, x), x), 1) == 0]
        assert len(roots) == (2 if self.q % 3 == 1 else 0)
        return roots[0] if roots else None


def points(F):
    return [(0, 0)] + [(i, F.inv(i)) for i in range(1, F.q)]


def convolution_fourth(F, f):
    pts = points(F)
    v = {}
    for i, (x, y) in enumerate(pts):
        for j, (u, w) in enumerate(pts):
            z = (F.add(x, u), F.add(y, w))
            v[z] = v.get(z, 0) + f[i] * f[j]
    return sum(abs(z) ** 2 for z in v.values())


def fourth_identity(F, f):
    B = sum(abs(z) ** 2 for z in f[1:])
    pairs = [(i, F.neg(i)) for i in range(1, F.q) if i < F.neg(i)]
    assert len(pairs) == (F.q - 1) // 2
    H = sum((f[i] * f[j] for i, j in pairs), 0j)
    Q = sum(abs(f[i] * f[j]) ** 2 for i, j in pairs)
    D = sum(abs(z) ** 4 for z in f[1:])
    c = f[0]
    lam = F.hex_root()
    U = 0j
    if lam is not None:
        lam_inv = F.inv(lam)
        U = sum((f[t] * (f[F.mul(lam, t)] * f[F.mul(lam_inv, t)]).conjugate()
                 for t in range(1, F.q)), 0j)
    return (2 * B * B - D - 4 * Q + abs(c * c + 2 * H) ** 2
            + 4 * abs(c) ** 2 * B + 8 * (c * U).real)


def root_r():
    lo, hi = 1.0, 2.0
    for _ in range(100):
        r = (lo + hi) / 2
        if 2 * r ** 3 + 6 * r ** 2 - 3 * r - 12 < 0:
            lo = r
        else:
            hi = r
    return (lo + hi) / 2


def sharp_witness(F, rng):
    f = [0j] * F.q
    if F.q % 3 == 2:
        f[0] = math.sqrt(1.5)
        for t in range(1, F.q):
            if t < F.neg(t):
                theta = rng.uniform(-math.pi, math.pi)
                f[t] = cmath.exp(1j * theta)
                f[F.neg(t)] = cmath.exp(-1j * theta)
        target = 3 * (2 * F.q - 1) / (2 * F.q + 1)
    else:
        lam = F.hex_root()
        a = 1
        u, v = rng.uniform(-3, 3), rng.uniform(-3, 3)
        phases = [u, v, v - u, -u, -v, u - v]
        for j in range(6):
            f[a] = cmath.exp(1j * phases[j])
            a = F.mul(a, lam)
        assert a == 1
        r = root_r()
        f[0] = r
        target = (r ** 4 + 36 * r ** 2 + 48 * r + 90) / (r ** 2 + 6) ** 2
    E = convolution_fourth(F, f)
    R = E / sum(abs(z) ** 2 for z in f) ** 2
    assert abs(R - target) < 1e-9, (F.q, R, target)
    return R


def main():
    rng = random.Random(20260418)
    cases = [Field(5), Field(7), Field(11), Field(13),
             Field(17), Field(19), Field(5, 2), Field(7, 3)]
    identity_tests = 0
    for F in cases:
        for _ in range(13):
            f = [complex(rng.randint(-3, 3), rng.randint(-3, 3))
                 for _ in range(F.q)]
            a, b = convolution_fourth(F, f), fourth_identity(F, f)
            assert abs(a - b) < 1e-7 * max(1, abs(a)), (F.q, a, b)
            identity_tests += 1
        for _ in range(3):
            sharp_witness(F, rng)
    r = root_r()
    assert abs(2 * r ** 3 + 6 * r ** 2 - 3 * r - 12) < 1e-12
    print('VERIFY_OK fields=8 including F25,F49 '
          f'complex_convolution_identity_tests={identity_tests} '
          'sharp_phase_extremizer_tests=24 root_residual=PASS')


if __name__ == '__main__':
    main()
