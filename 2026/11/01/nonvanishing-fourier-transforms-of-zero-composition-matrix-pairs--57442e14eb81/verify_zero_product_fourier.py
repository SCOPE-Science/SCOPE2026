#!/usr/bin/env python3
"""Exact character checks for Fourier multipliers of finite-field zero-product pairs.

All arithmetic is integral; the ternary transform uses the basis (1, omega)
for Z[omega], omega**2+omega+1=0. No floating point arithmetic.
"""
from itertools import product


def mul(a, b, q):
    if q != 4:
        return a*b % q
    a0,a1=a&1,a>>1
    b0,b1=b&1,b>>1
    return ((a0*b0 ^ a1*b1) | ((a0*b1 ^ a1*b0 ^ a1*b1)<<1))


def contains_zero_product(x,y,a,b,q):
    # X has shape a x b and Y shape b x a; row-major digit order.
    for i in range(a):
        for j in range(a):
            s=0
            for k in range(b):
                s = (s ^ mul(x[i*b+k],y[k*a+j],q)) if q==4 else (s+mul(x[i*b+k],y[k*a+j],q))%q
            if s: return False
    return True


def build_indicator(a,b,q):
    m=a*b; N=q**m
    tables=[tuple((t//(q**j))%q for j in range(m)) for t in range(N)]
    f=[0]*(N*N)
    for x in range(N):
        xx=tables[x]
        for y in range(N):
            if contains_zero_product(xx,tables[y],a,b,q):
                f[x+N*y]=1
    return f


def fwht(f):
    a=f[:]; h=1; N=len(a)
    while h<N:
        for start in range(0,N,2*h):
            for j in range(start,start+h):
                x=a[j]; y=a[j+h]
                a[j]=x+y; a[j+h]=x-y
        h*=2
    return a


def ternary_dft_exact(f,axes):
    """DFT on F_3^axes in Z[omega], giving (integer,omega-coefficient)."""
    c0=f[:];c1=[0]*len(f); stride=1; N=len(f)
    for axis in range(axes):
        step=3*stride
        for start in range(0,N,step):
            for offset in range(stride):
                ids=[start+offset+j*stride for j in range(3)]
                a=[(c0[i],c1[i]) for i in ids]
                def mulw(t,k):
                    x,y=t
                    if k==0:return x,y
                    if k==1:return -y,x-y
                    return y-x,-x
                for out in range(3):
                    terms=[mulw(a[t],(out*t)%3) for t in range(3)]
                    c0[ids[out]]=sum(z[0] for z in terms)
                    c1[ids[out]]=sum(z[1] for z in terms)
        stride=step
    assert not any(c1), 'Nonintegral cyclotomic Fourier coefficient'
    return c0


def run(a,b,q):
    assert a>=b and q in (2,3,4)
    f=build_indicator(a,b,q)
    F=ternary_dft_exact(f,2*a*b) if q==3 else fwht(f)
    c=b*(b-1)//2
    residue=((-1)**b *q**c) % q**(c+1)
    assert len(F)==q**(2*a*b)
    assert all(x % q**(c+1) == residue for x in F)
    assert all(x != 0 for x in F)
    assert min(abs(x) for x in F) == q**c
    assert max(abs(x) for x in F) == sum(f)
    print('EXACT_OK', 'q',q,'a',a,'b',b,'ambient',len(f),'set_size',sum(f),
          'min_modulus',min(abs(x) for x in F),'unique_eigenvalues',len(set(F)))


if __name__ == '__main__':
    for spec in [(2,2,2),(3,2,2),(3,3,2),(2,2,3),(2,2,4)]:
        run(*spec)
    print('ALL_ZERO_PRODUCT_FOURIER_EXACT_TESTS_OK')
