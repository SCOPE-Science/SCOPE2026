"""Exact algebra and rational-bound checks for the two-season quota-order theorem.
Run: python verify_quota_order.py (requires SymPy)."""
from fractions import Fraction
import sympy as S

r,k1,k2,H,L,x=S.symbols('r k1 k2 H L x', positive=True)
def transfer(k,h):
    return S.Matrix([[r*k-(r-1)*h,-k*h],[r-1,k]])
def polynomial(a,b):
    z=transfer(k2,b)*transfer(k1,a)
    return S.expand(z[1,0]*x*x+(z[1,1]-z[0,0])*x-z[0,1]),z
Qa,Ma=polynomial(H,L)
Qb,Mb=polynomial(L,H)
assert S.simplify(transfer(k1,L).det()-r*k1*k1)==0
assert S.simplify(S.trace(Ma)-S.trace(Mb)-(H-L)*(r-1)**2*(k1-k2))==0
R=(r-1)*x*x+((r+1)*k1-(r-1)*k2)*x-k1*k2
assert S.simplify(Qa-Qb+(H-L)*(r-1)*R)==0

subs={r:3,k1:4,k2:1,L:S.Rational(1,5)}
xi=(S.sqrt(57)-7)/2
assert S.simplify(R.subs(subs).subs(x,xi))==0
G1=lambda u:12*u/(4+2*u)
G2=lambda u:3*u/(1+2*u)
Hstar=S.radsimp(G2(G1(xi)-S.Rational(1,5))-xi)
assert S.simplify(Hstar-(1345-159*S.sqrt(57))/293)==0
assert S.simplify(Qa.subs(subs).subs({x:xi,H:Hstar}))==0
assert S.simplify(Qb.subs(subs).subs({x:xi,H:Hstar}))==0

def check_brackets(q,a,b):
    qa=q.subs(x,S.Rational(a)); qb=q.subs(x,S.Rational(b))
    assert qa>0 and qb<0, (q,qa,qb)

for high, abr, bbr in [
    (S.Rational(1,4),(S.Rational(141,1000),S.Rational(143,1000)),(S.Rational(131,1000),S.Rational(133,1000))),
    (S.Rational(1,2),(S.Rational(278,1000),S.Rational(280,1000)),(S.Rational(285,1000),S.Rational(287,1000)))]:
    q1=S.factor(Qa.subs(subs).subs(H,high))
    q2=S.factor(Qb.subs(subs).subs(H,high))
    check_brackets(q1,*abr);check_brackets(q2,*bbr)
    assert G1(abr[0])>high and G1(bbr[0])>S.Rational(1,5)
    # two strictly positive roots: positive lower root bracket and positive vertex-to-second-root sign.
    for q,br in ((q1,abr),(q2,bbr)):
        pol=S.Poly(q,x);a,b,c=pol.all_coeffs()
        assert a>0 and b<0 and c>0
        assert b*b-4*a*c>0
    print('H=',high,'A lower-root interval=',abr,'B lower-root interval=',bbr)

hfloat=float(Hstar)
assert S.Rational(49,100)<Hstar<S.Rational(1,2)
assert S.Rational(274,1000)<xi<S.Rational(275,1000)
assert G1(xi)>Hstar
qA=S.Poly(S.factor(Qa.subs(subs).subs(H,Hstar)),x)
qB=S.Poly(S.factor(Qb.subs(subs).subs(H,Hstar)),x)
for q in (qA,qB):
    a,b,c=q.all_coeffs()
    assert a>0 and S.simplify(-b/(2*a)-xi)>0
    assert S.simplify(q.as_expr().subs(x,xi))==0
assert S.simplify(G1(xi)-S.Rational(1,5))>0
assert S.simplify(G2(G1(xi)-Hstar)-S.Rational(1,5)-xi)==0
print('unique positive common root:',xi,'\nunique switch H*:',Hstar,'~',hfloat)
print('all exact symbolic and rational isolation tests passed')
