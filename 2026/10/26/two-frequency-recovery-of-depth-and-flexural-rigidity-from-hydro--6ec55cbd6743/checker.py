#!/usr/bin/env python3
"""Independent dimensionless dispersion inversion checks (not a proof)."""
from math import tanh, atanh, sinh, cosh, isclose
from scipy.optimize import brentq

def lower(u, q):
    if u < 1:
        return tanh(q * atanh(u))
    return 1 + q**4 * (u - 1)

def inverse(q, u, v):
    if not (q>1 and u>0 and lower(u,q)<v<q**5*u):
        raise ValueError('outside strict feasible domain')
    upper = atanh(u) if u<1 else max(40.,4.0/(q-1))
    def f(t):
        b=u/tanh(t)-1
        return (1+q**4*b)*tanh(q*t)-v
    t=brentq(f,1e-11,upper,xtol=1e-13)
    b=u/tanh(t)-1
    return t,b

def jacobian(t,b,q):
    th=tanh(t)
    thq=tanh(q*t)
    sech2=lambda s: 1/cosh(s)**2
    return q**4*(1+b)*sech2(t)*thq-q*(1+q**4*b)*th*sech2(q*t)

if __name__=='__main__':
    n=0
    for q in (1.05,1.2,1.75,2.,3.,5.):
        for t in (.05,.3,1.,2.,4.):
            for b in (.001,.1,1.,10.):
                u=(1+b)*tanh(t)
                v=(1+q**4*b)*tanh(q*t)
                assert lower(u,q)<v<q**5*u, (q,t,b,u,v)
                T,B=inverse(q,u,v)
                assert isclose(T,t,rel_tol=2e-7,abs_tol=5e-9),(q,t,b,T,B)
                assert isclose(B,b,rel_tol=2e-6,abs_tol=5e-8),(q,t,b,T,B)
                assert jacobian(t,b,q)>0,(q,t,b)
                n+=1
    q,t,b=2.,.8,.4
    u=(1+b)*tanh(t);v=(1+q**4*b)*tanh(q*t)
    T,B=inverse(q,u,v)
    print('PASS: %d interior samples, data bounds, unique numerical reconstruction and Jacobian orientation' % n)
    print('example q=%.8g t=%.8g b=%.8g u=%.12g v=%.12g inverse t=%.12g b=%.12g' %(q,t,b,u,v,T,B))
    print('for u=%.12g, admissible v lies in (%.12g, %.12g)' % (u,lower(u,q),q**5*u))
