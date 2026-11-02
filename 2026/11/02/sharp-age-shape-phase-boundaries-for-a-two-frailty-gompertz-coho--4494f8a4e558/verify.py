"""Reproducible checks for the two-point Gompertz cohort hazard classification.

The analytic proof, not this finite computation, establishes universal assertions.
Run with Python 3.10+; only standard-library dependencies.
"""
import math
import random


def p(u):
    return 1.0 / (1.0 + math.exp(u))


def g(u, A, k):
    v = p(u)
    return A + v - (u + k) * v * (1 - v)


def bisect(f, a, b, iterations=90):
    fa, fb = f(a), f(b)
    assert fa * fb <= 0, (a,b,fa,fb)
    for _ in range(iterations):
        m = (a + b)/2
        fm = f(m)
        if fa * fm <= 0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return (a + b)/2


def min_u(k):
    return bisect(lambda u: (u + k) * math.tanh(u/2) - 2, 0, 100)


def roots(A, k):
    us = min_u(k)
    res = []
    if g(0,A,k) > 1e-14 and g(us,A,k) < -1e-14:
        res.append(bisect(lambda u:g(u,A,k),0,us))
    if g(us,A,k) < -1e-14:
        res.append(bisect(lambda u:g(u,A,k),us,100))
    return res


def cohort_hazard(t, a, b, c):
    s = math.expm1(c*t)/c
    low = math.exp(-a*s)
    high = math.exp(-b*s)
    return math.exp(c*t)*(a*low+b*high)/(low+high)


def independent_sign_test():
    rng = random.Random(511930)
    for _ in range(3000):
        a = 10**rng.uniform(-1.5,.5)
        d = 10**rng.uniform(-1.5,.5)
        b = a+d
        c = 10**rng.uniform(-1,.7)
        t = rng.random()*min(1,2/c)
        A=a/d; k=d/c; u=k*math.expm1(c*t)
        h = 1e-5 / (1 + c)
        left = cohort_hazard(max(0,t-h),a,b,c)
        right = cohort_hazard(t+h,a,b,c)
        num = (right-left)/(t+h-max(0,t-h))
        analytic = c*d*(1+u/k)*g(u,A,k)
        assert math.isclose(num, analytic,rel_tol=2e-4,abs_tol=2e-5),(a,b,c,t,num,analytic)


def exact_phase_tests():
    A=.25
    kc=4*A+2-math.log1p(1/A)
    k0=4*A+2
    for k in (.1, 1.0, kc-.01):
        assert g(min_u(k),A,k)>0
        assert len(roots(A,k))==0
    for k in (kc+.01, 2.0, k0-.01):
        rr=roots(A,k)
        assert len(rr)==2, (k,rr)
        assert g(0,A,k)>0 and g(min_u(k),A,k)<0 and g(100,A,k)>0
    for k in (k0,k0+.01,9.0):
        rr=roots(A,k)
        assert len(rr)==1
        assert g(rr[0]-1e-4,A,k)<0 and g(rr[0]+1e-4,A,k)>0
    assert abs(g(math.log1p(1/A),A,kc))<1e-13
    assert abs((math.log1p(1/A)+kc)*math.tanh(math.log1p(1/A)/2)-2)<1e-13
    rr=roots(A,2.0)
    assert abs(rr[0]-0.634307250238139)<1e-11
    assert abs(rr[1]-2.418458919210159)<1e-11
    for eps in (1e-2,1e-3,1e-4):
        lo,hi=roots(A,kc+eps)
        pred=2*math.sqrt(2*eps/(2*A+1))
        assert abs((hi-lo)/pred-1)<3e-4
        first=roots(A,k0-eps)[0]
        assert abs(first/(eps/2)-1)<.002
    print('Verification passed: 3,000 independent derivative comparisons; phase boundaries, exact example and fold/endpoint scalings.')

if __name__=='__main__':
    independent_sign_test()
    exact_phase_tests()
