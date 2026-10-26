#!/usr/bin/env python3
"""Finite symbolic and numerical checks of a two-bath OU lag-asymmetry theorem.

Requires Python 3 and SymPy; the proof of global uniqueness remains analytic,
not an inference from sampled tests.
"""
from fractions import Fraction
import math
import random
import sympy as sp

checks = 0

def check(condition, description):
    global checks
    if not condition:
        raise AssertionError(description)
    checks += 1

k, u, t, T1, T2, x = sp.symbols('k u t T1 T2 x', positive=True)
s = k+u
A = sp.Matrix([[s,-u],[-u,s]])
B = sp.diag(T1,T2)
c12=u*(T1+T2)/(2*k*(k+2*u))
C=sp.Matrix([[(T1+u*c12)/s,c12],[c12,(T2+u*c12)/s]])
check((A*C+C*A-2*B).applyfunc(sp.simplify)==sp.zeros(2), 'Lyapunov identity')
check(sp.simplify(C[1,1]-C[0,0]-(T2-T1)/s)==0, 'difference of variances')
slow=sp.exp(-k*t)
fast=sp.exp(-(k+2*u)*t)
E=sp.Matrix([[(slow+fast)/2,(slow-fast)/2],[(slow-fast)/2,(slow+fast)/2]])
check((sp.diff(E,t)+A*E).applyfunc(sp.simplify)==sp.zeros(2), 'propagator equation')
check(E.subs(t,0)==sp.eye(2), 'propagator initial value')
S=E*C
Delta=sp.factor(S[0,1]-S[1,0])
claimed=(T2-T1)*(slow-fast)/(2*s)
check(sp.simplify(Delta-claimed)==0, 'exact delayed asymmetry')
check(sp.simplify(sp.diff(Delta,t).subs(t,0)-u*(T2-T1)/s)==0, 'initial circulation slope')
optimal_lag=sp.log((k+2*u)/k)/(2*u)
lag_derivative=sp.diff(claimed,t)
check(sp.simplify(lag_derivative.subs(t,optimal_lag))==0, 'critical lag')
P=sp.simplify(claimed.subs(t,optimal_lag)/(T2-T1))
g=x/((x+2)*(x+1))*(1+x)**(-1/x)
check(sp.simplify(P.subs(u,k*x/2)-g/k)==0, 'peak after lag optimization')
J=sp.simplify(sp.integrate(claimed,(t,0,sp.oo))/(T2-T1))
check(sp.simplify(J-u/(s*k*(k+2*u)))==0,'integrated lag asymmetry')
h=x/((x+2)*(x+1))
check(sp.simplify(J.subs(u,k*x/2)-h/k**2)==0, 'integrated scaling')
check(sp.simplify(sp.diff(h,x)-(2-x*x)/((x+1)**2*(x+2)**2))==0, 'area optimality derivative')
check(sp.simplify(h.subs(x,sp.sqrt(2))-(3-2*sp.sqrt(2)))==0,'exact area optimum')
loggprime=sp.log(1+x)/x**2-1/(x+2)
check(sp.simplify(sp.diff(sp.log(g),x)-loggprime)==0,'peak log derivative')
F=(x+2)*sp.log(1+x)-x**2
check(sp.simplify(sp.diff(F,x,2)-(x/(1+x)**2-2))==0,'strict concavity formula')
check(sp.simplify(sp.diff(F,x).subs(x,0)-2)==0,'strict concavity initial derivative')
check(sp.simplify(sp.limit(F/x**2,x,sp.oo)+1)==0,'large x negativity')

# Bisection is a numerical check of the unique root proved analytically.
lo,hi=2.0,3.0
fn=lambda a:(a+2)*math.log1p(a)-a*a
check(fn(lo)>0 and fn(hi)<0,'root bracket')
for _ in range(80):
    mid=(lo+hi)/2
    if fn(mid)>0: lo=mid
    else: hi=mid
xp=(lo+hi)/2
up=xp/2
peakconst=xp/((xp+2)*(xp+1))*math.exp(-math.log1p(xp)/xp)
area_const=3-2*math.sqrt(2)
check(2.22325494<xp<2.22325495,'root numerical bracket')
check(0.09647637<peakconst<0.09647638,'peak constant bracket')
check(math.sqrt(2)<xp and xp>2,'ordering of optima')

# Finite sample sweeps test both branches of each global profile; no numerical
# sweep is used to certify global uniqueness.
rng=random.Random(230207716)
for j in range(25):
    kval=10**rng.uniform(-1,1)
    uval=10**rng.uniform(-2,2)
    theta1=10**rng.uniform(-1,1)
    theta2=10**rng.uniform(-1,1)
    if abs(theta2-theta1)<0.05: theta2+=1
    lag=rng.uniform(0.03,2.2)/kval
    sv=kval+uval
    c12v=uval*(theta1+theta2)/(2*kval*(kval+2*uval))
    cv11=(theta1+uval*c12v)/sv
    cv22=(theta2+uval*c12v)/sv
    slowv=math.exp(-kval*lag)
    fastv=math.exp(-(kval+2*uval)*lag)
    e01=(slowv-fastv)/2
    direct=e01*(cv22-cv11)
    formula=(theta2-theta1)*(slowv-fastv)/(2*sv)
    check(math.isclose(direct,formula,rel_tol=2e-12,abs_tol=1e-13),f'time-lag test {j}')
    xval=2*uval/kval
    lagopt=math.log1p(xval)/(2*uval)
    pv=abs(theta2-theta1)*xval/((xval+2)*(xval+1))*math.exp(-math.log1p(xval)/xval)/kval
    pv_direct=abs((theta2-theta1)*(math.exp(-kval*lagopt)-math.exp(-(kval+2*uval)*lagopt))/(2*sv))
    check(math.isclose(pv,pv_direct,rel_tol=3e-12,abs_tol=1e-13),f'lag optimum test {j}')
    area=abs(theta2-theta1)*uval/(sv*kval*(kval+2*uval))
    areascale=abs(theta2-theta1)/kval**2*xval/((xval+2)*(xval+1))
    check(math.isclose(area,areascale,rel_tol=1e-12,abs_tol=1e-13),f'integrated formula test {j}')

for kval in [0.25,1.0,3.0]:
    for theta1,theta2 in [(1.0,2.0),(8.0,0.2)]:
        umax=kval*xp/2
        uarea=kval/math.sqrt(2)
        def pfun(q):
            y=2*q/kval
            return abs(theta2-theta1)/kval*y/((y+2)*(y+1))*math.exp(-math.log1p(y)/y)
        def jfun(q):
            y=2*q/kval
            return abs(theta2-theta1)/kval**2*y/((y+2)*(y+1))
        check(pfun(umax)>pfun(umax*0.95) and pfun(umax)>pfun(umax*1.05),'peak perturbation')
        check(jfun(uarea)>jfun(uarea*0.95) and jfun(uarea)>jfun(uarea*1.05),'area perturbation')
        check(jfun(uarea)>jfun(umax),'strictly distinct objectives')

print('All checks passed:',checks)
print('universal dimensionless peak-optimal x =',format(xp,'.15f'))
print('u_peak / k =',format(up,'.15f'))
print('u_integrated / k =',format(1/math.sqrt(2),'.15f'))
print('peak coefficient (multiplies |T2-T1|/k) =',format(peakconst,'.15f'))
print('integral coefficient (multiplies |T2-T1|/k^2) =',format(area_const,'.15f'))
