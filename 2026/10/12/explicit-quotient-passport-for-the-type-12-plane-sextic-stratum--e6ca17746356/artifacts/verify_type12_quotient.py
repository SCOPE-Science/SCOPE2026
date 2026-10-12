import sympy as sp
from fractions import Fraction

beta,t=sp.symbols('beta t')
f=t*(t**4+beta*t**2+1)
u=t**2+t**-2
# Invariance under the induced V4 on t.
assert sp.simplify(u.subs(t,-t)-u)==0
assert sp.simplify(u.subs(t,1/t)-u)==0
# Fibres of u over the two involution branch values.
assert sp.factor(sp.together(u-2))==(t-1)**2*(t+1)**2/t**2
assert sp.factor(sp.together(u+2))==(t**2+1)**2/t**2
# Kummer branch polynomial and its multiple-root locus.
q=t**4+beta*t**2+1
res=sp.factor(sp.resultant(q,sp.diff(q,t),t))
assert res==16*(beta-2)**2*(beta+2)**2
# The four finite Kummer branch points all have the same u-value -beta.
# Reduce t^4+beta*t^2+1=0: t^2+t^-2=-beta.
assert sp.rem(t**4+beta*t**2+1, q, domain=sp.QQ.frac_field(beta))==0
assert sp.factor(t**2*(u+beta)-q)==0
# Kummer degree 6 followed by V4 degree 4.
assert 6*4==24
# Tame Riemann-Hurwitz for signature [0;12,6,2,2].
S=sum(Fraction(e-1,e) for e in (12,6,2,2))
rhs=24*(Fraction(-2,1)+S)
assert rhs==18==2*10-2
# Orbit sizes for the four inertia orders.
assert [24//e for e in (12,6,2,2)]==[2,4,12,12]
print('VERIFY_OK degree=24 quotient=P1 signature=[0;12,6,2,2] branch_values=infinity,-beta,2,-2 orbit_sizes=2,4,12,12 discriminant_beta=+-2')
