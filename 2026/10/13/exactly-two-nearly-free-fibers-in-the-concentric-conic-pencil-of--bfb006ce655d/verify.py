"""Exact characteristic-zero verification for a pencil of conic-line arrangements.

Requires Python 3 and SymPy 1.14; all polynomial operations are exact over QQ[t].
"""
import sympy as S
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import QQ

x, y, z, t = S.symbols('x y z t')
quadratic = x*x + y*y - t*z*z
lines = [(y-x+4*z), (y+x-4*z), (y-x-4*z), (y+x+4*z)]
f = S.expand(quadratic*S.prod(lines))
assert S.expand(S.prod(lines) - ((x*x+y*y-16*z*z)**2 - 4*x*x*y*y)) == 0
partials = [S.Poly(S.diff(f, v), x, y, z) for v in (x, y, z)]


def homogeneous_monomials(d):
    return [(a, b, d-a-b) for a in range(d+1) for b in range(d-a+1)]


def syzygy_matrix(d):
    basis = homogeneous_monomials(d)
    target = homogeneous_monomials(d+5)
    row = {a:i for i,a in enumerate(target)}
    M = S.zeros(len(target), 3*len(basis))
    for derivative_index, partial in enumerate(partials):
        for power, coeff in partial.terms():
            for i, m in enumerate(basis):
                M[row[tuple(power[j]+m[j] for j in range(3))], derivative_index*len(basis)+i] += coeff
    return M, basis, target


def parity(m):
    return tuple(a%2 for a in m)


def inv_factors(d):
    M, source, target = syzygy_matrix(d)
    source_parity = [parity(tuple(m[j]+int(j == derivative_index) for j in range(3)))
                     for derivative_index in range(3) for m in source]
    target_parity = [parity(m) for m in target]
    out = {}
    for p in sorted(set(source_parity)):
        columns = [i for i, value in enumerate(source_parity) if value == p]
        rows = [i for i, value in enumerate(target_parity) if value == p]
        B = M.extract(rows, columns)
        D = smith_normal_form(B, domain=QQ.poly_ring(t))
        diag = [S.Poly(D[j,j], t, domain=QQ).monic().as_expr()
                for j in range(min(B.rows, B.cols)) if D[j,j] != 0]
        out[p] = (B.cols, len(diag), [S.factor(v) for v in diag if v != 1])
    return out

expected = {
    1: {(0,0,0):(3,3,[]), (0,1,1):(2,2,[]), (1,0,1):(2,2,[]), (1,1,0):(2,2,[])},
    2: {(0,0,1):(5,5,[t-16]),(0,1,0):(5,5,[]),(1,0,0):(5,5,[]),(1,1,1):(3,3,[])},
    3: {(0,0,0):(9,9,[t-16]),(0,1,1):(7,7,[(t-8)*(t-16)]),
        (1,0,1):(7,7,[(t-8)*(t-16)]),(1,1,0):(7,7,[t-8])},
    4: {(0,0,1):(12,11,[t-16,t*(t-8)*(t-16)]),
        (0,1,0):(12,11,[(t-8)*(t-16)]),
        (1,0,0):(12,11,[(t-8)*(t-16)]),
        (1,1,1):(9,8,[t-8])}
}
for degree in range(1,5):
    observed = inv_factors(degree)
    assert observed.keys() == expected[degree].keys(), (degree, observed)
    for p, (cols, nonzero, factors) in observed.items():
        ec, en, ef = expected[degree][p]
        assert (cols, nonzero) == (ec, en), (degree, p, observed[p])
        assert len(factors) == len(ef) and all(S.expand(a-b)==0 for a,b in zip(factors,ef)), (degree,p,observed[p])
    print('degree', degree, 'Smith invariants', observed)

syzygy_eight = [-y*(x*x+3*y*y-48*z*z), -x*(3*x*x+y*y-48*z*z), 8*x*y*z]
syzygy_sixteen = [16*x*z,-16*y*z,x*x-y*y]
for value, syz in [(8,syzygy_eight), (16,syzygy_sixteen)]:
    assert S.expand(sum(a*partial.as_expr().subs(t,value) for a,partial in zip(syz,partials))) == 0

# Tangency and triple-point events are read directly from restrictions to the lines.
for line in lines:
    # All four lines are either y=+/-x+/-4z; eliminate y by its linear equation.
    yy = S.solve(line, y)[0]
    q = S.Poly(quadratic.subs(y,yy).subs(z,1), x)
    assert S.expand(S.discriminant(q.as_expr(),x) - 8*(t-8)) == 0, (line, q, S.discriminant(q.as_expr(),x))

# Pairwise line intersections include four finite vertices and two points at infinity.
assert S.expand(quadratic.subs({x:4*z,y:0}) - (16-t)*z*z) == 0
assert S.expand(quadratic.subs({x:0,y:4*z}) - (16-t)*z*z) == 0
print('VERIFY_OK: smooth t!=0; singular strata 14A1 / 6A1+4A3 at t=8 / 2A1+4D4 at t=16; mdr 4/3/2; nearly-free iff t=8 or t=16')
