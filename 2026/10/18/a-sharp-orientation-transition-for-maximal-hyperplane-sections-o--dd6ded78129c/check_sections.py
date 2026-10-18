"""Numerical checks for sharp hyperplane sections of Euclidean ball prisms.
Run: python3 check_sections.py. Standard library only; proof is in RESULT.md.
"""
from math import gamma, pi, sqrt

def kappa(n):
    return pi ** (n/2) / gamma(n/2+1)

def integrate(f, a, b, steps=800):
    if a == b: return 0.0
    step=(b-a)/steps
    z=f(a)+f(b)
    for i in range(1, steps):
        z += (4 if i%2 else 2)*f(a+i*step)
    return z*step/3

def j(alpha,k):
    return integrate(lambda t:max(0.,1-t*t)**alpha,0.,k)

def monitor(alpha,k):
    z=k*k
    return 2*alpha*integrate(lambda t:t*t*((1-z*t*t)**(alpha-1)) / ((1-z)**alpha),0.,1.)

def area(d,h,k):
    if k==0: return 2*kappa(d-2)*h
    alpha=(d-2)/2
    if k>=1: return kappa(d-1)*sqrt(h*h+k*k)/k
    return 2*kappa(d-2)*sqrt(h*h+k*k)*j(alpha,k)/k

def predicted(d,h):
    hc=sqrt(3/(d-2))
    if h>=hc: return 0.
    lo,hi=0.,1.-1e-12
    for _ in range(56):
        mid=(lo+hi)/2
        if h*h*monitor((d-2)/2,mid)>1:hi=mid
        else:lo=mid
    return (lo+hi)/2

def numerical(d,h):
    a,b=1e-7,1.
    # Standalone golden-section optimization of the integrated area.
    r=(sqrt(5)-1)/2
    c=b-r*(b-a);e=a+r*(b-a)
    for _ in range(90):
        if area(d,h,c)>area(d,h,e):
            b=e;e=c;c=b-r*(b-a)
        else:
            a=c;c=e;e=a+r*(b-a)
    return (a+b)/2

checks=0
for d in (4,5,6,9,20):
    alpha=(d-2)/2
    previous=monitor(alpha,0.)
    assert abs(previous-(d-2)/3)<1e-12
    for i in range(1,100):
        x=i/100
        now=monitor(alpha,x)
        assert now>previous
        previous=now
        checks+=1
    hc=sqrt(3/(d-2))
    for r in (0.30,0.80,0.99,1.0,1.10):
        h=hc*r
        k=predicted(d,h)
        km=numerical(d,h)
        if k>0:assert abs(k-km)<0.00002,(d,r,k,km)
        else:assert km<0.001,(d,r,km)  # flat quartic onset is ill-conditioned numerically
        ac=area(d,h,k)
        assert ac+1e-9>=max(area(d,h,0),area(d,h,1),kappa(d-1))
        if d==4:
            exact=(4*pi/3)*(1+h*h/3)**1.5 if h<=hc else 2*pi*h
            assert abs(ac-exact)<1e-8,(h,ac,exact)
        checks+=1
print('EUCLIDEAN_CYLINDER_SECTION_CHECK_OK comparisons=',checks)
print('dimensions=',(4,5,6,9,20),'height_ratios=',(0.3,0.8,0.99,1,1.1))
print('critical_halfheight_squared=3/(d-2); four_dimensional_profile_checked')
