#!/usr/bin/env python3
"""Exact, standalone verification of five-tip rooted-PD rarefaction variance identities.

Requires only the Python standard library. All arithmetic uses fractions.Fraction.
"""
from fractions import Fraction as F
from itertools import combinations

class P:
    def __init__(self, data=None):
        self.d = {e: F(c) for e, c in (data or {}).items() if c}

    @staticmethod
    def const(q):
        return P({(0, 0, 0): F(q)})

    @staticmethod
    def variable(j):
        e = [0, 0, 0]
        e[j] = 1
        return P({tuple(e): F(1)})

    @staticmethod
    def coerce(x):
        return x if isinstance(x, P) else P.const(x)

    def __add__(self, rhs):
        rhs = P.coerce(rhs)
        out = dict(self.d)
        for e, c in rhs.d.items():
            out[e] = out.get(e, F(0)) + c
        return P(out)

    __radd__ = __add__

    def __neg__(self):
        return P({e: -c for e, c in self.d.items()})

    def __sub__(self, rhs):
        return self + (-P.coerce(rhs))

    def __rsub__(self, rhs):
        return P.coerce(rhs) - self

    def __mul__(self, rhs):
        rhs = P.coerce(rhs)
        d = {}
        for a, x in self.d.items():
            for b, y in rhs.d.items():
                e = tuple(i+j for i,j in zip(a,b))
                d[e] = d.get(e,F(0))+x*y
        return P(d)

    __rmul__ = __mul__

    def __truediv__(self, rhs):
        return self * P.const(F(1, rhs))

    def __eq__(self, rhs):
        return self.d == P.coerce(rhs).d

    def eval(self, abc):
        return sum(c*abc[0]**e[0]*abc[1]**e[1]*abc[2]**e[2]
                   for e,c in self.d.items())

A, B, C = (P.variable(j) for j in range(3))
ONE = P.const(1)

# The root and all internal nodes are tuples (age, left, right). Leaves
# are integer labels. The root age is 1 and each tip's age is 0.
TOPOLOGIES = {
    "caterpillar_1_4": (ONE, 0, (A, 1, (B, 2, (C, 3, 4)))),
    "double_cherry_1_4": (ONE, 0, (A, (B, 1, 2), (C, 3, 4))),
    "cherry_triplet_2_3": (ONE, (A, 0, 1), (B, 2, (C, 3, 4))),
}

def edge_list(tree):
    def descend(node):
        if isinstance(node, int):
            return P.const(0), frozenset([node]), []
        age, left, right = node
        lh, lm, le = descend(left)
        rh, rm, re = descend(right)
        assert not lm.intersection(rm)
        return age, lm | rm, [(age-lh, lm), (age-rh, rm)] + le + re
    age, tips, edges = descend(tree)
    assert age == ONE and tips == frozenset(range(5)) and len(edges) == 8
    return edges

def symbolic_variances(tree):
    edges = edge_list(tree)
    results = {}
    for k in range(1, 6):
        values = []
        for sample in combinations(range(5), k):
            chosen = set(sample)
            values.append(sum((w for w, descendants in edges
                               if chosen.intersection(descendants)), P.const(0)))
        count = len(values)
        mu = sum(values, P.const(0)) / count
        results[k] = sum((v*v for v in values), P.const(0)) / count - mu*mu
    return results

V = {key: symbolic_variances(tree) for key, tree in TOPOLOGIES.items()}
for name, var in V.items():
    assert var[1] == 0 and var[5] == 0, name

# Exact identity for 1+4 caterpillar. Set x=1-a, y=a-b, z=b-c.
x, y, z = ONE-A, A-B, B-C
P0 = -(12*x*y + 8*x*z + 15*y*y + 18*y*z + 12*z*z) / 100
assert V['caterpillar_1_4'][2] - V['caterpillar_1_4'][3] == P0

# Exact identity for the other 1+4 tree. Set x=1-a,
# y=a-b, z=a-c. All are positive for positive ultrametric edges.
x, y, z = ONE-A, A-B, A-C
P1 = -4*(2*x*(y+z) + 3*y*y - 4*y*z + 3*z*z) / 100
assert V['double_cherry_1_4'][2] - V['double_cherry_1_4'][3] == P1

# Exact shape-phase diagram for the 2+3 split, with 0<a<1,0<c<b<1.
P23 = (-12*A*A + 26*A*B + 16*A*C - 18*A - 9*B*B + 6*B*C
       - 14*B - 12*C*C + 2*C + 15) / 100
P43 = (3*A*A + 14*A*B - 14*A*C - 6*A - 9*B*B - 6*B*C
       + 10*B + 3*C*C + 14*C - 9) / 100
assert V['cherry_triplet_2_3'][2] - V['cherry_triplet_2_3'][3] == P23
assert V['cherry_triplet_2_3'][4] - V['cherry_triplet_2_3'][3] == P43

EXAMPLE = (F(1, 4), F(3, 4), F(2, 3))
var = V['cherry_triplet_2_3']
assert [var[k].eval(EXAMPLE) for k in range(1,6)] == [
    F(0), F(263, 4800), F(19, 400), F(29, 600), F(0)]
assert P23.eval(EXAMPLE) == F(7, 960)
assert P43.eval(EXAMPLE) == F(1, 1200)

# Independently evaluate all 31 nonempty sample subsets numerically,
# with exact fractions, without using the symbolic variance routine.
def concrete_edges():
    a, b, c = EXAMPLE
    return [
        (F(1)-a, {0,1}), (a,{0}), (a,{1}),
        (F(1)-b,{2,3,4}), (b,{2}), (b-c,{3,4}),
        (c,{3}), (c,{4})]
assert all(weight>0 for weight,_ in concrete_edges())
for k in range(1,6):
    values = [sum((weight for weight, descendants in concrete_edges()
                   if set(sample) & descendants), F(0))
              for sample in combinations(range(5),k)]
    mean = sum(values,F(0)) / len(values)
    variance = sum((value-mean)**2 for value in values) / len(values)
    assert variance == var[k].eval(EXAMPLE)

print("PASS: three five-tip topologies, exact symbolic differences,")
print("      complete 2+3 phase inequalities, positive ultrametric witness,")
print("      and all 31 independent exact subset evaluations.")
