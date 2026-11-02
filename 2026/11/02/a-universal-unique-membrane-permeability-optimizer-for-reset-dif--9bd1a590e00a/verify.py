"""Reproducible diagnostics for universal membrane-permeability optimization.

Uses the Python 3 standard library only.  The analytic proof is in RESULT.md.
"""
import math
import random


def bisect(fn, lo, hi, n=100):
    assert fn(lo) * fn(hi) < 0
    for _ in range(n):
        mid = (lo + hi)/2
        if fn(mid) * fn(lo) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi)/2


def stationary(D, L, r, atoms, kappa):
    eta = math.sqrt(r/D)
    denom = math.sinh(eta*L)
    A = eta/denom * sum(w*math.cosh(eta*(L-y)) for y,w in atoms)
    B = eta/denom * sum(w*math.cosh(eta*y) for y,w in atoms)
    g = math.tanh(eta*L/2)/(D*eta)
    J = kappa*(B-A)/(1+2*kappa*g)
    def pN(x):
        return eta/denom*sum(w*math.cosh(eta*min(x,y))*math.cosh(eta*(L-max(x,y))) for y,w in atoms)
    def p(x):
        return pN(x) + J*math.sinh(eta*(L/2-x))/(D*eta*math.cosh(eta*L/2))
    ep = J*math.log(p(L)/p(0))
    return A,B,g,J,p,ep


def universal(D,L,r,atoms):
    A,B,g,_,_,_ = stationary(D,L,r,atoms,1)
    h=abs(A-B)/(A+B)
    if h<1.e-12:
        return None,h,g
    fn = lambda t: math.atanh(h*t)-h*(1-t)/(1-h*h*t*t)
    t=bisect(fn,1.e-12,1-1.e-12)
    return (1/t-1)/(2*g),h,g


def simpson(f,L,n=10000):
    assert n%2==0
    dx=L/n
    return dx/3*(f(0)+f(L)+4*sum(f((2*i-1)*dx) for i in range(1,n//2+1))+2*sum(f(2*i*dx) for i in range(1,n//2)))


def check():
    checks=0
    rng=random.Random(7721)
    t_infty=bisect(lambda t: math.atanh(t)-1/(1+t),0.4,0.7)
    assert abs(t_infty-0.5643765885603998)<1e-14; checks+=1
    assert abs((1/t_infty-1)/2-.3859332759981943)<1e-14; checks+=1
    for case in range(30):
        L=rng.uniform(0.8,2.0); D=rng.uniform(0.6,2.0); r=rng.uniform(0.3,3.0)
        count=1+(case%5)
        ys=[rng.uniform(.05*L,.95*L) for _ in range(count)]
        ws=[rng.expovariate(1) for _ in range(count)]; ws=[w/sum(ws) for w in ws]
        atoms=list(zip(ys,ws))
        kappa,h,g=universal(D,L,r,atoms)
        assert 0<h<1 and .38593327<kappa*g<.5000001; checks+=1
        A,B,g,J,p,E=stationary(D,L,r,atoms,kappa)
        assert p(0)>0 and p(L)>0 and E>0; checks+=1
        assert abs(J-kappa*(p(L)-p(0)))<1e-12; checks+=1
        dx=1e-6*L
        assert abs(-D*(p(dx)-p(0))/dx-J)<2e-5; checks+=1
        assert abs(-D*(p(L)-p(L-dx))/dx-J)<2e-5; checks+=1
        assert abs(simpson(p,L,n=1500)-1)<2.5e-3; checks+=1
        etas=[kappa*math.exp(z/7) for z in range(-28,29)]
        vmax=max(stationary(D,L,r,atoms,k)[5] for k in etas)
        assert vmax<=E*(1+2e-12); checks+=1
        assert stationary(D,L,r,atoms,kappa*.8)[5]<E; checks+=1
        assert stationary(D,L,r,atoms,kappa*1.2)[5]<E; checks+=1
        # Verify independent positive-density Green representation away from atoms.
        x=L*.375
        if all(abs(x-y)>.02*L for y in ys):
            q=1e-4*L
            residual=D*(p(x+q)-2*p(x)+p(x-q))/(q*q)-r*p(x)
            assert abs(residual)<0.0003; checks+=1
    # Reflection-asymmetric reset laws can have zero interface entropy at a fixed r.
    x=.21; atoms=[(x,.5),(1-x,.5)]
    k,h,g=universal(1,1,2,atoms)
    assert k is None and h==0; checks+=1
    for k in [1.e-4,1.,1.e4]:
        A,B,g,J,p,E=stationary(1,1,2,atoms,k)
        assert abs(J)<1e-12 and abs(E)<1e-12; checks+=1
    # Extreme h is approached by large rate and resetting near a boundary.
    k,h,g=universal(1,1,400,[(.001,1.)])
    assert h>.97 and .38593<k*g<.4; checks+=1
    print('PASS',checks,'checks; sharp bound', (1/t_infty-1)/2)

if __name__ == '__main__':
    check()
