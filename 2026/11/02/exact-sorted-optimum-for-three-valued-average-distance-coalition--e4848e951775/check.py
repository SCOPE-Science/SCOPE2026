#!/usr/bin/env python3
"""Exact arithmetic checks of the three-value two-coalition formula."""
from fractions import Fraction as F


def half_cost(a,b,c,u,v):
    n=a+b+c
    return F(a*b*u+b*c*v+a*c*(u+v),n-1) if n>1 else F(0)


def check():
    count=0
    for a in range(1,8):
        for b in range(1,8):
            for c in range(1,8):
                A0=F(a*b,a+b-1)
                B0=F(b*c,b+c-1)
                cuts=[F(2)*A0,F(2)*B0]
                for aa in range(a+1):
                    for bb in range(b+1):
                        for cc in range(c+1):
                            s=aa+bb+cc
                            if not 0<s<a+b+c: continue
                            if s>1:
                                A1=F(aa*(bb+cc),s-1)
                                B1=F(cc*(aa+bb),s-1)
                            else:A1=B1=F(0)
                            t=a+b+c-s
                            if t>1:
                                A2=F((a-aa)*(b-bb+c-cc),t-1)
                                B2=F((c-cc)*(a-aa+b-bb),t-1)
                            else:A2=B2=F(0)
                            A=A1+A2;B=B1+B2
                            assert A/A0+B/B0>=1,(a,b,c,aa,bb,cc,A,B)
                            for u,v in [(1,1),(1,3),(3,1),(2,5),(5,2)]:
                                price=2*(u*A+v*B)
                                baseline=min(cuts[0]*u,cuts[1]*v)
                                assert price>=baseline,(a,b,c,aa,bb,cc,u,v,price,baseline)
                            count+=1
                # Also verify grand coalition cannot beat the stated minimum
                for u,v in [(1,1),(1,3),(3,1),(2,5),(5,2)]:
                    assert 2*half_cost(a,b,c,u,v)>=min(cuts[0]*u,cuts[1]*v)
    print(f'VERIFY_OK exact_count_profiles=343 exact_two_group_partitions={count} gap_pairs=5 singleton_allowed=True')

if __name__=='__main__':check()
