#!/usr/bin/env python3
import math

r=0.4
s=0.3
K=40.0
H=50.0
e=0.6
b=0.3
c=0.5
alpha=0.5
q=1
a0=0.8

def phi(N):
    return N/(1.0+N**(1.0-alpha))

def pplus(N):
    return 0.5*H*(1.0+math.sqrt(1.0+4.0*e*r*N*(K-N)/(s*K*H)))

def attack(N):
    P=pplus(N)
    return r*(1.0-N/K)*(1.0+N**(1.0-alpha))*(1.0+b*N**(alpha+q)+c*P)/P

def bisect(fun, lo, hi, n=160):
    flo=fun(lo)
    fhi=fun(hi)
    assert flo*fhi < 0.0
    for _ in range(n):
        mid=(lo+hi)/2.0
        fm=fun(mid)
        if flo*fm <= 0.0:
            hi=mid
            fhi=fm
        else:
            lo=mid
            flo=fm
    return (lo+hi)/2.0

def jacobian(N,P,a):
    delta=1.0-alpha
    den=1.0+b*N**(alpha+q)+c*P
    ph=phi(N)
    ph_N=(1.0+alpha*N**delta)/(1.0+N**delta)**2
    den_N=b*(alpha+q)*N**(alpha+q-1.0)
    dD_N=P*(ph_N*den-ph*den_N)/(den*den)
    dD_P=ph*(den-c*P)/(den*den)
    j11=r-2.0*r*N/K-a*dD_N
    j12=-a*dD_P
    j21=e*a*dD_N
    j22=s-2.0*s*P/H+e*a*dD_P
    return j11,j12,j21,j22

astar=c*r+r/H
assert abs(astar-0.208) < 1e-15

for N in (1e-8,1e-6,1e-4,1e-2):
    assert attack(N) > astar

n1=bisect(lambda x: attack(x)-a0, 1e-8, 15.0)
n2=bisect(lambda x: attack(x)-a0, 25.0, 39.999999)
p1=pplus(n1)
p2=pplus(n2)

def residuals(N,P,a):
    den=1.0+b*N**(alpha+q)+c*P
    pred=a*phi(N)*P/den
    f=r*N*(1.0-N/K)-pred
    g=s*P*(1.0-P/H)+e*pred
    return f,g

for N,P in ((n1,p1),(n2,p2)):
    f,g=residuals(N,P,a0)
    assert abs(f) < 2e-12
    assert abs(g) < 2e-12

j1=jacobian(n1,p1,a0)
j2=jacobian(n2,p2,a0)
tr1=j1[0]+j1[3]
det1=j1[0]*j1[3]-j1[1]*j1[2]
tr2=j2[0]+j2[3]
det2=j2[0]*j2[3]-j2[1]*j2[2]

assert det1 < 0.0
assert tr2 < 0.0 and det2 > 0.0

assert abs(n1-8.335819785268935) < 1e-9
assert abs(p1-54.81521255866335) < 1e-9
assert abs(n2-32.0797287674991) < 1e-9
assert abs(p2-54.649285875104226) < 1e-9

print("VERIFY_OK")
print("a_star", repr(astar))
print("saddle", repr(n1), repr(p1), repr(tr1), repr(det1))
print("stable", repr(n2), repr(p2), repr(tr2), repr(det2))
