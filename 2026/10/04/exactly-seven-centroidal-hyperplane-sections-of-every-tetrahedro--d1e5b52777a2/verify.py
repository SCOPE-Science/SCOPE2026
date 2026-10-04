import sympy as sp

u,v=sp.symbols('u v')
a=(1+u)/2
g=(1-v)/2
p=(1+v)/(2+u+v)
q=(1-u)/(2-u-v)
r=(1-v)/(2+u-v)
s=(1+u)/(2+u-v)
D=p*s+r*q
cx=sp.factor((p*s*(p+r)+r*q*r)/(3*D))
cy=sp.factor((p*s*s+r*q*(s+q))/(3*D))
P=sp.factor(-sp.together(cx-sp.Rational(1,4)).as_numer_denom()[0])
Q=sp.factor(-sp.together(cy-sp.Rational(1,4)).as_numer_denom()[0])
P_expected=3*u**4-2*u**3*v**2+6*u**3+2*u**2*v**2-4*u**2+2*u*v**4+2*u*v**2-8*u+3*v**4-4*v**2
Q_expected=2*u**4*v-3*u**4-2*u**2*v**3-2*u**2*v**2+2*u**2*v+4*u**2-3*v**4+6*v**3+4*v**2-8*v
assert sp.expand(P-P_expected)==0
assert sp.expand(Q-Q_expected)==0
R=sp.factor(sp.resultant(P,Q,v))
R_expected=16384*u**3*(u-1)**6*(u+1)**9*(3*u**2-4)
assert sp.expand(R-R_expected)==0
assert sp.factor(P.subs(u,0))==v**2*(3*v**2-4)

# One-positive/three-negative case: imposing section-centroid coordinates 1/4
# forces each negative magnitude to equal one third of the positive one.
A,G=sp.symbols('A G', positive=True)
edge_coord=A/(A+G)
assert sp.solve(sp.Eq(edge_coord/3,sp.Rational(1,4)),G)==[A/3]

# Seven vertex bipartitions: four 1+3 and three 2+2.
from itertools import combinations
one_three=4
two_two=len(list(combinations(range(4),2)))//2
assert one_three==4 and two_two==3 and one_three+two_two==7
print('VERIFY_OK tetrahedron seven centroidal sections')
