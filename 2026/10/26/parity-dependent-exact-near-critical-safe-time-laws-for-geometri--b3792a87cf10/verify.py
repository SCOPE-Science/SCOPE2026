#!/usr/bin/env python3
"""Exact finite rational checks of geometric-runner safe-time profiles."""
from fractions import Fraction as F

def segments(q, horizon, delta):
    intervals=[(delta,1-delta)]
    for j in range(1,horizon):
        denominator=q**j
        new=[]
        for a,z in intervals:
            for k in range(int(a*denominator)-1,int(z*denominator)+2):
                lo=max(a,(F(k)+delta)/denominator)
                hi=min(z,(F(k+1)-delta)/denominator)
                if lo<hi:new.append((lo,hi))
        intervals=new
    return intervals

def mass(intervals):
    return sum((z-a for a,z in intervals),F(0))

def main():
    checks=0
    for q in (2,4,6,8,10,12):
        delta0=F(q-1,2*q)
        critical=F(q,2*(q+1))
        for delta in (delta0,(delta0+critical)/2):
            for m in range(2,8):
                parts=segments(q,m,delta)
                expected=(1-F(2*(q+1),q)*delta)/q**(m-2)
                assert len(parts)==2,(q,m,delta,parts)
                assert mass(parts)==expected,(q,m,delta)
                assert parts[0][0]+parts[1][1]==1,(q,m,delta)
                checks+=1
        assert not segments(q,2,critical)
        checks+=1
    for q in (3,5,7,9,11):
        delta0=F(q-1,2*q)
        for delta in (delta0,(delta0+F(1,2))/2):
            for m in range(1,8):
                parts=segments(q,m,delta)
                expected=(1-2*delta)/q**(m-1)
                assert len(parts)==1,(q,m,delta,parts)
                assert mass(parts)==expected,(q,m,delta)
                assert parts[0][0]+parts[0][1]==1
                checks+=1
        assert mass(segments(q,1,F(1,2)))==0
        checks+=1
    print('CERTIFICATE_OK exact_rational_profile_cases=',checks)
if __name__=='__main__':main()
