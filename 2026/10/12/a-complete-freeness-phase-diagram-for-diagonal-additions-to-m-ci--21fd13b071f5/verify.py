#!/usr/bin/env python3
"""Exact finite checks for the diagonal-addition phase diagram."""
from itertools import combinations
from math import gcd

# Linear forms in parameter coordinates (a,b,c).
F = (1, 1, 2)
D = {
    "a+b": (1, 1, 0),
    "a-b": (1, -1, 0),
    "a+c": (1, 0, 1),
    "b+c": (0, 1, 1),
    "a+2c": (1, 0, 2),
    "b+2c": (0, 1, 2),
}

# Quotient lines in (X,Y,Z).
H = {
    "H0": (1, -1, 0),
    "H1": (1, 1, -1),
    "H2": (0, 2, -1),
    "H3": (2, 0, -1),
}
P = (1, 1, 2)

def dot(u, v):
    return sum(x*y for x, y in zip(u, v))

def cross(u, v):
    return (
        u[1]*v[2] - u[2]*v[1],
        u[2]*v[0] - u[0]*v[2],
        u[0]*v[1] - u[1]*v[0],
    )

def normalize(p):
    g = 0
    for x in p:
        g = gcd(g, abs(x))
    if g:
        p = tuple(x//g for x in p)
    for x in p:
        if x:
            if x < 0:
                p = tuple(-y for y in p)
            break
    return p

# 1. Quotient concurrency.
for name, h in H.items():
    assert dot(h, P) == 0, (name, h, P)
for h1, h2 in combinations(H.values(), 2):
    assert normalize(cross(h1, h2)) == P

# 2. Symbolic cross products L x H, with L=(a,b,c).
# Each coordinate is represented by its coefficient vector in (a,b,c).
def cross_symbolic_with_constant(h):
    # L x h = (b*h2-c*h1, c*h0-a*h2, a*h1-b*h0)
    return (
        (0, h[2], -h[1]),
        (-h[2], 0, h[0]),
        (h[1], -h[0], 0),
    )
expected = {
    "H0": {2: (1, 1, 0)},       # Z coordinate gives -(a+b), up to sign
    "H1": {0: (0, 1, 1), 1: (1, 0, 1), 2: (1, -1, 0)},
    "H2": {0: (0, 1, 2)},
    "H3": {1: (1, 0, 2)},
}
def proportional(u, v):
    return cross(u, v) == (0,0,0)
for name, coords in expected.items():
    got = cross_symbolic_with_constant(H[name])
    for idx, form in coords.items():
        assert proportional(got[idx], form), (name, idx, got[idx], form)

# 3. Parameter-line incidence classification.
points = {}
for (n1,l1),(n2,l2) in combinations(D.items(),2):
    p = normalize(cross(l1,l2))
    points[p] = {n for n,l in D.items() if dot(l,p)==0}
valid_triples = {p for p,s in points.items() if len(s)==3 and all(p) and p!=(1,1,-1)}
valid_doubles = {p for p,s in points.items() if len(s)==2 and all(p) and p!=(1,1,-1)}
assert valid_triples == {(2,2,-1)}
assert valid_doubles == {
    (1,-1,-1),(1,-1,1),(1,2,-1),(2,-2,-1),(2,-2,1),(2,1,-1)
}

# 4. The free line meets every branch line only in an inadmissible point
# or in the already-present smooth conic [1:1:-1].
allowed_bad = {(1,-1,0),(1,1,-1),(2,0,-1),(0,2,-1)}
for l in D.values():
    assert normalize(cross(F,l)) in allowed_bad

# 5. Count formula and source-theorem specialization.
def outcome(Fzero, r=None):
    if Fzero:
        k=4
    else:
        k=16-2*r
    m=k//2
    if m in (2,5):
        typ="free"
        data=(2,7) if m==2 else (4,5)
    elif m==6:
        typ="plus-one"
        data=((4,6),7)
    elif m>=7:
        typ="neither"
        data="res9" if m==7 else "res10"
    else:
        raise AssertionError((k,m))
    return k,typ,data
assert outcome(True)==(4,"free",(2,7))
assert outcome(False,3)==(10,"free",(4,5))
assert outcome(False,2)==(12,"plus-one",((4,6),7))
assert outcome(False,1)==(14,"neither","res9")
assert outcome(False,0)==(16,"neither","res10")

# 6. The two diagonal conics printed in Example 4.1.
def eval_form(l,p): return dot(l,p)
def r_value(p): return sum(eval_form(l,p)==0 for l in D.values())
C1=(1,3,-2)
C2=(1,2,-1)
assert eval_form(F,C1)==0 and all(C1) and C1!=(1,1,-1)
assert eval_form(F,C2)!=0 and r_value(C2)==2
assert outcome(True)[1:] == ("free",(2,7))
assert outcome(False,r_value(C2))[1:] == ("plus-one",((4,6),7))

# 7. Pencil sanity: all four base pencil members satisfy F=0 and span the line.
pencil_members=[(1,-1,0),(1,1,-1),(0,2,-1),(2,0,-1)]
assert all(dot(F,q)==0 for q in pencil_members)
# The first and fourth are linearly independent coefficient vectors.
assert cross(pencil_members[0],pencil_members[3]) != (0,0,0)

print("VERIFY_OK")
print("valid_triple", sorted(valid_triples))
print("valid_doubles", sorted(valid_doubles))
print("counts", [outcome(True)[0]]+[outcome(False,r)[0] for r in (3,2,1,0)])
