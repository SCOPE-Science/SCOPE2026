#!/usr/bin/env python3
"""Exact standard-library Saito determinant checks for several admissible members.
The accompanying proof establishes the universal parameter statement; these
finite symbolic checks are independent consistency tests, not its proof.
"""
from fractions import Fraction

class Ring:
    def __init__(self, characteristic):
        self.p = characteristic
        self.x, self.y, self.z = [self.monomial(i) for i in range(3)]

    def norm(self, value):
        return value % self.p if self.p else Fraction(value)

    def poly(self, data):
        return Poly(self, data)

    def const(self, value):
        return self.poly({(0, 0, 0): value})

    def monomial(self, i):
        exp = [0, 0, 0]
        exp[i] = 1
        return self.poly({tuple(exp): 1})

    def inverse(self, n):
        return pow(n, -1, self.p) if self.p else Fraction(1, n)

class Poly:
    def __init__(self, ring, data):
        self.ring = ring
        self.d = {e: ring.norm(c) for e, c in data.items() if ring.norm(c) != 0}

    def __add__(self, other):
        if not isinstance(other, Poly):
            other = self.ring.const(other)
        v = dict(self.d)
        for e, c in other.d.items():
            v[e] = v.get(e, 0) + c
        return self.ring.poly(v)

    __radd__ = __add__

    def __neg__(self):
        return self.ring.poly({e: -c for e, c in self.d.items()})

    def __sub__(self, other):
        return self + (-other if isinstance(other, Poly) else -self.ring.const(other))

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        if not isinstance(other, Poly):
            other = self.ring.const(other)
        v = {}
        for e, a in self.d.items():
            for f, b in other.d.items():
                ef = tuple(e[i] + f[i] for i in range(3))
                v[ef] = v.get(ef, 0) + a*b
        return self.ring.poly(v)

    __rmul__ = __mul__

    def __pow__(self, n):
        assert n >= 0 and isinstance(n, int)
        out, base = self.ring.const(1), self
        while n:
            if n % 2:
                out = out*base
            base = base*base
            n //= 2
        return out

    def diff(self, i):
        return self.ring.poly({tuple(e[j] - (j == i) for j in range(3)): c*e[i]
                               for e, c in self.d.items() if e[i]})

    def __eq__(self, other):
        if not isinstance(other, Poly):
            other = self.ring.const(other)
        return self.d == other.d


def det(v, w, t):
    return (v[0]*(w[1]*t[2]-w[2]*t[1])
            - v[1]*(w[0]*t[2]-w[2]*t[0])
            + v[2]*(w[0]*t[1]-w[1]*t[0]))


def apply(v, f):
    return sum(v[i]*f.diff(i) for i in range(3))


def check(p, weights, slopes):
    R = Ring(p)
    x, y, z = R.x, R.y, R.z
    # First linear form x, remaining forms y or x+a*y; all distinct in k.
    ell = [x] + [(y if a is None else x+a*y) for a in slopes]
    coeff = [0] + [(1 if a is None else a) for a in slopes]
    assert len(ell) == len(weights) and len(set(str(t.d) for t in ell)) == len(ell)
    m, d = len(weights), sum(weights)
    assert m >= 2 and all(t >= 1 for t in weights)
    G = R.const(1)
    P = R.const(1)
    L = R.const(1)
    for j, f in enumerate(ell):
        G = G*f
        P = P*(f**weights[j])
        if j:
            L = L*f
    H = P-z**d
    F = G*H
    alpha, beta = R.const(0), R.const(0)
    for j in range(1, m):
        q = R.const(coeff[j])
        for h in range(1, m):
            if h != j:
                q = q*ell[h]
        alpha += q
        beta += weights[j]*q
    assert L*G.diff(1) == alpha*G
    assert L*P.diff(1) == beta*P
    # Coordinates of A=L partial_y; first line is x.
    A = (R.const(0), L, R.const(0))
    assert det((x, y, R.const(0)), A, (R.const(0), R.const(0), R.const(1))) == G
    wild = bool(p and d % p == 0)
    assert (not wild) or any(t % p for t in weights)
    if not wild:
        e = (x, y, z)
        a = (R.const(0), L, z*beta*R.inverse(d))
        t = (x*z**(d-1), y*z**(d-1), P)
        assert det(e, a, t) == F
        assert apply(e, F) == (d+m)*F
        assert apply(a, F) == (alpha+beta)*F
        assert apply(t, F) == m*z**(d-1)*F
        assert F.diff(2) != 0
    else:
        v0 = (R.const(0), R.const(0), R.const(1))
        v1 = (x, y, R.const(0))
        v2 = (R.const(0), H*L, R.const(0))
        assert det(v0, v1, v2) == F
        assert apply(v0, F) == 0
        assert apply(v1, F) == m*F
        assert apply(v2, F) == (alpha*H+beta*P)*F
        assert F.diff(2) == 0
        assert H.diff(0) != 0 or H.diff(1) != 0
    return ('wild' if wild else 'ordinary', (0,1,d+m-1) if wild else (1,m-1,d))


def main():
    cases = [
        (0,[1,2],[None]),
        (0,[2,1,3],[None,1]),
        (0,[1,1,1,2],[None,1,2]),
        (2,[1,1],[None]),
        (2,[1,1,2],[None,1]),
        (2,[1,2,2],[None,1]),
        (3,[1,2],[None]),
        (3,[1,1,1],[None,1]),
        (3,[1,1,2],[None,1]),
        (5,[1,1,1,2],[None,1,2]),
        (5,[1,1,1,3],[None,1,2]),
        (7,[1,6],[None]),
        (7,[1,1,2],[None,1]),
    ]
    for p, k, a in cases:
        print('p=%s k=%s: %s %s' % (p, k, *check(p, k, a)))
    print('VERIFY_OK: exact coefficient-ring logarithmic identities and unit determinants in 13 cases')

if __name__ == '__main__':
    main()
