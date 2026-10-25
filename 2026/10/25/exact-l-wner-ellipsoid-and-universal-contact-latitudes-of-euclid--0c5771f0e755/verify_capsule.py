#!/usr/bin/env python3
"""Reproduce exact-support, contact, and asymptotic checks for a convex capsule's outer ellipsoid.

No floating-point test is a substitute for the theorem's analytic certificate.
"""
import math

def parameters(d, h):
    assert isinstance(d, int) and d >= 2 and h > 0
    t = 2.0 / (math.hypot((d-1)*h, 2*math.sqrt(d)) + (d-1)*h)
    B = 1+h*t
    A = B*(1+h/t)
    return t, A, B

def check():
    comparisons=0
    max_error=0.0
    for d in (2, 3, 4, 5, 11, 50, 200):
        for h in (.01, .1, .5, 1., 3., 10.):
            t,A,B=parameters(d,h)
            assert 0<t<1
            assert A>(h+1)**2 and B>1
            assert abs(d*t*(t+h)/(1+h*t)-1)<2e-11
            q=(t+h)**2/A
            assert abs(q-1/d)<2e-11
            assert abs((1-t*t)/B-(d-1)/d)<2e-11
            for k in range(201):
                s=k/200
                lhs=A*s*s+B*(1-s*s)-(1+h*s)**2
                rhs=h/t*(s-t)**2
                max_error=max(max_error,abs(lhs-rhs))
                assert abs(lhs-rhs)<2e-9*max(1,A)
                assert lhs>=-2e-9*max(1,A)
                comparisons+=1
    for tau in (0.0,.5,1.,3.,10.):
        u=(math.sqrt(tau*tau+4)-tau)/2
        target=math.exp(tau*u/2)/u
        vals=[]
        for d in (500,2000,8000):
            h=max(tau,1e-12)/math.sqrt(d)
            t,A,B=parameters(d,h)
            V=math.sqrt(A)*math.exp((d-1)/2*math.log(B))
            vals.append(abs(V-target))
        assert (tau==0 or vals[-1]<vals[0]) and vals[-1]<0.05
    for h in (0.1,1.,8.):
        d=16000;t,A,B=parameters(d,h)
        ratio=math.sqrt(A)*math.exp((d-1)/2*math.log(B))/(h*math.sqrt(d))
        assert abs(ratio-math.sqrt(math.e))<0.02
    print('PASS:',comparisons,'support comparisons; 42 isotropy/contact checks; 15 crossover checks; 3 wide-separation checks; max residual',max_error)
if __name__=='__main__':check()
