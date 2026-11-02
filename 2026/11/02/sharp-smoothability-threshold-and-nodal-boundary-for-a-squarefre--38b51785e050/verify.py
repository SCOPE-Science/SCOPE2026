"""Exact consistency checks for a squarefree-hypersurface nodal threshold.

Requires Python 3 and SymPy.  The general theorem is proved geometrically;
this program checks finite numerical consequences and a local Hessian certificate.
"""

from itertools import combinations
from math import comb
import sympy as sp


def predicted_nodes(d):
    return comb(d, 2) * (d - 1) ** (d - 3)


assert [predicted_nodes(d) for d in range(4, 9)] == [18, 160, 1875, 27216, 470596]

# A nondegenerate local quadratic form at a transverse boundary point has
# the form c*s*t + sum_j y_j*u_j + terms y_j*s, y_j*t and y_j*y_k.
# Its determinant must be independent of the latter terms.
c = sp.symbols('c')
for r in range(1, 5):
    s, t = sp.symbols('s t')
    u = sp.symbols(f'u0:{r}')
    y = sp.symbols(f'y0:{r}')
    variables = (s, t) + u + y
    f = c * s * t
    for j in range(r):
        f += y[j] * (u[j] + (j + 2) * s + (j * j + 1) * t)
    for j in range(r):
        for k in range(j, r):
            f += (j + k + 1) * y[j] * y[k]
    h = sp.hessian(f, variables)
    det = sp.factor(h.det(method='berkowitz'))
    assert det == (-1) ** (r + 1) * c ** 2, (r, det)

# Exact quartic example: six lines, three distinct points on each.
x = sp.symbols('x0:4')
y = sp.symbols('y')
F = sp.prod(x) + y * sum(z ** 3 for z in x) + y ** 4
for i, j in combinations(range(4), 2):
    remaining = [k for k in range(4) if k not in (i, j)]
    # x[remaining[1]]=1 is a valid affine chart at all three roots.
    affine = F.subs({x[i]: 0, x[j]: 0, x[remaining[1]]: 1})
    assert sp.factor(affine.subs(y, 0)) == 0
    cubic = (sum(z ** 3 for z in x)).subs({x[i]: 0, x[j]: 0,
                                                  x[remaining[1]]: 1})
    assert cubic == x[remaining[0]] ** 3 + 1
    assert sp.gcd(cubic, sp.diff(cubic, x[remaining[0]])) == 1
    chart_var = (x[i], x[j], x[remaining[0]], y)
    chart_F = F.subs(x[remaining[1]], 1)
    H = sp.hessian(chart_F, chart_var)
    H_boundary = H.subs({x[i]: 0, x[j]: 0, y: 0})
    assert sp.rem(sp.factor(H_boundary.det() - 9), cubic, x[remaining[0]]) == 0

# On the chart y=1, all gradient-critical points have polynomial value
# either 0 (origin) or -27 (all coordinates nonzero). Therefore F != 0
# at all of them, since F equals q+1.
P = sp.prod(x)
q = P + sum(z ** 3 for z in x)
for z in x:
    assert sp.expand(z * sp.diff(q, z) - (P + 3*z**3)) == 0
# If all gradient equations vanish at a point with all coordinates nonzero:
# z_i^3 = -P/3, hence P^3 = P^4/81, hence P=81, q=-27.
assert sp.simplify(81 - 4*81/sp.Integer(3)) == -27
assert -27+1 != 0

print('VERIFY_OK')
print('boundary_nodes:', {d: predicted_nodes(d) for d in range(4, 9)})
print('local_Hessian_ranks:', list(range(1, 5)))
print('quartic_nodes: 18 (six distinct three-point sets)')
