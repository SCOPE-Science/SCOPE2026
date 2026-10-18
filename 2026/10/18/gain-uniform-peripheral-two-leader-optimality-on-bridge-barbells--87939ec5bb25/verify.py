#!/usr/bin/env python3
"""Exact algebraic verification for optimal two-leader barbell placement.

Requires Python 3 and SymPy. No external files or external services.
"""
from itertools import combinations
import sympy as sp

m, k = sp.symbols('m k', positive=True)


def quotient(types):
    """Types on each side: (hub_pinned, count_pinned_interior)."""
    groups = []
    for side, (hub_pin, pin_interior) in enumerate(types):
        groups.append((side, True, sp.Integer(1), hub_pin))
        if pin_interior:
            groups.append((side, False, sp.Integer(pin_interior), True))
        # For m >= 4, this group is nonempty for every case.
        # At m = 3, a zero-size group is omitted in the direct checks below.
        groups.append((side, False, m - 1 - pin_interior, False))
    groups = [g for g in groups if g[2] != 0]
    Q = sp.zeros(len(groups))
    for i, (side, hub, size, pin) in enumerate(groups):
        degree = m if hub else m - 1
        Q[i, i] = degree + (k if pin else 0) - (0 if hub else size - 1)
        for j, (side2, hub2, size2, _) in enumerate(groups):
            if i != j and (side == side2 or (hub and hub2)):
                Q[i, j] = -size2
    return sp.factor(sp.trace(Q.inv()) + sum(
        (size - 1)/(m + (k if pin else 0))
        for _, hub, size, pin in groups if not hub
    ))


orbit_types = {
    'opposite_interior': ((False, 1), (False, 1)),
    'opposite_hub_interior': ((True, 0), (False, 1)),
    'both_hubs': ((True, 0), (True, 0)),
    'same_hub_interior': ((True, 1), (False, 0)),
    'same_two_interior': ((False, 2), (False, 0)),
}
T = k*(m+4) + 2*m
U = k*(m+2) + 2*m
J0 = 2*(k**2*(2*m**2+5*m-10)+k*(m**3+6*m**2-4*m)+m**3)/(k*m*T)
D = {
    'opposite_interior': 0,
    'opposite_hub_interior': k*(k*(m+2)+2*m**2+2*m+4)/(U*T),
    'both_hubs': 2*k*(k*(m+2)+2*m**2+2*m+4)/(m*(k+2)*T),
    'same_hub_interior': (k**2*(2*m**2+7*m-2)+k*(2*m**3+10*m**2+2*m+4)+2*m**3)/(2*(k+m)*T),
    'same_two_interior': (k**2*(m**2+5*m+5)+k*(m**3+6*m**2+8*m+2)+m**3+2*m**2)/((k+m)*T),
}

for name, params in orbit_types.items():
    symbolic = quotient(params)
    assert sp.cancel(symbolic - J0 - D[name]) == 0, name
print('Five rational trace formulas and their factored differences: exact symbolic PASS.')

# At m=3 one peripheral part of the same-clique PP orbit is empty.
# Verify the boundary symbolically in gain after omitting that part.
Q3 = sp.zeros(5)
# Parts: left hub (1), left pinned peripherals (2), right hub (1),
# right unpinned peripherals (2).  The true quotient therefore has 4 parts.
Q3 = sp.Matrix([[3,-2,-1,0],[-1,1+k,0,0],[-1,0,3,-2],[0,0,-1,1]])
J3 = sp.factor(sp.trace(Q3.inv()) + 1/(3+k) + 1/3)
assert sp.cancel(J3 - (J0 + D['same_two_interior']).subs(m,3)) == 0
print('Boundary m=3 with its empty part omitted: symbolic PASS.')


def direct_laplacian(order):
    N = 2*order
    L = sp.zeros(N)
    edges = []
    for side in (0, 1):
        for a, b in combinations(range(order), 2):
            edges.append((side*order+a, side*order+b))
    edges.append((0, order))
    for i, j in edges:
        L[i, i] += 1
        L[j, j] += 1
        L[i, j] -= 1
        L[j, i] -= 1
    return L


def kind(u, v, n):
    same = (u//n == v//n)
    hubs = (u % n == 0) + (v % n == 0)
    return ('same_two_interior' if same and hubs == 0 else
            'same_hub_interior' if same else
            'both_hubs' if hubs == 2 else
            'opposite_hub_interior' if hubs == 1 else
            'opposite_interior')

count = 0
for n in (3, 4, 5, 6):
    L = direct_laplacian(n)
    for gain in (sp.Rational(1, 3), sp.Integer(1), sp.Rational(7, 2)):
        actual = {}
        for i, j in combinations(range(2*n), 2):
            key = kind(i, j, n)
            if key in actual:
                continue
            M = L.copy()
            M[i, i] += gain
            M[j, j] += gain
            measured = sp.trace(M.inv())
            expected = (J0 + D[key]).subs({m:n, k:gain})
            assert sp.cancel(measured - expected) == 0, (n, gain, key)
            actual[key] = measured
            count += 1
        assert len(actual) == 5
        assert all(actual['opposite_interior'] < value
                   for key, value in actual.items()
                   if key != 'opposite_interior')
print(f'{count} full-matrix rational orbit tests: PASS.')
print('All positivity follows analytically from factored coefficients for m>=3 and k>0.')
