"""Reproduce the sharp speed-weighted residual gain for pinned ignition orbits.

Pure Python 3 standard library.  Numerical tests supplement, but do not
replace, the analytical proof of uniqueness and the large-order limit.
"""
from math import exp, log, isclose
from random import Random


def theta(y, q):
    return log(y / (1-y)) - sum(1/(j*y**j) for j in range(1, q))


def speed(y, q):
    return y**(q-1)*(1-y)


def discrepancy(y, q):
    a = (q-1)/q
    return 1/(y**(q-1)*(q-1-q*y)) - (theta(a, q)-theta(y, q))


def root(q):
    a = (q-1)/q
    lo = (0.001 if q == 2 else (0.015 if q <= 4 else a*.35))
    hi = a*(1-1e-7)
    assert discrepancy(lo, q) < 0 and discrepancy(hi, q) > 0
    for _ in range(90):
        mid = (lo+hi)/2
        if discrepancy(mid, q) < 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def gain(q):
    y = root(q)
    return (1-y)/(q-1-q*y)


def simpson(f, a, b, n=800):
    assert n%2==0
    h=(b-a)/n
    return h/3*(f(a)+f(b)+4*sum(f(a+(2*i-1)*h) for i in range(1,n//2+1))
                  +2*sum(f(a+2*i*h) for i in range(1,n//2)))


def e_lim(z):
    return exp(z)/(z-1)-simpson(lambda u:exp(u)/u,1,z,n=1200)


def limit_root():
    lo,hi=2.,8.
    for _ in range(75):
        mid=(lo+hi)/2
        if e_lim(mid)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2


def main():
    checks=0
    results=[]
    for q in (2,3,4,5,6,8,10,12,16,20,40):
        y=root(q)
        a=(q-1)/q
        b=gain(q)
        assert 0<y<a and b>1/(q-1)
        assert abs(discrepancy(y,q)) < max(5e-8, abs(theta(y,q))*2e-13)
        assert isclose(b,speed(y,q)*(theta(a,q)-theta(y,q)),rel_tol=1e-10,abs_tol=1e-11)
        assert b>log(q/(q-1))
        checks+=4
        for k in range(1,401):
            z= (0.001+(0.999-0.001)*k/401)
            if z <= y:
                v=speed(z,q)*(theta(a,q)-theta(z,q))
                assert v<=b*(1+5e-12)
                checks+=1
            if z>=a:
                v=speed(z,q)*(theta(z,q)-theta(a,q))
                assert v<=b*(1+5e-12)
                checks+=1
        results.append((q,y,b,q*b))
    # The derivative identity D'(y)=y^(1-q)/((1-y)(q-1-q*y)^2)
    for q in (2,3,4,5,6):
        a=(q-1)/q
        for k in range(1,21):
            y=0.025+(a-0.06)*k/22
            h=2e-6*y
            numeric=(discrepancy(y+h,q)-discrepancy(y-h,q))/(2*h)
            symbolic=y**(1-q)/((1-y)*(q-1-q*y)**2)
            assert isclose(numeric,symbolic,rel_tol=2e-5,abs_tol=1e-5)
            checks+=1
    z=limit_root()
    b_inf=z/(z-1)
    assert abs(z-4.30064097)<2e-7
    assert abs(b_inf-1.30297145584)<2e-9
    checks+=2
    print('Unique left-side maximizers and sharp gains (q, y_q, B_q, q*B_q):')
    for r in results: print('%2d %.12g %.12g %.12g'%r)
    print('Limiting scaled location %.12g and gain %.12g'%(z,b_inf))
    print('PASSED %d supplementary checks'%checks)

if __name__=='__main__':
    main()
