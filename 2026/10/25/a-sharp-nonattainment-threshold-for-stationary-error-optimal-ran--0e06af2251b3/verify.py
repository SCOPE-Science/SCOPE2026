#!/usr/bin/env python3
"""Exact symbolic checks for the two-component randomized-resolvent frontier.
Requires SymPy 1.13 or newer. Run `python verify.py`.
"""
from fractions import Fraction
import sympy as sp

p,h=sp.symbols('p h',positive=True)
q=1-p
r1=p/(p+2*h)
r2=q/(q+h)
c1=h/(3*(p+2*h))
c2=-h/(3*(q+h))
R=sp.factor(p*r1+q*r2)
R2=sp.factor(p*r1**2+q*r2**2)
C=sp.factor(p*c1+q*c2)
m=sp.factor(C/(1-R))
Delta=sp.factor((r1-r2)*m+(c1-c2))
var=sp.factor(p*q*Delta**2/(1-R2))
V=sp.factor(m*m+var)
K=sp.expand(-4*h**3+h**2*(-6*p**2+16*p-8)+9*h*p**2*q+6*p**2*q**2)
T=sp.factor((p+2*h)**2*(q+h)**2*(1-R2)/h)
P=200*h**5+5829*h**4-1620*h**3+528*h**2-1008*h-528

checks=0
def check(condition, label):
    global checks
    if not condition: raise AssertionError(label)
    checks+=1

def zero(expr,label):
    check(sp.cancel(expr)==0,label)

zero(m-h*(3*p-2)/(3*(2*h+3*p*q)), 'stationary mean')
zero(Delta-h/(2*h+3*p*q), 'two-outcome stationary difference')
zero(V-(m*m+p*q*Delta**2/(1-R2)), 'stationary second moment')
zero(V-sp.factor((2*(p*r1*c1+q*r2*c2)*m+p*c1**2+q*c2**2)/(1-R2)), 'independent moment equation')
zero(V-sp.Rational(1,36)+(p+2*h)*q*K/(12*(2*h+3*p*q)*T),'sharp risk comparison')
zero(T-(4*h**3-4*h**2*p+8*h**2+3*h*p**3-15*h*p**2+12*h*p+6*p**4-12*p**3+6*p**2),'denominator identity')
zero(sp.resultant(K,sp.diff(K,p),p)+2592*h**4*(3*h+1)**2*P,'discriminant resultant')
zero(sp.diff(P,h,2)-(4000*h**3+69948*h**2-9720*h+1056),'quintic curvature')
check(9720**2-4*69948*1056<0,'positive curvature discriminant')
check(P.subs(h,sp.Rational(7,10))<0 and P.subs(h,sp.Rational(3,4))>0,'unique positive-root bracket')
check(sp.simplify(K.subs({p:sp.Rational(4,5),h:sp.Rational(7,10)}))==sp.Rational(73,1250),'strict interior improvement')
zero(K.subs(p,0)+4*h*h*(h+2),'p=0 limit')
zero(K.subs(p,1)-2*h*h*(1-2*h),'p=1 limit')
zero(sp.diff(K,p).subs(p,0)-16*h*h,'p derivative left')
zero(sp.diff(K,p).subs(p,1)-h*(4*h-9),'p derivative right')
zero(sp.diff(K,p,2).subs(p,0)-(12+18*h-12*h*h),'p second derivative left')
zero(sp.diff(K,p,2).subs(p,1)-(12-36*h-12*h*h),'p second derivative right')
check(sp.Rational(1,10)>0 and sp.Rational(1,10)<1,'range')
zero(sp.limit(V,p,0,dir='+')-sp.Rational(1,9), 'p=0 risk')
zero(sp.limit(V,p,1,dir='-')-sp.Rational(1,36), 'p=1 risk')
zero(sp.limit(V/h,h,0,dir='+')-1/(54*p*q),'small-step asymptotic')

for H in (sp.Rational(1,10),sp.Rational(1,4),sp.Rational(1,2),sp.Rational(7,10),sp.Rational(3,4),sp.Integer(1),sp.Integer(2),sp.Integer(5)):
    for j in range(1,20):
        prob=sp.Rational(j,20)
        nums={p:prob,h:H}
        a1=sp.Rational(2)
        a2=sp.Rational(1)
        rk1=prob/(prob+H*a1)
        rk2=(1-prob)/(1-prob+H*a2)
        ck1=H/(3*(prob+H*a1))
        ck2=-H/(3*(1-prob+H*a2))
        AA=prob*rk1+(1-prob)*rk2
        BB=prob*ck1+(1-prob)*ck2
        mm=BB/(1-AA)
        vv=(2*(prob*rk1*ck1+(1-prob)*rk2*ck2)*mm+prob*ck1**2+(1-prob)*ck2**2)/(1-(prob*rk1**2+(1-prob)*rk2**2))
        check(vv==V.subs(nums), 'rational moments')
        check((vv-sp.Rational(1,36))*K.subs(nums)<=0, 'sign comparison')
        check(T.subs(nums)>0, 'positive denominator')

root=sp.nsolve(P,sp.Rational(7,10),prec=75)
critical=sp.nsolve(sp.diff(K,p).subs(h,root),sp.Rational(4,5),prec=75)
check(0.7166725626<float(root)<0.7166725628,'root numerical interval')
check(0.8029974024<float(critical)<0.8029974027,'probability numerical interval')
check(abs(float(K.subs({h:root,p:critical})))<1e-55,'double-root validation')
check(abs(float(sp.diff(K,p).subs({h:root,p:critical})))<1e-55,'stationarity validation')
print(f'VERIFY_OK {checks} exact/symbolic/numeric assertions')
print('h_critical',sp.N(root,18),'p_critical',sp.N(critical,18))
