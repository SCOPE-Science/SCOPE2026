#!/usr/bin/env python3
"""Exact checks for finite-census richness--sample-trait covariance.
No third-party packages; every probability is a Fraction.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb

import json

def C(n, k):
    return comb(n,k) if n>=0 and k>=0 and k<=n else 0

def exact_formula(a,t,m):
    N=sum(a)
    assert N>=2 and 1<=m<=N
    t=list(map(Q,t))
    mu=sum(x*y for x,y in zip(a,t))/N
    return sum((x*(y-mu)*C(N-x-1,m-1) for x,y in zip(a,t)),Q()) / (N*C(N-1,m-1))

def direct_labeled_subsets(a,t,m):
    labels=[]
    for i,ai in enumerate(a): labels += [i]*ai
    N=len(labels)
    t=list(map(Q,t))
    E_K=E_T=E_KT=Q()
    for selection in combinations(range(N),m):
        species={labels[i] for i in selection}
        k=len(species)
        z=sum(t[labels[i]] for i in selection)/m
        E_K+=k
        E_T+=z
        E_KT+=k*z
    div=C(N,m)
    return E_KT/div - (E_K/div)*(E_T/div)

def sign(v):return (v>0)-(v<0)

def reversals(xs):
    nonzero=[sign(x) for x in xs if x]
    return sum(x!=y for x,y in zip(nonzero,nonzero[1:]))

def gaussian_solve(mat,vector):
    n=len(vector)
    A=[[Q(z) for z in row]+[Q(v)] for row,v in zip(mat,vector)]
    for j in range(n):
        h=next(k for k in range(j,n) if A[k][j]!=0)
        A[j],A[h]=A[h],A[j]
        pivot=A[j][j]
        A[j]=[z/pivot for z in A[j]]
        for k in range(n):
            if k==j:continue
            fac=A[k][j]
            A[k]=[u-fac*v for u,v in zip(A[k],A[j])]
    return [A[i][-1] for i in range(n)]

def integer_partitions(N,lower=1):
    if N==0:
        yield ()
    else:
        for p in range(lower,N+1):
            for tail in integer_partitions(N-p,p):
                yield (p,)+tail

def partial_abundance_levels(a,t):
    mu=sum(x*y for x,y in zip(a,t))/sum(a)
    levels=sorted(set(a),reverse=True)
    b=[sum(x*(y-mu) for x,y in zip(a,t) if x==v) for v in levels]
    B=[]; cumulative=Q()
    for z in b[:-1]:
        cumulative+=z
        B.append(cumulative)
    return B

def main():
    record={}
    a=[1,2,3,4]
    b=[21,-69,76,-28]
    t=[Q(35)+Q(z,x) for x,z in zip(a,b)]
    v=[exact_formula(a,t,m) for m in range(1,11)]
    num=[sum(z*C(10-x-1,m-1) for x,z in zip(a,b)) for m in range(1,11)]
    assert num==[0,1,-1,1,55,155,181,99,21,0],num
    assert v[1]==Q(1,90) and v[2]==Q(-1,360) and v[3]==Q(1,840),v
    assert reversals(v[1:-1])==2
    for m in range(1,11):
        assert v[m-1]==direct_labeled_subsets(a,t,m),(m,v[m-1],direct_labeled_subsets(a,t,m))
    record['four_level_witness']={"abundances":a,"traits":[str(z) for z in t],"numerator_sequence":num,"covariance_sample_sizes_2_to_4":[str(z) for z in v[1:4]],"strict_reversals":2}

    # Verify exact analytic formula vs unrelated exhaustive labeled-subset enumeration
    # for every composition profile through N=8 and several nonmonotone traits.
    profiles=0
    pair_tests=0
    variation_tests=0
    for N in range(2,9):
        for ab in integer_partitions(N):
            profiles+=1
            for seed in range(3):
                traits=[Q(((3*i+5*seed + ai*ai)%13)-4,2) for i,ai in enumerate(ab)]
                s=len(set(ab))
                seq=[]
                for m in range(1,N+1):
                    d=direct_labeled_subsets(ab,traits,m)
                    f=exact_formula(ab,traits,m)
                    assert f==d,(ab,traits,m,f,d)
                    seq.append(f)
                    pair_tests+=1
                bound=max(0,s-2)
                assert reversals(seq[1:-1])<=bound,(ab,traits,seq,bound)
                B=partial_abundance_levels(ab,traits)
                assert reversals(seq[1:-1])<=reversals(B),(ab,B,seq)
                variation_tests+=1
    record['exhaustive_subset_comparisons']={"population_range":"2..8","abundance_profiles":profiles,"trait_choices_per_profile":3,"exact_formula_vs_subset_checks":pair_tests,"variation_diminishing_sequence_checks":variation_tests}

    # Infinite sharpness reduced to invertibility of Pascal basis at distinct nodes;
    # computational witnesses through 8 classes independently test constraints.
    sharp=[]
    for r in range(2,9):
        ai=list(range(1,r+1))
        N=sum(ai)
        M=[[C(N-a-1,m-1) for a in ai] for m in range(1,r+1)]
        target=[0]+[(-1)**m for m in range(2,r+1)]
        bj=gaussian_solve(M,target)
        assert sum(bj)==0,(r,bj)
        ti=[z/a for a,z in zip(ai,bj)]
        values=[exact_formula(ai,ti,m) for m in range(2,r+1)]
        assert [sign(z) for z in values] == [(-1)**m for m in range(2,r+1)]
        assert reversals(values)==r-2
        if r<=4:
            for m in range(1,N+1):
                assert direct_labeled_subsets(ai,ti,m)==exact_formula(ai,ti,m)
        sharp.append({"number_of_abundance_levels":r,"individuals":N,"reversals":r-2,"numerator_target":target})
    record['sharpness'] = sharp
    # Fixed-trait-rank monotonicity check on all profiles through 9, sign only.
    checks=0
    for N in range(2,10):
        for ab in integer_partitions(N):
            for reverse in (False, True):
                traits=[Q(-a if reverse else a) for a in ab]
                for m in range(1,N+1):
                    z=exact_formula(ab,traits,m)
                    assert (z>=0 if reverse else z<=0),(ab,traits,m,z)
                    checks+=1
    record['monotone_trait_sign_checks']=checks
    print(json.dumps(record,sort_keys=True,indent=2))
if __name__=='__main__':main()
