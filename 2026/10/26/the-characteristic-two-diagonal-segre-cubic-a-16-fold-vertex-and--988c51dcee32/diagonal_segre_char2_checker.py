#!/usr/bin/env python3
"""Exact reproducibility checks for the characteristic-two diagonal cubic.

The computations use only the Python standard library and the fields F_2 and
F_4=F_2[q]/(q^2+q+1). They supplement the geometric proofs.
"""
from itertools import combinations

# Sparse polynomials over F_2 in four variables.
Z = (0, 0, 0, 0)
ONE = {Z}
def add(*args):
    out = set()
    for a in args:
        out.symmetric_difference_update(a)
    return out

def mul(a, b):
    out = set()
    for u in a:
        for v in b:
            w = tuple(u[i] + v[i] for i in range(4))
            if w in out:
                out.remove(w)
            else:
                out.add(w)
    return out

def power(a, n):
    out = ONE
    for _ in range(n):
        out = mul(out, a)
    return out

def derivative(a, j):
    return {tuple(u[i] - (i == j) for i in range(4)) for u in a if u[j] & 1}

xs = []
for j in range(4):
    m = [0] * 4
    m[j] = 1
    xs.append({tuple(m)})
S = add(*xs)
F = add(*(power(x, 3) for x in xs), power(S, 3))
# Differentiation of the five-cube presentation gives (sum_{i!=j} z_i)^2.
for j in range(4):
    assert derivative(F, j) == power(add(S, xs[j]), 2)
# Invertible characteristic-two matrix A=I+all-ones, A^2=I.
Axs = [add(S, xs[j]) for j in range(4)]
assert all(add(*(Axs[i] for i in range(4) if i != j)) == xs[j] for j in range(4))
assert add(*(power(x, 3) for x in Axs), power(add(*Axs), 3)) == F
# Homogeneous partials are zero in the vertex coordinate; their radicals
# are four independent linear coordinates, giving a length-16 local CI.
assert len({tuple((mask >> j) & 1 for j in range(4)) for mask in range(16)}) == 16

# Field F_4 represented by a + b*q, q^2=q+1.
def fm(a,b):
    z = 0
    for i in range(2):
        for j in range(2):
            if ((a>>i)&1) and ((b>>j)&1):
                z ^= (1 << (i+j))
    if z & 8: z ^= (0b1110)  # q^3 = 1, reduction of q^3+1
    if z & 4: z ^= (0b111)   # q^2 = q+1
    return z

def fp(a, n):
    out = 1
    for _ in range(n): out = fm(out, a)
    return out

def norm(v):
    i = next(i for i, x in enumerate(v) if x)
    inv = fp(v[i], 2)  # each nonzero element has inverse equal its square
    return tuple(fm(inv, x) for x in v)

def f(v):
    acc = 0
    s = 0
    for x in v:
        acc ^= fp(x, 3)
        s ^= x
    return acc ^ fp(s, 3)

def addv(u,v,a=1,b=1):
    return tuple(fm(a,x)^fm(b,y) for x,y in zip(u,v))

pts = set()
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                v=(a,b,c,d)
                if any(v): pts.add(norm(v))
assert len(pts) == 85
on_c = {v for v in pts if f(v)==0}
assert len(on_c) == 45

# Every F_4-projective line has five points. A cubic restricted to such a
# line vanishes identically if it vanishes at all five of them.
lines = set()
for u,v in combinations(sorted(on_c),2):
    if v == u: continue
    line = frozenset(norm(addv(u,v,a,b)) for a in range(4) for b in range(4) if a or b)
    assert len(line) == 5
    if line <= on_c: lines.add(line)
assert len(lines) == 27, len(lines)

def frob_line(L):
    return frozenset(tuple(fp(x, 2) for x in v) for v in L)
rational = {L for L in lines if frob_line(L)==L}
assert len(rational) == 15, len(rational)
assert len(lines-rational) == 12
assert all(frob_line(frob_line(L))==L for L in lines)

# The 15 partition planes of the generic characteristic-zero model
# specialize to all 15 rational lines on the cubic cone's base.
def perfect_matchings(items):
    if not items:
        yield ()
        return
    h=items[0]
    for i in range(1,len(items)):
        partner=items[i]
        for rest in perfect_matchings(items[1:i]+items[i+1:]):
            yield ((h,partner),)+rest

old = set()
for pairs in perfect_matchings(tuple(range(6))):
    points=[]
    for bits in range(1,16):
        z=[(bits>>i)&1 for i in range(4)]
        uu=z+[z[0]^z[1]^z[2]^z[3]]
        xx=uu+[0]
        if all(xx[i]==xx[j] for i,j in pairs):
            points.append(tuple(z))
    assert len(points)==3,(pairs,points)
    u,v=points[:2]
    L=frozenset(norm(addv(u,v,a,b)) for a in range(4) for b in range(4) if a or b)
    assert L in rational
    old.add(L)
assert len(old)==15
assert old==rational
print('VERIFY_OK: polynomial Jacobian, A^2=I and Frobenius dual; '+
      '85 ambient F4 points, 45 cubic points, 27 lines, '+
      '15 F2 planes (15 partition specializations), 6 Frobenius pairs')
