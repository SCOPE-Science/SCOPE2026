#!/usr/bin/env python3
"""Exact cut certificates and embeddings for dense cycle-complement metrics."""
from fractions import Fraction as F
from collections import Counter

P_R=((0,3,1),(0,4,1),(0,5,1),(1,4,1),(1,5,2),(1,6,1),(2,5,1),(2,6,1),(3,6,1))

def bit(mask,i):return (mask>>i)&1

def cut(mask,i,j):return bit(mask,i)^bit(mask,j)

def c7_counts(mask):
    return tuple(sum(cut(mask,i,(i+k)%7) for i in range(7)) for k in (1,2,3))

def p7_margin(mask):
    left=sum(cut(mask,i,i+1) for i in range(6))
    right=sum(w*cut(mask,i,j) for i,j,w in P_R)
    return right-left

def averaged_cut(n,mask,k):
    return F(sum(cut(mask,i,(i+k)%n) for i in range(n)),n)

def main():
    # Complement path P7 cut-facet certificate; 128 possible cuts, no numerical tolerance.
    for mask in range(1<<7): assert p7_margin(mask)>=0,('P7',mask)
    # Complement cycle C7 cut-facet certificate; 128 possible cuts.
    for mask in range(1<<7):
        e1,e2,e3=c7_counts(mask)
        assert e2+4*e3-3*e1>=0,('C7',mask)
    # Check examples of equality to avoid vacuity.
    assert min(p7_margin(m) for m in range(128))==0
    assert min(c7_counts(m)[1]+4*c7_counts(m)[2]-3*c7_counts(m)[0] for m in range(128))==0
    # Verify the exact three upper-bound embeddings on every pair by cyclic rotation averages.
    constructions={
      5:[(F(5,2),0b00101)],
      6:[(F(3,2),0b001001),(F(1),0b010101)],
      7:[(F(7,5),0b0001001),(F(7,5),0b0010101)]
    }
    for n,recipe in constructions.items():
        for i in range(n):
            for j in range(i+1,n):
                k=min(j-i,n-(j-i))
                rho=sum(w*averaged_cut(n,mask,k) for w,mask in recipe)
                desired=F(2) if k==1 else F(6,5) if n==7 else F(1)
                assert rho==desired,(n,i,j,rho,desired)
    # The displayed graph-metric formula really is its shortest path metric.
    for n in range(5,35):
        for i in range(n):
            for j in range(i+1,n):
                adjacent_in_cycle=(j-i==1 or j-i==n-1)
                if adjacent_in_cycle:
                    possible=[k for k in range(n) if k not in (i,j) and ((k-i)%n not in (1,n-1)) and ((k-j)%n not in (1,n-1))]
                    assert possible,(n,i,j)
    print('CHECK_OK: 256 complete cut inequalities; 5,6,7 exact embeddings; n=5..34 graph distances')
    for name, func in [('C7',lambda m:c7_counts(m)[1]+4*c7_counts(m)[2]-3*c7_counts(m)[0]),('P7',p7_margin)]:
        bysize={}
        for m in range(1<<7):
            t=bin(m).count('1')
            bysize[t]=min(bysize.get(t,100),func(m))
        print(name,'min margins by cut size',bysize,'equalities',sum(func(m)==0 for m in range(128)))
if __name__=='__main__':main()
