#!/usr/bin/env python3
"""Standalone exact-arithmetic checks for additive multiset support spectra.
Dependencies: Python 3 standard library only.
"""
from itertools import product
from math import comb, gcd, lcm
from collections import defaultdict


def divisors(n):
    return [d for d in range(1, n+1) if n%d == 0]


def mobius(n):
    if n==1: return 1
    ans=1
    p=2
    while p*p<=n:
        if n%p==0:
            n//=p
            if n%p==0:return 0
            ans=-ans
            while n%p==0:n//=p
        p+=1
    if n>1:ans=-ans
    return ans


def group_elements(moduli):
    return tuple(product(*(range(m) for m in moduli)))


def plus(x,y,moduli):
    return tuple((a+b)%m for a,b,m in zip(x,y,moduli))


def neg(x,moduli):
    return tuple((-a)%m for a,m in zip(x,moduli))


def character_order_sum(d,a,moduli):
    # R_d(a) by Möbius inversion over e-torsion of the dual group.
    total=0
    for e in divisors(d):
        mu=mobius(d//e)
        if mu==0:continue
        torsion=1
        for m,coord in zip(moduli,a):
            g=gcd(m,e)
            if coord%g:
                torsion=0
                break
            torsion*=g
        total+=mu*torsion
    return total


def q_polynomial(d,h,k):
    # Coefficients [u^r] [t^k] ((1-(1-u)^d*t)/(1-t))^h.
    out=[0]*(d*h+1)
    for j in range(min(h,k)+1):
        scalar=(-1)**j*comb(h,j)*comb(h+k-j-1,h-1)
        for r in range(d*j+1):
            out[r]+=scalar*(-1)**r*comb(d*j,r)
    return out


def theory(moduli,n,a):
    q=1
    for m in moduli:q*=m
    exponent=lcm(*moduli)
    out=[0]*(min(n,q)+1)
    for d in divisors(gcd(n,exponent)):
        if q%d:continue
        R=character_order_sum(d,a,moduli)
        polynomial=q_polynomial(d,q//d,n//d)
        for r in range(len(out)):
            out[r]+=R*polynomial[r]
    assert all(x%q==0 for x in out), (moduli,n,a,out)
    return [x//q for x in out]


def compositions(n,q):
    if q==1:
        yield (n,)
    else:
        for j in range(n+1):
            for rest in compositions(n-j,q-1):
                yield (j,)+rest


def brute(moduli,n):
    elements=group_elements(moduli)
    q=len(elements)
    counts={a:[0]*(min(n,q)+1) for a in elements}
    for x in compositions(n,q):
        a=tuple(sum(xi*e[k] for xi,e in zip(x,elements))%m for k,m in enumerate(moduli))
        r=sum(xi>0 for xi in x)
        counts[a][r]+=1
    return counts


def check(moduli,n):
    actual=brute(moduli,n)
    q=len(actual)
    B=comb(n+q-2,q-1)
    assert sum(sum(r*c for r,c in enumerate(row)) for row in actual.values())==q*B
    assert sum(sum(r*c for r,c in enumerate(row))==B for row in actual.values())
    for a,profile in actual.items():
        expected=theory(moduli,n,a)
        assert profile==expected, (moduli,n,a,profile,expected)
    if gcd(n,lcm(*moduli))==1:
        assert len({tuple(v) for v in actual.values()})==1
    else:
        assert len({tuple(v) for v in actual.values()})>1
    if len(moduli)==1 and all(moduli[0]%p for p in range(2,int(moduli[0]**.5)+1)):
        p=moduli[0]
        for a,profile in actual.items():
            for r in range(1,min(p,n)+1):
                base=comb(p,r)*comb(n-1,r-1)
                corr=(p-1 if a==(0,) else -1)*(-1)**(r-1)*comb(p,r) if n%p==0 else 0
                assert p*profile[r]==base+corr
    return sum(sum(v) for v in actual.values()),len({tuple(v) for v in actual.values()})


def check_interclass(moduli,n):
    G=group_elements(moduli); q=len(G)
    classes=brute(moduli,n)
    total=0
    for x in compositions(n,q):
        sx=tuple(sum(xi*g[k] for xi,g in zip(x,G))%m for k,m in enumerate(moduli))
        for t in G:
            if all(v==0 for v in t):continue
            b=plus(sx,t,moduli)
            observed=set()
            for gindex,g in enumerate(G):
                if x[gindex]:
                    h=plus(g,t,moduli)
                    other=list(x);other[gindex]-=1;other[G.index(h)]+=1
                    observed.add(tuple(other))
                    sy=tuple(sum(vi*z[k] for vi,z in zip(other,G))%m for k,m in enumerate(moduli))
                    assert sy==b
            assert len(observed)==sum(v>0 for v in x)
            total+=len(observed)
    assert total==q*(q-1)*comb(n+q-2,q-1)

if __name__=='__main__':
    total_count=0; cases=0
    for moduli,lim in [((2,),16),((3,),14),((4,),12),((5,),11),((6,),9),((7,),8),((2,2),11),((2,3),8),((2,2,2),6),((3,3),5)]:
        for n in range(1,lim+1):
            num,types=check(moduli,n)
            total_count+=num;cases+=1
            if n in (1,lim):print('CHECK',moduli,n,'multisets',num,'types',types)
    for moduli in [(2,),(3,),(4,),(2,2),(2,3)]:
        for n in (2,3,4):
            check_interclass(moduli,n)
    print('ADDITIVE_MULTISET_SUPPORT_OK', cases, 'parameter settings',total_count,'enumerated codewords')
    print('CROSS_SYNDROME_TRANSFER_OK',15,'parameter settings')
