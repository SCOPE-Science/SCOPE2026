"""Numerical cross-checks for the two-number-state radial mask theorem.
Uses only the Python standard library. Numerical sampling is corroborative,
not a substitute for the analytic inequalities in RESULT.md.
"""
import math


def root_t(m):
    lo, hi = 1.0e-12, float(m)
    for _ in range(95):
        mid = (lo + hi) / 2
        if m * (-math.expm1(-mid)) > mid:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def dens(k, t):
    return math.exp(-t) * t**k / math.factorial(k)


def numint(k, u, v, steps=256):
    h = (v-u)/steps
    return h/3*(dens(k,u)+dens(k,v)+4*sum(dens(k,u+h*j) for j in range(1,steps,2))+2*sum(dens(k,u+h*j) for j in range(2,steps,2)))


def verify():
    tests=0
    for m in range(2,16):
        t = root_t(m)
        a,b = dens(0,t), dens(m,t)
        theta = b/(1+b-a)
        c = math.factorial(m)**(1/m)
        p = (b-a)/(1+b-a)
        assert m-1 < t < m
        assert b > a and 0 < p < 1
        assert theta > math.exp(-c)
        assert abs(m*(-math.expm1(-t))-t) < 1e-12
        assert abs(theta*a+(1-theta)*b-theta)<2e-14
        tests+=5
        for j in range(1,5001):
            s = j*max(m+2,10)/5000
            F=theta*dens(0,s)+(1-theta)*dens(m,s)
            assert F <= theta + 3e-14
        tests+=1
        for A in [0.01,0.025,0.05,0.10]:
            u=p*A
            v=t-(1-p)*A/2
            w=t+(1-p)*A/2
            x0 = numint(0,0,u)+numint(0,v,w)
            xm = numint(m,0,u)+numint(m,v,w)
            assert min(x0,xm)<=theta*A+2e-12
            # Dividing by the small area approaches the predicted sharp constant.
            assert abs(min(x0,xm)/A-theta)<0.025
            tests+=2
    for A in [0.01,0.1,1.0,3.0,8.0]:
        u=A/math.expm1(A)
        x0 = numint(0,u,u+A,4096)
        x1 = numint(1,u,u+A,4096)
        assert abs(x0-x1)<2e-11
        assert abs(x0-math.exp(-u)*(1-math.exp(-A)))<2e-11
        tests+=2
    return tests

if __name__=='__main__':
    n=verify()
    print(f'PASS: {n} deterministic analytical-identity and quadrature assertions')
