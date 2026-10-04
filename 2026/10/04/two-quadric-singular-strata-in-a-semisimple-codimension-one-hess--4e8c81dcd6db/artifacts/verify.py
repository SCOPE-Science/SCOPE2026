import sympy as sp
from itertools import permutations

# Local incidence chart at a singular point of the +1 eigenvalue stratum.
x,y,z,u,p,q = sp.symbols('x y z u p q')
F1 = u + x + p*y + q*z
F2 = u + x - p*y - q*z
Fp = sp.expand((F1+F2)/2)
Fm = sp.expand((F1-F2)/2)
assert Fp == u+x
assert Fm == p*y+q*z

g = Fm
vars4 = (p,q,y,z)
grad = [sp.diff(g,t) for t in vars4]
assert grad == [y,z,p,q]
H = sp.hessian(g, vars4)
assert H.rank() == 4
assert sp.factor(H.det()) != 0

# Insko--Precup Example 5.5 patch: after an invertible triangular change,
# the cubic-looking equation is a nondegenerate quadric in four variables.
a,r,s = sp.symbols('a r s')
source = p*a*s - p*r - q*s
rr = sp.symbols('rr')
changed = sp.expand(source.subs(r, rr+a*s))
assert changed == -p*rr-q*s
H2 = sp.hessian(changed, (p,q,rr,s))
assert H2.rank() == 4 and H2.det() != 0

# The global description predicts eight singular torus-fixed flags:
# among the 24 permutations of the labelled eigenvalues, the first and
# fourth entries must have the same eigenvalue. This gives 4 per component.
evals = [1,1,-1,-1]
count = 0
by_sign = {1:0,-1:0}
for perm in permutations(range(4)):
    vals = [evals[i] for i in perm]
    if vals[0] == vals[3]:
        count += 1
        by_sign[vals[0]] += 1
assert count == 8
assert by_sign == {1:4,-1:4}

print('local_equations', Fp, Fm)
print('node_hessian_det', H.det())
print('source_patch_normal_form', changed)
print('singular_torus_fixed_count', count, by_sign)
print('VERIFY_OK')
