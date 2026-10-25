#!/usr/bin/env python3
"""Self-contained finite verification of commuting-pair orbit formula for quandle algebras."""
from itertools import product
from math import prod
from random import Random

def T(m,q):
    assert m>=1 and q>=2
    u0,u1=2,q
    for _ in range(2,m+1):u0,u1=u1,q*u1+q*(q-1)*u0
    u=u1 if m>0 else u0
    return u+q*(q-1)**m

def centerdim(vals):
    m=len(vals)
    if m==1:return 1
    if all(v==0 for v in vals):return m
    if all(v!=0 for v in vals):return 1
    z=[v==0 for v in vals]
    # Count nonzero runs and zeros not adjacent to nonzero, cyclic wrap accounted for.
    runs=sum((not z[i]) and z[(i-1)%m] for i in range(m))
    free_zeros=sum(z[i] and z[(i-1)%m] and z[(i+1)%m] for i in range(m))
    return runs+free_zeros

def matrix_rank_mod(mat,q):
    a=[row[:] for row in mat]
    rank=0
    for col in range(len(a[0])):
        pivot=next((i for i in range(rank,len(a)) if a[i][col]%q),None)
        if pivot is None:continue
        a[rank],a[pivot]=a[pivot],a[rank]
        inv=pow(a[rank][col],-1,q)
        a[rank]=[(x*inv)%q for x in a[rank]]
        for i in range(len(a)):
            if i!=rank and a[i][col]:
                z=a[i][col]
                a[i]=[(x-z*y)%q for x,y in zip(a[i],a[rank])]
        rank+=1
    return rank

def check_transfer():
    for q,m in [(2,1),(2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(4,3),(5,2),(11,4)]:
        # brute over all u cycle coordinates; centralizer dimension vs rank.
        total=0
        for a in product(range(q),repeat=m):
            dimension=centerdim(a)
            total+=q**dimension
            if q in (2,3,5,11) and (q**m<=10000):
                mat=[]
                for i in range(m):
                    row=[0]*m
                    row[(i+1)%m]=a[i]
                    row[i]=(row[i]-a[(i+1)%m])%q
                    mat.append(row)
                assert m-matrix_rank_mod(mat,q)==dimension,(q,m,a,dimension)
        assert total==T(m,q),(q,m,total,T(m,q))
        print('CYCLE_OK',q,m,total)

def check_quandle_prime(n,q,zeta,phi):
    assert pow(zeta,n,q)==1
    assert all(pow(zeta,i,q)!=1 for i in range(1,n))
    h=lambda a:[sum(a[x]*pow(zeta,j*x,q) for x in range(n))%q for j in range(n)]
    def mul(a,b):
        out=[0]*n
        for x,v in enumerate(a):
            for y,w in enumerate(b):out[(phi*x+(1-phi)*y)%n]=(out[(phi*x+(1-phi)*y)%n]+v*w)%q
        return out
    r=Random(20261022+n)
    for _ in range(3000):
        a=[r.randrange(q) for _ in range(n)]
        b=[r.randrange(q) for _ in range(n)]
        aa=h(a);bb=h(b)
        ab=h(mul(a,b));ba=h(mul(b,a))
        for j in range(n):
            assert ab[j]==aa[(phi*j)%n]*bb[((1-phi)*j)%n]%q
            assert ba[j]==bb[(phi*j)%n]*aa[((1-phi)*j)%n]%q
        pred=all(aa[j]*bb[(((1-phi)*pow(phi,-1,n))*j)%n]%q==bb[j]*aa[(((1-phi)*pow(phi,-1,n))*j)%n]%q for j in range(n))
        assert pred==(ab==ba)
    print('QUANDLE_PRODUCT_OK',n,q,zeta,phi)

def check_center():
    n,q=9,19
    zeta=next(z for z in range(2,q) if pow(z,n,q)==1 and all(pow(z,k,q)!=1 for k in range(1,n)))
    # Universal commuting center via linear equations (all v): u_j=0 on all non-fixed h-orbits.
    fixed=[j for j in range(n) if (-2*j)%n==j]
    assert len(fixed)==3 and fixed==[0,3,6]
    for j in range(n):
        a=[0]*n;a[j]=1
        is_center=all(a[i]==0 and a[(-2*i)%n]==0 for i in range(n) if (-2*i)%n!=i)
        assert is_center==(j in fixed)
    # General Alexander phi=2, T=(1-phi)/phi=4 mod 9; fixed chars 0,3,6.
    assert [j for j in range(n) if (((1-2*2)*j)%n)==0]==fixed
    print('CENTER_OK',n,q,len(fixed))

if __name__=='__main__':
    check_transfer()
    check_quandle_prime(5,11,3,4)
    check_quandle_prime(5,11,3,2)
    check_quandle_prime(5,11,3,3)
    check_quandle_prime(3,7,2,2) # 2 has order 3 modulo 7
    check_center()
    print('VERIFY_OK')
