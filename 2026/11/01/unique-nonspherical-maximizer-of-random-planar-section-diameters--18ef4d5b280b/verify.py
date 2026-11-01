"""Numerical cross-checks for the planar-section mean-radius integral.
These tests are finite diagnostics, not proofs of universal statements.
Standard-library-only; run with python verify.py.
"""
import math


def simpson(fun, a, b, n=4096):
    assert n % 2 == 0
    h = (b-a)/n
    s = fun(a)+fun(b)
    for i in range(1,n):
        s += (4 if i % 2 else 2)*fun(a+h*i)
    return s*h/3


def density(d):
    return (math.sin(d)+(math.pi-d)*math.cos(d))/4


def phi(t):
    return simpson(lambda d: density(d)/(math.cosh(2*t)-math.cos(d)*math.sinh(2*t))**0.5,0,math.pi)


def dphi(t):
    return simpson(lambda d: density(d)*(math.cos(d)*math.cosh(2*t)-math.sinh(2*t))/(math.cosh(2*t)-math.cos(d)*math.sinh(2*t))**1.5,0,math.pi)


def check():
    assert abs(simpson(density,0,math.pi)-1)<3e-10
    assert abs(phi(0)-1)<3e-10
    assert abs(dphi(0)-math.pi**2/16)<3e-9
    # Direct comparison of numerically integrated profile and its unique critical region.
    assert dphi(0.7887)>0 and dphi(0.7889)<0
    left,right=.7887,.7889
    for _ in range(40):
        mid=(left+right)/2
        if dphi(mid)>0:left=mid
        else:right=mid
    t=(left+right)/2
    assert abs(t-.7888103975)<3e-7
    assert abs(phi(t)-1.27326059867)<3e-7
    assert abs(math.exp(2*t)-4.84341860599)<1e-6
    # Sampled strict log-concavity: a diagnostic, not the proof.
    for a in [-1.2,-.3,0,.3,.7,1.5,2.7]:
        for b in [.2,.8,1.4,3.2]:
            if abs(a-b)<1e-8:continue
            m=(a+b)/2
            assert math.log(phi(m))>(math.log(phi(a))+math.log(phi(b)))/2+1e-5
    # Cusa-Huygens inequality, the positive proof certificate's elementary core.
    for k in range(1,250):
        q=math.pi*k/250
        assert q*(2+math.cos(q))>3*math.sin(q)
    print('PASS: normalization, derivative, critical bracket, sampled concavity, analytic-lemma diagnostics')
    print('t* approximately %.12f; optimal mean radius approximately %.12f'%(t,phi(t)))

if __name__=='__main__':
    check()
