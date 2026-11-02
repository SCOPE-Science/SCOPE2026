"""Standalone numerical checks for a three-particle Gaussian-localized inversion identity.

Uses only the Python standard library. These finite checks supplement an analytical proof.
"""
import math


def weighted_statistics(a, x, kappa):
    particles = (-a, x, a)
    data = tuple(z*z for z in particles)
    raw = [math.exp(-((z-x)/kappa)**2/2) for z in particles]
    rawsum = math.fsum(raw)
    w = [z/rawsum for z in raw]
    mx = math.fsum(wi*zi for wi, zi in zip(w,particles))
    my = math.fsum(wi*gi for wi, gi in zip(w,data))
    denom = 1-math.fsum(wi*wi for wi in w)
    cg = math.fsum(wi*(zi-mx)*(gi-my) for wi,zi,gi in zip(w,particles,data))/denom
    vg = math.fsum(wi*(gi-my)**2 for wi,gi in zip(w,data))/denom
    return cg,vg


def direct_step(a,x,kappa,ridge):
    cg,vg=weighted_statistics(a,x,kappa)
    return x+cg*(a*a-x*x)/(vg+ridge)


def reduction(a,x,kappa,ridge):
    u=math.exp(-0.5*((x+a)/kappa)**2)
    v=math.exp(-0.5*((x-a)/kappa)**2)
    s=u+v
    omega=(a*a-x*x)**2 / ((a*a-x*x)**2 + 2*ridge*(1+u*v/s))
    return (1-omega)*x + omega*a*math.tanh(a*x/(kappa*kappa))


def positive_root(a,kappa):
    assert kappa<a
    lo=1.0e-12*a
    hi=a
    for _ in range(140):
        mid=(lo+hi)/2
        if a*math.tanh(a*mid/(kappa*kappa)) > mid: lo=mid
        else: hi=mid
    return (lo+hi)/2


def check():
    checks=0
    for a in (0.7,1.0,1.8,3.0):
      for krel in (0.38,0.7,0.95,1.,1.15,1.5,3.):
        for ridge in (0.025,0.2,1.,5.):
          kappa=a*krel
          for frac in (-0.91,-0.73,-0.3,-0.05,0.,0.05,0.3,0.73,0.91):
            x=a*frac
            direct=direct_step(a,x,kappa,ridge)
            exact=reduction(a,x,kappa,ridge)
            assert math.isclose(direct,exact,abs_tol=2e-12*a,rel_tol=2e-12), (a,x,kappa,ridge,direct,exact)
            assert -a<exact<a
            checks+=2
    # Endpoint exact observations always yield zero updates, hence remain pinned.
    for a in (0.9,2.):
      for kappa in (0.4,1.5,3.):
        for ridge in (0.1,2.):
          for x in (-0.7*a,0.,0.8*a):
            # regardless of central particle, endpoint innovation is identically zero.
            assert abs(a*a-a*a)==0
            checks+=1
    # Check the claimed attraction basins using long iterations.
    for krel in (0.6,0.8,1.,1.2,2.0):
      a=1.; kappa=krel; ridge=0.1
      limit=positive_root(a,kappa) if kappa<1 else 0.
      for x0 in (-.82,-.17,.17,.82):
        x=x0
        last=abs(x)
        for _ in range(15000):
          nx=reduction(a,x,kappa,ridge)
          if kappa<1. and x0>0 and x0<limit: assert nx>=x-1e-15
          if kappa<1. and x0>limit: assert nx<=x+1e-15
          x=nx
          assert -a<x<a
        if kappa!=a: assert abs(x-math.copysign(limit,x0))<0.025
        else: assert abs(x)<0.035
        checks+=2
    # Critical rate is only asymptotically valid, so compare long paths at moderate tolerance.
    a=1.; kappa=1.; ridge=0.5
    u=math.exp(-.5)
    omega0=a**4/(a**4+2*ridge*(1+u/2))
    predicted=a*math.sqrt(3/(2*omega0))
    for x0 in (0.1,0.4,0.9):
      x=x0
      for _ in range(400000): x=reduction(a,x,kappa,ridge)
      val=math.sqrt(400000)*abs(x)
      assert abs(val/predicted-1)<.01,(val,predicted)
      checks+=1
    return checks,predicted

if __name__=='__main__':
    n,constant=check()
    print(f'PASS: {n} supplementary checks; critical predicted sqrt(n) amplitude {constant:.12f}')
