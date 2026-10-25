"""Reproduce inverse-distance-moment identities for planar parallelograms.
Uses the standard library; does not constitute independent scientific audit.
"""
from fractions import Fraction as F
from math import factorial
import random


def e_tri(n):
    return F(0) if n & 1 else F(2, (n+1)*(n+2))


def independent_moment(a,b,c,k):
    total=F(0)
    for i in range(k+1):
        for j in range(k-i+1):
            ell=k-i-j
            total += F(factorial(k),factorial(i)*factorial(j)*factorial(ell))*a**i*b**j*(2*c)**ell*e_tri(2*i+ell)*e_tri(2*j+ell)
    return total


def given_moments(a,b,c):
    m2=(a+b)/6
    m4=(a*a+b*b)/15+a*b/18+c*c/9
    m6=(a**3+b**3)/28+a*b*(a+b)/30+F(2,15)*c*c*(a+b)
    return m2,m4,m6


def inverse(m2,m4,m6):
    x=m4/m2**2
    y=m6/m2**3
    p=-F(70,41)*x+F(175,738)*y+F(93,41)
    q=-F(155,164)*x+F(245,1476)*y+F(81,82)
    return p,q


def normalized(p,q):
    return F(12,5)-F(14,5)*p+4*q, F(54,7)-F(558,35)*p+F(144,5)*q


def test():
    rng=random.Random(82613)
    checks=0
    for _ in range(1400):
        a=F(rng.randint(1,30),rng.randint(1,17))
        b=F(rng.randint(1,30),rng.randint(1,17))
        c=F(rng.randint(-20,20),rng.randint(7,25))
        if c*c>=a*b: continue
        moments=given_moments(a,b,c)
        for k,m in enumerate(moments,1):
            assert independent_moment(a,b,c,k)==m
            checks+=1
        p,q=inverse(*moments)
        assert p==a*b/(a+b)**2 and q==c*c/(a+b)**2
        assert 0<p<=F(1,4) and 0<=q<p
        assert normalized(p,q)==(moments[1]/moments[0]**2,moments[2]/moments[0]**3)
        checks+=3
    vertices=[(F(0),F(0),F(12,5),F(54,7)),
              (F(1,4),F(0),F(17,10),F(261,70)),
              (F(1,4),F(1,4),F(27,10),F(153,14))]
    for p,q,x,y in vertices:
        assert normalized(p,q)==(x,y)
        assert inverse(F(1),x,y)==(p,q)
        checks+=2
    # An entire continuum of noncongruent shapes shares (M2,M4)=(1,2).
    values=[]
    for i in range(101):
        p=F(1,7)+(F(1,4)-F(1,7))*i/100
        q=-F(1,10)+F(7,10)*p
        assert F(0)<=q<p
        x,y=normalized(p,q)
        assert x==2
        assert inverse(F(1),x,y)==(p,q)
        values.append(y)
        checks+=3
    assert len(set(values))==101
    # An independent deterministic sampling check for a non-rectangular example.
    uu=(2.,0.); vv=(1.,3.)
    a=F(4); b=F(10); c=F(2)
    target=tuple(map(float,given_moments(a,b,c)))
    n=200000
    sums=[0.,0.,0.]
    for _ in range(n):
        xi=rng.random()-rng.random()
        eta=rng.random()-rng.random()
        r2=4*xi*xi+10*eta*eta+4*xi*eta
        sums[0]+=r2; sums[1]+=r2*r2; sums[2]+=r2*r2*r2
    sample=[s/n for s in sums]
    rel=[abs(s-t)/t for s,t in zip(sample,target)]
    assert max(rel)<0.045,(target,sample,rel)
    # No two normalized invariant pairs can have the same inverse p,q.
    print('VERIFY_OK',checks,'exact checks; MC', n, 'samples, relative errors',rel)

if __name__=='__main__':test()
