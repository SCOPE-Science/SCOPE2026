#!/usr/bin/env python3
"""Independent quadrature/zonotope checks for finite-horizon oscillator support area.
Requires only Python 3 standard library. This is finite numerical evidence, not an infinite proof.
"""
import math


def impulse(t, m, gamma, mu):
    alpha = gamma / (2*m)
    omega2 = mu/m-alpha*alpha
    if omega2 > 1e-14:
        w=math.sqrt(omega2)
        return math.exp(-alpha*t)*math.sin(w*t)/w, math.exp(-alpha*t)*(math.cos(w*t)-alpha*math.sin(w*t)/w)
    if omega2 < -1e-14:
        k=math.sqrt(-omega2)
        return math.exp(-alpha*t)*math.sinh(k*t)/k, math.exp(-alpha*t)*(math.cosh(k*t)-alpha*math.sinh(k*t)/k)
    return t*math.exp(-alpha*t), (1-alpha*t)*math.exp(-alpha*t)


def area_integral(T, m, gamma, mu, force, N=10000):
    hstep=T/N
    val=0.0
    decay=gamma/m
    for j in range(N):
        t=(j+0.5)*hstep
        h,_=impulse(t,m,gamma,mu)
        val+=abs(h)*(-math.expm1(-decay*(T-t)))/decay
    return 4*(force/m)**2*val*hstep


def area_zonotope(T, m, gamma, mu, force, N=800):
    """Polygon area for a discrete Minkowski sum of N line segments."""
    dt=T/N
    generators=[]
    for j in range(N):
        t=(j+0.5)*dt
        h,hp=impulse(t,m,gamma,mu)
        generators.append(((force/m)*dt*h,(force/m)*dt*hp))
    area=0.0
    for j,(x,y) in enumerate(generators):
        for x2,y2 in generators[j+1:]:
            area+=abs(x*y2-y*x2)
    return 4*area


def limit_area(m,gamma,mu,force):
    alpha=gamma/(2*m)
    w2=mu/m-alpha**2
    base=4*force**2/(gamma*mu)
    if w2<=0: return base
    z=math.pi*alpha/(2*math.sqrt(w2))
    return base/math.tanh(z)


def check():
    tests=[
        (1.,5.,1.,1.,1.),
        (1.,2.,1.,1.,2.3),
        (1.,1.,1.,1.,2.0),
        (1.,1.,1.,1.,8.0),
        (1.,0.5,1.,1.,5.2),
        (2.,3.,0.8,1.3,3.1),
        (1.,1.,4.,2.,7.7),
    ]
    count=0
    for m,g,k,f,T in tests:
        a=area_integral(T,m,g,k,f)
        z=area_zonotope(T,m,g,k,f)
        rel=abs(a-z)/a
        assert rel < 0.0007, ('quadrature-zonotope mismatch',m,g,k,T,a,z,rel)
        assert 0<a<limit_area(m,g,k,f),('area monotone upper bound',m,g,k,T,a)
        print(f'm={m} gamma={g} mu={k} force={f} T={T}: analytic={a:.10f}, polygon={z:.10f}, relerr={rel:.2g}')
        count+=2
    for m,g,k,f in [(1,5,1,1),(1,2,1,1),(1,1,1,1),(1,.5,1,1),(2,3,.8,1.3)]:
        target=limit_area(m,g,k,f)
        for T in [200.0,250.0]:
            # For low damping, this is deep into the settled finite-horizon regime.
            val=area_integral(T,m,g,k,f,N=25000)
            assert abs(val-target)/target < 0.0003,(m,g,k,T,val,target)
            count+=1
    # Exact cusp times and jump ratios, tested against one-sided derivatives of |h|.
    for m,g,k,f in [(1,1,1,1),(1,.5,1,2),(3,2,3,1.7)]:
        alpha=g/(2*m);omega=math.sqrt(k/m-alpha**2);b=f/m
        span=math.pi/omega
        jumps=[]
        for n in (1,2,3):
            t=n*span
            eps=1e-6
            l=abs(impulse(t,m,g,k)[0])-abs(impulse(t-eps,m,g,k)[0])
            rr=abs(impulse(t+eps,m,g,k)[0])-abs(impulse(t,m,g,k)[0])
            numeric=4*b*b*(rr-l)/eps
            exact=8*b*b*math.exp(-alpha*t)
            assert abs(numeric-exact)/exact < 1e-5,('cusp',n,numeric,exact)
            jumps.append(exact)
            count+=1
        assert abs(jumps[1]/jumps[0]-math.exp(-alpha*span))<1e-12
        count+=1
    # Independent short-time cubic coefficient.
    for m,g,k,f in [(1,5,1,1),(1,1,1,1),(2,3,.8,1.3)]:
        t=0.001
        a=area_integral(t,m,g,k,f,N=1000)
        leading=(2/3)*(f/m)**2*t**3
        assert abs(a/leading-1)<0.0025,(m,g,k,a,leading)
        count+=1
    print('PASS',count,'independent finite checks')

if __name__=='__main__':check()
