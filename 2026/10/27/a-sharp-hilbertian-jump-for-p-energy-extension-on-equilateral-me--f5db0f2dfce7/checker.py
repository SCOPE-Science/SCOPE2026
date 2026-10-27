"""Numerical cross-check of the scalar graph p-energy star response."""
import math
import random

def psi(z,p):
    return (1 if z>0 else -1 if z<0 else 0)*abs(z)**(p-1)

def center(v,p):
    low=min(v);high=max(v)
    for _ in range(130):
        c=(low+high)/2
        F=sum(psi(c-x,p) for x in v)
        if F>0: high=c
        else: low=c
    return (low+high)/2

def seminorm_leaf(x):
    return (max(x)-min(x))/2

def seminorm_star(x,c):
    return max(seminorm_leaf(x),max(abs(y-c) for y in x))

def check():
    rng=random.Random(20261024)
    num=0
    for m in (2,3,4,7):
        for p in (1.2,1.5,1.9,2,2.1,3,5):
            sharp=1 if m==2 else (2*(m-1)/m if p==2 else 2)
            for _ in range(90):
                a=[rng.uniform(-5,5) for j in range(m)]
                b=[rng.uniform(-5,5) for j in range(m)]
                ca=center(a,p);cb=center(b,p)
                dif=[aa-bb for aa,bb in zip(a,b)]
                s=seminorm_leaf(dif)
                if s>1e-10:
                    ratio=seminorm_star(dif,ca-cb)/s
                    assert ratio <= sharp+1e-9, (m,p,ratio,sharp)
                    num+=1
    # Attainment of the quadratic sharp bound by a singleton perturbation.
    for m in range(2,11):
        u=[1]+[0]*(m-1)
        c=center(u,2)
        ratio=seminorm_star(u,c)/seminorm_leaf(u)
        assert abs(ratio-2*(m-1)/m)<1e-10,(m,ratio)
        num+=1
    # Cusp exponents and coefficients: approach epsilon -> 0.
    for p,m in ((1.3,3),(1.5,4),(1.7,7),(2.5,3),(3.0,4),(4.5,7)):
        epsilon=0.00002 if p<2 else 0.001
        v=[-1,0,1]+[0]*(m-3)
        u=v.copy()
        if p<2: u[0]+=epsilon
        else: u[1]+=epsilon
        dc=center(u,p)-center(v,p)
        if p<2: prediction=((p-1)/(m-2))**(1/(p-1))*epsilon**(1/(p-1))
        else: prediction=epsilon**(p-1)/(2*(p-1))
        # tiny terms below double precision ignored
        if prediction>1e-12:
            assert abs(dc/prediction-1)<0.08,(p,m,dc,prediction)
            num+=1
    print('PASS',num,'random inequalities and asymptotic/equality checks')

if __name__=='__main__':check()
