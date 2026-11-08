#!/usr/bin/env python3
"""Exact all-outcome/all-cohesive-group EJR-1 verifier for two-bloc budget family.

Self-contained Python 3 standard library; default checks both incompatible and compatible cells.
No external data files required.
"""
from math import comb
from fractions import Fraction


def actual(k, c):
    c=Fraction(c)
    scale=c.denominator
    H=c.numerator
    U=scale
    costs=[H,H]+[U]*(2*k)
    m=len(costs); full=(1<<m)-1
    A=[3|sum(1<<j for j in range(2,2+k)),3|sum(1<<j for j in range(2+k,m))]
    masks=[A[0],A[1],3]
    cost=[0]*(1<<m)
    for mask in range(1,1<<m):
        z=mask&-mask
        cost[mask]=cost[mask^z]+costs[z.bit_length()-1]
    witnesses=[]
    for g in range(3):
        b=H if g<2 else 2*H
        witnesses.append([(mask,mask.bit_count(),cost[mask]) for mask in range(1<<m) if not(mask&~masks[g]) and cost[mask]<=b])
    passed=[]
    for W in range(1<<m):
        if cost[W]>2*H:continue
        U0=full^W
        card=[(W&A[i]).bit_count() for i in range(2)]
        cval=[cost[W&A[i]] for i in range(2)]
        cardmax=[card[i]+bool(U0&A[i]) for i in range(2)]
        cmax=[cval[i]+max((costs[j] for j in range(m) if U0>>j&1 and A[i]>>j&1),default=0) for i in range(2)]
        valid=True
        for g in range(3):
            for T,tcard,tcost in witnesses[g]:
                if not(T&~W):continue
                if g<2:
                    if cardmax[g]<=tcard or cmax[g]<=tcost:valid=False;break
                else:
                    if max(cardmax)<=tcard or max(cmax)<=tcost:valid=False;break
            if not valid:break
        if valid:passed.append(W)
    return passed


def predicted(k,c):
    c=Fraction(c)
    if k<3: raise ValueError('k>=3 required')
    if c<3: return None
    if c>=2*(k-1):
        return 2*sum(comb(k,i)*comb(k,j) for i in range(k-1,k+1) for j in range(k-1,k+1) if i+j<=c)
    m=c.numerator//c.denominator
    if 3<=m<k and c-m>=Fraction(1,2):
        return 2*comb(k,m)*comb(k,m+1)
    return 0


def verify():
    cells=0; passed_outcomes=0
    for k in range(3,6):
        for c in map(Fraction,['1/2','1','2','5/2','11/4','3','13/4','7/2','15/4','4','17/4','9/2','19/4','5','21/4','11/2','23/4','6','13/2','7','15/2','8','9','10']):
            observed=actual(k,c)
            pred=predicted(k,c)
            if pred is None:assert observed,(k,c,'expected compatibility')
            else:assert len(observed)==pred,(k,c,len(observed),pred)
            cells+=1;passed_outcomes+=len(observed)
    print(f'PASS {cells} cells (k=3..5 and 24 rational ratios), all feasible labeled outcomes and all cohesive group/project witnesses; {passed_outcomes} jointly fair outcomes')
    for k,c in [(3,3),(3,Fraction(7,2)),(4,Fraction(7,2)),(4,4),(4,Fraction(9,2)),(4,6),(5,Fraction(9,2)),(5,5),(5,8)]:
        print('k',k,'c',str(c),'actual',len(actual(k,c)),'formula',predicted(k,c))

if __name__=='__main__':verify()
