#!/usr/bin/env python3
"""Finite checks for the norm-one-torus sampling theorem in characteristic 3."""
from itertools import product, combinations
from collections import Counter

P = 3

def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] % P == 0:
        a.pop()
    return tuple(x % P for x in a)

def poly_divmod(f, g):
    f, g = list(trim(f)), list(trim(g))
    inv = pow(g[-1], -1, P)
    q = [0] * max(1, len(f) - len(g) + 1)
    while len(f) >= len(g) and not (len(f) == 1 and f[0] == 0):
        c = f[-1] * inv % P
        d = len(f) - len(g)
        q[d] = c
        for i, gi in enumerate(g):
            f[d+i] = (f[d+i] - c*gi) % P
        f = list(trim(f))
    return trim(q), trim(f)

def monic_polys(deg):
    for coeff in product(range(P), repeat=deg):
        yield tuple(coeff) + (1,)

def irreducible(f):
    m = len(f) - 1
    for d in range(1, m//2 + 1):
        for g in monic_polys(d):
            if poly_divmod(f, g)[1] == (0,):
                return False
    return True

class GF3m:
    def __init__(self, m):
        self.m, self.q = m, P**m
        if m == 1:
            self.mod = (0, 1)
        else:
            self.mod = next(f for f in monic_polys(m) if f[0] and irreducible(f))
        self.coeffs = [self._decode(i) for i in range(self.q)]
    def _decode(self, a):
        c = []
        for _ in range(self.m):
            c.append(a % P); a //= P
        return tuple(c)
    def _encode(self, c):
        return sum((x % P) * (P**i) for i, x in enumerate(c))
    def add(self, a, b):
        return self._encode(tuple((x+y) % P for x,y in zip(self.coeffs[a], self.coeffs[b])))
    def neg(self, a):
        return self._encode(tuple((-x) % P for x in self.coeffs[a]))
    def sub(self, a, b): return self.add(a, self.neg(b))
    def mul(self, a, b):
        ca, cb = self.coeffs[a], self.coeffs[b]
        z = [0] * (2*self.m - 1)
        for i,x in enumerate(ca):
            for j,y in enumerate(cb): z[i+j] = (z[i+j] + x*y) % P
        for deg in range(len(z)-1, self.m-1, -1):
            c = z[deg] % P
            if c:
                for i in range(self.m):
                    z[deg-self.m+i] = (z[deg-self.m+i] - c*self.mod[i]) % P
        return self._encode(tuple(z[:self.m]))
    def pow(self, a, e):
        r, x = 1, a
        while e:
            if e & 1: r = self.mul(r, x)
            x = self.mul(x, x); e >>= 1
        return r
    def inv(self, a): return self.pow(a, self.q-2)
    def chi(self, a):
        if a == 0: return 0
        z = self.pow(a, (self.q-1)//2)
        return 1 if z == 1 else -1

def kadd(x,y,F): return (F.add(x[0],y[0]), F.add(x[1],y[1]))
def kneg(x,F): return (F.neg(x[0]), F.neg(x[1]))
def ksub(x,y,F): return kadd(x,kneg(y,F),F)
def knorm(x,F,d): return F.sub(F.mul(x[0],x[0]), F.mul(d,F.mul(x[1],x[1])))

def verify(m):
    F = GF3m(m); q = F.q
    d = next(a for a in range(1,q) if F.chi(a) == -1)
    T = [(a,b) for a in range(q) for b in range(q) if knorm((a,b),F,d) == 1]
    assert len(T) == q+1
    Tset = set(T)
    T2 = {kadd(x,y,F) for x in T for y in T}
    length3 = [(a,b) for a in range(q) for b in range(q)
               if (a,b) != (0,0) and (a,b) not in Tset and (a,b) not in T2]
    triple_counts = Counter()
    for x,y,z in combinations(T,3):
        triple_counts[kadd(kadd(x,y,F),z,F)] += 1
    by_M = Counter()
    for S in length3:
        n = knorm(S,F,d)
        M = 0
        for beta in T:
            B = ksub(S,beta,F)
            a = knorm(B,F,d)
            assert a not in (0,1)
            if F.chi(F.sub(1,F.inv(a))) == -1:
                M += 1
        J = 0
        for a in range(q):
            c = F.sub(F.add(n,1), a)
            Delta = F.sub(F.mul(c,c), n)  # 4=1 in characteristic 3
            quartic = F.mul(F.mul(a,F.sub(a,1)), Delta)
            J += F.chi(quartic)
        assert 2*M == q + 2 + J
        assert abs(2*M - (q+1)) <= 2*(q**0.5) + 1e-12
        assert M % 3 == 0
        assert triple_counts[S] == M // 3
        assert abs((M//3) - (q+1)/6) <= (q**0.5)/3 + 1e-12
        by_M[M] += 1
    return q, len(T2), len(length3), min(by_M) if by_M else None, max(by_M) if by_M else None, dict(sorted(by_M.items()))

for m in (2,3,4):
    q,t2,l3,mn,mx,hist = verify(m)
    print(f"q={q}: |T+T|={t2}, length3={l3}, success-count range={mn}..{mx}, leader-count range={mn//3}..{mx//3}, histogram={hist}")
print("PASS")
