"""Exact-rational finite probability checks for symmetric Dirichlet exceedance counts.
Uses only the Python standard library. This is supplementary finite verification,
not a proof of an infinite-parametric theorem.
"""
from fractions import Fraction as F
from math import comb, factorial, exp, gamma


def beta_tail(n, d, a):
    """P(V>a), V~Beta(d,(n-1)d), integer d>0; rational a."""
    if not F(0) <= a <= F(1):
        raise ValueError('a out of range')
    b = (n - 1) * d
    c = F(factorial(n*d-1), factorial(d-1) * factorial(b-1))
    return c * sum(F(comb(d-1,i) * factorial(i) * factorial(b-1),factorial(i+b)) * a**(d-1-i) * (1-a)**(i+b) for i in range(d))


def pair_tail(n, d, a, b):
    """P(V1>a,V2>b), symmetric Dirichlet(d,...,d), integer d>0."""
    if a+b>=1:return F(0)
    c = F(factorial(n*d-1), factorial(d-1)**2 * factorial((n-2)*d-1))
    m=(n-2)*d-1; r=1-a-b
    return c*sum(F(comb(d-1,i)*comb(d-1,j)*factorial(i)*factorial(j)*factorial(m),factorial(i+j+m+2)) * a**(d-1-i)*b**(d-1-j)*r**(i+j+m+2) for i in range(d) for j in range(d))


def covariance(n,d,a,b):
    pa=beta_tail(n,d,a); pb=beta_tail(n,d,b); q=pair_tail(n,d,a,b)
    return n*pb*(1-n*pa)+n*(n-1)*q


def verify():
    cases=0; monotone=0; threshold=0
    for d in (1,2,3):
        for n in range(3,10):
            for j in range(1,13):
                a=F(j,25)
                if a>=1:continue
                pa=beta_tail(n,d,a)
                assert F(0)<pa<F(1), (n,d,a,pa)
                assert pair_tail(n,d,a,a) <= pa
                assert covariance(n,d,a,a)>0
                last=None; signs=[]
                for k in range(j,25):
                    b=F(k,25)
                    pb=beta_tail(n,d,b)
                    co=covariance(n,d,a,b)
                    ratio=co/(n*pb)
                    if last is not None:
                        assert ratio <= last, ('ratio non-monotone',n,d,a,b,last,ratio)
                    last=ratio
                    signs.append((co>0)-(co<0))
                    cases+=1
                # With increasing b there can be one + to - transition, never - to +.
                assert all(not(signs[i]<0 and signs[i+1]>=0) for i in range(len(signs)-1))
                monotone+=1
                if n*pa>1 and 1-a>=a:
                    assert covariance(n,d,a,1-a)<0
                    threshold+=1
                if n*pa<1:
                    assert all(z>0 for z in signs)
                if d==1:
                    for k in range(j,25):
                        b=F(k,25)
                        assert pair_tail(n,d,a,b)==max(F(0),1-a-b)**(n-1)
    # The one-dimensional density perturbations reproduce the dependence term.
    algebra=0
    for d in (1,2,3,5):
        alpha=F(d)
        for ti in (F(1,2), F(5,3),F(7)):
            for sj in (F(1,3),F(9,4)):
                h1=lambda t:-alpha*(alpha+1)/2+(alpha+1)*t-t*t/2
                h2=-alpha*(2*alpha+1)+(2*alpha+1)*(ti+sj)-(ti+sj)**2/2
                assert h2-h1(ti)-h1(sj)==-(ti-alpha)*(sj-alpha)
                algebra+=1
    # Explicit alpha=1 asymptotic curve: threshold y=(exp(x)-1)/x.
    for x in (0.15,0.6,1.4,3.0):
        y=(exp(x)-1)/x
        assert y>x
        kernel=lambda z:exp(-z)*(1-exp(-x)*(1+x*z))
        assert kernel(y/2)>0 if y/2>=x else kernel(x)>0
        assert abs(kernel(y))<1e-13
        assert kernel(y+1)<0
    print('EXACT_BETA_DIRICHLET_CHECK_PASS',cases,'threshold-certified',threshold)
    print('MONOTONE_NORMALIZED_COVARIANCE_CHECK_PASS',monotone)
    print('DENSITY_EXPANSION_IDENTITY_PASS',algebra)
    print('UNIFORM_GAP_ASYMPTOTIC_CURVE_PASS')
    print('VERIFY_OK')

if __name__=='__main__':verify()
