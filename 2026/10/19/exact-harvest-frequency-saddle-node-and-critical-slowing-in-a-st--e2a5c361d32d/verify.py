"""Independent numerical and symbolic checks for a cubic-Allee pulse fishery.
Requires sympy and scipy. Run with python verify.py.
"""
import math
import random
import sympy as S
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

def critical(a, q, r):
    return (math.log(q)/a+(1+a)*math.log((1-a*q)/(q-a))/(a*(1-a)))/r

def flow(z,t,a,r):
    def rhs(_,y):
        x=y[0]
        return [r*x*(1-x)*(x-a)]
    return solve_ivp(rhs, [0,t], [z], rtol=2e-12, atol=5e-14).y[0,-1]

def test():
    x,a,q,r=S.symbols('x a q r', positive=True)
    f=lambda z:r*z*(1-z)*(z-a)
    xx=q*(1+a)/(1+q)
    yy=(1+a)/(1+q)
    assert S.factor(xx+yy-(1+a)) == 0
    assert S.factor((yy-xx)-(1+a)*(1-q)/(1+q)) == 0
    assert S.factor((f(yy)/f(xx))-1/q)==0
    critical_p2=S.factor((S.diff(f(x),x).subs(x,yy)-S.diff(f(x),x).subs(x,xx))/f(xx))
    expect_p2=-(1+a)*(1-q)/(q*(1-xx)*(xx-a))
    assert S.simplify(critical_p2-expect_p2)==0
    K=S.factor(-2/critical_p2)
    assert S.simplify(K-2*q*(1-a*q)*(q-a)/((1+q)**2*(1+a)*(1-q)))==0
    print('symbolic identities: all passed')
    rng=random.Random(51444)
    total=0
    for _ in range(12):
        A=rng.uniform(0.08,0.76)
        Q=rng.uniform(A+0.02,0.99)
        R=rng.uniform(0.55,2.5)
        tc=critical(A,Q,R)
        X=Q*(1+A)/(1+Q)
        Y=(1+A)/(1+Q)
        assert abs(flow(X,tc,A,R)-Y)<3e-9
        for factor, nroot in [(0.90,0),(1.10,2)]:
            tau=factor*tc
            # sample total monotone structure away from endpoints
            grid=[A+(Q-A)*j/120 for j in range(121)]
            vals=[Q*flow(z,tau,A,R)-z for z in grid]
            flips=sum(vals[j]*vals[j+1]<0 for j in range(len(vals)-1))
            assert flips==nroot,(A,Q,factor,flips)
            total+=1
    print('numeric saddle-node threshold checks: %d passed'%total)
    A,Q,R=.5,.75,1.
    tc=critical(A,Q,R)
    X=Q*(1+A)/(1+Q)
    def ret(z):return Q*flow(z,tc,A,R)
    z=X+0.07
    for k in range(1,1001):z=ret(z)
    K=10/49
    assert abs(1000*(z-X)/K-1)<0.13
    assert abs(tc-math.log(140625/1024))<1e-12
    print('critical polynomial decay and exact example: passed')
if __name__=='__main__':test()
