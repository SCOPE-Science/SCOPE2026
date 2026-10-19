#!/usr/bin/env python3
"""Standalone checks for the weighted three-class greedy adsorption law.
Scientific verification only. Python standard library; execute python3 check_weighted_jamming.py.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import exp, isclose
import random


def terminal_density(a, c, ell):
    """a,c positive class densities; A,B initially each a; ell=AB/AC rate."""
    a, c, ell = float(a), float(c), float(ell)
    if not (a>0 and c>0 and ell>0):
        raise ValueError("positive densities and rate required")
    if ell==2:
        return c*exp(-2*a/c)
    z=1+(ell-2)*a/c
    return 0.0 if z<=0 else c*z**(-2/(ell-2))


def reduced_exact(a,b,c,ell):
    ell=F(ell)
    @lru_cache(None)
    def rec(a,b,c):
        tot=ell*a*b+(a+b)*c
        if tot==0:
            return F(a+b+c)
        s=F(0)
        if a*b:
            s+=ell*a*b*rec(a-1,b-1,c)/tot
        if a*c:
            s+=a*c*rec(a-1,b,c-1)/tot
        if b*c:
            s+=b*c*rec(a,b-1,c-1)/tot
        return s
    return rec(a,b,c)


def labeled_exact(a,b,c,ell):
    """Independent calculation using labeled available edges, not count transitions."""
    ell=F(ell)
    class_of=(0,)*a+(1,)*b+(2,)*c
    edges=[]
    for i in range(a+b+c):
        for j in range(i+1,a+b+c):
            if class_of[i]!=class_of[j]:
                weight=ell if {class_of[i],class_of[j]}=={0,1} else F(1)
                edges.append((1<<i | 1<<j,weight))
    @lru_cache(None)
    def rec(mask):
        available=[(e,w) for e,w in edges if (mask&e)==e]
        if not available:
            return F(mask.bit_count())
        denom=sum((w for _,w in available),F())
        return sum((w*rec(mask^e)/denom for e,w in available),F())
    return rec((1<<(a+b+c))-1)


def simulate(a,b,c,ell,rng):
    while (a*b+a*c+b*c)>0:
        z1=ell*a*b
        z2=z1+a*c
        z3=z2+b*c
        u=rng.random()*z3
        if u<z1:
            a-=1;b-=1
        elif u<z2:
            a-=1;c-=1
        else:
            b-=1;c-=1
    return a+b+c


def check_symbolic_first_integral():
    # For p!=1, verify d/dt [x*y**(-p) - y**(1-p)/(2(1-p))]=0.
    # This direct identity is stronger than a sampled numerical equality.
    for p in (F(1,4),F(1,2),F(9,10),F(3,2),F(2)):
        for x,y in product((F(1,5),F(2,3),F(7,4)),repeat=2):
            yp=-2*x*y
            xp=-x*(2*p*x+y)
            # Multiply the derivative by y**p to avoid nonrational powers.
            derivative_scaled = xp-p*x*yp/y - F(1,2)*yp
            assert derivative_scaled==0,(p,x,y,derivative_scaled)
    # When p=1, d/dt [x/y -(1/2)log(y)] = 0.
    for x,y in product((F(1,5),F(2,3),F(7,4)),repeat=2):
        yp=-2*x*y
        xp=-x*(2*x+y)
        assert xp/y-x*yp/y**2-F(1,2)*yp/y==0


def run():
    check_symbolic_first_integral()
    num=0
    for a,b,c in product(range(3),repeat=3):
        if a+b+c==0:continue
        for ell in (F(1,3),F(1),F(3),F(7,2)):
            r=reduced_exact(a,b,c,ell)
            l=labeled_exact(a,b,c,ell)
            assert r==l,(a,b,c,ell,r,l)
            num+=1
    # The equal-rate case agrees with the known three-partite product law.
    for a,c in ((.3,.4),(.4,.2),(.1,.8)):
        assert isclose(terminal_density(a,c,1),c*max(0,1-a/c)**2,abs_tol=1.e-14)
    assert terminal_density(.3,.4,.4)==0
    assert isclose(terminal_density(.3,.4,1),.025,abs_tol=1.e-14)
    assert isclose(terminal_density(.3,.4,3),.4/(1+.3/.4)**2,abs_tol=1.e-14)
    # Representative finite-size tests: finite N need not equal limiting expectation.
    rng=random.Random(20040309)
    mc=[]
    for lam in (F(2,5),F(1),F(9,5),F(2),F(3)):
        N=5000; aa=3*N//10;cc=N-2*aa
        avg=sum(simulate(aa,aa,cc,float(lam),rng) for _ in range(300))/(300*N)
        target=terminal_density(.3,.4,lam)
        assert abs(avg-target)<0.012,(lam,avg,target)
        mc.append((str(lam),round(avg,6),round(target,6)))
    print('PASS independent labeled-edge vs count-chain exact checks:',num)
    print('PASS first-integral algebra and equal-rate reduction')
    print('PASS seeded finite-size checks N=5000, 300 repetitions per rate:')
    for line in mc:print('  rate, sample, limit =',*line)
    print('NOTE finite-size checks do not prove infinite-system convergence')

if __name__=='__main__':run()
