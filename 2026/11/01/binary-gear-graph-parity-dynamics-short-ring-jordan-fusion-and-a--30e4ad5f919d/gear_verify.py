#!/usr/bin/env python3
"""Reproducible exact binary linear algebra for synchronous open-neighborhood updating on gear graphs.
Python 3 standard library only. No external datasets.
"""
from math import gcd

def gf2_deg(x):
    return x.bit_length()-1

def gf2_mod(a,b):
    assert b
    while a and gf2_deg(a)>=gf2_deg(b):
        a ^= b<<(gf2_deg(a)-gf2_deg(b))
    return a

def gf2_div(a,b):
    q=0
    while a and gf2_deg(a)>=gf2_deg(b):
        j=gf2_deg(a)-gf2_deg(b)
        q^=1<<j
        a^=b<<j
    assert a==0
    return q

def gf2_gcd(a,b):
    while b:
        a,b=b,gf2_mod(a,b)
    return a

def gf2_mul(a,b):
    s=0
    while b:
        if b&1:s^=a
        b>>=1;a<<=1
    return s

def gf2_pow(a,e):
    r=1
    while e:
        if e&1:r=gf2_mul(r,a)
        a=gf2_mul(a,a);e>>=1
    return r

def v2(n):
    return (n&-n).bit_length()-1

def poly_H(n):
    e=1<<v2(n)
    return gf2_div((1<<n)|1, gf2_pow(3,e))

def fix_dimension(n,t):
    H=poly_H(n)
    k=t if t%2 else t//2
    p=gf2_pow(5,k)^(1<<k)  # (X^2+1)^k + X^k over F2
    q=gf2_deg(gf2_gcd(H,p))
    hub = (1 if t%2 else 2) if n%2 else 0
    return hub + (q if t%2 else 2*q)

def nil_lengths(n):
    e=1<<v2(n)
    if n%2:return (1,)
    if e==2:return (3,1,1)
    return (e,e,1)

def periodic_dimension(n):
    e=1<<v2(n)
    return 2*n if n%2 else 2*n-2*e

def entry_by(n,t):
    return 1 << (periodic_dimension(n) + sum(min(t,j) for j in nil_lengths(n)))

def gear_matrix(n):
    d=2*n+1; M=[0]*d
    for i in range(n):
        M[0] ^= (1<<(1+i))
        M[1+i] ^= (1<<0)|(1<<(1+n+i))|(1<<(1+n+(i-1)%n))
        M[1+n+i] ^= (1<<(1+i))|(1<<(1+(i+1)%n))
    return M

def gf2_rank(rows):
    piv={}
    for y in rows:
        while y:
            k=y.bit_length()-1
            if k in piv:y ^= piv[k]
            else:piv[k]=y;break
    return len(piv)

def prod_rows(A,B):
    out=[]
    for row in A:
        w=0
        while row:
            b=row&-row;w ^= B[b.bit_length()-1];row^=b
        out.append(w)
    return out

def act(A,x):
    z=0
    for j,r in enumerate(A):
        if (r&x).bit_count()&1:z |= 1<<j
    return z

def empirical_entry_and_fixes(n,tmax=15):
    A=gear_matrix(n);d=len(A);ident=[1<<i for i in range(d)]
    cur=ident
    seen_ranks=[]
    for t in range(max(tmax,1<<v2(n))+5):
        rank=gf2_rank(cur)
        seen_ranks.append(rank)
        predicted_null=sum(min(t,j) for j in nil_lengths(n))
        assert d-rank == predicted_null,(n,t,rank,predicted_null)
        cur=prod_rows(A,cur)
    cur=ident
    for t in range(1,tmax+1):
        cur=prod_rows(A,cur)
        dims=d-gf2_rank([r^(1<<i) for i,r in enumerate(cur)])
        assert dims==fix_dimension(n,t),(n,t,dims,fix_dimension(n,t))
    return len(seen_ranks), tmax

def exhaustive_direct(n):
    A=gear_matrix(n); d=len(A);total=1<<d
    max_depth=max(nil_lengths(n))
    # Check membership of a periodic state x by equality F^t(x)=x for some t <= number of nonzero states.
    # Use the matrix-periodic-image rank property: F^max_depth(x) lies in the eventual image;
    # for each x iterate trajectory until it repeats, count the entry index and period.
    depths={}; fixes={t:0 for t in (1,2,3,4,6,8)}
    for x in range(total):
        loc={};z=x
        while z not in loc:
            loc[z]=len(loc)
            z=act(A,z)
        depth=loc[z];period=len(loc)-depth
        depths[depth]=depths.get(depth,0)+1
        for t in fixes:
            if depth==0 and t%period==0:fixes[t]+=1
    cum=0
    for t in range(max_depth+1):
        cum+=depths.get(t,0)
        assert cum==entry_by(n,t),(n,t,cum,entry_by(n,t))
    for t,v in fixes.items():
        assert v==(1<<fix_dimension(n,t)),(n,t,v,fix_dimension(n,t))
    return len(depths),sum(fixes.values())

if __name__=='__main__':
    matrix_tests=0;fixed_tests=0
    for n in range(3,65):
        p,f=empirical_entry_and_fixes(n,tmax=32)
        matrix_tests+=p;fixed_tests+=f
    exhaustive_states=0
    for n in range(3,9):
        exhaustive_direct(n)
        exhaustive_states+=(1<<(2*n+1))
    print('VERIFY_OK')
    print('all_n=3..64')
    print('rank_tests=',matrix_tests)
    print('return_time_tests=',fixed_tests)
    print('exhaustive_states=',exhaustive_states)
    for n in (3,4,5,6,7,8,9,10,12,14,16):
        print('n',n,'nil',nil_lengths(n),'periodic',1<<periodic_dimension(n),'fixed_t1_t2_t3',*[1<<fix_dimension(n,t) for t in (1,2,3)])
