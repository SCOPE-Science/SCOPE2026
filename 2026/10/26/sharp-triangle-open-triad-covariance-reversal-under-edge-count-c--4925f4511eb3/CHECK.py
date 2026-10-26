#!/usr/bin/env python3
"""Exact finite checks for a theorem about the two natural three-vertex motif counts."""
from fractions import Fraction as Q
from itertools import combinations
from math import comb

def fixed_formula(n,m):
    E=comb(n,2)
    if m<3 or m>E-2:return Q(0)
    z=(n-1)*(n*n-n-4)+m*(n*n-3*n-8)
    return Q(-4*m*(m-1)*(m-2)*(E-m)*(E-m-1)*z,
             (n+1)**2*(n+2)*(E-5)*(E-4)*(E-2)**2)

def moment_overlap(n, edge_moment):
    A=comb(n,3)
    q=edge_moment
    cov_tw=A*(3*q(3)+6*(n-3)*q(4)+(3*A-3-6*(n-3))*q(5)-3*A*q(3)*q(2))
    var_t=A*(q(3)+3*(n-3)*q(5)+(A-1-3*(n-3))*q(6)-A*q(3)**2)
    return cov_tw-3*var_t

def bern_formula(n,p):
    return 3*comb(n,3)*p**4*(1-p)*(2*(n-3)-(3*n-8)*p)

def full_sums(n):
    edges=list(combinations(range(n),2));M=len(edges)
    triple_sets=[list(combinations(tr,2)) for tr in combinations(range(n),3)]
    sums={}
    for bits in range(1<<M):
        chosen={e for j,e in enumerate(edges) if bits>>j&1}
        t=path=0
        for tr in triple_sets:
            k=len(set(tr)&chosen)
            t+=(k==3)
            path+=(k==2)
        m=len(chosen)
        s=sums.setdefault(m,[0,0,0,0])
        s[0]+=1;s[1]+=t;s[2]+=path;s[3]+=t*path
    return sums

for n in range(4,20):
    E=comb(n,2)
    for m in range(E+1):
        q=lambda r: Q(comb(m,r),comb(E,r)) if m>=r else Q(0)
        assert fixed_formula(n,m)==moment_overlap(n,q),(n,m)
        assert (fixed_formula(n,m)<0)==(3<=m<=E-2),(n,m)
print('PASS: hypergeometric moment identity and signs, n=4..19, all m')
for n in range(4,7):
    sums=full_sums(n)
    for m,(total,st,sp,stp) in sums.items():
        assert total==comb(comb(n,2),m)
        assert Q(stp,total)-Q(st*sp,total*total)==fixed_formula(n,m)
    print('PASS: independent exhaustive G(n,m) enumeration',n)
for n in (4,5):
    sums=full_sums(n);E=comb(n,2)
    for p in (Q(1,5),Q(1,2),Q(4,5)):
        et=ep=etp=Q(0)
        for m,(_,st,sp,stp) in sums.items():
            weight=p**m*(1-p)**(E-m)
            et+=weight*st;ep+=weight*sp;etp+=weight*stp
        expected=bern_formula(n,p)
        assert etp-et*ep==expected,(n,p)
        assert expected==moment_overlap(n,lambda k:p**k)
    print('PASS: independent exhaustive G(n,p) enumeration',n)
print('ALL NEW-FINDING CHECKS PASS')
