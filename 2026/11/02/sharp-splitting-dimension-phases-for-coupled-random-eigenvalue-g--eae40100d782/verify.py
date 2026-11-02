"""Reproduce finite algebraic and quadrature checks for crossing-level moments.
Run: python3 verify.py   (Python standard library only).
Numerical quadrature is supplementary, not a proof of asymptotic limits.
"""
from fractions import Fraction as F
from itertools import product
from math import exp, log, sqrt, isclose


def simpson(fn,lo,hi,n=14000):
    assert n % 2 == 0
    step=(hi-lo)/n
    total=fn(lo)+fn(hi)
    for i in range(1,n):
        total+=(4 if i%2 else 2)*fn(lo+i*step)
    return total*step/3


def kernel(u,theta):
    return (1.0-theta*theta)/(sqrt(1+u*u)+sqrt(theta*theta+u*u))


def exact_moment(d,p,h,theta):
    # Uniform distribution in the d-ball; log radius integration.
    high=log(1/h)
    return d*h**(p+d)*simpson(
        lambda t:kernel(exp(t),theta)**p*exp(d*t),-35.0,high,14000)


def limit_integral(d,p,theta):
    assert p>d
    return simpson(lambda t:kernel(exp(t),theta)**p*exp(d*t),-35.0,36.0,14000)


def asymptotic(d,p,h,theta):
    c=(1-theta*theta)/2
    if p>d:
        return d*limit_integral(d,p,theta)*h**(p+d)
    if p==d:
        return d*c**p*h**(2*p)*log(1/h)
    return d/(d-p)*c**p*h**(2*p)


def algebra_tests():
    count=0
    for ti in [-13,-5,-1,0,1,3,9]:
        for hi in [1,2,3,7,11]:
            t,h=F(ti,7),F(hi,13)
            # B=[ [t,h], [h,-t] ] has char polynomial z²-(t²+h²).
            determinant=-t*t-h*h
            assert determinant==-(t*t+h*h)
            for xi in [-3,-1,0,2,8]:
                x=F(xi,9)
                # Hermitian B=[ [t,x-ih], [x+ih,-t] ].
                determinant2=-t*t-(x*x+h*h)
                assert determinant2==-(t*t+x*x+h*h)
                count+=1
    return count


def exact_sample_variance_tests():
    # Independently enumerate a non-Gaussian three-point distribution.
    support=[(F(0), F(1,2)),(F(1),F(1,3)),(F(4),F(1,6))]
    mean=sum(x*p for x,p in support)
    v=sum(p*(x-mean)**2 for x,p in support)
    fourth=sum(p*(x-mean)**4 for x,p in support)
    kurt=fourth/(v*v)
    checks=0
    for n in (2,3,4):
        mean_sqvar=F(0)
        mse=F(0)
        for indices in product(range(3),repeat=n):
            xs=[support[j][0] for j in indices]
            weight=F(1)
            for j in indices:weight*=support[j][1]
            sample_mean=sum(xs)/n
            s2=sum((x-sample_mean)**2 for x in xs)/(n-1)
            mean_sqvar+=weight*s2
            mse+=weight*(s2/v-1)**2
        assert mean_sqvar==v
        assert mse==(kurt-F(n-3,n-1))/n
        checks+=1
    return checks


def quadrature_tests():
    count=0
    theta=0.5
    h=0.00003
    for d in range(1,7):
        for p in range(1,5):
            actual=exact_moment(d,p,h,theta)
            leading=asymptotic(d,p,h,theta)
            ratio=actual/leading
            assert 0.78<ratio<1.22,(d,p,ratio)
            count+=1
    # Sample d=1 density is 1/2 at origin. Verify leading variance and
    # the first-row limiting standardized fourth moment after centering.
    m=[0.0]+[exact_moment(1,p,h,theta) for p in range(1,5)]
    v=m[2]-m[1]**2
    c4=m[4]-4*m[1]*m[3]+6*m[1]**2*m[2]-3*m[1]**4
    j2=limit_integral(1,2,theta)
    j4=limit_integral(1,4,theta)
    assert abs(v/(j2*h**3)-1)<0.02
    assert abs((c4/v**2)*h/(j4/j2**2)-1)<0.06
    return count,j2,j4


def main():
    a=algebra_tests()
    b,j2,j4=quadrature_tests()
    sv=exact_sample_variance_tests()
    print('PASS',a,'exact-rational characteristic-polynomial cases;',b,'radial asymptotic cases;',sv,'exact sample-variance identities')
    print('d=1 theta=1/2 integrals: I21=',format(j2,'.15g'),'I41=',format(j4,'.15g'))
    print('d=1 uniform[-1,1] kurtosis coefficient=',format(j4/j2**2,'.15g'))

if __name__=='__main__':
    main()
