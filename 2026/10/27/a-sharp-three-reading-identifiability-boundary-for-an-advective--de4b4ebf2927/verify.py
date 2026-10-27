"""Exact-rational checks for an instantaneous Gaussian tracer inverse-design theorem.

The additive Gaussian log normalization removes elementary transcendental factors.
No external packages are needed.
"""
from fractions import Fraction as Q
import random


def y(x, t, p, q, A):
    return A - x*x*p/(4*t) + x*q/2 - q*q*t/(4*p)


def design(x1, x2, t1, t2):
    a = (x1+x2)/(2*t1)
    kappa = x1*x1/(t1*t2) - a*a
    return a, kappa


def recovered_from_rectangle(x1, x2, t1, t2, yy):
    d1 = (yy[(x2,t1)]-yy[(x1,t1)])/(x2-x1)
    d2 = (yy[(x2,t2)]-yy[(x1,t2)])/(x2-x1)
    p = 4*(d2-d1)/((x1+x2)*(1/t1-1/t2))
    q = 2*d1+(x1+x2)*p/(2*t1)
    A = yy[(x1,t1)] + x1*x1*p/(4*t1) - x1*q/2 + q*q*t1/(4*p)
    return p, q, A


def check_witness():
    x1, x2, t1, t2 = Q(1),Q(2),Q(1),Q(2)
    a,kappa = design(x1,x2,t1,t2)
    assert (a,kappa) == (Q(3,2),Q(-7,4))
    p1,q1,A1=Q(1,2),Q(7,4),Q(0)
    p2,q2,A2=Q(8,7),Q(19,7),Q(-27,112)
    expected=[Q(-25,32),Q(-9,32),Q(-9,4)]
    for (xx,tt),correct in zip([(x1,t1),(x2,t1),(x1,t2)],expected):
        assert y(xx,tt,p1,q1,A1)==y(xx,tt,p2,q2,A2)==correct
    assert y(x2,t2,p1,q1,A1)==Q(-25,16)
    assert y(x2,t2,p2,q2,A2)==Q(-37,28)
    assert recovered_from_rectangle(x1,x2,t1,t2,{(x,t):y(x,t,p1,q1,A1) for x in (x1,x2) for t in (t1,t2)})==(p1,q1,A1)
    return 1


def check_boundary():
    # x1=3, x2=1, t1=1, t2=9/4 gives kappa=0; all p>0, q=2p.
    x1,x2,t1,t2=Q(3),Q(1),Q(1),Q(9,4)
    a,kappa=design(x1,x2,t1,t2)
    assert (a,kappa)==(Q(2),Q(0))
    p1,p2=Q(1),Q(3)
    q1,q2=a*p1,a*p2
    A1=Q(0)
    A2=y(x1,t1,p1,q1,A1)-y(x1,t1,p2,q2,Q(0))
    for xx,tt in [(x1,t1),(x2,t1),(x1,t2)]:
        assert y(xx,tt,p1,q1,A1)==y(xx,tt,p2,q2,A2)
    return 1


def check_random_exact(n=6000):
    rng=random.Random(314159)
    unique_cases=double_cases=0
    for _ in range(n):
        x1=Q(rng.randint(2,19))
        x2=Q(rng.randint(1,19))
        if x1==x2:continue
        t1=Q(rng.randint(1,8))
        t2=t1*Q(rng.randint(105,400),100)
        a,kappa=design(x1,x2,t1,t2)
        p=Q(rng.randint(1,40),rng.randint(1,40))
        q=Q(rng.randint(1,40),rng.randint(1,40))
        A=Q(rng.randint(-5,5))
        yy={(x,t):y(x,t,p,q,A) for x in (x1,x2) for t in (t1,t2)}
        b=2*(yy[(x2,t1)]-yy[(x1,t1)])/(x2-x1)
        gamma=4*(yy[(x1,t2)]-yy[(x1,t1)])/(t2-t1)
        assert q==a*p+b
        assert gamma==kappa*p-2*a*b-b*b/p
        assert kappa*p*p-(gamma+2*a*b)*p-b*b==0
        assert recovered_from_rectangle(x1,x2,t1,t2,yy)==(p,q,A)
        if kappa>0:
            assert -b*b/kappa<=0 # product of algebraic roots
            unique_cases+=1
        elif kappa<0:
            # choose b>0 to construct an independent physical double root
            b0=Q(rng.randint(1,15))
            p0=Q(rng.randint(1,20),rng.randint(1,20))
            p_other=-b0*b0/(kappa*p0)
            if p0==p_other:continue
            q0=a*p0+b0
            qo=a*p_other+b0
            assert p0>0 and p_other>0 and q0>0 and qo>0
            A0=Q(0)
            Ao=y(x1,t1,p0,q0,A0)-y(x1,t1,p_other,qo,Q(0))
            for xx,tt in [(x1,t1),(x2,t1),(x1,t2)]:
                assert y(xx,tt,p0,q0,A0)==y(xx,tt,p_other,qo,Ao)
            double_cases+=1
    assert unique_cases>100 and double_cases>100
    return unique_cases,double_cases

if __name__=='__main__':
    assert check_witness()==1
    assert check_boundary()==1
    u,d=check_random_exact()
    print(f'PASS: exact witness, critical continuum, {u} positive-kappa cases, {d} two-root constructions, and four-reading reconstruction')
