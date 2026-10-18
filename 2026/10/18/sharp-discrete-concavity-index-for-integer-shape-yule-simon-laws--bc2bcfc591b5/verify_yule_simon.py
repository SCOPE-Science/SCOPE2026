"""Standalone numerical cross-checks for the sharp lattice concavity boundary.
No finite sweep substitutes for the continuous derivative proof.
"""
import math

def threshold(rho):
    assert isinstance(rho,int) and rho>=1
    ell=math.log(rho+2)
    rr=math.log((rho+3)/2)
    def f(a): return math.expm1(a*rr)+math.expm1(-a*ell)
    lo=1e-10
    hi=1.0
    while f(hi)<=0: hi*=2
    for _ in range(90):
        mid=(lo+hi)/2
        if f(mid)>0:hi=mid
        else:lo=mid
    return (lo+hi)/2

def local(rho,k,a):
    # Normalized second difference of p(k)^(-a) (normalizer cancels).
    return math.expm1(a*math.log((k+rho+1)/k))+math.expm1(-a*math.log((k+rho)/(k-1)))

def harmonic_curvature(rho,x):
    weights=[1/(x+j) for j in range(rho+1)]
    return sum(u*u for u in weights)/(sum(weights)**2)

checks=0
for rho in range(1,17):
    a=threshold(rho)
    a_source=harmonic_curvature(rho,1)
    assert (rho+1)**-1 < a < a_source
    checks+=1
    assert abs(local(rho,2,a))<2e-13
    checks+=1
    assert local(rho,2,a*0.995)<-1e-6
    checks+=1
    for k in range(3,350):
        assert local(rho,k,a)>-1e-13,(rho,k,a,local(rho,k,a))
        checks+=1
    previous=harmonic_curvature(rho,1)
    for k in range(2,30):
        cur=harmonic_curvature(rho,k)
        assert cur<previous,(rho,k)
        previous=cur
        checks+=1

assert abs(threshold(1)-0.523305268852739)<3e-13
checks+=1
print('PASS:',checks,'numerical cross-check assertions (not an infinite proof)')
print('rho=1 sharp',format(threshold(1),'.15f'),'earlier sufficient',format(harmonic_curvature(1,1),'.15f'))
