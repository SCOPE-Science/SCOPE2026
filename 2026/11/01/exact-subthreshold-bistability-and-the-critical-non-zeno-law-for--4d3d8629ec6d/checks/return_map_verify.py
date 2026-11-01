"""Standalone numerical and algebraic spot checks for exponential-relaxation impact return."""
import math

def integral_I(u, eta):
    if abs(u) < 1e-4:
        return sum(((-u)**k / math.factorial(k)) * (1/(k+1)-(1+eta)/(k+2)) for k in range(10))
    q=-math.expm1(-u)
    return (1+eta*math.exp(-u)-(1+eta)*q/u)/u

def integral_I_prime(u, eta):
    if abs(u) < 1e-3:
        return -sum(((-u)**k/math.factorial(k))*(1/(k+2)-(1+eta)/(k+3)) for k in range(10))
    e=math.exp(-u)
    q=1-e
    numerator=(1+eta)*(q-u*e)-eta*u*u*e - u*(1+eta*e-(1+eta)*q/u) # dH * u-H
    return numerator/(u**3)

def bisect(fun, left, right, iters=85):
    fl=fun(left)
    assert fl*fun(right)<0,(left,right,fl,fun(right))
    for _ in range(iters):
        mid=(left+right)/2
        if mid ==left or mid==right:break
        fm=fun(mid)
        if fl*fm<=0:right=mid
        else:left=mid;fl=fm
    return (left+right)/2

def v_given_period(u,r):
    return u/2-r*(1-(-math.expm1(-u))/u)

def preimpact_given_period(u,r):
    return v_given_period(u,r)+r*(-math.expm1(-u))-u

def r_of_period(u,eta):
    return (1-eta)/(2*integral_I(u,eta))

def flight_period(v,r):
    # v=0 and r>1 has nonzero flight; bracketing positive root except at v=0.
    def h(u):
        return v_given_period(u,r)-v
    left=1e-12;right=max(10.0,4*r+4*v)
    assert h(left)<0 and h(right)>0, (v,r,h(left),h(right))
    return bisect(h,left,right)

def map_v(v,r,eta):
    t=flight_period(v,r)
    return -eta*preimpact_given_period(t,r)

# Verify exact finite identities and physicality of all fixed orbit branches.
for eta in (0.2,0.5,0.51,0.8,0.99):
    for u in (0.02,0.1,0.4,1.5,5,18):
        r=r_of_period(u,eta)
        v=v_given_period(u,r)
        incoming=preimpact_given_period(u,r)
        assert v>0 and incoming<0,(eta,u,v,incoming)
        assert math.isclose(-eta*incoming,v,rel_tol=2e-8,abs_tol=1e-13)
        assert abs((r*integral_I(u,eta)-(1-eta)/2)) <2e-10

eta=0.8
ustar=bisect(lambda u:integral_I_prime(u,eta),0.01,6)
rstar=r_of_period(ustar,eta)
assert abs(ustar-1.8256460599269313) < 1e-8 # exact numeric reference
assert abs(rstar-0.6049417558) < 1e-8,(ustar,rstar)
r=0.8
ul=bisect(lambda u:r_of_period(u,eta)-r,1e-4,ustar)
ur=bisect(lambda u:r_of_period(u,eta)-r,ustar,20)
assert abs(ul-0.29694240479500456) < 1e-8,(ul,ur)
assert abs(ur-5.352910578596973) < 1e-8
vl,vr=(v_given_period(u,r) for u in (ul,ur))
for v,kind in ((vl,'repelling'),(vr,'attracting')):
    d=1e-6*max(v,1)
    deriv=(map_v(v+d,r,eta)-map_v(v-d,r,eta))/(2*d)
    assert (deriv>1 if kind=='repelling' else 0<deriv<1),(kind,deriv)
    print(kind,'launch speed=',v,'multiplier=',deriv)
print('eta=',eta,'threshold period',ustar,'r_min=',rstar,'branches:',ul,ur)

# Check critical map drift to 2 terms in small-flight parameter.
for u in (0.04,0.02,0.01):
    v=v_given_period(u,1)
    p=-0.5*preimpact_given_period(u,1)
    k=(v-p)/v**1.5
    assert abs(k-math.sqrt(6)/8)<0.01,(u,k)
    print('critical',u,'coefficient',k)

# Verify 1/n asymptotic without unstable near-zero flight root computation:
# iterate using the smooth u period parametrization, solve period for v with bisection for first 100000 steps
u=.5
out=[]
for n in range(1,30001):
    v=v_given_period(u,1)
    p=-.5*preimpact_given_period(u,1)
    # solve v(u_next)=p; on r=1 V strictly increasing
    u=bisect(lambda x:v_given_period(x,1)-p, max(1e-12,u*.2),u,48)
    if n in (100,1000,10000,30000): out.append((n,n*n*p,n*u))
for record in out:print('critical n,n² v,n u=',record)
assert abs(out[-1][1]-128/3) < 4.0, out[-1]
assert abs(out[-1][2]-16)<1, out[-1]
print('ALL CHECKS PASS')
