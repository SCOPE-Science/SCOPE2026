#!/usr/bin/env python3
"""Independent exact finite-time tests for two Hata--Yano interval maps.
Standard-library only. This is a verification aid, not a substitute for the infinite proof.
"""
from collections import defaultdict
from fractions import Fraction as F

H = F(1,2)

def direct(p,n,side=0):
    # Each item: current interval [a,b], Lebesgue density, crossings.
    # Input is uniformly distributed in the indicated half interval.
    states=[(F(0),H,F(2),0)] if side==0 else [(H,F(1),F(2),0)]
    for _ in range(n):
        nxt=[]
        for a,b,d,c in states:
            for lo,hi in [(a,min(b,H)),(max(a,H),b)]:
                if lo>=hi: continue
                src_side=int(lo>=H)
                for selection,weight in [(0,p),(1,1-p)]:
                    if selection==0:
                        m,t=(H,F(0)) if src_side==0 else (F(2),-F(1))
                    else:
                        m,t=(F(2),F(0)) if src_side==0 else (H,H)
                    u,v=m*lo+t,m*hi+t
                    for x,y in [(u,min(v,H)),(max(u,H),v)]:
                        if x>=y: continue
                        dst_side=int(x>=H)
                        nxt.append((x,y,d*weight/m,c+(dst_side!=src_side)))
        states=nxt
    counts=defaultdict(F)
    for a,b,d,c in states: counts[c]+=(b-a)*d
    assert sum(counts.values())==1, (p,n,side,sum(counts.values()))
    return dict(counts)

def shells(p,n,side=0):
    # The tail k>=n cannot switch side during n steps, and is represented by k=n.
    states=defaultdict(F)
    for k in range(n): states[(side,k,0)]+=F(1,2**(k+1))
    states[(side,n,0)]+=F(1,2**n)
    for _ in range(n):
        nxt=defaultdict(F)
        for (s,k,c),mass in states.items():
            inward=(1-p if s==0 else p)
            outward=1-inward
            nxt[(s,k+1,c)]+=outward*mass
            if k>=1: nxt[(s,k-1,c)]+=inward*mass
            else:
                # The exit maps the core shell uniformly to the opposite half.
                for j in range(n):
                    nxt[(1-s,j,c+1)]+=inward*mass*F(1,2**(j+1))
                nxt[(1-s,n,c+1)]+=inward*mass*F(1,2**n)
        states=nxt
    counts=defaultdict(F)
    for (s,k,c),v in states.items():counts[c]+=v
    assert sum(counts.values())==1
    return dict(counts)

def first_success(p,side):
    q=1-p
    if side==0:
        return 1 if p<=q else q/(2*p-q)
    return 1 if q<=p else p/(2*q-p)

def check_infinite(p):
    q=1-p
    if p!=q:
        r=(1-abs(p-q))/(1+3*abs(p-q))
        assert 0<r<1
        for side in (0,1):
            target=0 if p>q else 1
            s=int(side!=target)
            mean=s+2*r/(1-r)
            expected=(q if side==0 else p)/abs(p-q)
            assert mean==expected,(p,side,mean,expected)
            # Geometric normalization and first crossing from starting half.
            prob_positive = r if s==0 else F(1)
            assert prob_positive==first_success(p,side),(p,side,prob_positive)
    # The harmonic equations for nearest-neighbor entrance into level -1.
    for side in (0,1):
        out=p if side==0 else q
        inn=1-out
        h=lambda k: F(1) if out<=inn else (inn/out)**(k+1)
        assert h(-1)==1
        for k in range(0,15):
            assert h(k)==out*h(k+1)+inn*h(k-1)
        avg=F(1) if out<=inn else (inn/out)/(2-inn/out)
        assert avg==first_success(p,side)

if __name__=='__main__':
    tests=0
    for p in [F(1,3),F(2,5),F(1,2),F(3,5),F(2,3),F(5,7)]:
        check_infinite(p)
        for side in (0,1):
            for n in range(1,9):
                left=direct(p,n,side)
                right=shells(p,n,side)
                assert left==right,(p,side,n,left,right)
                tests+=1
    print('PASS:',tests,'exact finite-time interval-vs-shell comparisons; all harmonic and moment checks')
