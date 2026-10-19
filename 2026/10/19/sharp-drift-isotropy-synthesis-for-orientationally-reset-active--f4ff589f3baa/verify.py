"""Finite numerical diagnostics for sharp drift-isotropy synthesis in angular resetting.
The theorem and its infinite-family proof are in RESULT.md; these checks support it.
Python 3 standard library only. Execute: python verify.py
"""
from __future__ import annotations
import cmath
import math
import random

EPS=1e-10
checks=0

def near(z, w, tol=EPS):
    global checks
    assert abs(z-w) <= tol, (z,w,abs(z-w))
    checks+=1

def a_b(t):
    return t/(t+1),t/(t+4)

def moments(weights_angles):
    assert abs(sum(w for w, _ in weights_angles)-1) < 1e-10
    return (sum(w*cmath.exp(1j*theta) for w,theta in weights_angles),
            sum(w*cmath.exp(2j*theta) for w,theta in weights_angles))

def chord(mu, direction):
    """Two atom chord realizing first moment mu and maximal variance direction."""
    assert abs(mu)<1
    u=cmath.exp(1j*direction)
    h=(mu.conjugate()*u).real
    root=math.sqrt(h*h+1-abs(mu)**2)
    tminus=-h-root
    tplus=-h+root
    wplus=-tminus/(tplus-tminus)
    wminus=tplus/(tplus-tminus)
    assert wplus>=0 and wminus>=0
    zplus=mu+tplus*u
    zminus=mu+tminus*u
    near(abs(zplus),1)
    near(abs(zminus),1)
    return [(wplus,cmath.phase(zplus)),(wminus,cmath.phase(zminus))]

def realize(mu,nu2):
    """Realize all feasible first/second angular moments with at most four atoms."""
    qmax=1-abs(mu)**2
    if qmax<1e-12:
        near(nu2,mu*mu,1e-9)
        return [(1.0,cmath.phase(mu))]
    z=(nu2-mu*mu)/qmax
    assert abs(z)<=1+1e-9
    radius=min(1.0,abs(z))
    phi=cmath.phase(z)/2
    left=chord(mu,phi)
    right=chord(mu,phi+math.pi/2)
    return [((1+radius)*w/2,theta) for w,theta in left]+[((1-radius)*w/2,theta) for w,theta in right]

def diffusion_moments(mu,nu2,t,v=1.0,Dr=1.0,D=0.1):
    a,b=a_b(t)
    c1=a*mu
    z=b*nu2-c1*c1
    scalar=v*v/(2*Dr*(1+t))
    tr=1-abs(c1)**2
    return ((D+scalar*(tr+z.real),scalar*z.imag),
            (scalar*z.imag,D+scalar*(tr-z.real)))

def optimal_drift(t,v=1):
    a,b=a_b(t)
    return v*a*math.sqrt(b/(b+abs(b-a*a)))

# Published fixed-direction result (Baouche et al., arXiv:2405.06769,
# Eqs. 19-20) is recovered for the singleton reset law.
for k in range(1,301):
    t=k/40
    K=diffusion_moments(1+0j,1+0j,t,v=2,Dr=3,D=0)
    x=(4+10*t)/((1+t)**3*(4+t))
    y=4/((1+t)*(4+t))
    near(2*3/(2*2)*K[0][0],x,2e-14)
    near(2*3/(2*2)*K[1][1],y,2e-14)
    near(K[0][1],0)

# The exact complex disk is attained on every boundary direction by two
# reset angles. Any interior point is synthesized by at most four atoms.
rng=random.Random(4102026)
for j in range(240):
    mu=cmath.rect(.985*math.sqrt(rng.random()),2*math.pi*rng.random())
    direction=2*math.pi*rng.random()
    p=chord(mu,direction)
    got1,got2=moments(p)
    near(got1,mu)
    near(got2,mu*mu+(1-abs(mu)**2)*cmath.exp(2j*direction))
    z=math.sqrt(rng.random())*cmath.exp(1j*2*math.pi*rng.random())
    desired=mu*mu+(1-abs(mu)**2)*z
    synthesized=realize(mu,desired)
    m1,m2=moments(synthesized)
    near(m1,mu)
    near(m2,desired)
    near(sum(w for w,theta in synthesized),1)
    assert all(w>=-1e-14 for w,theta in synthesized)
    checks+=1

# Exact maximum drift for isotropic long-time diffusion, with sharp
# two-atom extremizers on both sides of the critical reduced rate 1/2.
for k in range(1,501):
    t=k/200
    a,b=a_b(t)
    q=b/(b+abs(b-a*a))
    mu=math.sqrt(q)
    if abs(t-.5)<1e-13:
        dist=[(1.,0.)]
    elif t<.5:
        angle=math.acos(mu)
        dist=[(.5,angle),(.5,-angle)]
    else:
        dist=[((1+mu)/2,0),((1-mu)/2,math.pi)]
    m1,m2=moments(dist)
    near(m1,mu)
    near(b*m2,a*a*mu*mu)
    K=diffusion_moments(m1,m2,t)
    near(K[0][0],K[1][1])
    near(K[0][1],0)
    near(a*mu,optimal_drift(t))
    assert b*(1-q)+1e-14 >= abs(b-a*a)*q
    checks+=1

# A strictly below-cutoff drift can be made exactly isotropic; a strictly
# above-cutoff drift cannot, as checked through the exact moment disk.
for k in range(1,241):
    t=(k+20)/70
    a,b=a_b(t)
    qc=b/(b+abs(b-a*a))
    low=0.73*math.sqrt(qc)
    eta=(a*a/b)*low*low
    assert abs(eta-low*low)<=1-low*low+1e-14
    dist=realize(low+0j,eta+0j)
    m1,m2=moments(dist)
    K=diffusion_moments(m1,m2,t)
    near(K[0][0],K[1][1])
    near(K[0][1],0)
    if qc<1-1e-10:
        qhigh=(qc+1)/2
        assert abs((a*a/b-1)*qhigh)>1-qhigh
        checks+=1

# Four-angle example with nonzero drift and isotropic dispersion:
# Dr=lambda=v=1, ν(0)=37/64, ν(pi)=5/64, ν(±pi/2)=11/64 each.
dist=[(37/64,0.),(5/64,math.pi),(11/64,math.pi/2),(11/64,-math.pi/2)]
mu,eta=moments(dist)
near(mu,1/2)
near(eta,5/16)
K=diffusion_moments(mu,eta,1,v=1,Dr=1,D=0)
near(K[0][0],15/64)
near(K[1][1],15/64)
near(K[0][1],0)

# Independently sample the stationary angular process: last-reset age is
# exponential; the angular displacement conditional on age is Gaussian.
for t in [0.2,0.5,1,3]:
    Dr=1.; lam=t; D=0
    law=[(.55,.2),(.30,1.7),(.15,-2.2)]
    m1,m2=moments(law)
    analytic=a_b(t)[0]*m1
    analytic2=a_b(t)[1]*m2
    cumulative=[]
    s=0
    for w,theta in law:
        s+=w
        cumulative.append((s,theta))
    z1=0j;z2=0j;nn=60000
    for _ in range(nn):
        h=rng.random()
        th=next(th for cutoff,th in cumulative if h<=cutoff)
        age=rng.expovariate(lam)
        ph=th+rng.gauss(0,math.sqrt(2*Dr*age))
        z=cmath.exp(1j*ph)
        z1+=z;z2+=z*z
    near(z1/nn,analytic,0.018)
    near(z2/nn,analytic2,0.018)

print('PASS:',checks,'checks (finite diagnostics; infinite-family claims proved analytically)')
