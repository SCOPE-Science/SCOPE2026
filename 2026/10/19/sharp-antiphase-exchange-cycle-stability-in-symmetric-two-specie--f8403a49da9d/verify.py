#!/usr/bin/env python3
"""Standalone arithmetic and Floquet checks for a two-species Ricker exchange cycle.
The global uniqueness and completeness statements are proved analytically in RESULT.md.
"""
from fractions import Fraction as Q
from math import log, tanh, sinh, cosh, sqrt, exp

def bracket_log4(n=36):
    r=Q(3,5)
    lower=2*sum((r**(2*k+1)/Q(2*k+1)) for k in range(n))
    upper=lower + 2*r**(2*n+1)/(Q(2*n+1)*(1-r*r))
    return lower,upper

L,U=bracket_log4()
assert Q(1386,1000) < L < U < Q(1387,1000)
Slo,Sup=Q(100,27)*L,Q(100,27)*U
Dlo=1-Sup+Q(1584,729)*L*L
Dhi=1-Slo+Q(1584,729)*U*U
Plo=Q(10,3)*L-Q(1584,729)*U*U
assert Dlo > -1 and Plo > 0
assert Q(1,10)>0
print('Exact rational lower bounds for D+1 and 1-a*S-D:', float(1+Dlo),float(Plo))

# The witness satisfies the swap equations identically as logarithmic identities.
# rho-X-aY=-log(4) and rho-Y-aX=+log(4).
assert Q(55,27)-Q(80,27)-Q(1,10)*Q(20,27)==-1
assert Q(55,27)-Q(20,27)-Q(1,10)*Q(80,27)==1
z=log(4)
x,y,rho=80*z/27,20*z/27,55*z/27
a=.1
fx=x*exp(rho-x-a*y)
fy=y*exp(rho-y-a*x)
assert abs(fx-y)<1e-12 and abs(fy-x)<1e-12
D=float((Dlo+Dhi)/2)
tr=-a*(x+y)
eplus=(-a*(x+y)+sqrt((a*(x+y))**2+4*D))/2
eminus=(-a*(x+y)-sqrt((a*(x+y))**2+4*D))/2
assert abs(eplus)<1 and abs(eminus)<1
print('Exact swap witness:', {'X':x,'Y':y,'rho':rho,'D':D,'Floquet_multipliers':(eplus*eplus,eminus*eminus)})

def C(z): return z / tanh(z/2)
def J(z): return z*z/(2*sinh(z/2)**2)
def A(z): return (sinh(z)-z)/(sinh(z)+z)
def bisect(f, lo, hi, n=110):
    flo=f(lo); fhi=f(hi)
    assert flo*fhi<0
    for _ in range(n):
        mid=(lo+hi)/2
        if (f(mid)>0)==(flo>0): lo, flo=mid,f(mid)
        else: hi, fhi=mid,f(mid)
    return (lo+hi)/2

zc=bisect(lambda z:A(z)-1/(1+C(z)),.01,6)
ac=A(zc)
rhoc=(1+ac)/(1-ac)*C(zc)
assert .27783<ac<.27785
assert abs(ac-1/(1+C(zc)))<1e-14
print('Critical values (numerical, not proof of uniqueness):', {'z_critical':zc,'a_critical':ac,'rho_critical':rhoc})
for a in (.01,.1,.25,.27):
    zlo=bisect(lambda z:A(z)-a,.001,10)
    zhi=bisect(lambda z:C(z)-(1+a)*J(z)-(1-a),.001,10)
    assert zlo<zhi
    zmid=(zlo+zhi)/2
    S=2*C(zmid)/(1-a)
    t=tanh(zmid/2)
    X,Y=S*(1+t)/2,S*(1-t)/2
    rho=(1+a)*S/2
    assert abs(X*exp(rho-X-a*Y)-Y)<1e-9
    assert abs(Y*exp(rho-Y-a*X)-X)<1e-9
    d=1-S+(1-a*a)*X*Y
    assert 1-d-a*S>0 and d>-1
    # Exact 2x2 trace/determinant Jury values, plus direct monodromy.
    b11=(Y/X)*(1-X); b12=-a*Y
    b21=-a*X; b22=(X/Y)*(1-Y)
    K=[[b21,b22],[b11,b12]]
    assert abs(K[0][0]+K[1][1]+a*S)<1e-10
    assert abs(K[0][0]*K[1][1]-K[0][1]*K[1][0]+d)<1e-10
    print('Stable wedge witness:',a,zlo,zhi,zmid,rho,d)
for a in (.28,.5,.9):
    zlo=bisect(lambda z:A(z)-a,.001,40)
    zhi=bisect(lambda z:C(z)-(1+a)*J(z)-(1-a),.001,40)
    assert zlo>zhi
print('PASS: exact rational witness and numerical consistency checks')
