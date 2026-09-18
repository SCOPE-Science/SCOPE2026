#!/usr/bin/env python3
"""Finite checks for full-evaluation generalized Roth--Lempel hull constructions.

Two fields are used:
  * GF(8), to check a case where 2*ell does not divide e and to enumerate distances;
  * GF(27), ell=2, to check a case where ell itself does not divide e.
No external finite-field package is required.
"""

from itertools import product


class PrimePowerField:
    def __init__(self, p, mod):
        self.p = p
        self.mod = tuple(mod)  # monic low-to-high coefficients
        self.e = len(mod) - 1
        self.q = p ** self.e

    def coeffs(self, a):
        out = []
        for _ in range(self.e):
            out.append(a % self.p)
            a //= self.p
        return out

    def encode(self, c):
        z = 0
        mul = 1
        for x in c:
            z += (x % self.p) * mul
            mul *= self.p
        return z

    def add(self, a, b):
        ca, cb = self.coeffs(a), self.coeffs(b)
        return self.encode([(x + y) % self.p for x, y in zip(ca, cb)])

    def neg(self, a):
        return self.encode([(-x) % self.p for x in self.coeffs(a)])

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        ca, cb = self.coeffs(a), self.coeffs(b)
        prod = [0] * (2 * self.e - 1)
        for i, x in enumerate(ca):
            for j, y in enumerate(cb):
                prod[i + j] = (prod[i + j] + x * y) % self.p
        # x^e = -sum_{j<e} mod[j] x^j
        for deg in range(len(prod) - 1, self.e - 1, -1):
            z = prod[deg] % self.p
            if not z:
                continue
            for j in range(self.e):
                prod[deg - self.e + j] = (
                    prod[deg - self.e + j] - z * self.mod[j]
                ) % self.p
        return self.encode(prod[: self.e])

    def pow(self, a, n):
        out = 1
        while n:
            if n & 1:
                out = self.mul(out, a)
            a = self.mul(a, a)
            n >>= 1
        return out

    def inv(self, a):
        if a == 0:
            raise ZeroDivisionError
        return self.pow(a, self.q - 2)

    def rank(self, M):
        A = [row[:] for row in M]
        if not A:
            return 0
        nr, nc = len(A), len(A[0])
        r = 0
        for c in range(nc):
            piv = next((i for i in range(r, nr) if A[i][c] != 0), None)
            if piv is None:
                continue
            A[r], A[piv] = A[piv], A[r]
            z = self.inv(A[r][c])
            A[r] = [self.mul(z, x) for x in A[r]]
            for i in range(nr):
                if i != r and A[i][c] != 0:
                    z = A[i][c]
                    A[i] = [
                        self.sub(A[i][j], self.mul(z, A[r][j]))
                        for j in range(nc)
                    ]
            r += 1
            if r == nr:
                break
        return r


def find_beta(F, frob_power):
    exponent = frob_power + 1
    for a in range(1, F.q):
        if F.pow(a, exponent) != 1:
            return a
    raise AssertionError("no beta found")


def generator(F, ell, h, s=2, A=None):
    k = 3
    if A is None:
        A = [[1, 0], [0, 1]]
    Q = F.p ** ell
    beta = find_beta(F, Q)
    z = k - s - h
    eval_points = list(range(F.q))
    multipliers = [beta if i < z else 1 for i in range(F.q)]
    G = [[0] * (F.q + s) for _ in range(k)]
    for r in range(k):
        for j, a in enumerate(eval_points):
            G[r][j] = F.mul(multipliers[j], F.pow(a, r))
    G[1][F.q], G[1][F.q + 1] = A[0]
    G[2][F.q], G[2][F.q + 1] = A[1]
    return G, beta


def hull_dimension(F, ell, G):
    Q = F.p ** ell
    k = len(G)
    gram = []
    for i in range(k):
        row = []
        for j in range(k):
            z = 0
            for c in range(len(G[0])):
                z = F.add(z, F.mul(G[i][c], F.pow(G[j][c], Q)))
            row.append(z)
        gram.append(row)
    return k - F.rank(gram)


def min_distance(F, G):
    k = len(G)
    n = len(G[0])
    best = n + 1
    multiplicity = 0
    for msg in product(range(F.q), repeat=k):
        if all(x == 0 for x in msg):
            continue
        word = []
        for j in range(n):
            z = 0
            for i in range(k):
                z = F.add(z, F.mul(msg[i], G[i][j]))
            word.append(z)
        w = sum(x != 0 for x in word)
        if w < best:
            best, multiplicity = w, 1
        elif w == best:
            multiplicity += 1
    return best, multiplicity


def check_gf8():
    # x^3+x+1
    F = PrimePowerField(2, [1, 1, 0, 1])
    # A_zeta = [[0,1],[1,zeta]].  zeta=1 is AMDS; zeta=0 is MDS.
    rows = []
    for zeta, kind, expected_d in [(1, "AMDS/NMDS", 7), (0, "MDS", 8)]:
        A = [[0, 1], [1, zeta]]
        for h in (0, 1):
            G, beta = generator(F, ell=1, h=h, A=A)
            hd = hull_dimension(F, 1, G)
            d, mult = min_distance(F, G)
            assert hd == h
            assert d == expected_d
            rows.append((kind, h, beta, d, mult))
    return rows


def check_gf27():
    # x^3+2x+1 has no root in GF(3), so it is irreducible.
    F = PrimePowerField(3, [1, 2, 0, 1])
    rows = []
    A = [[0, 1], [1, 0]]  # zeta=0; for the full field, 0 lies in Delta_2
    for h in (0, 1):
        G, beta = generator(F, ell=2, h=h, A=A)
        hd = hull_dimension(F, 2, G)
        d, mult = min_distance(F, G)
        assert hd == h
        assert F.pow(beta, 10) != 1
        assert d == 26
        rows.append((h, beta, hd, d, mult))
    return rows


def main():
    gf8 = check_gf8()
    gf27 = check_gf27()
    print("finite-field verification: PASS")
    print("GF(8), e=3, ell=1:")
    for kind, h, beta, d, mult in gf8:
        print(f"  {kind}: h={h}, beta={beta}, d={d}, A_d={mult}")
    print("GF(27), e=3, ell=2 (ell does not divide e):")
    for h, beta, hd, d, mult in gf27:
        print(f"  h={h}, beta={beta}, hull_dim={hd}, d={d}, A_d={mult}")


if __name__ == "__main__":
    main()
