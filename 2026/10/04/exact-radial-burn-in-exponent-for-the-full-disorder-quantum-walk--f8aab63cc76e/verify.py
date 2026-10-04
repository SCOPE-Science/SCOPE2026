#!/usr/bin/env python3
import cmath, math, random

def step(w,s,chi):
    return cmath.exp(-1j*chi)*(w+s)/(1+s*w)

def check_identity():
    pts=[0.1+0.2j,-0.3+0.4j,0.7j,-0.5+0.1j]
    for s in (0.2,0.6,0.9):
        for w in pts:
            if abs(w)>=1: continue
            f=(w+s)/(1+s*w)
            lhs=1-abs(f)**2
            rhs=(1-s*s)*(1-abs(w)**2)/abs(1+s*w)**2
            assert abs(lhs-rhs)<2e-12,(s,w,lhs,rhs)

def check_haar_jensen():
    # Trapezoidal rule is exponentially accurate for this analytic periodic integrand.
    for s in (0.2,0.6,0.9):
        for rho in (0.0,0.2,0.6,0.95):
            N=32768
            mean=sum(math.log(abs(1+s*rho*cmath.exp(2j*math.pi*k/N))) for k in range(N))/N
            assert abs(mean)<2e-12,(s,rho,mean)

def check_telescoping():
    rng=random.Random(1729)
    for s in (0.3,0.7):
        w=0.1+0.2j
        D=math.log(1-abs(w)**2)
        for _ in range(20):
            x=math.log(abs(1+s*w))
            D += math.log(1-s*s)-2*x
            w=step(w,s,2*math.pi*rng.random())
            assert abs(D-math.log(1-abs(w)**2))<1e-8

def check_empirical_rate():
    rng=random.Random(271828)
    for s in (0.3,0.7):
        target=math.log(1-s*s)
        vals=[]
        for _ in range(2000):
            w=0.1+0.2j
            D=math.log(1-abs(w)**2)
            for _ in range(100):
                D += math.log(1-s*s)-2*math.log(abs(1+s*w))
                w=step(w,s,2*math.pi*rng.random())
            vals.append(D/100)
        mean=sum(vals)/len(vals)
        assert abs(mean-target)<0.02,(s,mean,target)

if __name__=='__main__':
    check_identity(); check_haar_jensen(); check_telescoping(); check_empirical_rate()
    print('VERIFY_OK')
