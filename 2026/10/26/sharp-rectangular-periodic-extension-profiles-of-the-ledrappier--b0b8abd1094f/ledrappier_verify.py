#!/usr/bin/env python3
"""Exact GF(2) computations for rectangular periodic-extension theorem."""

def poly_rem(a, b):
    while a and a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length()-b.bit_length())
    return a

def poly_gcd(a, b):
    while b:
        a,b=b,poly_rem(a,b)
    return a

def poly_mul(a,b):
    r=0
    while b:
        if b&1:r^=a
        a<<=1
        b>>=1
    return r

def poly_div_exact(a,b):
    q=0
    while a and a.bit_length()>=b.bit_length():
        j=a.bit_length()-b.bit_length()
        a^=b<<j;q^=1<<j
    assert a==0
    return q

def poly_powmod(a,k,m):
    r=1
    while k:
        if k&1:r=poly_rem(poly_mul(r,a),m)
        a=poly_rem(poly_mul(a,a),m);k>>=1
    return r

def row_basis(n):
    mod=(1<<n)|1
    p=poly_powmod(3,n,mod)^1
    g=poly_gcd(mod,p)
    d=g.bit_length()-1
    h=poly_div_exact(mod,g)
    b=[h<<j for j in range(d)]
    assert all(x.bit_length()<=n for x in b)
    assert all(poly_rem(poly_mul(p,x),mod)==0 for x in b)
    return b,d

def rank_bitsets(vecs):
    piv={}
    for x in vecs:
        while x:
            j=x.bit_length()-1
            if j not in piv:
                piv[j]=x
                break
            x^=piv[j]
    return len(piv)

def patch(seed,n,w,h):
    out=0;cur=seed;mask=(1<<n)-1
    for y in range(h):
        for x in range(w):
            out|=((cur>>(x%n))&1)<<(y*w+x)
        cur^=((cur>>1)|((cur&1)<<(n-1)))
        cur&=mask
    return out

if __name__=='__main__':
    for n in range(1,35):
        basis,d=row_basis(n)
        if n<=16:
            for w in range(1, min(9,n+4)):
                for h in range(1,min(9,n+4)):
                    r=rank_bitsets([patch(f,n,w,h) for f in basis])
                    assert r==min(d,w+h-1),(n,d,w,h,r)
        if n&(n-1)==0:
            assert d==0
        if (n+1)&n==0:
            assert d==n-1
            # exactly the even-parity code, incl n=1
            assert all(f.bit_count()%2==0 for f in basis)
        if n<=10:
            good=[s for s in range(1<<n) if poly_rem(poly_mul(poly_powmod(3,n,(1<<n)|1)^1,s),(1<<n)|1)==0]
            assert len(good)==(1<<d)
            for w,h in [(1,1),(2,2),(1,n+1),(n+1,1),(4,6)]:
                assert len({patch(s,n,w,h) for s in good}) == 1<<min(d,w+h-1)
    print('VERIFY_OK: n=1..34; widths/heights through min(8,n+3) for n<=16; exhaustive n<=10 tests')
