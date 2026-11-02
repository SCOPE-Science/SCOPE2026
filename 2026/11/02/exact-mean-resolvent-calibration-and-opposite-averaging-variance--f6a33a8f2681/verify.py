#!/usr/bin/env python3
"""Reproduce exact stationary and long-run variance identities for random scalar resolvents.
Ordinary proof checks: algebraic identities and independent stochastic simulations.
"""
from fractions import Fraction as F
from random import Random
import sympy as s


def general_exact(curvatures, centers, eta):
    a = [F(q) for q in curvatures]
    c = [F(q) for q in centers]
    t = F(eta)
    n = len(a)
    S = sum(a)
    m = sum(q*v for q, v in zip(a, c)) / S
    z = n + t*S
    probs = [(1+t*q)/z for q in a]
    rs = [1/(1+t*q) for q in a]
    K = sum(q*(v-m) for q,v in zip(a,c))
    assert K == 0
    R = sum(p*r for p,r in zip(probs,rs))
    assert R == n/z
    assert sum(probs) == 1
    assert sum(p*(r*F(17)+(1-r)*ci) for p,r,ci in zip(probs,rs,c)) == (n*F(17)+t*sum(q*ci for q,ci in zip(a,c)))/z
    noise = [t*q*(ci-m)/(1+t*q) for q,ci in zip(a,c)]
    assert sum(p*v for p,v in zip(probs, noise)) == 0
    T = sum((q*(ci-m))**2/(1+t*q) for q,ci in zip(a,c))
    U = sum(q/(1+t*q) for q in a)
    V = t*T/(S+U)
    second_r = sum(p*r*r for p,r in zip(probs,rs))
    assert V == second_r*V+sum(p*v*v for p,v in zip(probs,noise))
    Gamma = (2*n+t*S)*T/(S*(S+U))
    assert Gamma == V*(1+R)/(1-R)
    return probs,m,R,V,Gamma


def symbolic_checks():
    a,b,t,r,u,d = s.symbols('a b t r u d',positive=True,real=True)
    S=a+b
    m=(a*d+b*(-d))/S
    # pair centers +d and -d
    g=a*(d-m)
    q=a*b*(2*d)/S
    assert s.simplify(g-q)==0
    T=g**2*(1/(1+a*t)+1/(1+b*t))
    U=a/(1+a*t)+b/(1+b*t)
    V=s.factor(t*T/(S+U))
    G=s.factor((4+t*S)*T/(S*(S+U)))
    assert s.simplify(V-t*g**2/(S+a*b*t))==0
    assert s.simplify(G-g**2*(4+t*S)/(S*(S+a*b*t)))==0
    assert s.simplify(s.diff(G,t)-g**2*(a-b)**2/(S*(S+a*b*t)**2))==0
    # Triple: (a,b,b), centers (0,1,-1), scaling r=a/b, u=t*b.
    D=r*(r+2)*u**2+(r*r+6*r+2)*u+2*r+4
    triple=2*(1+r*u)*(6+(r+2)*u)/((r+2)*D)
    P=r*r*(r+2)*u**2+4*r*(r+2)*u+4*(2*r+1)
    assert s.simplify(s.diff(triple,u)-2*(r-1)*P/((r+2)*D**2))==0
    assert s.simplify(s.limit(triple,u,0)-6/(r+2)**2)==0
    assert s.simplify(s.limit(triple,u,s.oo)-2/(r+2))==0
    assert s.simplify(triple.subs({r:s.Rational(1,10),u:s.Rational(3,2)})-general_exact([1,10,10],[0,1,-1],F(3,20))[4])==0
    Vr=2*u*(1+r*u)/D
    assert s.simplify(Vr-u*(2/(1+u))/(r+2+r/(1+r*u)+2/(1+u)))==0
    assert s.simplify(s.diff(Vr,u)-2*(r*r*(r+5)*u*u+4*r*(r+2)*u+2*r+4)/D**2)==0
    print('Symbolic identity groups: 10 PASS')


def exact_checks():
    rng=Random(9032023)
    cases=0
    for n in [2,3,4,5,8]:
        for _ in range(55):
            a=[F(rng.randint(1,40),rng.randint(1,9)) for _ in range(n)]
            c=[F(rng.randint(-16,16),rng.randint(1,7)) for _ in range(n)]
            eta=F(rng.randint(1,20),rng.randint(1,11))
            general_exact(a,c,eta)
            cases+=1
    print('Exact rational recurrence cases:',cases,'PASS')


def stochastic_checks():
    rng=Random(230809310)
    # Three independent seeded trajectories; compare mean, variance, and lag-one covariance.
    for a,c,t in [([1,10,10],[0,1,-1],0.2),([1,10,10],[0,1,-1],2.0),([1,5],[1,-1],0.4)]:
        probs,m,R,V,Gamma=general_exact(a,c,F(str(t)))
        pp=[float(p) for p in probs]
        limits=[];total=0.
        for p in pp:
            total+=p; limits.append(total)
        x=float(m);burn=400;arr=[]
        for j in range(160000):
            h=rng.random(); i=next(i for i,limit in enumerate(limits) if h<limit)
            x=(x+t*a[i]*c[i])/(1+t*a[i])
            if j>=burn:arr.append(x)
        mu=sum(arr)/len(arr);n=len(arr)
        vv=sum((z-mu)**2 for z in arr)/n
        # covariance comparison at lag 1/2; beyond-lag estimates may fluctuate
        c1=sum((arr[i]-mu)*(arr[i+1]-mu) for i in range(n-1))/(n-1)
        assert abs(mu-float(m))<0.035
        assert abs(vv-float(V)) <0.055*max(1.,float(V))
        assert abs(c1-float(V*R)) <0.06*max(1.,float(V))
        print('Simulation a=',a,'eta=',t,'mean=',round(mu,5),'variance=',round(vv,5),'lag1=',round(c1,5),'PASS')


if __name__=='__main__':
    symbolic_checks()
    exact_checks()
    stochastic_checks()
    print('ALL CHECKS PASS')
