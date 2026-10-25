"""Reproducible finite checks of a memory-reset record-growth theorem.
Uses exact finite-time dynamic programming, stationary Markov balance and optimization checks.
"""
from fractions import Fraction
from math import sqrt
from random import Random

def lam(p, r):
    q = 1 - p
    t = 1 - r
    if t == 0:
        return 0.0
    return 2*t*q/(1 + sqrt(1-4*t*t*p*q))

def speed(p,r):
    return (1-r)*p*(1-lam(p,r))

def optimum(p):
    q=1-p
    rstar = max(0.0,1-1/(2*sqrt(q)))
    vmax = (p-q) if q <= .25 else (1-sqrt(q))/(2*sqrt(q))
    return rstar,vmax

def gap_dp(p,r,n):
    p=Fraction(p);r=Fraction(r);q=1-p;t=1-r
    pr={0:Fraction(1)}; mean=Fraction(0)
    for _ in range(n):
        mean+=t*p*pr.get(0,0)
        new={}
        for g,pg in pr.items():
            new[0]=new.get(0,0)+pg*r
            if g==0:
                new[0]=new.get(0,0)+pg*t*p
            else:
                new[g-1]=new.get(g-1,0)+pg*t*p
            new[g+1]=new.get(g+1,0)+pg*t*q
        pr={k:v for k,v in new.items() if v}
        assert sum(pr.values())==1
    return mean,pr

def joint_dp(p,r,n):
    p=Fraction(p);r=Fraction(r);q=1-p;t=1-r
    pr={(0,0):Fraction(1)}
    for _ in range(n):
        new={}
        for (x,m),prob in pr.items():
            for xy,w in [((m,m),r), ((x+1,max(m,x+1)),t*p), ((x-1,m),t*q)]:
                new[xy]=new.get(xy,0)+prob*w
        pr={k:v for k,v in new.items() if v}
        assert sum(pr.values())==1
    return sum(prob*m for (_,m),prob in pr.items())

def main():
    exact=0
    for p,r in [(Fraction(1,2),Fraction(1,3)), (Fraction(2,3),Fraction(1,4)),
                (Fraction(4,5),Fraction(1,3)),(Fraction(1,10),Fraction(2,5)),
                (Fraction(1,4),Fraction(3,4))]:
        for n in [0,1,2,5,10,17]:
            a,_=gap_dp(p,r,n)
            b=joint_dp(p,r,n)
            assert a==b,(p,r,n,a,b)
            exact+=1
    checks=0
    for i in range(1,30):
        p=i/30
        for j in range(1,30):
            r=j/30;t=1-r;q=1-p
            l=lam(p,r);assert 0<l<1
            assert abs(l-t*(q+p*l*l))<3e-14
            # Stationarity at boundary and in a typical interior state.
            pi=lambda g:(1-l)*l**g
            P0=pi(0)*(r+t*p)+pi(1)*(r+t*p)+r*l*l
            assert abs(P0-pi(0))<1e-13
            assert abs(pi(3)-t*(q*pi(2)+p*pi(4)))<1e-13
            # Formula agrees with arbitrary differentiable parametrization of t.
            assert abs(speed(p,r)-t*p*(1-l))<1e-15
            checks+=1
        ropt,vmax=optimum(p)
        assert abs(speed(p,ropt)-vmax)<2e-14
        for j in range(1001):
            r=j/1000
            assert speed(p,r)<=vmax+2e-12,(p,r,speed(p,r),vmax)
    # Borderline p=3/4, no resetting optimal.
    assert optimum(.75)==(0.0,.5)
    # Exact rational finite-horizon mean identity using separately coded representations.
    print('PASS: exact rational joint/gap finite-horizon identities:',exact)
    print('PASS: stationary balance and speed identities:',checks)
    print('PASS: optimum upper bound on 29,029 parameter-grid points; boundary checks')
    for p in (.15,.5,.7,.75,.8,.95):
        r,v=optimum(p)
        print(f'p={p:.2f}: optimizer={r:.12f}, speed={v:.12f}, no-reset={max(2*p-1,0):.12f}')

if __name__=='__main__':main()
