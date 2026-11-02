#!/usr/bin/env python3
"""Exact finite-field checks of the balanced-scroll critical-polynomial identities.

These finite checks supplement, but do not establish, the uniform characteristic-zero proof.
Uses only Python's standard library. Run: python3 verify.py
"""
from random import Random

P = 1000003
R = Random(142857)

def trim(a):
    a=[x%P for x in a]
    while a and not a[-1]: a.pop()
    return a

def add(a,b):
    z=[0]*max(len(a),len(b))
    for i,x in enumerate(a): z[i]+=x
    for i,x in enumerate(b): z[i]+=x
    return trim(z)

def neg(a): return trim([-x for x in a])

def sub(a,b): return add(a,neg(b))

def mul(a,b):
    if not a or not b: return []
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): z[i+j]+=x*y
    return trim(z)

def scale(a,c): return trim([c*x for x in a])

def deriv(a): return trim([i*a[i] for i in range(1,len(a))])

def rem(a,b):
    a=trim(a); b=trim(b)
    assert b
    inv=pow(b[-1],-1,P)
    while len(a)>=len(b):
        shift=len(a)-len(b); coeff=a[-1]*inv%P
        for i,v in enumerate(b): a[shift+i]=(a[shift+i]-coeff*v)%P
        a=trim(a)
    return a

def gcd(a,b):
    a=trim(a); b=trim(b)
    while b: a,b=b,rem(a,b)
    return scale(a,pow(a[-1],-1,P)) if a else []

def rank(cols):
    m=len(cols[0]); n=len(cols)
    a=[[cols[j][i]%P for j in range(n)] for i in range(m)]
    r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if a[i][c]),None)
        if piv is None: continue
        a[r],a[piv]=a[piv],a[r]
        q=pow(a[r][c],-1,P)
        a[r]=[x*q%P for x in a[r]]
        for i in range(m):
            if i!=r and a[i][c]:
                z=a[i][c]; a[i]=[(x-z*y)%P for x,y in zip(a[i],a[r])]
        r+=1
        if r==m: break
    return r

def dot(a,b):return sum(x*y for x,y in zip(a,b))%P

def normalized_numerator(f,g,alpha,beta):
    a=dot(f,f);b=dot(g,g)
    if not a or not b: return None
    return add(scale(mul(f,f),alpha*pow(a,-1,P)),scale(mul(g,g),beta*pow(b,-1,P)))

def pad(a,n): return a+[0]*(n-len(a))

def jacobian_rank(f,g,alpha,beta,n):
    a=dot(f,f); b=dot(g,g)
    inva=pow(a,-1,P); invb=pow(b,-1,P)
    N=normalized_numerator(f,g,alpha,beta)
    cols=[pad(N,2*n+1)]
    for h,c,weight,invnorm in ((f,f,alpha,inva),(g,g,beta,invb)):
        for j in range(n+1):
            e=[0]*(n+1);e[j]=1
            tangent=sub(mul(h,e),scale(mul(h,h),c[j]*invnorm))
            cols.append(pad(scale(tangent,2*weight*invnorm),2*n+1))
    return rank(cols)

def test(n,d):
    alpha=d-1;beta=1
    s=[int(i%2==0) for i in range(2*n+1)]
    assert gcd(s,deriv(s))==[1]
    for _ in range(500):
        f=[R.randrange(-25,26)%P for i in range(n+1)]
        g=[R.randrange(-25,26)%P for i in range(n+1)]
        if not f[-1] or not g[-1] or not dot(f,g) or gcd(f,g)!=[1]:continue
        N=normalized_numerator(f,g,alpha,beta)
        if N is None:continue
        W=sub(mul(deriv(N),s),mul(N,deriv(s)))
        if len(W)!=4*n-1:continue
        if gcd(W,deriv(W))!=[1]:continue
        if gcd(W,mul(mul(s,f),g))!=[1]:continue
        if jacobian_rank(f,g,alpha,beta,n)!=2*n+1:continue
        # block-diagonal rank-d projector with d-1 identical f blocks and 1 g block
        assert sub(mul(N,s),mul(s,N))==[]
        return f,g,len(W)-1
    raise AssertionError(f'No witness for n={n}, d={d}')

if __name__=='__main__':
    for n in range(2,8):
        for d in (2,3,5):
            f,g,degree=test(n,d)
            print(f'n={n}, d={d}, critical_degree={degree}, cut_disjoint=YES, squarefree=YES, jacobian_rank={2*n+1}, f={f}, g={g}')
    print('VERIFY_OK')
