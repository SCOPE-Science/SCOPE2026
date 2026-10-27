#!/usr/bin/env python3
"""Exact rank and zero-product checks for finite cyclic Alexander quandle algebras.

No external packages.  Enumerates every coefficient vector for small primes,
calculates left/right multiplication matrices from the defining quandle table,
then checks the Frobenius-orbit rank enumerators and zero-product count.
"""
from itertools import product
from collections import Counter
from math import gcd

def matrix_rank(mat, p):
    if not mat:
        return 0
    a=[row[:] for row in mat]
    n,m=len(a),len(a[0]); r=0
    for c in range(m):
        piv=next((i for i in range(r,n) if a[i][c]%p),None)
        if piv is None: continue
        a[r],a[piv]=a[piv],a[r]
        inv=pow(a[r][c],-1,p)
        a[r]=[(v*inv)%p for v in a[r]]
        for i in range(r+1,n):
            if a[i][c]:
                fac=a[i][c]
                a[i]=[(v-fac*w)%p for v,w in zip(a[i],a[r])]
        r+=1
        if r==n: break
    return r

def multiplication_matrix(u,n,p,a,left):
    mat=[[0]*n for _ in range(n)]
    if left:
        for y in range(n):
            for x,c in enumerate(u):
                z=(a*x+(1-a)*y)%n
                mat[z][y]=(mat[z][y]+c)%p
    else:
        for x in range(n):
            for y,c in enumerate(u):
                z=(a*x+(1-a)*y)%n
                mat[z][x]=(mat[z][x]+c)%p
    return mat

def orbit_profile(n,p,a):
    f=gcd(n,1-a)
    B={(1-a)*x%n for x in range(n)}
    assert len(B)*f==n
    lengths=[]
    while B:
        start=next(iter(B)); orbit=[];k=start
        while k not in orbit:
            orbit.append(k);k=p*k%n
        assert k==start
        assert set(orbit)<=B
        B-=set(orbit); lengths.append(len(orbit))
    return f, lengths

def polynomial_factor_product(factors):
    v=Counter({0:1})
    for exp,w in factors:
        nxt=Counter()
        for deg,coeff in v.items():
            nxt[deg]+=coeff; nxt[deg+exp]+=coeff*w
        v=nxt
    return {i:x for i,x in v.items() if x}

def predicted(n,p,a):
    f,ds=orbit_profile(n,p,a)
    r=n//f
    left=polynomial_factor_product([(d,p**(f*d)-1) for d in ds])
    right={k:v*p**(n-r) for k,v in polynomial_factor_product([(f*d,p**d-1) for d in ds]).items()}
    pairs=p**(n-r)
    for d in ds: pairs*=p**d+p**(f*d)-1
    return left,right,pairs,ds,f

def check(n,p,a):
    assert gcd(n,p)==gcd(n,a)==1
    lpred,rpred,zpred,ds,f=predicted(n,p,a)
    assert sum(lpred.values())==sum(rpred.values())==p**n
    actual_l=Counter(); actual_r=Counter();z=0
    for vec in product(range(p),repeat=n):
        lr=matrix_rank(multiplication_matrix(vec,n,p,a,True),p)
        rr=matrix_rank(multiplication_matrix(vec,n,p,a,False),p)
        actual_l[lr]+=1; actual_r[rr]+=1
        z+=p**(n-lr)
    assert dict(actual_l)==lpred,(n,p,a,'left',actual_l,lpred)
    assert dict(actual_r)==rpred,(n,p,a,'right',actual_r,rpred)
    assert z==zpred,(n,p,a,'zero products',z,zpred)
    print('OK',dict(n=n,p=p,a=a,f=f,orbits=ds,left=lpred,right=rpred,zero_pairs=z))

def gf4_mul(a,b):
    # F_2[t]/(t^2+t+1); coefficients are two-bit vectors.
    r=0
    for j in range(2):
        if (b>>j)&1: r^=a<<j
    if r&8:r^=0b1110
    if r&4:r^=0b111
    return r

def gf4_rank(mat):
    a=[row[:] for row in mat]
    n,m=len(a),len(a[0]);r=0
    for col in range(m):
        pivot=next((k for k in range(r,n) if a[k][col]),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        inverse=next(b for b in range(1,4) if gf4_mul(a[r][col],b)==1)
        a[r]=[gf4_mul(t,inverse) for t in a[r]]
        for i in range(r+1,n):
            t=a[i][col]
            if t:a[i]=[v^gf4_mul(t,w) for v,w in zip(a[i],a[r])]
        r+=1
        if r==n:break
    return r

def matrix_gf4(u,n,a,left):
    mat=[[0]*n for _ in range(n)]
    if left:
        for y in range(n):
            for x,c in enumerate(u):mat[(a*x+(1-a)*y)%n][y]^=c
    else:
        for x in range(n):
            for y,c in enumerate(u):mat[(a*x+(1-a)*y)%n][x]^=c
    return mat

def check_gf4(n,a):
    lpred,rpred,zpred,ds,f=predicted(n,4,a)
    left=Counter();right=Counter();z=0
    for u in product(range(4),repeat=n):
        rl=gf4_rank(matrix_gf4(u,n,a,True));rr=gf4_rank(matrix_gf4(u,n,a,False))
        left[rl]+=1;right[rr]+=1;z+=4**(n-rl)
    assert dict(left)==lpred,(n,a,left,lpred)
    assert dict(right)==rpred,(n,a,right,rpred)
    assert z==zpred,(n,a,z,zpred)
    print('OK_GF4',dict(n=n,a=a,f=f,orbits=ds,zero_pairs=z))

def check_c3_square(p,a,b):
    # A=C_3 x C_3; diagonal automorphism (a,b), where a,b in {1,2}.
    points=list(product(range(3),repeat=2)); n=9
    multiplication=[[0]*n for _ in range(n)]
    for i,x in enumerate(points):
        for j,y in enumerate(points):
            z=((a*x[0]+(1-a)*y[0])%3,(b*x[1]+(1-b)*y[1])%3)
            multiplication[i][j]=points.index(z)
    image={( (1-a)*x[0]%3,(1-b)*x[1]%3) for x in points}
    f=n//len(image)
    lengths=[]
    while image:
        x=next(iter(image));now=x;orbit=[]
        while now not in orbit:
            orbit.append(now)
            now=tuple(p*z%3 for z in now)
        assert now==x
        image-=set(orbit);lengths.append(len(orbit))
    r=n//f
    lp=polynomial_factor_product([(d,p**(f*d)-1) for d in lengths])
    rp={j:val*p**(n-r) for j,val in polynomial_factor_product([(f*d,p**d-1) for d in lengths]).items()}
    zp=p**(n-r)
    for d in lengths:zp*=p**d+p**(f*d)-1
    la=Counter();ra=Counter();za=0
    for u in product(range(p),repeat=n):
        left=[[0]*n for _ in range(n)];right=[[0]*n for _ in range(n)]
        for i,c in enumerate(u):
            if not c:continue
            for j in range(n):
                left[multiplication[i][j]][j]=(left[multiplication[i][j]][j]+c)%p
                right[multiplication[j][i]][j]=(right[multiplication[j][i]][j]+c)%p
        l=matrix_rank(left,p);rnk=matrix_rank(right,p)
        la[l]+=1;ra[rnk]+=1;za+=p**(n-l)
    assert dict(la)==lp,(a,b,la,lp)
    assert dict(ra)==rp,(a,b,ra,rp)
    assert za==zp,(a,b,za,zp)
    print('OK_C3_SQUARED',dict(p=p,a=a,b=b,f=f,orbits=lengths,left=lp,right=rp,zero_pairs=za))

if __name__=='__main__':
    for args in [(1,2,1),(3,2,2),(4,3,1),(4,3,3),(5,2,2),(5,2,4),(5,3,2),(6,5,5),(7,2,3),(9,2,8)]:
        if args==(6,5,5):
            n,p,a=args; lp,rp,z,ds,f=predicted(n,p,a)
            assert sum(lp.values())==sum(rp.values())==p**n
            print('FORMULA_ONLY',dict(n=n,p=p,a=a,f=f,orbits=ds,zero_pairs=z))
        else: check(*args)
    for n,a in [(3,2),(5,2),(5,4)]:check_gf4(n,a)
    for a,b in [(2,2),(1,2),(1,1)]:check_c3_square(2,a,b)
    print('VERIFY_OK')
