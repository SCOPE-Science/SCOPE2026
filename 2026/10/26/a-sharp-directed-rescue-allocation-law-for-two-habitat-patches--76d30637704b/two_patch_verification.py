#!/usr/bin/env python3
"""Independent finite checks for two-patch extinction-time allocation law.

No claim of proving statements over all real parameters is made by this code.
"""
from fractions import Fraction
from random import Random
from math import isclose


def direct_linear_solve(a, b):
    a = [list(row) + [b[i]] for i, row in enumerate(a)]
    n = len(a)
    for j in range(n):
        k = max(range(j, n), key=lambda i: abs(a[i][j]))
        a[j], a[k] = a[k], a[j]
        assert abs(a[j][j]) > 1e-15
        d = a[j][j]
        a[j] = [z / d for z in a[j]]
        for i in range(n):
            if i != j:
                d = a[i][j]
                a[i] = [a[i][h] - d*a[j][h] for h in range(n + 1)]
    return [row[-1] for row in a]


def t_vector(e1,e2,u,v):
    s = e1 + e2
    den = e1*e2*(s+u+v)
    return ((u+e2)*(v+s)/den,
            (v+e1)*(u+s)/den,
            (u*v+(u+v)*s+e1*e1+e1*e2+e2*e2)/den)


def persistence(e1,e2,C,alpha,beta,gamma,u):
    a,b,c=t_vector(e1,e2,u,C-u)
    return alpha*a+beta*b+gamma*c


def optimum(e1,e2,C,alpha,beta,umin=0.0,umax=None):
    if umax is None: umax=C
    return min(umax,max(umin,(C+alpha*e1-beta*e2)/2))


def almost(x,y):
    return isclose(x,y,rel_tol=2e-11,abs_tol=2e-11)


def run():
    e1,e2,C=Fraction(1),Fraction(4),Fraction(2)
    vals=t_vector(e1,e2,Fraction(1),Fraction(1))
    assert vals[2]==Fraction(8,7), vals
    assert t_vector(e1,e2,Fraction(0),C)[2]==Fraction(31,28)
    assert t_vector(e1,e2,C,Fraction(0))[2]==Fraction(31,28)
    assert t_vector(e1,e2,Fraction(3,2),Fraction(1,2))[0]==Fraction(121,112)
    assert t_vector(e1,e2,C,Fraction(0))[0]==Fraction(15,14)
    rng=Random(20261023)
    n=5000
    for _ in range(n):
        e1=10**rng.uniform(-1,1)
        e2=10**rng.uniform(-1,1)
        C=10**rng.uniform(-1,1)
        u=rng.random()*C
        v=C-u
        weights=[rng.random() for _ in range(3)]
        alpha,beta,gamma=[q/sum(weights) for q in weights]
        ta,tb,tc=t_vector(e1,e2,u,v)
        matrix=((e1+u,0,-u),(0,e2+v,-v),(-e2,-e1,e1+e2))
        sa,sb,sc=direct_linear_solve(matrix,(1.,1.,1.))
        assert almost(ta,sa) and almost(tb,sb) and almost(tc,sc)
        u0=(C+alpha*e1-beta*e2)/2
        ustar=optimum(e1,e2,C,alpha,beta)
        # Quadratic comparison, including noninterior case.
        actual=persistence(e1,e2,C,alpha,beta,gamma,ustar)
        trial=persistence(e1,e2,C,alpha,beta,gamma,u)
        D=e1*e2*(C+e1+e2)
        predicted=((u-u0)**2-(ustar-u0)**2)/D
        assert almost(actual-trial,predicted)
        assert actual+1e-10>=trial
        lower=rng.random()*C*0.4
        upper=lower+(C-lower)*rng.random()
        upr=optimum(e1,e2,C,alpha,beta,lower,upper)
        best=persistence(e1,e2,C,alpha,beta,gamma,upr)
        for z in (lower,upper,(lower+upper)/2):
            assert best+1e-10>=persistence(e1,e2,C,alpha,beta,gamma,z)
    print('PASS exact rational benchmarks; {} independent Markov-system checks, quadratic optimality/regret checks, baseline-constrained checks'.format(n))

if __name__=='__main__':run()
