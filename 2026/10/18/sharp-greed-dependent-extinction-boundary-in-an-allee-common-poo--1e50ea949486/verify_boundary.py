"""Numerical checks for the survival separatrix of an Allee resource game.

Standard-library only.  Numerical integration is supporting evidence; the
continuum theorem is established by the mathematical proof, not sampling.
Run: python verify_boundary.py
"""
import math
import random


def roots(A, c, d, x):
    e = d - (d - c) * x
    disc = (1 - A)**2 - 4*A*e
    assert disc > 0
    return (1 + A - math.sqrt(disc))/2, (1 + A + math.sqrt(disc))/2


def boundary(A, c, d, T, w, x_end, step=0.002):
    """Integrate invariant-graph equation using logit(x) as coordinate."""
    rd = roots(A, c, d, 0)[0]
    lam = math.sqrt((1-A)**2 - 4*A*d)/A
    assert 0 < x_end < 1
    z0 = -25.0
    zend = math.log(x_end/(1-x_end))
    count = math.ceil((zend-z0)/step)
    dz = (zend-z0)/count
    # The stable-manifold slope supplies the asymptotic initial condition.
    x0 = 1/(1+math.exp(-z0))
    tangent = -T*(d-c)/(w+T*lam)
    R = rd + tangent*x0

    def F(z, y):
        x=1/(1+math.exp(-z))
        return -T/w*((y/A-1)*(1-y)-d+(d-c)*x)

    for j in range(count):
        z = z0+j*dz
        k1 = F(z,R)
        k2 = F(z+dz/2,R+dz*k1/2)
        k3 = F(z+dz/2,R+dz*k2/2)
        k4 = F(z+dz,R+dz*k3)
        R += (dz/6)*(k1+2*k2+2*k3+k4)
        assert math.isfinite(R)
    return R


def outcome(A, c, d, T, w, R, x, t_end=220, dt=0.02):
    def rhs(R,x):
        return (T*R*((R/A-1)*(1-R)-d+(d-c)*x),-w*R*x*(1-x))
    for _ in range(int(t_end/dt)):
        r1,x1=rhs(R,x)
        r2,x2=rhs(R+dt*r1/2,x+dt*x1/2)
        r3,x3=rhs(R+dt*r2/2,x+dt*x2/2)
        r4,x4=rhs(R+dt*r3,x+dt*x3)
        R += dt*(r1+2*r2+2*r3+r4)/6
        x += dt*(x1+2*x2+2*x3+x4)/6
    return R,x


def main():
    # The exact figures reproduce the parameter setting in the source model.
    A,c,d,T=0.1,0.5,1.5,2.0
    x=0.5
    rD=roots(A,c,d,0)[0]
    rC=roots(A,c,d,1)[0]
    expected=(rD+rC)/2
    bounds=[]
    for w in (0.1,0.2,0.5,1.0):
        h=boundary(A,c,d,T,w,x)
        r=roots(A,c,d,x)[0]
        lam=math.sqrt((1-A)**2-4*A*d)/A
        upper=(d-c)*w/(4*T*lam**2)
        assert r < h < rD and h-r < upper
        bounds.append(h)
    assert all(a<b for a,b in zip(bounds,bounds[1:]))
    h=bounds[-1]
    print('source_parameters boundary at x=0.5, w=1:',format(h,'.14f'))
    print('source_parameters linear interpolation at x=0.5:',format(expected,'.14f'))
    print('difference:',format(expected-h,'.14f'))
    assert abs(h-0.2329591070365)<3e-9
    for shift,should_survive in [(-0.01,False),(0.01,True)]:
        Rout,_=outcome(A,c,d,T,1.0,h+shift,x)
        print('initial displacement',shift,'resource at t=220',Rout)
        assert (Rout>0.5)==should_survive

    rng=random.Random(20261013)
    tests=0
    for j in range(60):
        A=rng.uniform(0.055,0.32)
        cap=(1-A)**2/(4*A)
        d=cap*rng.uniform(0.3,0.76)
        c=d*rng.uniform(0.15,0.8)
        T=rng.uniform(0.8,2.4)
        x=rng.uniform(0.18,0.76)
        w1=rng.uniform(0.26,0.57)
        w2=rng.uniform(w1+0.08,1.0)
        l=roots(A,c,d,x)[0]
        rD=roots(A,c,d,0)[0]
        lam=math.sqrt((1-A)**2-4*A*d)/A
        h1=boundary(A,c,d,T,w1,x)
        h2=boundary(A,c,d,T,w2,x)
        assert l<h1<h2<rD,(j,A,c,d,T,w1,w2,x,h1,h2,l,rD)
        assert h1-l<(d-c)*w1/(4*T*lam*lam)*(1+2e-6)
        assert h2-l<(d-c)*w2/(4*T*lam*lam)*(1+2e-6)
        tests+=1
    print('random parameter pairs checked:',tests)
    print('PASS (numerical corroboration only)')

if __name__=='__main__':
    main()
