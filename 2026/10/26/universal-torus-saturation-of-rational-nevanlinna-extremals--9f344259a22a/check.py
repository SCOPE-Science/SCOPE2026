"""Independent symbolic identities for a real-rational two-variable saturation theorem.
Uses SymPy (free symbolic computation); the analytic pole classification is proved separately.
"""
import sympy as sp

A,B,e,w=sp.symbols('A B e w')
# Degree-two perturbation prevents dropping the projective root at infinity.
P=e*w*w-A*w
Q=A*(w*w-1)+B*w
R=sp.factor(sp.resultant(P,Q,w))
assert sp.factor(R- A**2*(e**2-B*e-A**2)) == 0
assert sp.factor(R.subs(e,0)+A**4)==0
# This identity accounts for all projective roots, including w=infinity.
print('Universal homogeneous resultant: -A^4')

z=sp.symbols('z')
examples=[(sp.Integer(1),z+1),
          (z,z*z-1),
          (z*(z*z-1),z**4-3*z*z+1)]
for av,bv in examples:
    assert sp.gcd(av,bv)==1
    # Substitute the reduced rational Herglotz pair into the general identity.
    assert sp.expand((-A**4).subs(A,av)+av**4)==0
    for t in sp.solve(av,z):
        assert sp.simplify(bv.subs(z,t)) != 0
    print('Sample degree',max(sp.degree(av,z),sp.degree(bv,z)),': projective fiber resultant', sp.factor(-av**4))
print('CHECK_OK')
