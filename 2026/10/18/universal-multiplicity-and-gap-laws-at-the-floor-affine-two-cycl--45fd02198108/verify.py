#!/usr/bin/env python3
"""Exact rational independent checks of the phase-averaged two-cycle theorem.
No external files or packages required.
"""
from fractions import Fraction as Q
from math import floor, ceil

def intervals(eps, sign):
    # sign=+1 means lambda=-1+eps; sign=-1 means lambda=-1-eps
    kmax=(eps.denominator // eps.numerator)+3  # generous, then filter
    I=[]
    for k in range(1,kmax+1):
        if eps*k>=1: continue
        if k%2==0:
            j=k//2
            I.append((eps*j, 1-eps*j, k))
        else:
            j=(k-1)//2
            if sign==1:
                I.append((1+eps*j, 2-eps*(j+1), k))
            else:
                I.append((1+eps*(j+1),2-eps*j,k))
    return I

def count_iti(mu,eps,sign):
    return sum(a<=mu<b for a,b,k in intervals(eps,sign))

def count_direct(mu,eps,sign):
    lam=-1+sign*eps
    f=lambda z: floor(lam*z+mu)
    bound=ceil(1/eps)+10
    return sum(1 for x in range(-bound,bound+1) if f(x)>x and f(f(x))==x)

def length_tail(eps,sign,m):
    q=2-sign*eps
    if m==0:return Q(1)
    return (max(Q(0),1-2*eps*m)+max(Q(0),1-eps*(2*m-1)))/q

checks=0
for eps in [Q(1,2),Q(1,3),Q(1,4),Q(2,5),Q(2,7),Q(1,7),Q(1,13),Q(3,4),Q(4,5),Q(19,20)]:
    for sign in [-1,1]:
        q=2-sign*eps
        I=intervals(eps,sign)
        pts={Q(0),q-Q(1,100000)}
        for a,b,k in I:
            for x in (a,b):
                for off in [Q(-1,100000),Q(0),Q(1,100000)]:
                    if 0<=x+off<q:pts.add(x+off)
        pts.update(q*Q(h,59) for h in range(59))
        for mu in sorted(pts):
            c1=count_iti(mu,eps,sign)
            c2=count_direct(mu,eps,sign)
            assert c1==c2, (eps,sign,mu,c1,c2)
            checks+=1
            # Limiting triangular phase profile with a uniform error bound.
            tau=(max(Q(0),min(mu,1-mu)) if mu<1 else
                 max(Q(0),min(mu-1,2-mu)) if mu<2 else Q(0))
            assert abs(eps*c2-tau)<=eps,(eps,sign,mu,c2,tau)
            checks+=1
        # Exact distribution by atomized interval endpoints; equivalently integrate N>=m.
        ends=sorted({Q(0),q}|{x for a,b,k in I for x in (a,b)})
        for m in range(1,ceil(1/eps)+2):
            mass=sum((v-u) for u,v in zip(ends,ends[1:]) if count_direct((u+v)/2,eps,sign)>=m)
            target=length_tail(eps,sign,m)*q
            assert mass==target,(eps,sign,m,mass,target)
            checks+=1
print('PASS',checks,'exact-rational independent cycle and survival checks')
# Independently integrate moments of the gap of a cycle selected uniformly
# within each nonempty phase atom. Results should approach 1/4 and 1/9.
for eps in [Q(1,8),Q(1,16),Q(1,32),Q(1,64)]:
    for sign in (-1,1):
        q=2-sign*eps
        I=intervals(eps,sign)
        ends=sorted({Q(0),q}|{x for a,b,k in I for x in (a,b)})
        mass=Q(0); m1=Q(0); m2=Q(0)
        for a,b in zip(ends,ends[1:]):
            mu=(a+b)/2
            ks=[k for left,right,k in I if left<=mu<right]
            if not ks: continue
            w=b-a
            mass+=w
            m1+=w*sum(eps*k for k in ks)/len(ks)
            m2+=w*sum((eps*k)**2 for k in ks)/len(ks)
        assert mass>0
        assert abs(m1/mass-Q(1,4))<=eps
        assert abs(m2/mass-Q(1,9))<=eps
print('PASS 16 exact-rational near-critical orbit-gap moment comparisons')
