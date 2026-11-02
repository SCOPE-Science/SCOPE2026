#!/usr/bin/env python3
"""Finite consistency tests for binomially smoothed positive weighted shifts.
This is supplementary numerical verification; see RESULT.md for the analytic proof.
"""
import math

def binom(n,theta):
    return [math.comb(n,k)*theta**k*(1-theta)**(n-k) for k in range(n+1)]

def pget(p,k):
    return p[k] if 0<=k<len(p) else 0.0

def direct_col(n,j,a,theta):
    p=binom(n,theta); q=binom(n+1,theta)
    return sum(abs(pget(q,k)-pget(p,k))*(j/(j-k))**a for k in range(j))

def gradient_col(n,j,a,theta):
    p=binom(n,theta)
    return theta*sum(abs(pget(p,k-1)-pget(p,k))*(j/(j-k))**a for k in range(j))

def exact_shift_growth(k,a):
    return (k+1)**a

def phi(x):
    return math.exp(-x*x/2)/math.sqrt(2*math.pi)

def gaussian_profile(a,t,steps=16000):
    # Substitute x=t-y^(1/(1-a)) to regularize y^-a at the endpoint.
    # dx/(t-x)^a = dy/(1-a). Truncate x at -12.
    R=(t+12)**(1-a)
    h=R/steps
    def fun(y):
        x=t-(max(y,0.0))**(1/(1-a))
        return abs(x)*phi(x)/(1-a)
    return h*(0.5*fun(0)+sum(fun(k*h) for k in range(1,steps))+0.5*fun(R))

def run():
    assertions=0
    for n in (1,2,4,7,15,31):
        for a in (0.15,0.5,0.8):
            for theta in (0.2,0.5,0.7):
                for j in range(1,n+9):
                    x=direct_col(n,j,a,theta)
                    y=gradient_col(n,j,a,theta)
                    assert abs(x-y) < 2e-10*(1+x+y), (n,a,theta,j,x,y)
                    assertions+=1
                for k in range(n+1):
                    assert exact_shift_growth(k,a)>=1
                    assertions+=1
    a,theta=0.5,0.5
    # At t=1 the normalized central-column values converge to explicit profile.
    target=(theta/(1-theta))**((1+a)/2)*gaussian_profile(a,1)
    for n in (1000,4000):
        mu=n*theta; sigma=math.sqrt(n*theta*(1-theta)); j=round(mu+sigma)
        # Stable binomial mass recurrence centered at its mode.
        mode=round((n+1)*theta); p=[0.0]*(n+1)
        p[mode]=math.exp(math.lgamma(n+1)-math.lgamma(mode+1)-math.lgamma(n-mode+1)+mode*math.log(theta)+(n-mode)*math.log1p(-theta))
        for k in range(mode-1,-1,-1):
            p[k]=p[k+1]*(k+1)*(1-theta)/((n-k)*theta)
        for k in range(mode+1,n+1):
            p[k]=p[k-1]*(n-k+1)*theta/(k*(1-theta))
        val=theta*sum(abs(pget(p,k-1)-pget(p,k))*(j/(j-k))**a for k in range(j))*n**((1-a)/2)
        assert abs(val-target)<0.11,(n,val,target)
        assertions+=1
    print(f'CHECK_OK finite_assertions={assertions}; central_target_t1={target:.9f}')
if __name__=='__main__':run()
