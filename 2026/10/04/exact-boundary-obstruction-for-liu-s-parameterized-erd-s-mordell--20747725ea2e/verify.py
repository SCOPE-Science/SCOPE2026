#!/usr/bin/env python3
import math, random
from fractions import Fraction


def dist(p,q):
    return math.hypot(p[0]-q[0],p[1]-q[1])

def line_dist(p,a,b):
    num=abs((b[0]-a[0])*(a[1]-p[1])-(a[0]-p[0])*(b[1]-a[1]))
    den=dist(a,b)
    return num/den

def data(A,B,C,P):
    R=[dist(P,A),dist(P,B),dist(P,C)]
    r=[line_dist(P,B,C),line_dist(P,C,A),line_dist(P,A,B)]
    s=sum(r); T=sum(R)
    Bv=sum(r[i]*(R[i]+r[i]) for i in range(3))
    D=sum(r[i]*R[i] for i in range(3))-2*(r[0]*r[1]+r[1]*r[2]+r[2]*r[0])
    E=s*(T-2*s)
    return R,r,s,T,Bv,D,E

def middle(R,r,k):
    s=sum(r)
    num=0.0
    for i in range(3):
        j=(i+1)%3; ell=(i+2)%3
        num+=(k*r[i]+r[j]+r[ell])*(R[i]+r[i])
    return 2*num/((k+2)*s)

def alpha_u(u):
    return -(u**4-12*u**3+4*u-1)/(4*u**3)

def bisect_root():
    lo,hi=0.0,1.0
    for _ in range(100):
        mid=(lo+hi)/2
        f=mid**4-8*mid+3
        if f>0: lo=mid
        else: hi=mid
    return (lo+hi)/2

random.seed(20261002)
max_mid=0.0; max_low=0.0; max_up=0.0
min_D=1e100; min_E=1e100
samples=12000
for _ in range(samples):
    A=(0.0,0.0); B=(1.0,0.0)
    C=(random.uniform(-0.5,1.5),random.uniform(0.15,2.0))
    q=[random.random()+0.05 for _ in range(3)]
    z=sum(q); q=[v/z for v in q]
    P=(q[0]*A[0]+q[1]*B[0]+q[2]*C[0],q[0]*A[1]+q[1]*B[1]+q[2]*C[1])
    R,r,s,T,Bv,D,E=data(A,B,C,P)
    k=random.uniform(0.05,1.9)
    M=middle(R,r,k)
    M2=2*(s*(T+s)+(k-1)*Bv)/((k+2)*s)
    max_mid=max(max_mid,abs(M-M2))
    low_lhs=(k+2)*s*(M-2*s)/2
    up_lhs=(k+2)*s*(T-M)
    max_low=max(max_low,abs(low_lhs-(E+(k-1)*D)))
    max_up=max(max_up,abs(up_lhs-(k*E+2*(1-k)*D)))
    min_D=min(min_D,D); min_E=min(min_E,E)

# Exact-rational boundary parameterization checks.
for p,q in [(1,5),(1,3),(2,5),(3,5),(4,5),(7,10)]:
    u=Fraction(p,q)
    t=4*u/(1+u*u)
    h=(1-u*u)/(1+u*u)
    alpha1=2*(t+h-2*t*h)/(t*(1-h))
    alpha2=-(u**4-12*u**3+4*u-1)/(4*u**3)
    assert alpha1==alpha2

u=bisect_root()
a=alpha_u(u)
klo=1-a
khi=2/(2-a)
quart=27*a**4-260*a**3+876*a**2-1140*a+397
assert abs(u**4-8*u+3)<2e-15
assert abs(quart)<2e-12
assert abs(klo-0.464434945162939)<2e-15
assert abs(khi-1.365714473426112)<2e-15

# Interior counterexamples just beyond each outer endpoint.
t=4*u/(1+u*u); h=(1-u*u)/(1+u*u)
A=(-t/2,0.0); C=(t/2,0.0); B=(0.0,h)
P=(0.0,h*1e-7)
R,r,s,T,Bv,D,E=data(A,B,C,P)
kl=klo-1e-4
ku=khi+1e-4
Ml=middle(R,r,kl); Mu=middle(R,r,ku)
assert Ml < 2*s
assert T < Mu

assert max_mid < 2e-12
assert max_low < 2e-11
assert max_up < 2e-11
assert min_D > -2e-12
assert min_E > -2e-12
print('VERIFY_OK')
print('samples',samples)
print('max_middle_reduction_error',format(max_mid,'.3e'))
print('max_lower_defect_error',format(max_low,'.3e'))
print('max_upper_defect_error',format(max_up,'.3e'))
print('min_sample_D',format(min_D,'.3e'))
print('min_sample_E',format(min_E,'.3e'))
print('u_star',format(u,'.15f'))
print('alpha_star',format(a,'.15f'))
print('k_lower',format(klo,'.15f'))
print('k_upper',format(khi,'.15f'))
print('alpha_quartic_residual',format(abs(quart),'.3e'))
