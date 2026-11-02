"""Exact finite checks for a two-probe leave-one-out trace estimator.

Run: python verify.py
Requires only the Python standard library.
The infinite-dimensional-parameter statement is proved in RESULT.md;
finite checks here test independent algebraic implementations.
"""
from fractions import Fraction as F
from itertools import product


def dot(a, b):
    return sum((x*y for x,y in zip(a,b)), F(0))


def base_estimate(a, probe, other):
    """A direct residual-projector evaluation, not the Walsh formula."""
    s2=sum((x*x for x in a),F(0))
    if s2==0:
        raise ValueError('The input diagonal must not be zero')
    v=[ai*oi for ai,oi in zip(a,other)]
    alpha=dot(v,probe)/s2
    residual=[z-alpha*w for z,w in zip(probe,v)]
    return sum((ai*vi*vi for ai,vi in zip(a,v)),F(0))/s2 + sum((ai*ri*ri for ai,ri in zip(a,residual)), F(0))


def polynomial_estimate(a, probe, other):
    s2=sum((z*z for z in a),F(0))
    s3=sum((z*z*z for z in a),F(0))
    signs=[x*y for x,y in zip(probe,other)]
    p1=dot(a,signs)
    p2=sum((x*x*y for x,y in zip(a,signs)),F(0))
    return sum(a,F(0))+s3/s2 -2*p1*p2/s2+s3*p1*p1/(s2*s2)


def variance_identity(a):
    s2=sum((z*z for z in a),F(0))
    s3=sum((z*z*z for z in a),F(0))
    return F(4,s2**4)*sum((a[i]**2*a[j]**2*(s3-s2*(a[i]+a[j]))**2
                                 for i in range(len(a)) for j in range(i+1,len(a))),F(0))


def exhaustive(a):
    a=list(map(F,a))
    n=len(a)
    signs=list(product((F(-1),F(1)),repeat=n))
    total=F(0)
    sq=F(0)
    checks=0
    for g in signs:
        for h in signs:
            t1=base_estimate(a,g,h)
            t2=base_estimate(a,h,g)
            t3=polynomial_estimate(a,g,h)
            assert t1==t2==t3,(a,g,h,t1,t2,t3)
            assert (t1-t2)**2/F(4)==0
            total+=t1
            sq+=(t1-sum(a))**2
            checks+=1
    assert total/checks==sum(a), (a,total/checks,sum(a))
    assert sq/checks==variance_identity(a),(a,sq/checks,variance_identity(a))
    return checks


def main():
    cases=((1,1), (1,2), (-1,1), (0,3),
           (1,2,3), (0,2,4), (-2,1,5),
           (1,1,1,1),(1,-1,0,0),(1,2,3,4),
           (1,1,1,1,1),(1,2,3,4,5),
           (1,1,1,1,1,1))
    count=0
    for a in cases:
        count+=exhaustive(a)
    for n in range(2,11):
        mse=variance_identity([F(1)]*n)
        assert mse==2*F(n-1,n)
    for a in ((1,),(-2,), (1,-1),(1,2),(2,-2),(1,1,1), (0,0,1), (0,2,-2)):
        nonzero=[v for v in a if v!=0]
        predicted=(len(nonzero)<=1 or (len(nonzero)==2 and sum(nonzero)==0))
        assert (variance_identity(list(map(F,a)))==0)==predicted
    print('VERIFY_OK',count,'exhaustive ordered probe pairs; exact mean, variance, equality, and classification checks')

if __name__=='__main__':
    main()
