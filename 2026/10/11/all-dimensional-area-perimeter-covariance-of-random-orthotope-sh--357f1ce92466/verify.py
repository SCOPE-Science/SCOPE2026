"""Reproduce the exact low-dimensional anchors and independent Haar-plane checks.
Only Python's standard library is required. Finite tests do not prove the theorem.
"""
from math import gamma, lgamma, exp, sqrt, pi, isclose
from random import Random
from itertools import combinations


def coefficients(d):
    assert d >= 3
    a = 2 * exp(lgamma((d-1)/2)-lgamma(d/2))/(d*sqrt(pi))
    p = sqrt(pi)*exp(lgamma(d/2)-lgamma((d+1)/2))/2
    b = p/(d-1)
    return a,b,p


def moments(side):
    d=len(side)
    e1=sum(side)
    e2=sum(side[i]*side[j] for i,j in combinations(range(d),2))
    e3=sum(side[i]*side[j]*side[k] for i,j,k in combinations(range(d),3))
    a,b,p=coefficients(d)
    mixed=2*a*(e1*e2-3*(1-pi/4)*e3)
    covariance=2*((a-b)*e1*e2-3*(1-pi/4)*a*e3)
    bound=6*((d/(d-2))*(a-b)-(1-pi/4)*a)*e3
    return mixed,covariance,bound,e2/(d-1),2*p*e1


def haar_frame(rng,d):
    x=[rng.gauss(0,1) for _ in range(d)]
    rx=sqrt(sum(t*t for t in x)); x=[t/rx for t in x]
    y=[rng.gauss(0,1) for _ in range(d)]
    dot=sum(a*b for a,b in zip(x,y))
    y=[b-dot*a for a,b in zip(x,y)]
    ry=sqrt(sum(t*t for t in y)); y=[t/ry for t in y]
    return x,y


def sample(side,num,rng):
    d=len(side)
    sums=[0.0]*7
    for _ in range(num):
        x,y=haar_frame(rng,d)
        radial=[sqrt(a*a+b*b) for a,b in zip(x,y)]
        det=lambda i,j:abs(x[i]*y[j]-x[j]*y[i])
        A=sum(side[i]*side[j]*det(i,j) for i,j in combinations(range(d),2))
        P=2*sum(z*r for z,r in zip(side,radial))
        sums[0]+=A*P; sums[1]+=A; sums[2]+=P
        sums[3]+=det(0,1)*radial[0]
        sums[4]+=det(0,1)*radial[2]
        sums[5]+=det(0,1)
        sums[6]+=radial[0]
    return [z/num for z in sums]


def check():
    assert abs(moments([1,1,1])[0]-(2+16/pi)) <1e-13
    assert abs(moments([1]*4)[0]-(6+3*pi/2)) <1e-13
    for d in range(3,1000):
        a,b,p=coefficients(d)
        assert a>b, (d,a,b)
        assert 6*((d/(d-2))*(a-b)-(1-pi/4)*a)>0, d
    rng=Random(20261010)
    checks=0
    for sides in ([1.,1.,1.], [1.,2.,4.], [1.]*4,
                  [1.,2.,3.,1.,4.], [1.,1.,2.,2.,3.,3.,5.,8.]):
        d=len(sides)
        num=24000
        s=sample(sides,num,rng)
        mixed,cov,bound,mean_a,mean_p=moments(sides)
        # The three first moment statistics and two incidence identities
        # are tested independently by constructing random Gaussian frames.
        target=[mixed,mean_a,mean_p,coefficients(d)[0],
                (pi/4)*coefficients(d)[0],1/(d-1),coefficients(d)[2]]
        for observed,want in zip(s,target):
            assert abs(observed-want) < 0.045*max(1,abs(want)), (d,observed,want)
            checks+=1
        assert cov >= bound-1e-10
        assert abs((cov-bound))<1e-10 if len(set(sides))==1 else cov>bound
        checks+=2
    print('VERIFY_OK', checks, 'Haar planes',24000*5)

if __name__=='__main__':
    check()
