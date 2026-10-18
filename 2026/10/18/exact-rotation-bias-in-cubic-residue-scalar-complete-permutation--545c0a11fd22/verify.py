"""Exact finite-field checks for the cubic scalar complete-permutation spectrum.

Uses integer arithmetic throughout; the extension-field sample is GF(64),
represented by the primitive polynomial X^6+X+1 over GF(2).
"""
from itertools import product


class Field:
    def __init__(self, q):
        self.q = q
        if q not in (19, 37, 64, 73, 109, 127, 163, 199):
            raise ValueError("Unsupported verification example")

    def add(self, a, b):
        return (a ^ b) if self.q == 64 else ((a + b) % self.q)

    def neg(self, a):
        return a if self.q == 64 else (-a) % self.q

    def mul(self, a, b):
        if self.q != 64:
            return a * b % self.q
        z = 0
        while b:
            if b & 1:
                z ^= a
            b >>= 1
            a <<= 1
            if a & 64:
                a ^= 0b1000011
        return z

    def pow(self, a, n):
        z = 1
        while n:
            if n & 1:
                z = self.mul(z, a)
            a = self.mul(a, a)
            n >>= 1
        return z

    def primitive(self):
        for g in range(2, self.q):
            y = 1
            seen = set()
            for _ in range(self.q - 1):
                seen.add(y)
                y = self.mul(y, g)
            if len(seen) == self.q - 1 and y == 1:
                return g
        raise AssertionError("Primitive generator not found")


def check(q):
    F = Field(q)
    s = (q - 1) // 3
    assert q % 9 == 1
    g = F.primitive()
    omega = F.pow(g, s)
    mu = [1, omega, F.mul(omega, omega)]
    assert len(set(mu)) == 3
    K = [F.pow(g, 3 * i) for i in range(s)]
    assert len(set(K)) == s and all(F.pow(a, s) == 1 for a in K)
    assert all(F.pow(u, s) == 1 for u in mu)
    idx = {u: i for i, u in enumerate(mu)}

    def cubic_class(a):
        return None if a == 0 else idx[F.pow(a, s)]

    N = [0] * 3
    for a in K:
        j = cubic_class(F.add(1, a))
        if j is not None:
            N[j] += 1
    assert sum(N) == s - 1

    J_c = [0, 0, 0]
    for t in range(q):
        a = cubic_class(t)
        b = cubic_class(F.add(1, F.neg(t)))
        if a is not None and b is not None:
            J_c[(a + b) % 3] += 1
    U, V = J_c[0] - J_c[2], J_c[1] - J_c[2]
    assert U * U - U * V + V * V == q, (q, U, V)
    A, B = U - 2, V
    norm = A * A - A * B + B * B
    predicted = [(q - 4 + d) // 9 for d in (2 * A - B, -A + 2 * B, -A - B)]
    assert [(q - 4 + d) % 9 for d in (2 * A - B, -A + 2 * B, -A - B)] == [0] * 3
    assert N == predicted, (q, N, predicted)

    rotations = sum(x ** 3 for x in N)
    transpositions = 3 * N[0] * N[1] * N[2]
    assert 27 * (rotations - transpositions) == (q - 4) * norm
    assert rotations > transpositions > 0

    # Exhaustive independent field-map check on the four smallest test fields.
    if q in (19, 37, 64, 73):
        coset = [cubic_class(x) for x in range(q)]
        count_rot, count_trans = 0, 0
        for aa in product(K, repeat=3):
            images_f = {0}
            images_F = {0}
            for x in range(1, q):
                a = aa[coset[x]]
                images_f.add(F.mul(x, a))
                images_F.add(F.mul(x, F.add(1, a)))
            is_cpp = len(images_f) == q and len(images_F) == q
            shifts = [cubic_class(F.add(1, a)) for a in aa]
            induced = None if any(j is None for j in shifts) else [(i + j) % 3 for i, j in enumerate(shifts)]
            expected = induced is not None and len(set(induced)) == 3
            assert is_cpp == expected, (q, aa, is_cpp, expected)
            if is_cpp:
                if len(set(shifts)) == 1:
                    count_rot += 1
                else:
                    assert set(shifts) == {0, 1, 2}
                    count_trans += 1
        assert count_rot == rotations and count_trans == transpositions, (q, rotations, transpositions, count_rot, count_trans)

    return q, N, rotations, transpositions, U, V


if __name__ == '__main__':
    for q in (19, 37, 64, 73, 109, 127, 163, 199):
        print('q,N,R,T,Jacobi_Eisenstein:', check(q))
    print('VERIFY_OK')
