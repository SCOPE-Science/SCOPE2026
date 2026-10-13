#!/usr/bin/env python3
"""Finite checks for the cototient-derivative two-prime theorem; not a proof."""

def least_factors(limit):
    spf = list(range(limit + 1))
    for p in range(2, int(limit ** 0.5) + 1):
        if spf[p] == p:
            for n in range(p*p, limit+1, p):
                if spf[n] == n:
                    spf[n] = p
    return spf


def factor(n, spf):
    ans=[]
    while n > 1:
        p=spf[n]; e=0
        while n%p==0:
            n//=p; e+=1
        ans.append((p,e))
    return ans


def derivative(n, spf):
    return sum(e*(n//p) for p,e in factor(n,spf))


def phi(n, spf):
    for p,_ in factor(n,spf):
        n -= n//p
    return n


def theorem_pair(n, spf):
    fac=factor(n,spf)
    if len(fac)!=2 or fac[0][0]!=2:
        return False
    (p2,a),(p,b)=fac
    if a!=2 or b!=1:
        return False
    z=p+1; t=0
    while z%2==0:
        t+=1;z//=2
    if t==1:
        return derivative(z,spf)==z-1
    if t==2:
        return 2*derivative(z,spf)==z-1
    return False


def verify(N=200000):
    spf=least_factors(N)
    hits=[]; pair_count=0
    for n in range(2,N+1):
        fs=factor(n,spf)
        if len(fs)==2 and fs[0][0]==2:
            pair_count+=1
            m=n-phi(n,spf)
            actual=(derivative(m,spf)==n)
            theor=theorem_pair(n,spf)
            if actual != theor:
                raise AssertionError((n,actual,theor,m,fs))
            if actual:
                hits.append(n)
    assert hits == [12,44,332], hits
    half=[];odd=[]
    for u in range(1, 50001, 2):
        d=derivative(u,spf)
        if 2*d==u-1:
            half.append(u)
        if d==u-1:
            odd.append(u)
    assert half[:3]==[1,3,21],half[:5]
    assert odd==[1], odd
    print('VERIFY_OK complete_n=%d two_support_checked=%d two_support_hits=%r' % (N,pair_count,hits))
    print('ODD_U_CHECK_OK u_le=50000 half_port=%r primary_odd=%r' % (half,odd))

if __name__=='__main__':
    verify()
