"""Exact verification for the two-patch stationary fluctuation-variance theorem.

Requires Python 3 and SymPy. No external datasets are required.
"""
from fractions import Fraction
from itertools import product
from math import sqrt
import sympy as sp

a,b,d,q,r,c=sp.symbols('a b d q r c', positive=True)
# Symbol c is algebraically unrestricted when forming polynomial identities.
v11,v22,v12=sp.symbols('v11 v22 v12')
eqs=[2*(a+d)*v11-2*d*v12-q,
     (a+b+2*d)*v12-d*(v11+v22)-c,
     2*(b+d)*v22-2*d*v12-r]
sol=sp.solve(eqs,(v11,v22,v12))
K=a*a+4*a*b+b*b
J=a*a+4*a*b+5*b*b
A=sp.expand(K*r+(2*a*a+4*a*b-2*b*b)*c-J*q)
B=sp.expand(4*a*b*(a+b)*c+2*a*b*(a+b)*r-2*b*(a*a+3*a*b+2*b*b)*q)
C=b*b*(a+b)*(2*a*c-(a+b)*q)
formula=(a*b*q+a*d*q+b*b*q+3*b*d*q+2*b*c*d+(q+r+2*c)*d*d)/(2*(a+b+2*d)*(a*b+(a+b)*d))
assert sp.cancel(sol[v11]-formula)==0
assert sp.cancel(sol[v22]-formula.xreplace({a:b,b:a,q:r,r:q}))==0
assert sp.cancel(sp.diff(formula,d)-(A*d*d+B*d+C)/(2*(a+b+2*d)**2*(a*b+(a+b)*d)**2))==0
assert sp.cancel((2*(a+b+2*d)*(a*b+(a+b)*d)*formula).expand() -
                 (a*b*q+a*d*q+b*b*q+3*b*d*q+2*b*c*d+(q+r+2*c)*d*d))==0
# Difference between equalizing-pole parameters is strictly positive for a,b>0.
s=(a+b)/2
t=a*b/(a+b)
assert sp.cancel(s-t-(a*a+b*b)/(2*(a+b)))==0
# The covariance restriction enforces A>=0 whenever C>=0.
h=sp.symbols('h', real=True)
F=sp.expand(K*h*h+(2*a*a+4*a*b-2*b*b)*h-J)
h0=(a+b)/(2*a)
assert sp.factor(F.subs(h,h0))==(a-b)**2*K/(4*a*a)
assert sp.factor(sp.diff(F,h).subs(h,h0))==(3*a**3+9*a*a*b+3*a*b*b+b**3)/a
assert sp.factor(B.subs(r,sp.solve(A,r)[0])-4*(a+b)*C/K)==0
assert sp.factor(B.subs(c,(a+b)*q/(2*a))+2*b*(a+b)*(b*q-a*r))==0
# Every pair of local variances has a strictly decreasing sum unless degenerate.
H=sp.Matrix([[a+d,-d],[-d,b+d]])
L=sp.Matrix([[1,-1],[-1,1]])
Q=sp.Matrix([[q,c],[c,r]])
Sig=sp.Matrix([[sol[v11],sol[v12]],[sol[v12],sol[v22]]])
assert all(sp.cancel(e)==0 for e in H*Sig+Sig*H-Q)
assert sp.cancel(sp.trace(Sig)-sp.trace(Q*H.inv())/2)==0
assert sp.cancel(sp.diff(sp.trace(Sig),d)+sp.trace(Q*H.inv()*L*H.inv())/2)==0
# A strict independent-noise threshold for one local variance.
assert sp.factor(J*(b*b+4*a*b+5*a*a)-K*K)==4*(a+b)**4
# Exact example: equal return rates, independent forcing strengths 1 and 4.
f=sp.factor(formula.subs({a:1,b:1,q:1,r:4,c:0}))
assert sp.cancel(f-(5*d*d+4*d+2)/(4*(d+1)*(2*d+1)))==0
assert sp.cancel(sp.diff(f,d)-(7*d*d+2*d-2)/(4*(d+1)**2*(2*d+1)**2))==0
dstar=(sp.sqrt(15)-1)/7
assert sp.simplify(sp.diff(f,d).subs(d,dstar))==0
assert sp.simplify(f.subs(d,dstar))==(sp.sqrt(15)-3)/2
assert f.subs(d,0)==sp.Rational(1,2)
assert sp.limit(f,d,sp.oo)==sp.Rational(5,8)
# Exact rational parameter census for covariance PSD, supplementing the all-real proof.
checks=0
for ai,bi,qi,ri,theta in product((1,2,3,5),(1,2,3,5),(1,2,3,5),(1,2,3,5),(-1,sp.Rational(-1,2),0,sp.Rational(1,2),1)):
    qq=qi*qi; rr=ri*ri;cc=theta*qi*ri
    aa=sp.Integer(ai);bb=sp.Integer(bi)
    aa1=A.subs({a:aa,b:bb,q:qq,r:rr,c:cc});cc1=C.subs({a:aa,b:bb,q:qq,r:rr,c:cc})
    aa2=A.subs({a:bb,b:aa,q:rr,r:qq,c:cc});cc2=C.subs({a:bb,b:aa,q:rr,r:qq,c:cc})
    assert not (cc1>0 and aa1<0)
    assert not (cc2>0 and aa2<0)
    assert not (aa1>0 and cc1<0 and aa2>0 and cc2<0)
    checks+=1
print('PASS: exact Lyapunov, derivative, coefficient, trace and witness identities')
print('PASS: rational PSD covariance grid:',checks,'parameter sets')
print('PASS: unique local-minimum example at d=(sqrt(15)-1)/7')
