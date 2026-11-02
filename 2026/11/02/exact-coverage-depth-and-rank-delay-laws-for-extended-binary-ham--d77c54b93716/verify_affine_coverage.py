"""Standalone exact checks for complementary Reed--Muller coverage laws.

Python standard library only. Run: python verify_affine_coverage.py
"""
from fractions import Fraction
from itertools import combinations
from math import comb, factorial


def rank_gf2(cols):
    pivots = {}
    for v in cols:
        while v:
            pivot = v.bit_length() - 1
            if pivot in pivots:
                v ^= pivots[pivot]
            else:
                pivots[pivot] = v
                break
    return len(pivots)


def matrices(m):
    exponents = [mask for mask in range(1 << m) if mask.bit_count() <= m-2]
    C = []
    D = []
    for x in range(1 << m):
        C.append(sum(1 << j for j, a in enumerate(exponents) if (x & a) == a))
        D.append((x << 1) | 1)
    return C,D


def independent_counts(m):
    n=1<<m
    out=[1]
    for t in range(1,m+2):
        if t==1: out.append(n)
        else:
            num=out[-1]*(n-(1 << (t-2)))
            assert num%t==0
            out.append(num//t)
    return out


def exact_E(m):
    n=1<<m
    ind=independent_counts(m)
    H=lambda z:sum((Fraction(1,t) for t in range(1,z+1)),Fraction())
    return n*H(n)-sum((Fraction(n*ind[t],t*comb(n,t)) for t in range(1,m+2)),Fraction())


def exhaustive(m):
    C,D=matrices(m)
    n=len(C)
    k=n-m-1
    assert rank_gf2(C)==k and rank_gf2(D)==m+1
    span=[0]*(n+1)
    indep=[0]*(m+2)
    for mask in range(1<<n):
        s=mask.bit_count()
        cs=[C[x] for x in range(n) if (mask>>x)&1]
        dr=[D[x] for x in range(n) if (mask>>x)&1]
        rC=rank_gf2(cs)
        rD=rank_gf2(dr)
        if rC==k: span[s]+=1
        if s<=m+1 and rD==s: indep[s]+=1
        if m==4:
            # Verify the dual rank identity on every subset, not just independent cases.
            other=[D[x] for x in range(n) if not (mask>>x)&1]
            assert rC==s-(m+1)+rank_gf2(other)
    assert indep==independent_counts(m), (m,indep,independent_counts(m))
    for s in range(n+1):
        expected= indep[n-s] if 0<=n-s<=m+1 else 0
        assert span[s]==expected,(m,s,span[s],expected)
    if m==3:
        E=[Fraction()]*(1<<n)
        for mask in sorted(range(1<<n),key=int.bit_count,reverse=True):
            if rank_gf2([C[x] for x in range(n) if (mask>>x)&1])==k:
                E[mask]=Fraction()
            else:
                j=mask.bit_count()
                E[mask]=(Fraction(n)+sum((E[mask|(1<<x)] for x in range(n) if not (mask>>x)&1),Fraction()))/(n-j)
        assert E[0]==exact_E(m),(E[0],exact_E(m))
    else:
        E=[0.0]*(1<<n)
        for mask in sorted(range(1<<n),key=int.bit_count,reverse=True):
            if rank_gf2([C[x] for x in range(n) if (mask>>x)&1])==k:
                E[mask]=0.
            else:
                j=mask.bit_count()
                E[mask]=(n+sum(E[mask|(1<<x)] for x in range(n) if not (mask>>x)&1))/(n-j)
        assert abs(E[0]-float(exact_E(m))) < 1e-10,(E[0],exact_E(m))
    return n,k,indep,span,exact_E(m)


def check_cdf(m):
    n=1<<m
    ind=independent_counts(m)
    cdf=[]
    for h in range(m+2):
        t=m+1-h
        cdf.append(Fraction(ind[t],comb(n,t)))
    assert all(cdf[j]<=cdf[j+1] for j in range(m+1))
    assert cdf[-1]==1
    # Exact tail expectation for distinct-coordinate overshoot.
    EJ=sum((1-cdf[h] for h in range(m+1)),Fraction())
    H=lambda z:sum((Fraction(1,t) for t in range(1,z+1)),Fraction())
    baseline=n*(H(n)-H(m+1))
    penalty=sum((Fraction(n,m+1-h)*(1-cdf[h]) for h in range(m+1)),Fraction())
    assert baseline+penalty==exact_E(m)
    return EJ,cdf[0],penalty


def limit_constant():
    C=sum(1/(2**j-1) for j in range(1,60))
    Q=[]
    for h in range(35):
        prod=1.0
        for j in range(h+1,100):prod*=1-2.**(-j)
        Q.append(prod)
    tail=sum(1-x for x in Q)
    assert abs(C-tail)<1e-9,(C,tail)
    return C

if __name__=='__main__':
    for m in (3,4):
        n,k,indep,span,E=exhaustive(m)
        print('EXHAUSTIVE',m,'n',n,'k',k,'independent',indep,'spanning tail',[span[s] for s in range(k,n+1)],'E',E)
    for m in range(3,13):
        EJ,p0,penalty=check_cdf(m)
        if m<=7:print('EXACT',m,'E',exact_E(m),'P(J=0)',p0,'E[J]',EJ,'excess',penalty)
    print('ERDOS_BORWEIN',format(limit_constant(),'.15f'))
    print('AFFINE_COVERAGE_VERIFY_OK')
