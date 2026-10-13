#!/usr/bin/env python3
"""Standalone reproduction of rational guards and sampled SIR incidence signs.
The mathematical proof in RESULT.md applies to all positive integers, not just tests.
"""
from fractions import Fraction as Q
from math import exp, erf, pi, sqrt

def guards():
    T = Q(1,20)
    s_lower = Q(18,25)
    i_upper = Q(2,17)
    beta_lower = Q(39,10)
    H_lower = beta_lower*(s_lower-i_upper)-1
    H_upper = Q(4)*Q(9,10)-1
    assert H_lower == Q(2867,2125)
    assert H_lower > Q(13,10)
    assert H_upper == Q(13,5)
    assert beta_lower*s_lower-1 > Q(18,10)
    assert Q(1,10)+Q(4,100) < H_lower
    assert Q(13,5)-4 < 0
    assert T == Q(1,20)

def beta_and_log_slope(t, k, eps):
    T = 1/20
    delta = min(eps,1/100)
    drift = min(1/10,delta/(8*T))
    space = T/(k+1)
    width = min(space/20, delta/(128*k))
    centers = [j*space for j in range(1,k+1)]
    # integral from zero to t of exp(-((u-c)/w)^2)
    theta = drift*t + 2*sqrt(pi)*width*sum(erf((t-c)/width)-erf(-c/width) for c in centers)
    q = drift + 4*sum(exp(-((t-c)/width)**2) for c in centers)
    return 4*exp(-theta),q,centers,width

def sample(k, eps):
    T = 0.05
    steps = max(20000, 4000*k)
    h = T/steps
    s,i=0.9,0.1
    t=0.
    def rhs(tt,ss,ii):
        b=beta_and_log_slope(tt,k,eps)[0]
        return -b*ss*ii, b*ss*ii-ii
    while t < T-h/2:
        k1,l1=rhs(t,s,i)
        k2,l2=rhs(t+h/2,s+h*k1/2,i+h*l1/2)
        k3,l3=rhs(t+h/2,s+h*k2/2,i+h*l2/2)
        k4,l4=rhs(t+h,s+h*k3,i+h*l3)
        s+=h*(k1+2*k2+2*k3+k4)/6
        i+=h*(l1+2*l2+2*l3+l4)/6
        t+=h
    b,_,centers,w=beta_and_log_slope(T,k,eps)
    assert s>0 and i>0.1
    assert -__import__('math').log(b/4) < eps
    assert w<T/(10*(k+1))
    for j in range(k):
        c=centers[j]
        at_c=beta_and_log_slope(c,k,eps)[1]
        assert at_c>=4
        mid_prev=(0 if j==0 else centers[j-1])/2+c/2
        mid_next=(T if j==k-1 else centers[j+1])/2+c/2
        for x in [mid_prev,mid_next]:
            assert beta_and_log_slope(x,k,eps)[1] < 0.15

def main():
    guards()
    for k,eps in [(1,1e-2),(2,1e-3),(4,1e-4),(7,1e-3),(12,1e-5)]:
        sample(k,eps)
    print('VERIFY_OK: rational guards and five independent sampled Gaussian schedules')

if __name__=='__main__':
    main()
