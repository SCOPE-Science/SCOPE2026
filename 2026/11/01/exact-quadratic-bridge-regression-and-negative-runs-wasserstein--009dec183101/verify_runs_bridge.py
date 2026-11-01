#!/usr/bin/env python3
"""Exact rational finite verification of conditional run regression and bridge-cut dependence."""
from fractions import Fraction
from itertools import combinations
from math import comb

def law(a,b,k):
    N=a+b
    out={}
    for chosen in combinations(range(N),a):
        word=[0]*N
        for pos in chosen:word[pos]=1
        r=1+sum(word[i]!=word[i-1] for i in range(1,N))
        c=sum(word[:k]);out.setdefault(c,[]).append(r)
    return out

def conditional_formula(a,b,k,c):
    N=a+b;t=N-k
    return (Fraction(1)+Fraction(2*c*(k-c),k)+Fraction(2*(a-c)*(b-k+c),t)
        +Fraction(c*(b-k+c)+(k-c)*(a-c),k*t))

def verify():
    checks=0; words=0; profiles=0
    for a in range(1,8):
      for b in range(1,8):
        N=a+b;profiles+=1
        for k in range(1,N):
            rows=law(a,b,k)
            words+=sum(len(q) for q in rows.values())
            for c, values in rows.items():
                measured=Fraction(sum(values),len(values));expect=conditional_formula(a,b,k,c)
                assert measured==expect, ('conditional regression',a,b,k,c,measured,expect)
                checks+=1
    for m in range(1,9):
      N=2*m
      if N==2:continue
      from itertools import combinations
      for k in range(1,N):
        rows=law(m,m,k)
        full=[(r,2*c-k) for c,lst in rows.items() for r in lst]
        L=len(full)
        e_r=Fraction(sum(r for r,s in full),L)
        assert e_r==Fraction(N+2,2)
        for c, rs in rows.items():
            s=2*c-k
            expect=Fraction(N+3,2)-Fraction((N-1)*s*s,2*k*(N-k))
            assert Fraction(sum(rs),len(rs))==expect
            checks+=1
        for power in [1,2,4]:
            vals=[(r,abs(s)**power) for r,s in full]
            E_g=Fraction(sum(g for r,g in vals),L)
            cov=Fraction(sum(r*g for r,g in vals),L)-e_r*E_g
            assert cov <= 0
            if 2<=k<=N-2:assert cov<0
            else:assert cov==0
            if power==2:
                expect=-Fraction(N*(k-1)*(N-k-1),(N-3)*(N-1))
                assert cov==expect,('parabolic',N,k,cov,expect)
            checks+=1
    # Weighted first-Wasserstein distance of balanced empirical distributions,
    # conditional on a deterministic strictly increasing pooled sample.
    for m in range(2,7):
      N=2*m; ws=[]
      gaps=[j+1 for j in range(1,N)]
      for chosen in combinations(range(N),m):
        word=[0]*N
        for j in chosen:word[j]=1
        r=1+sum(word[j]!=word[j-1] for j in range(1,N))
        s=0; q=0
        for j in range(N-1):
            s+=2*word[j]-1
            q+=gaps[j]*abs(s)
        ws.append((r,q))
      total=len(ws)
      cov=Fraction(sum(r*q for r,q in ws),total)-Fraction(sum(r for r,q in ws)*sum(q for r,q in ws),total**2)
      assert cov<0,(m,cov)
      checks+=1
    return checks,words,profiles

if __name__=='__main__':
 c,w,p=verify()
 print(f'PASS: {c} exact assertions; {w} conditional-enumeration word instances; {p} unbalanced/balanced profiles.')
