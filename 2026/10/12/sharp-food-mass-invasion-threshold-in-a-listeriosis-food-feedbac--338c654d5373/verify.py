"""Reproducible exact-arithmetic algebra checks for a food-associated SIR equilibrium criterion.

This checks finite algebraic identities and the explicit witness; the uniform theorem
about every positive parameter is established analytically in RESULT.md.
"""
from fractions import Fraction as Q
import sympy as s

L, mu, delta, gam, beta, xi, d, p, a3, a4, F=s.symbols('L mu delta gam beta xi d p a3 a4 F', positive=True)
S,I,B,U,C=s.symbols('S I B U C', nonnegative=True)
h=mu+delta+gam
lam=beta*(B+a3*C)
vector=[L+gam*I-(mu+lam)*S,lam*S-h*I,xi*I-d*B,p*(U+C)-(B+a4*C+p)*U,(B+a4*C)*U-p*C]
assert s.simplify(vector[3]+vector[4])==0
assert s.simplify((vector[0]+vector[1])-(L-mu*(S+I)-delta*I))==0
# Exact positive example: printed R=2/3<1 but positive equilibrium.
values={L:Q(1),mu:Q(1),delta:Q(1),gam:Q(1),beta:Q(2),xi:Q(1),d:Q(1),p:Q(1),a3:Q(1),a4:Q(1),F:Q(9,10),S:Q(3,5),I:Q(1,5),B:Q(1,5),U:Q(3,5),C:Q(3,10)}
for j,expr in enumerate(vector): assert s.simplify(expr.subs(values))==0, (j,expr.subs(values))
assert values[U]+values[C]==values[F]
old=s.cancel(beta*xi*L/(mu*d*h))
new=s.cancel(old*(1+a3*F/(p-a4*F)))
assert s.simplify(old.subs(values))==s.Rational(2,3)
assert s.simplify(new.subs(values))==s.Rational(20,3)
# Fixed food total: solve food equilibrium for U=F-C, test implicit derivative.
q=s.expand(a4*C*C+(B+p-a4*F)*C-B*F)
assert s.expand((B+a4*C)*(F-C)-p*C)==-q
D=s.diff(q,C)
assert s.simplify(-s.diff(q,B)/D-(F-C)/D)==0
# The infected linearization at the DFE on F-leaf and the threshold test vector.
W=s.Matrix([I,B,C])
Infected=s.Matrix([vector[1].subs(S,L/mu), vector[2], ((B+a4*C)*(F-C)-p*C)])
M=Infected.jacobian(W).subs({I:0,B:0,C:0})
expected=s.Matrix([[-h,beta*L/mu,beta*a3*L/mu],[xi,-d,0],[0,F,-p+a4*F]])
assert s.simplify(M-expected)==s.zeros(3)
k=xi/d
x=s.Matrix([1,k,k*F/(p-a4*F)])
assert s.simplify(M*x-s.Matrix([h*(new-1),0,0]))==s.zeros(3,1)
# Denominator in implicit derivative is positive on B>0,C>0: D=(a4*C**2+B*F)/C.
assert s.simplify(C*D-(a4*C*C+B*F)-q)==0
assert s.simplify(q.subs(C,0)+B*F)==0
assert s.simplify(q.subs(C,F)-p*F)==0
cp=(F-C)/D
cpp=s.diff(cp,B)+s.diff(cp,C)*cp
assert s.simplify(cpp+2*cp*(1+a4*cp)/D)==0
# Exact nonzero endpoint and condition at witness; confirms sharp boundary is nontrivial.
assert values[p]-values[a4]*values[F]==Q(1,10)
print('VERIFY_OK')
