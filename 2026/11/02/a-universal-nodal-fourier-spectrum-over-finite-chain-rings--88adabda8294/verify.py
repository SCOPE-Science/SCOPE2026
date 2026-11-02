#!/usr/bin/env python3
"""Exact cyclotomic verification of Fourier spectra of modular nodal cones."""
from collections import Counter
from math import isqrt

def valuation(x,p,k):
    if x == 0:return k
    t=0
    while x % p == 0:
        t+=1;x//=p
    return t

def formula(p,k,u,v):
    a,b=valuation(u,p,k),valuation(v,p,k)
    z=p**(k-1)
    if a==k and b==k:return z*(p+k*(p-1))
    if a==k:return z*(p-1)*(b+1)
    if b==k:return z*(p-1)*(a+1)
    s=a+b
    if s<k-1:return 0
    return z*((p-1)*(s-k+1)-1)

def exact_cyclotomic_eval(exps,p,k):
    N=p**k; Q=N//p
    hist=[0]*N
    for r in exps:hist[r%N]+=1
    c=[0]*N
    for r in range(Q):
        base=hist[r+(p-1)*Q]
        for j in range(p-1):c[r+j*Q]=hist[r+j*Q]-base
    if any(c[1:]):raise AssertionError(('noninteger Fourier coefficient',c))
    return c[0]

def test(p,k):
    N=p**k
    cone=[(x,y) for x in range(N) for y in range(N) if x*y%N==0]
    got=Counter();pred=Counter()
    for u in range(N):
        for v in range(N):
            claimed=formula(p,k,u,v)
            val=exact_cyclotomic_eval(((u*x+v*y)%N for x,y in cone),p,k)
            if val!=claimed:raise AssertionError((p,k,u,v,val,claimed))
            got[val]+=1;pred[claimed]+=1
    assert got==pred
    assert got[0]==N*N - (N*(1+k*(p-1)) - ((k-1)*2**(k-2) if p==2 and k>=2 else 0))
    if p==2:
        expected=N*(k+1)-(k-1)*2**(k-2) if k>=2 else N*(k+1)
    else:expected=N*(1+k*(p-1))
    assert N*N-got[0]==expected
    negcount=k*(p-1)**2 *p**(k-1)
    assert sum(m for e,m in got.items() if e<0)==negcount
    assert len(cone)==p**(k-1)*(p+k*(p-1))
    assert sum(e*m for e,m in got.items())==N*N # trace sum = |G| * indicator(0) = N²
    print(f'EXACT_CYCLOTOMIC_PASS p={p} k={k} N={N} cone={len(cone)} rank={expected} zero={got[0]} negative={negcount} levels={len(got)}')

if __name__=='__main__':
    for p,k in [(2,1),(2,2),(2,3),(2,4),(2,5),(3,1),(3,2),(3,3),(5,1),(5,2),(7,1)]:test(p,k)
    print('NODAL_FOURIER_EXACT_CERTIFICATE_OK')

def test_truncated_polynomial_ring(p,k):
    # F_p[t]/(t^k) with the coefficient-at-t^(k-1) generating character.
    Q=p**k
    def digits(x):
        out=[]
        for _ in range(k):out.append(x%p);x//=p
        return out
    ds=[digits(i) for i in range(Q)]
    def mul(u,v):
        A=ds[u];B=ds[v];C=[sum(A[i]*B[j-i] for i in range(j+1))%p for j in range(k)]
        return sum(c*p**j for j,c in enumerate(C))
    def val(x):
        for j,c in enumerate(ds[x]):
            if c:return j
        return k
    cone=[(x,y) for x in range(Q) for y in range(Q) if mul(x,y)==0]
    for u in range(Q):
        for v in range(Q):
            hist=[0]*p
            for x,y in cone:
                s=(ds[mul(u,x)][-1]+ds[mul(v,y)][-1])%p
                hist[s]+=1
            assert len(set(hist[1:]))==1,(p,k,u,v,hist)
            exact=hist[0]-hist[1] if p>1 else hist[0]
            a,b=val(u),val(v)
            z=p**(k-1)
            if a==k and b==k:claimed=z*(p+k*(p-1))
            elif a==k:claimed=z*(p-1)*(b+1)
            elif b==k:claimed=z*(p-1)*(a+1)
            elif a+b<k-1:claimed=0
            else:claimed=z*((p-1)*(a+b-k+1)-1)
            assert exact==claimed,(p,k,u,v,exact,claimed)
    print(f'TRUNCATED_POLYNOMIAL_RING_OK q={p} length={k} ring_card={Q} cone={len(cone)}')

def test_gf4_dual_numbers():
    # GF(4)=F2[a]/(a^2+a+1). Ring GF(4)[t]/(t^2).
    def fm(x,y):
        a0,a1=x&1,x>>1;b0,b1=y&1,y>>1
        return ((a0*b0+a1*b1)&1) | (((a0*b1+a1*b0+a1*b1)&1)<<1)
    def tr(x):return (x>>1)&1
    def mul(x,y):
        x0,x1=x&3,x>>2;y0,y1=y&3,y>>2
        return fm(x0,y0) | ((fm(x0,y1)^fm(x1,y0))<<2)
    def val(x):return 2 if not x else 1 if (x&3)==0 else 0
    Q=16;p=4;k=2;cone=[(x,y) for x in range(Q) for y in range(Q) if mul(x,y)==0]
    counts={}
    for u in range(Q):
        for v in range(Q):
            value=sum(1 if (tr(mul(u,x)>>2)^tr(mul(v,y)>>2))==0 else -1 for x,y in cone)
            a,b=val(u),val(v)
            z=p
            if a==k and b==k:claimed=z*(p+k*(p-1))
            elif a==k:claimed=z*(p-1)*(b+1)
            elif b==k:claimed=z*(p-1)*(a+1)
            elif a+b<k-1:claimed=0
            else:claimed=z*((p-1)*(a+b-k+1)-1)
            assert value==claimed,(u,v,value,claimed)
            counts[value]=counts.get(value,0)+1
    assert Q*Q-counts.get(0,0)==Q*(1+k*(p-1))
    print('GF4_DUAL_NUMBERS_OK q=4 length=2 ring_card=16 rank=112')

if __name__=='__main__':
    for p,k in [(2,2),(2,3),(2,4),(3,2),(3,3)]:test_truncated_polynomial_ring(p,k)
    test_gf4_dual_numbers()
    print('CHAIN_RING_SPECTRUM_UNIVERSALITY_OK')
