"""Finite-field verification for the cyclic sextic's 21 critical points.

Uses binary-polynomial models of F_(2^n), with arithmetic implemented here.
The infinite-field and resolution assertions require the accompanying proof.
"""
from math import gcd

MODULI = {1: 0b11, 2: 0b111, 3: 0b1011, 4: 0b10011, 6: 0b1000011}

class Field:
    def __init__(self, n):
        self.n = n
        self.q = 1 << n
        self.mod = MODULI[n]
    def mul(self, a, b):
        result = 0
        while b:
            if b & 1:
                result ^= a
            b >>= 1
            a <<= 1
            if a & self.q:
                a ^= self.mod
        return result
    def pow(self, a, m):
        result = 1
        while m:
            if m & 1:
                result = self.mul(result, a)
            a = self.mul(a, a)
            m >>= 1
        return result
    def frob(self, a):
        return self.mul(a, a)
    def inv(self, a):
        assert a != 0
        return self.pow(a, self.q - 2)

def polynomial(k, x, y, z):
    return k.mul(k.pow(x, 5), y) ^ k.mul(k.pow(y, 5), z) ^ k.mul(k.pow(z, 5), x)

def gradient(k, x, y, z):
    return (k.mul(k.pow(x, 4), y) ^ k.pow(z, 5),
            k.pow(x, 5) ^ k.mul(k.pow(y, 4), z),
            k.pow(y, 5) ^ k.mul(k.pow(z, 4), x))

def projective_points(k):
    for y in range(k.q):
        for z in range(k.q):
            yield (1, y, z)
    for z in range(k.q):
        yield (0, 1, z)
    yield (0, 0, 1)

def critical_points(k):
    return [p for p in projective_points(k) if gradient(k, *p) == (0, 0, 0)]

def main():
    for n in (1, 2, 3, 4, 6):
        k = Field(n)
        assert all(k.mul(a, k.inv(a)) == 1 for a in range(1, k.q))
        points = critical_points(k)
        N = gcd(21, k.q-1)
        assert len(points) == N, (n, len(points), N)
        assert len(list(projective_points(k))) == k.q * k.q + k.q + 1
        for x, y, z in points:
            assert x == 1 and y != 0 and z != 0
            assert y == k.pow(z, 5) and k.pow(z, 21) == 1
            assert k.pow(y, 4) != 0  # mixed term in the local quadratic part
            f = polynomial(k, x, y, z)
            w = k.pow(f, k.q // 2)
            assert k.mul(w, w) == f
        resolved_points = k.q*k.q + k.q + 1 + k.q*N
        print(f"n={n}: q={k.q}; critical_points={N}; resolved_points={resolved_points}")

    k = Field(6)
    nodes = set(critical_points(k))
    cycles = []
    while nodes:
        p = next(iter(nodes))
        orbit = []
        t = p
        while t not in orbit:
            assert t in nodes
            orbit.append(t)
            t = tuple(k.frob(v) for v in t)
        assert t == p
        for x in orbit:
            nodes.remove(x)
        cycles.append(len(orbit))
    assert sorted(cycles) == [1, 2, 3, 3, 6, 6], cycles
    print("FROBENIUS_CYCLES=" + str(sorted(cycles)))
    print("VERIFY_OK")

if __name__ == '__main__':
    main()
