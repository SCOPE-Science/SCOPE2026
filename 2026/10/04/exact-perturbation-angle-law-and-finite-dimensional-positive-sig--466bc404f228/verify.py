#!/usr/bin/env python3
import math

SQRT2=math.sqrt(2.0)
SQRT2PI=math.sqrt(2.0*math.pi)

def Phi(x):
    return 0.5*(1.0+math.erf(x/SQRT2))

def phi(x):
    return math.exp(-0.5*x*x)/SQRT2PI

def F(lam,rho):
    a=lam*math.sqrt(1.0+rho)
    b=lam*math.sqrt(1.0-rho)
    return Phi(a)*Phi(b)+Phi(-a)*Phi(-b)

def Fprime(lam,rho):
    a=lam*math.sqrt(1.0+rho)
    b=lam*math.sqrt(1.0-rho)
    sa=2.0*Phi(a)-1.0
    sb=2.0*Phi(b)-1.0
    return 0.5*lam*lam*(sb*phi(a)/a-sa*phi(b)/b)

def Fpp0(lam):
    s=2.0*Phi(lam)-1.0
    return -0.5*s*lam*(lam*lam+1.0)*phi(lam)-lam*lam*phi(lam)**2

def A(lam):
    return -0.5*Fpp0(lam)

def fd(d,rho):
    c=math.gamma(d/2.0)/(math.sqrt(math.pi)*math.gamma((d-1.0)/2.0))
    return c*(1.0-rho*rho)**((d-3.0)/2.0)

def simpson(fun,a,b,n=80000):
    if n%2: n+=1
    h=(b-a)/n
    s=fun(a)+fun(b)
    for k in range(1,n):
        s+=(4.0 if k%2 else 2.0)*fun(a+k*h)
    return s*h/3.0

def Pi(d,lam):
    # d>=3 in replay cases, so endpoint density is finite.
    return simpson(lambda r:F(lam,r)*fd(d,r),-1.0,1.0)

def mirror(u,v):
    return abs(u+v)-abs(u-v)

def rhs(u,v):
    if u*v>0: sg=1.0
    elif u*v<0: sg=-1.0
    else: sg=0.0
    return 2.0*sg*min(abs(u),abs(v))

for u in [i/4 for i in range(-12,13)]:
    for v in [i/5 for i in range(-15,16)]:
        assert abs(mirror(u,v)-rhs(u,v))<1e-14

for lam in [0.15,0.3,0.5,1.0,2.0,4.0]:
    for k in range(1,100):
        rho=k/100.0
        assert Fprime(lam,rho)<0.0

for lam in [0.5,1.0,2.0]:
    h=1e-4
    numeric=(F(lam,h)-2.0*F(lam,0.0)+F(lam,-h))/(h*h)
    assert abs(numeric-Fpp0(lam))<2e-6

expected={
    (3,1.0):0.6839397205857211,
    (10,1.0):0.7208645403887461,
    (3,2.0):0.8772894548610847,
}
for (d,lam),target in expected.items():
    val=Pi(d,lam)
    assert abs(val-target)<1e-8,(d,lam,val,target)

# Leading coefficient check at moderate/large d.
for d in [50,100]:
    loss=d*(F(1.0,0.0)-Pi(d,1.0))
    assert abs(loss-A(1.0))<0.005,(d,loss,A(1.0))

print('VERIFY_OK')
