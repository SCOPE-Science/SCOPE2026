"""Numerical and elementary-algebra checks for small-shell reset transitions.

Standard-library only. Not a substitute for the asymptotic/global proof.
"""
import math

Z=(2/(3*math.e**2))**(1/3)
K=1/3+1/(9*math.e**2)
S=4/Z**2

def mean0(c,z):
    x=z*c**(1/3)
    return (1-x*x-c*(1+c)*(1/x-1))/6

def mean_reset(c,z,h):
    delta=c**(1/3); x=z*delta; a=h/x
    # Stable exponential representation of the exact Dirichlet transform.
    den=-math.expm1(-2*a*(1-c))
    u=(c/x)*math.exp(-a*(x-c))*(-math.expm1(-2*a*(1-x)))/den
    u+=(1/x)*math.exp(-a*(1-x))*(-math.expm1(-2*a*(x-c)))/den
    return (1-u)/(a*a*u)

def golden(f,lo,hi,n=150):
    t=(math.sqrt(5)-1)/2
    a,b=lo,hi
    x=b-t*(b-a);y=a+t*(b-a)
    fx,fy=f(x),f(y)
    for _ in range(n):
        if fx<fy:
            b,y,fy=y,x,fx;x=b-t*(b-a);fx=f(x)
        else:
            a,x,fx=x,y,fy;y=a+t*(b-a);fy=f(y)
    h=(a+b)/2
    return h,f(h)

def transition(c):
    def diff(z):
        h,f=golden(lambda hh:mean_reset(c,z,hh),1,4)
        return f-mean0(c,z),h
    l,r=.3,.7
    assert diff(l)[0]<0 and diff(r)[0]>0
    for _ in range(75):
        mid=(l+r)/2
        if diff(mid)[0]<0:l=mid
        else:r=mid
    z=(l+r)/2; d,h=diff(z)
    return z,h,d

assert abs(Z**3-2/(3*math.e**2))<1e-14
assert abs(3*math.e**2*Z**2/4-1/(2*Z))<1e-14
assert abs(math.e**2*Z**3/8-1/12)<1e-14
assert abs(K-(Z**3*(math.e**2+1/6)-1/3))<1e-14
print('exact-identity checks: 4 PASS')
for c in (1e-3,1e-5,1e-7):
    z,h,d=transition(c)
    delta=c**(1/3)
    print('c=%.0e z=%.12f h=%.9f gamma*c^(2/3)=%.9f normalized-correction=%.8f' %
          (c,z,h,h*h/(z*z),(z-Z)/delta**2))
    assert abs(d)<1e-10
    assert abs(z-Z)<.01
    assert abs(h-2)<.07
    assert abs(h*h/(z*z)-S)<.7
# The limiting high-reset branch minimizes at h=2, and crosses 1/6 at z=Z.
assert abs(Z**3*math.exp(2)/4-1/6)<1e-14
for z in (Z*.8,Z*1.2):
    branch=z**3*math.e**2/4
    assert (branch<1/6)==(z<Z)
print('transition/branch checks: PASS')
