from fractions import Fraction as Q
from math import log
import sympy as S
u,v,C,D=Q(21,17),Q(14,17),Q(187,153),Q(127,153)
m,z,e=Q(49,51),Q(7,17),Q(20,51)
s=Q(258,425)
assert C-D == Q(20,51) and s*Q(425)==258
J=10*((u+v)*s-u)
assert J==Q(42,289)
assert u*(1-u)+2*J==0 and v*(1-v)-J==0
assert u-C+Q(1,30)*(D-C)==0
assert v-D+Q(1,60)*(C-D)==0
assert (u+2*v)/3==m and u-v==z
q=S.symbols('q',positive=True)
M=S.Matrix([[-S.Rational(47,51),-S.Rational(28,153),0],[S.Rational(28,5),-S.Rational(3857,255),S.Rational(1809612,122825)*q],[0,1,-S.Rational(21,20)]])
l=S.symbols('l')
p=S.Poly(M.charpoly(l).as_expr(),l)
a1,a2,a3=p.all_coeffs()[1:]
assert a1==S.Rational(5813,340)
assert S.expand(a2+28*(64629*q-139553)/122825)==0
assert S.expand(a3+21*(5400112*q-6249047)/8352100)==0
assert S.expand(a1*a2-a3+7*(1421751828*q-3151150651)/41760500)==0
upper=S.Rational(28,25)
assert a1>0 and a2.subs(q,upper)>0 and a3.subs(q,upper)>0 and (a1*a2-a3).subs(q,upper)>0
anti=S.Matrix([[-S.Rational(571,85),S.Rational(603204,122825)*q],[1,-S.Rational(61,60)]])
assert S.trace(anti)<0 and S.det(anti).subs(q,upper)>0
zz=S.Rational(91,425)
logupper=2*(zz+zz**3/(3*(1-zz**2)))
chiupper=S.Rational(51,20)*logupper
assert chiupper==S.Rational(47803483,43086000) and chiupper<upper
chi=float(S.Rational(51,20))*log(258/167)
assert 1.1<chi<float(chiupper)
# Check full original six-dimensional Jacobian via symbolic differentiation.
n0,n1,n2,c0,c1,c2=S.symbols('n0 n1 n2 c0 c1 c2',real=True)
Ns=[n0,n1,n2]; Cs=[c0,c1,c2]; edges=[(0,1),(0,2)]
F=[x*(1-x) for x in Ns]+[Ns[i]-Cs[i] for i in range(3)]
chiSym=S.symbols('chiSym',real=True)
for i,j in edges:
    t=S.exp(chiSym*Cs[i])/(S.exp(chiSym*Cs[i])+S.exp(chiSym*Cs[j]))
    flux=10*((Ns[i]+Ns[j])*t-Ns[i]); F[i]+=flux; F[j]-=flux
    F[3+i]+=S.Rational(1,60)*(Cs[j]-Cs[i]); F[3+j]+=S.Rational(1,60)*(Cs[i]-Cs[j])
Jfull=S.Matrix(F).jacobian(Ns+Cs)
sub={n0:S.Rational(21,17),n1:S.Rational(14,17),n2:S.Rational(14,17),c0:S.Rational(187,153),c1:S.Rational(127,153),c2:S.Rational(127,153),S.exp(chiSym*(c0-c1)):S.Rational(258,167)}
# Full Jacobian checking via numerical evaluation at chi; complete spectrum negative.
import numpy as np
jnum=np.array(Jfull.subs({n0:u,n1:v,n2:v,c0:C,c1:D,c2:D,chiSym:chi}).evalf(),dtype=float)
vals=np.linalg.eigvals(jnum)
assert all(t.real< -0.02 for t in vals),vals
print('All exact equilibrium, Routh-Hurwitz, anti-mode, logarithmic-bound and full-Jacobian tests passed; eigenvalues=',vals)
