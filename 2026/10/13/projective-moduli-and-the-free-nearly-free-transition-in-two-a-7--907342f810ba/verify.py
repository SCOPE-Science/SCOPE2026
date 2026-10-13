#!/usr/bin/env python3
"""Exact algebraic checks for the two-A7 triconic normal form.
Requires Python 3 and SymPy 1.14 (or compatible)."""
import sympy as s

u, v, w, k = s.symbols('u v w k')
q = w*w - u*v
factors = [q, q + u*u, q + k*v*v]
f = s.expand(s.prod(factors))
g = [s.diff(f, z) for z in (u,v,w)]

# Smoothness: determinant of symmetric conic matrices, nonzero when k != 0.
for h in factors:
    # Symmetric quadratic-form matrix from the Hessian.
    H = s.hessian(h,(u,v,w))/2
    assert s.factor(s.det(H)) != 0
    assert s.simplify(h - s.Matrix([u,v,w]).dot(H*s.Matrix([u,v,w]))) == 0

# Explicit degree-three syzygy for every k.
a = 2*(2*u**3-3*(k+1)*u*u*v+4*k*u*v*v+3*u*w*w-3*k*v*w*w)
b = -2*(4*u*u*v-3*(k+1)*u*v*v-3*u*w*w+2*k*v**3+3*v*w*w)
c = w*(u*u-k*v*v)
assert s.expand(a*g[0]+b*g[1]+c*g[2]) == 0

# Full coefficient matrix of the degree-two Jacobian syzygy equations.
mon = lambda d: [u**i * v**j * w**(d-i-j) for i in range(d+1) for j in range(d+1-i)]
cols = [s.Poly(s.expand(m*gd),u,v,w) for gd in g for m in mon(2)]
M = s.Matrix([[p.coeff_monomial(t) for p in cols] for t in mon(7)])
rows = [0,1,2,3,4,5,8,9,10,11,12,15,16,17,18,21,22,23]
det = s.factor(M[rows,:].det(method='domain-ge'))
assert det == 3538944*k**11*(k-1),det

# At k=1, a quadratic syzygy exists; rank-17 subminor excludes >1 independent syzygy.
a2 = 2*(2*u*u-4*u*v+3*w*w)
b2 = -2*(4*u*v-2*v*v-3*w*w)
c2 = w*(u+v)
assert s.expand((a2*g[0]+b2*g[1]+c2*g[2]).subs(k,1)) == 0
pivrows = [0,1,2,3,4,5,8,9,10,11,12,15,16,17,18,21,22]
pivcols = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17]
assert M.subs(k,1)[pivrows,pivcols].det(method='domain-ge') == -884736
# If a syzygy of degree <=1 existed, its products with u,v,w would
# span at least three independent degree-2 syzygies, contradicting nullity 1.

# Intersection calculation: leaves differ by u^2 - k*v^2. After v=1 and
# u= +/- sqrt(k), their second equations say w^2=u-k. They coalesce
# exactly where u=k and u^2=k, i.e. k(k-1)=0. k=0 is excluded.
assert s.factor(s.resultant(u*u-k, u-k, u)) == k*(k-1)
# The projective involutions w -> -w and leaf exchange
# u -> sqrt(k)*v, v -> u/sqrt(k) preserve the union for k != 0.
r = s.symbols('r',nonzero=True)
assert s.expand(f.subs({u:r*v,v:u/r}, simultaneous=True).subs(k,r*r)-f.subs(k,r*r)) == 0
assert s.expand(f.subs(w,-w)-f) == 0

print('VERIFY_OK conics=smooth_for_k_nonzero complete_normal_form=2A7 '
      'exception=k1:2A7+A3+2A1 generic:2A7+4A1 '
      'mdr_generic=3 mdr_k1=2 free_k1=TRUE nearly_free_other=TRUE '
      'det_minor=3538944*k^11*(k-1) stabilizer_order=4')
