#!/usr/bin/env python3
"""Exhaustive GF(2) group-law check for two five-dimensional monomial local algebras."""
from itertools import product

class Algebra:
    def __init__(self, basis, generators):
        self.basis = basis
        self.pos = {a: i for i, a in enumerate(basis)}
        self.one = 1 << self.pos[(0, 0)]
        self.x = 1 << self.pos[(1, 0)]
        self.y = 1 << self.pos[(0, 1)]
        self.x2 = 1 << self.pos[(2, 0)] if (2, 0) in self.pos else 0
        self.y2 = 1 << self.pos[(0, 2)] if (0, 2) in self.pos else 0
        self.xy = 1 << self.pos[(1, 1)] if (1, 1) in self.pos else 0
        self.generators = generators

    def mul(self, a, b):
        z = 0
        for i, ei in enumerate(self.basis):
            if not (a >> i) & 1:
                continue
            for j, ej in enumerate(self.basis):
                if not (b >> j) & 1:
                    continue
                t = self.pos.get((ei[0] + ej[0], ei[1] + ej[1]))
                if t is not None:
                    z ^= 1 << t
        return z

    def power(self, a, e):
        z = self.one
        for _ in range(e):
            z = self.mul(z, a)
        return z

    def eval(self, images, a):
        x, y = images
        z = 0
        for i, (u, v) in enumerate(self.basis):
            if (a >> i) & 1:
                z ^= self.mul(self.power(x, u), self.power(y, v))
        return z

    def compose(self, f, g):
        # f after g
        return (self.eval(f, g[0]), self.eval(f, g[1]))

    def enumerated_aut(self):
        ans = set()
        for a in range(0, 1 << len(self.basis), 2):
            for b in range(0, 1 << len(self.basis), 2):
                # tangent determinant over F2, with coordinates (x,y)
                xa, ya = ((a & self.x) != 0), ((a & self.y) != 0)
                xb, yb = ((b & self.x) != 0), ((b & self.y) != 0)
                if (xa and yb) == (ya and xb):
                    continue
                if all(self.mul(self.power(a, u), self.power(b, v)) == 0
                       for u, v in self.generators):
                    ans.add((a, b))
        return ans

A = Algebra([(0,0),(1,0),(0,1),(0,2),(1,1)], [(2,0),(1,2),(0,3)])
B = Algebra([(0,0),(1,0),(0,1),(2,0),(0,2)], [(1,1),(3,0),(0,3)])
AutA = A.enumerated_aut()
AutB = B.enumerated_aut()
assert len(AutA) == len(AutB) == 32
C = Algebra([(0,0),(1,0),(0,1),(0,2)], [(2,0),(1,1),(0,3)])
D = Algebra([(0,0),(1,0),(0,1),(1,1)], [(2,0),(0,2)])
assert len(C.enumerated_aut()) == 8
assert len(D.enumerated_aut()) == 24

def nA(u,v,s,r):
    return (A.x ^ (u * A.y2) ^ (v * A.xy),
            A.y ^ (s * A.y2) ^ (r * A.xy))

def nB(u,v,s,r):
    # C = u E11 + v E12 + s I + r S.
    return (B.x ^ ((u ^ s) * B.x2) ^ (r * B.y2),
            B.y ^ ((v ^ r) * B.x2) ^ (s * B.y2))

TA = (A.x, A.y ^ A.x)
SB = (B.y, B.x)
assert A.compose(TA,TA) == (A.x,A.y)
assert B.compose(SB,SB) == (B.x,B.y)

bijection = {}
for u,v,s,r,t in product((0,1),repeat=5):
    a = A.compose(TA,nA(u,v,s,r)) if t else nA(u,v,s,r)
    b = B.compose(SB,nB(u,v,s,r)) if t else nB(u,v,s,r)
    assert a in AutA and b in AutB
    assert a not in bijection
    bijection[a] = b
assert len(bijection) == 32 and set(bijection.values()) == AutB
for f in AutA:
    for g in AutA:
        assert bijection[A.compose(f,g)] == B.compose(bijection[f],bijection[g])

# Frobenius-square map on the cotangent space is distinguished by its kernel.
A_sq = [A.power(0,2), A.power(A.x,2), A.power(A.y,2), A.power(A.x ^ A.y,2)]
B_sq = [B.power(0,2), B.power(B.x,2), B.power(B.y,2), B.power(B.x ^ B.y,2)]
assert sum(z == 0 for z in A_sq) == 2
assert sum(z == 0 for z in B_sq) == 1
print('VERIFY_OK: A,B have 32 automorphisms each; 1,024 isomorphism-law checks; dimension-four comparison 8 versus 24; distinct square-map kernels.')
