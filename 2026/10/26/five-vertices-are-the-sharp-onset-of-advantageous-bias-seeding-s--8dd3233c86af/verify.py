"""Reproduce exact two-seed death-birth fixation comparisons.

Run with Python 3 and SymPy: python verify.py
All graph computations are symbolic over Q(r), not sampling.
"""
from itertools import combinations
from fractions import Fraction
import sympy as sp

r = sp.symbols('r', positive=True)

def solve_lumped(a, b):
    """Complete bipartite graph, lumped by mutant counts in each side."""
    states = [(i, j) for i in range(a + 1) for j in range(b + 1)
              if (i, j) not in ((0, 0), (a, b))]
    idx = {s: k for k, s in enumerate(states)}
    M = sp.zeros(len(states)); rhs = sp.zeros(len(states), 1)
    for k, (i, j) in enumerate(states):
        d1, d2 = r * j + b - j, r * i + a - i
        moves = [((i + 1, j), sp.Rational(a - i, a + b) * r * j / d1),
                 ((i - 1, j), sp.Rational(i, a + b) * (b - j) / d1),
                 ((i, j + 1), sp.Rational(b - j, a + b) * r * i / d2),
                 ((i, j - 1), sp.Rational(j, a + b) * (a - i) / d2)]
        for target, p in moves:
            if p == 0:
                continue
            M[k, k] += p
            if target == (a, b):
                rhs[k] += p
            elif target != (0, 0):
                M[k, idx[target]] -= p
    v = M.inv(method='DM') * rhs
    return {s: sp.factor(v[k]) for k, s in enumerate(states)}

def solve_all_states(n, edges, numeric_bias=None):
    """Independent, unlumped absorption equations on all 2**n configurations."""
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v); adj[v].add(u)
    assert all(adj)
    states = list(range(1, (1 << n) - 1))
    idx = {x: k for k, x in enumerate(states)}
    M = sp.zeros(len(states)); rhs = sp.zeros(len(states), 1)
    for x in states:
        k = idx[x]
        for u in range(n):
            mutants = sum((x >> v) & 1 for v in adj[u])
            degree = len(adj[u]); prob_mutant = r * mutants / (r * mutants + degree - mutants)
            prob = (1 - prob_mutant if ((x >> u) & 1) else prob_mutant) / n
            if numeric_bias is not None:
                prob = prob.subs(r, numeric_bias) if hasattr(prob, "subs") else prob
            if prob == 0:
                continue
            y = x ^ (1 << u)
            M[k, k] += prob
            if y == (1 << n) - 1:
                rhs[k] += prob
            elif y:
                M[k, idx[y]] -= prob
    v = M.inv(method='DM') * rhs
    return {x: sp.factor(v[idx[x]]) for x in states}

def prove_positive_on_r_ge_1(expr):
    z = sp.symbols('z', positive=True)
    num, den = sp.fraction(sp.cancel(expr))
    for p in (num, den):
        coeffs = sp.Poly(sp.expand(p.subs(r, z + 1)), z).all_coeffs()
        assert all(x >= 0 for x in coeffs), (p, coeffs)
        assert any(x > 0 for x in coeffs), p

P = 48*r**7+290*r**6+365*r**5-856*r**4-2239*r**3-1600*r**2-460*r-48
Q = 8*r**6+53*r**5+113*r**4+102*r**3+113*r**2+53*r+8
f = solve_lumped(2, 3)
high, split, low = f[(2, 0)], f[(1, 1)], f[(0, 2)]
assert sp.simplify(high - (72*r**7+535*r**6+1340*r**5+1341*r**4+794*r**3+330*r**2+80*r+8)/(10*(r+1)*Q)) == 0
assert sp.simplify(split - r*(3*r+2)*(4*r+1)*(8*r**4+51*r**3+92*r**2+27*r+2)/(12*(r+1)*Q)) == 0
assert sp.simplify(low - r**2*(20*r**5+143*r**4+335*r**3+278*r**2+107*r+17)/(3*(r+1)*Q)) == 0
assert sp.simplify(high - split + P / (60 * (r + 1) * Q)) == 0
assert sp.simplify(split - low - r*(16*r**6+128*r**5+341*r**4+326*r**3+77*r**2+8*r+4)/(12*(r+1)*Q)) == 0
assert sp.simplify(high - low - (16*r**7+175*r**6+670*r**5+1243*r**4+1312*r**3+820*r**2+240*r+24)/(30*(r+1)*Q)) == 0
assert sp.Poly(P, r).count_roots(1, sp.oo) == 1
assert P.subs(r,1) < 0 and P.subs(r,3) > 0
assert all(c > 0 for c in sp.Poly(Q, r).all_coeffs())
for e in (split - low, high - low):
    prove_positive_on_r_ge_1(e)
print('K2,3: exact rational fixation functions, unique positive threshold and dominated third orbit: PASS')

# Every connected simple graph on at most four vertices, up to isomorphism.
# Listed by edges, with a seed pair that is optimal for all r>1.
SMALL = [
    (3, [(0,1),(0,2)], (0,1), 'P3'),
    (3, [(0,1),(0,2),(1,2)], (0,1), 'K3'),
    (4, [(0,3),(1,3),(2,3)], (0,3), 'K1,3'),
    (4, [(0,1),(0,3),(1,2)], (0,1), 'P4'),
    (4, [(0,3),(1,2),(1,3),(2,3)], (1,3), 'paw'),
    (4, [(0,1),(0,3),(1,2),(2,3)], (0,1), 'C4'),
    (4, [(0,1),(0,2),(0,3),(1,2),(2,3)], (0,2), 'K4-e'),
    (4, list(combinations(range(4),2)), (0,1), 'K4'),
]
for n, edges, optimum, name in SMALL:
    v = solve_all_states(n, edges)
    fav = v[sum(1 << j for j in optimum)]
    for pair in combinations(range(n),2):
        gap = sp.factor(fav - v[sum(1 << j for j in pair)])
        if gap != 0:
            prove_positive_on_r_ge_1(gap)
    print(name, ': all competitor gaps nonnegative for r>1: PASS')

# An independent all-state check for K2,3 at exact rational bias 2 and 3.
# Comparing exact rational values avoids a second symbolic 30x30 inversion.
for bias in (sp.Rational(2), sp.Rational(3)):
    full = solve_all_states(5, [(u,v) for u in (0,1) for v in (2,3,4)], numeric_bias=bias)
    for count_state, mask in (((2,0), 3), ((1,1), 5), ((0,2), 20)):
        assert sp.cancel(full[mask]-f[count_state].subs(r,bias)) == 0
print('Independent 32-state transition system at exact rational biases: PASS')
print('All claimed verification steps completed.')
