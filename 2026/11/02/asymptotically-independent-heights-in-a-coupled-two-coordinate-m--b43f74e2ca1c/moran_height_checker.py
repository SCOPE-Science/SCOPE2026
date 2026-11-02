"""Exact and numerical checks of two-coordinate Moran height identities."""
from fractions import Fraction
from itertools import product
from math import exp, log, ceil

def check():
    assertions=0
    for q in (Fraction(3,5),Fraction(3,4),Fraction(9,10)):
        b=1-q; a=2*q-1; assert 0<=a<q*q; assertions+=1
        for ell in range(1,5):
            p=b*q**ell
            for k in range(1,ell+1):
                # brute enumerate all step strings of length k+ell+1. marker X at time 0 and Y at k
                m=k+ell+1; total=Fraction(0)
                for s in product(range(3),repeat=m):
                    # 0 X-only: Y reset, 1 Y-only: X reset, 2 both survive
                    good=(s[0]==1 and all(s[j]!=1 for j in range(1,ell+1)) and s[k]==0 and all(s[j]!=0 for j in range(k+1,k+ell+1)))
                    if good:
                        total += (b**sum(v!=2 for v in s))*(a**sum(v==2 for v in s))
                expected=b*b*q**(2*k-1)*a**(ell-k)
                assert total==expected,(q,ell,k,total,expected)
                assertions+=1
            # same-coordinate start separation <= ell excludes intersection
            for k in range(1,ell+1):
                for s in product(range(3),repeat=k+ell+1):
                    x0=(s[0]==1 and all(s[j]!=1 for j in range(1,ell+1)))
                    xk=(s[k]==1 and all(s[j]!=1 for j in range(k+1,k+ell+1)))
                    assert not (x0 and xk)
                    assertions+=1
    # Pathwise equivalence: threshold exceedance without an initial all-success
    # run is exactly a marked post-reset survival run.
    for h in (2,3,4):
        ell=h-1
        for n in range(h,9):
            for seq in product(range(3),repeat=n):
                ages=[0,0]; tops=[0,0]; marks=[False,False]
                for t,v in enumerate(seq):
                    inc=(v==0 or v==2,v==1 or v==2)
                    for i in (0,1):
                        ages[i]=ages[i]+1 if inc[i] else 1
                        tops[i]=max(tops[i],ages[i])
                        if t>=ell and not inc[i] and t+ell<n:
                            pass
                for i in (0,1):
                    fail=1 if i==0 else 0
                    success=lambda v,i=i: v != (1 if i==0 else 0)
                    marks[i]=any(seq[t]==fail and all(success(seq[j]) for j in range(t+1,t+ell+1)) for t in range(n-ell))
                    initial=all(success(seq[t]) for t in range(h))
                    assert (tops[i]>=h)==(marks[i] or initial)
                    assertions+=1
    # Exact finite dynamic recursion of height and marker-free event, with initial run exception.
    for q in (0.6,0.8):
        b=1-q; a=2*q-1
        for h1,h2 in ((3,4),(4,3),(5,5)):
            # Reset-to-one convention. At step t from initial 0, increments or reset to one.
            state={(0,0):1.0}; n=10
            for t in range(n):
                nxt={}
                for (x,y),p in state.items():
                    for xx,yy,prob in ((x+1,1,b),(1,y+1,b),(x+1,y+1,a)):
                        if xx<h1 and yy<h2:
                            nxt[xx,yy]=nxt.get((xx,yy),0)+p*prob
                state=nxt
            prob=sum(state.values())
            assert 0<=prob<=1
            assertions+=1
            lam1=max(0,n-h1+1)*b*q**(h1-1)
            lam2=max(0,n-h2+1)*b*q**(h2-1)
            assert abs(prob-exp(-lam1-lam2))<0.5
            assertions+=1
    print('PASS',assertions,'assertions')
if __name__=='__main__': check()
