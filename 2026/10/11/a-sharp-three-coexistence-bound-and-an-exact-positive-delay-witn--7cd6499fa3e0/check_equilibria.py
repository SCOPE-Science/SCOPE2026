"""Exact symbolic reproducibility checks for a plant--vector coexistence count.

Run: python check_equilibria.py
Dependency: SymPy (see requirements.txt).
All displayed witness signs are rational, not floating-point root tests.
"""
from fractions import Fraction as F
from sympy import (symbols, Rational as R, simplify, expand, Poly, exp, log)

z, A, Re, h, q = symbols('z A Re h q', positive=True)
u = (1 + A*z)/(Re*(1-z))
v = h*z
H = (1 + A*z)/Re + h*z*(1-z)
E = 1 - (u+v)/(1-z) - q*v/(u+v)
Q = expand(((1-z)**2 - H)*H - q*h*z*(1-z)**3)
assert simplify(E*(1-z)**2*H-Q) == 0
assert Poly(Q,z).degree() <= 4
assert simplify(Q.subs(z,0) - (Re-1)/Re**2) == 0
assert simplify(Q.subs(z,1) + (1+A)**2/Re**2) == 0

# Positive-delay witness: exp(-tau1)=exp(-tau2)=1/2, tau1=tau2=log(2).
r=R(40); K=R(1); lam=R(10000); m=R(1); b=R(1,20)
a=R(1); beta=R(2,25); mu=R(1); t1=t2=log(2)
c1=simplify(exp(-m*t1)); c2=simplify(exp(-mu*t2))
assert c1==c2==R(1,2)
Aa=r*c1/m
RR=a*K*K*beta*lam*c1*c2/(m*mu)
hh=r/(lam*a*K)
qq=mu/(b*c2)
assert (Aa,RR,hh,qq)==(20,200,R(1,250),40)
S=K*(1-z)/(1+Aa*z)
I=Aa*S*z
U=(a*K/RR)*(1+Aa*z)/(1-z)
V=(r/lam)*z
N=U+V; M=S+I
FS=r*S*(1-M/K)-lam*S*V
FI=lam*c1*S*V-m*I
FU=b*N*(1-N/(a*M))-beta*U*I
FV=beta*c2*U*I-mu*V
for rhs in (FS,FI,FV): assert simplify(rhs)==0
assert simplify(FU/(b*N)-E.subs({A:Aa,Re:RR,h:hh,q:qq}))==0
Qsample=expand(Q.subs({A:Aa,Re:RR,h:hh,q:qq})*1000000)
assert Qsample==155984*z**4-367168*z**3+262224*z**2-67040*z+4975

# Root isolation by four disjoint sign changes, including one nonphysical root > 1.
def Qexact(x):
    D=5+104*x-4*x*x
    return (1000*(1-x)**2-D)*D-160000*x*(1-x)**3
samples=[(F(1,10),+1),(F(1,5),-1),
         (F(3,10),-1),(F(2,5),+1),
         (F(3,5),+1),(F(2,3),-1),
         (F(1),-1),(F(3,2),+1)]
for pt,sign in samples:
 val=Qexact(pt)
 assert (val>0)-(val<0)==sign,(pt,val,sign)
 assert R(val.numerator,val.denominator)==Qsample.subs(z,R(pt.numerator,pt.denominator))
 print('witness_sign',str(pt),str(val),'positive' if sign>0 else 'negative')
# Four distinct disjoint intervals contain roots; quartic has exactly four, all simple.
assert Poly(Qsample,z).degree()==4
print('CHECK_OK')
