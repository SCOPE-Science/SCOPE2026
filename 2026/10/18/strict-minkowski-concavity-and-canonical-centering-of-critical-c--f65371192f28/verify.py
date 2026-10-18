#!/usr/bin/env python3
"""Deterministic finite numerical checks of critical transition-body centering.
No external dependencies. The general-dimensional assertions are established
by the separate analytic proof, not by these finite quadratures.
"""
import math

PI=math.pi
NORMALS=240
ANGLES=80
BETA=1.0
nv=[(math.cos(2*PI*j/NORMALS), math.sin(2*PI*j/NORMALS)) for j in range(NORMALS)]
uv=[(math.cos(2*PI*j/ANGLES), math.sin(2*PI*j/ANGLES)) for j in range(ANGLES)]
W=2*PI/NORMALS
U=2*PI/ANGLES
LOG2=math.log(2)

def logcosh(z):
    t=abs(z)
    return t+math.log1p(math.exp(-2*t))-LOG2

def phi(t,rr,u):
    total=0.0
    for v0,v1 in nv:
        h=1+t*v0
        z=rr*(u[0]*v0+u[1]*v1)/(2*h)
        total+=h*logcosh(z)
    return total*W

def radius(t,u):
    lo,hi=0.,8.
    assert phi(t,hi,u)>BETA
    for _ in range(45):
        mid=(lo+hi)/2
        if phi(t,mid,u)>BETA:hi=mid
        else:lo=mid
    return (lo+hi)/2

def area(rr):
    return 0.5*U*sum(x*x for x in rr)

def hess_integrand(u,r):
    d=0.
    n=0.
    for v0,v1 in nv:
        dot=u[0]*v0+u[1]*v1
        z=r*dot/2
        d+=0.5*dot*math.tanh(z)*W
        n+=v0*v0*(r*dot)**2/4/(math.cosh(z)**2)*W
    assert d>0 and n>0
    return n/d

r0=[radius(0,u) for u in uv]
v0=area(r0)
coefficient=0.5*U*sum(r*hess_integrand(u,r) for u,r in zip(uv,r0))
assert 3.16<coefficient<3.18
losses=[]
for shift in (0.02,0.04,0.08):
    rr=[radius(shift,u) for u in uv]
    assert all(q<p-1e-8 for p,q in zip(r0,rr))
    loss=(v0-area(rr))/(shift*shift)
    losses.append(loss)
    assert abs(loss-coefficient)<0.01
assert abs(losses[0]-coefficient)<abs(losses[1]-coefficient)<abs(losses[2]-coefficient)

# Numerical confirmation of strict perspective interpolation for disk translates.
a0,a1=0.13,-0.18
ra=[radius(a0,u) for u in uv]
rb=[radius(a1,u) for u in uv]
for k in range(0,ANGLES,8):
    for j in range(0,ANGLES,10):
        p=ra[k]*uv[k][0]/2+rb[j]*uv[j][0]/2
        q=ra[k]*uv[k][1]/2+rb[j]*uv[j][1]/2
        r=math.hypot(p,q)
        if r>1e-9:
            val=phi((a0+a1)/2,r,(p/r,q/r))
            assert val<BETA-1e-9, (k,j,val)

# The scalar perspective has the expected positive h-curvature.
for h,z in ((0.3,0.2),(1.0,1.5),(2.0,-3.0)):
    f=lambda hh:hh*logcosh(z/(2*hh))
    eps=1e-4*h
    numerical=(f(h+eps)-2*f(h)+f(h-eps))/(eps*eps)
    exact=z*z/(4*h**3*math.cosh(z/(2*h))**2)
    assert abs(numerical/exact-1)<0.00005,(h,z,numerical,exact)

print('CRITICAL_TRANSITION_RECENTERING_CHECKS_OK')
print('disk_beta=1, radius_approx=',round(r0[0],12))
print('quadratic_loss_coefficient_approx=',round(coefficient,12))
print('finite_difference_losses=',[round(x,10) for x in losses])
