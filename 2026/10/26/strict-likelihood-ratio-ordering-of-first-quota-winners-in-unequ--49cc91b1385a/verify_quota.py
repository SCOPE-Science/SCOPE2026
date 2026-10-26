"""Exact-rational independent checks for the quota-winning likelihood-ratio law.

Run: python3 verify_quota.py
No third-party dependencies; arithmetic uses fractions.Fraction throughout.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import factorial


def polynomial_joint(p, r):
    """Return (time,winner)->mass by truncating each losing-type EGF."""
    m=len(p)
    ans={}
    for i in range(m):
        coeff=[F(1)]
        for h in range(m):
            if h==i:
                continue
            nxt=[F(0)]*(len(coeff)+r-1)
            for k, c in enumerate(coeff):
                for a in range(r):
                    nxt[k+a] += c * p[h]**a/F(factorial(a))
            coeff=nxt
        for k,c in enumerate(coeff):
            ans[r+k,i]=F(factorial(r+k-1),factorial(r-1))*p[i]**r*c
    return ans


def dynamic_joint(p,r):
    """Independent absorbing Markov chain enumerator over bounded occupancy vectors."""
    m=len(p)
    dp={(0,)*m:F(1)}
    mass={}
    for t in range(1,m*(r-1)+2):
        nxt=defaultdict(F)
        for c,prob in dp.items():
            for i,pi in enumerate(p):
                if c[i]==r-1:
                    mass[t,i]=mass.get((t,i),F(0))+prob*pi
                else:
                    cc=list(c);cc[i]+=1
                    nxt[tuple(cc)]+=prob*pi
        dp=nxt
    return mass


def enumerate_joint(p,r):
    """Third construction: enumerate surviving full words at small parameters."""
    m=len(p)
    out=defaultdict(F)
    def rec(count, mass, t):
        for i,pi in enumerate(p):
            if count[i]==r-1:
                out[t,i]+=mass*pi
            else:
                new=list(count);new[i]+=1
                rec(tuple(new),mass*pi,t+1)
    rec((0,)*m,F(1),1)
    return out


def check(m,r,weight):
    p=tuple(F(x,sum(weight)) for x in weight)
    a=polynomial_joint(p,r)
    b=dynamic_joint(p,r)
    assert all(a[t,i]==b.get((t,i),F(0)) for t in range(r,m*(r-1)+2) for i in range(m))
    assert sum(a.values(),F(0))==1
    for i in range(m):
        for j in range(m):
            if p[i]>=p[j]:
                continue
            for t in range(r,m*(r-1)+1):
                assert a[t+1,i]*a[t,j]>a[t,i]*a[t+1,j],(m,r,weight,i,j,t)
            assert a[r,i]/a[r,j]==(p[i]/p[j])**r
            assert a[m*(r-1)+1,i]/a[m*(r-1)+1,j]==p[i]/p[j]
    if m<=3 and r<=3 and max(weight)<=2:
        c=enumerate_joint(p,r)
        assert all(a[t,i]==c.get((t,i),F(0)) for t in range(r,m*(r-1)+2) for i in range(m))

if __name__=='__main__':
    tested=0
    for r in (2,3,4):
        for m in (2,3,4,5):
            weights=(1,2,3) if m==5 else (1,2,3,4)
            for w in product(weights,repeat=m):
                check(m,r,w)
                tested+=1
            print('passed m=%d, r=%d, profiles=%d' %(m,r,len(weights)**m))
    print('PASS: %d exact-rational parameter profiles; polynomial, Markov, and small-word checks.'%tested)
    example=(F(1,2),F(1,3),F(1,6))
    for r in (2,3,4):
        w=polynomial_joint(example,r)
        odds=[str(w[t,2]/w[t,0]) for t in range(r,len(example)*(r-1)+2)]
        print('example r=%d, rare/common odds from earliest to latest: %s'%(r,','.join(odds)))
