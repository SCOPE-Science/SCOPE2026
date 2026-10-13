"""Exact small-network checks for a parametric undirected opinion equilibrium.

Requires Python 3 and SymPy. Finite checks supplement, not replace, the
spectral and partial-fraction proof in RESULT.md.
"""
from sympy import Matrix, symbols, eye, zeros, cancel, Poly, prod, simplify, solve, Rational


def path_laplacian(n):
    matrix = zeros(n)
    for i in range(n - 1):
        matrix[i, i] += 1
        matrix[i+1, i+1] += 1
        matrix[i, i+1] -= 1
        matrix[i+1, i] -= 1
    return matrix


def check_prescribed_crossings(n):
    t = symbols('t')
    L = path_laplacian(n)
    A = eye(n) + t*L
    denominator = A.det()
    unknowns = symbols('s0:'+str(n))
    diff = cancel(((A.inv() * Matrix(unknowns))[0] - (A.inv() * Matrix(unknowns))[1])*denominator)
    target = prod(t-j for j in range(1, n-1))
    equations = Poly(diff-target,t).all_coeffs() + [sum(unknowns)]
    ans = solve(equations, unknowns, dict=True)
    assert len(ans) == 1, (n, len(ans))
    raw = Matrix([ans[0][z] for z in unknowns])
    span = max(raw)-min(raw)
    assert span > 0
    normalized = (raw-Matrix([min(raw)]*n))/span
    assert min(normalized) == 0 and max(normalized) == 1
    value = cancel((A.inv()*normalized)[0] - (A.inv()*normalized)[1])
    assert simplify(value-target/(span*denominator)) == 0
    assert all(simplify(value.subs(t,j)) == 0 for j in range(1,n-1))
    return normalized, span, denominator


n3, _, _ = check_prescribed_crossings(3)
n4, _, _ = check_prescribed_crossings(4)
n5, span5, den5 = check_prescribed_crossings(5)
n6, _, _ = check_prescribed_crossings(6)
assert n5 == Matrix([Rational(59,152),Rational(65,152),Rational(9,76),1,0])
assert span5 == 152
assert simplify(den5-(symbols('t')**2+3*symbols('t')+1)*(5*symbols('t')**2+5*symbols('t')+1))==0
print('VERIFY_OK exact_path_profiles=4 designed_crossings=1+2+3+4 explicit_five_path=1', flush=True)
