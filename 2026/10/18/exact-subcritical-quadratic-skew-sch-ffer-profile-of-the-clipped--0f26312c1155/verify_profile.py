"""Standalone finite diagnostics for an exact two-dimensional norm profile.

Only the analytic inequalities in RESULT.md prove the global statement.
Run with Python 3 standard library.
"""
import math

def N(x):
    return max(math.sqrt(2.0)*abs(x[0]), math.hypot(x[0], x[1]))

def evaluate(r):
    z=r*r
    U=(1-r*math.sqrt(1-z+z*z))/(1+z*z)
    t=1-U
    assert abs((1+z*z)*U*U-2*U+1-z)<2e-12
    u=(2*U-1)/math.sqrt(2)
    v=(1-(1+z)*U)/(math.sqrt(2)*r)
    d=(1-(1-z)*U)/(math.sqrt(2)*r)
    assert 0<u<1/math.sqrt(2) and 0<v<1/math.sqrt(2)
    assert abs(v*v+d*d-1)<1e-9
    x=(1/math.sqrt(2),u)
    y=(-v,d)
    assert abs(N(x)-1)<1e-10 and abs(N(y)-1)<1e-10
    A=[x[i]+r*y[i] for i in range(2)]
    B=[r*x[i]-y[i] for i in range(2)]
    assert abs(A[0]-A[1])<1e-9
    assert abs(B[0]+B[1])<1e-9
    F=(N(A)**2+N(B)**2)/2
    target=(1+z)**2*(1+(1-z)*U*U)/2
    assert abs(F-target)<2e-9
    ell=-(t*t-U*z)/(t*(t-z))
    mu=(1-2*t)*(U*z+t)*(t-U*z)/(t*(t-z))
    q=1+z
    f=1-z
    aa=q*(1-ell)-mu*f
    bb=2*q*(1+ell)-2*mu*f
    assert -1<ell<0 and mu>0 and mu-ell<1
    assert aa>0 and bb>0
    assert abs(2*aa*u-4*mu*r*d)<1e-8
    assert abs(2*bb*v+4*mu*r*u*v/d-4*mu*r/math.sqrt(2))<1e-8
    assert abs((1+ell-mu)-2*(1-2*t)*U**2*z*z/(t*(t-z)))<1e-8
    return target

if __name__ == '__main__':
    rcrit=math.sqrt(2-math.sqrt(3))
    for j in range(1,2001):
        r=rcrit*j/2001
        evaluate(r)
    for r in [0.025,0.1,0.2,0.3,0.4,0.5,0.517]:
        print(f'r={r:.6f}, S(r)^2={evaluate(r):.12f}')
    assert abs(evaluate(rcrit*(1-1e-5))-.75*(1+rcrit*rcrit))<2e-5
    print('PASS: 2000 interior certificates, seven reference samples, transition diagnostic')
