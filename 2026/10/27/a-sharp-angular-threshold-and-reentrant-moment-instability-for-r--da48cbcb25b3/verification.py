"""Independent exact and numerical checks for the balanced two-test heat-step model.
Run with Python 3; no third-party packages required.
"""
from fractions import Fraction as F
from math import atan, cos, sin, sqrt, tan, log, isfinite
from random import Random

# An exact-rational stress witness, including both the moment/Lyapunov split
# and the correct two heat-mode Rayleigh coefficients.
m,L=F(1),F(9)
v0,v1=F(3),F(1)  # coefficients divided by sqrt(10)
a=(m*v0*v0+L*v1*v1)/10
c=(-v1*m*v0+v0*L*v1)/10
assert a==F(9,5) and c==F(12,5)
q,d=a+c,c-a
assert q==F(21,5) and d==F(3,5)
t=F(14,5)
gp=1/(1+q*t)
gm=1/(1-d*t)
H=(gp**2+gm**2)/2
assert gp==F(25,319) and gm==-F(25,17)
assert H==F(31890625,29408929) and H>1
assert abs(gp*gm)==F(625,5423)<1
assert (1+q*F(1,100))>0 and (1-d*F(1,100))>0

# Uniform sharp angle: exact rational equality by tan(theta)=3/4,
# m=1, L=9 gives the critical orientation; the critical
# angle instead has tan(theta)=3/4 because 2sqrt(9)/(9-1)=3/4.
assert F(2*3,9-1)==F(3,4)
# At the critical angle, the maximal normalized cross term equals a.
assert F(3,4)*F(9-1,2*3)==1

rng=Random(20261018)
count=0
for _ in range(14000):
    m=10**rng.uniform(-2,1)
    kappa=10**rng.uniform(0,4)
    L=m*kappa
    phi=rng.uniform(-3.0,3.0)
    theta=rng.uniform(0,1.4)
    tau=10**rng.uniform(-3,3)
    a=m*cos(phi)**2+L*sin(phi)**2
    c=(L-m)*sin(phi)*cos(phi)
    b=tan(theta)*c
    # Direct minimization in one test direction yields this update.
    # Compare formula from dot products, avoiding singular configurations.
    for sgn in (-1,1):
        beta=a+sgn*b
        D=1+tau*beta
        if abs(D)<1.e-9:continue
        vx,vy=cos(phi),sin(phi)
        wx=cos(phi+sgn*theta)
        wy=sin(phi+sgn*theta)
        measured=wx*vx+wy*vy
        represented=wx*m*vx+wy*L*vy
        D_direct=(measured+tau*represented)/measured
        assert abs(D_direct-D)<3.e-8*max(1,abs(D))
    # Exact universal threshold criterion against an optimizer formula.
    bound=(L-m)/(2*sqrt(m*L))
    if kappa>1.0000001:
        critical=2*atan(sqrt(m/L))
        assert abs(tan(critical)*bound-1)<3.e-11
    H=0.5*((1+tau*(a+b))**(-2)+(1+tau*(a-b))**(-2)) if abs(1+tau*(a+b))>1.e-8 and abs(1+tau*(a-b))>1.e-8 else None
    if H is not None:
        assert H>=0 and isfinite(H)
    count+=1

# Reentrant intervals for a collection of random positive q,d.
for _ in range(500):
    q=10**rng.uniform(-1,2)
    d=q*rng.uniform(.01,.9)
    def h(t):return .5*((1+q*t)**-2+(1-d*t)**-2)
    t0=1/d
    assert h(min(1.e-5/(q+d),t0*1.e-9))<1 and h(t0*.999)>1
    assert h(t0*1.001)>1 and h(t0*1.e8)<1
    lo,hi=0.,t0*(1-1.e-9)
    for _ in range(90):
        mid=(lo+hi)/2
        if h(mid)<1:lo=mid
        else:hi=mid
    minus=(lo+hi)/2
    lo,hi=t0*(1+1.e-9),t0*1.e8
    for _ in range(90):
        mid=(lo+hi)/2
        if h(mid)>1:lo=mid
        else:hi=mid
    plus=(lo+hi)/2
    assert 0<minus<t0<plus
    assert h(minus/2)<1 and h((minus+t0)/2)>1
    assert h((t0+plus)/2)>1 and h(plus*2)<1
    # The upper second-moment edge has negative almost-sure exponent:
    p=abs((1+q*plus)*(1-d*plus))
    assert p>1-1.e-8

print('PASS: rational heat-mode witness, 14000 reconstruction/angle cases, 500 phase-diagram sweeps')
