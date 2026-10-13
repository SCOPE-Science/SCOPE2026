#!/usr/bin/env python3
import cmath, math

def h2(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p*math.log2(p)-(1-p)*math.log2(1-p)

def mi_from_channel(u,k):
    # uniform input x; W(y|x)=(1+y*u+x*y*k)/2
    probs={}
    for x in (-1,1):
        for y in (-1,1):
            probs[x,y]=0.25*(1+y*u+x*y*k)
    px={x:sum(probs[x,y] for y in (-1,1)) for x in (-1,1)}
    py={y:sum(probs[x,y] for x in (-1,1)) for y in (-1,1)}
    out=0.0
    for x in (-1,1):
        for y in (-1,1):
            p=probs[x,y]
            if p>0:
                out += p*math.log2(p/(px[x]*py[y]))
    return out

def direct_prob(lam,alpha,theta,phi,x,y):
    # Alice equatorial eigenvector; Bob arbitrary Bloch eigenvector.
    # + eigenstate n(theta,phi): cos(theta/2)|0>+e^{iphi}sin(theta/2)|1>.
    def eig(th,ph,s):
        if s==1:
            return (math.cos(th/2), cmath.exp(1j*ph)*math.sin(th/2))
        return (-cmath.exp(-1j*ph)*math.sin(th/2), math.cos(th/2))
    av=eig(math.pi/2,alpha,x)
    bv=eig(theta,phi,y)
    amp=(math.sqrt(lam)*av[0].conjugate()*bv[0].conjugate()+
         math.sqrt(1-lam)*av[1].conjugate()*bv[1].conjugate())
    return abs(amp)**2

def close(a,b,tol=3e-11):
    if abs(a-b)>tol:
        raise AssertionError((a,b,abs(a-b)))

# Direct-amplitude probability formula.
for lam in (0.05,0.2,0.5,0.83,0.97):
    C=2*math.sqrt(lam*(1-lam)); r=2*lam-1
    for alpha in (0.0,0.37,1.2,2.4):
        for theta in (0.1,0.7,1.3,2.2,3.0):
            for phi in (0.0,0.5,1.7,2.8):
                ax,ay=math.cos(alpha),math.sin(alpha)
                bx=math.sin(theta)*math.cos(phi); by=math.sin(theta)*math.sin(phi); bz=math.cos(theta)
                t=ax*bx-ay*by
                for x in (-1,1):
                    for y in (-1,1):
                        formula=0.25*(1+y*r*bz+x*y*C*t)
                        close(direct_prob(lam,alpha,theta,phi,x,y),formula)

# Kernel identity and mutual-information data processing throughout the cone.
for C in (0.0,0.1,0.35,0.7,0.95,0.999):
    r=math.sqrt(max(0.0,1-C*C))
    zmax=1.0 if C==0 else math.sqrt((1-C)/(1+C))
    for zfrac in (-1.0,-0.55,0.0,0.4,1.0):
        z=zfrac*zmax
        u=r*z
        for t in (-0.9,-0.33,0.15,0.72):
            # A physical Bob axis also requires t^2+z^2<=1; skip otherwise.
            if t*t+z*z>1+1e-12:
                continue
            if abs(u)+C>1+1e-12:
                raise AssertionError('cone stochasticity')
            for x in (-1,1):
                for y in (-1,1):
                    lhs=0.0
                    for y0 in (-1,1):
                        K=0.5*(1+y*(u+C*y0))
                        W1=0.5*(1+x*y0*t)
                        if K < -1e-12 or K > 1+1e-12:
                            raise AssertionError('invalid kernel')
                        lhs += K*W1
                    rhs=0.5*(1+y*u+x*y*C*t)
                    close(lhs,rhs)
            if mi_from_channel(u,C*t) > mi_from_channel(0.0,t)+2e-12:
                raise AssertionError('data processing violation')

# Necessity for nonzero t within the binary affine parameterization: matching row
# average and difference uniquely forces alpha=u, beta=C; stochasticity iff |u|+C<=1.
for C in (0.2,0.6,0.9):
    r=math.sqrt(1-C*C)
    threshold=(1-C)/r
    for z in (0.0,0.5*threshold,threshold,min(1.0,1.05*threshold)):
        u=r*z
        valid=(abs(u)+C<=1+1e-12)
        formula=(z<=threshold+1e-12)
        if valid != formula:
            raise AssertionError('boundary mismatch')

print('VERIFY_OK')
