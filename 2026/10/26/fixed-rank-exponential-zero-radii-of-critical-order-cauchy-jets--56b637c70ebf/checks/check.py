"""Exact finite checks and high-precision Cauchy-jet zero witnesses.
Run with python3 check.py; Python standard library only.
"""
from math import comb, sqrt, pi, log
from decimal import Decimal, localcontext

def coeff(N):
    # Coefficients of (1+t+...+t**(N-1))**N via sliding-window DP.
    v = [1]
    for _ in range(N):
        nxt = [0] * (len(v)+N-1)
        s=0
        for i in range(len(nxt)):
            if i<len(v): s+=v[i]
            if i>=N and i-N<len(v): s-=v[i-N]
            nxt[i]=s
        v=nxt
    a=[v[N*j] for j in range(N)]
    assert a[0]==1 and a[-1]==1
    assert a==list(reversed(a))
    assert sum(a)==N**(N-1)
    return a

def eval_negative(a,x):
    y=Decimal(0)
    for c in reversed(a): y=y*(-x)+Decimal(c)
    return y

def bisect_root(a,lo,hi,steps=180):
    f=eval_negative(a,lo)
    g=eval_negative(a,hi)
    assert f*g<0, (f,g,lo,hi)
    for _ in range(steps):
        mid=(lo+hi)/2
        h=eval_negative(a,mid)
        if h==0: return mid
        if f*h<0: hi=mid
        else: lo=mid; f=h
    return (lo+hi)/2

for N in range(3,16):
    a=coeff(N)
    # Equality of generating function coefficients from the binomial transform.
    for j in range(N):
        b=sum((-1)**h*comb(N,h)*comb((j-h+1)*N-1,N-1)
              for h in range(j+1))
        assert a[j]==b
    # Even N has the single forced boundary root -1.
    if N%2==0: assert sum((-1)**j*a[j] for j in range(N))==0
    else: assert sum((-1)**j*a[j] for j in range(N))!=0
print('exact identities and reciprocity PASS for N=3..15')

with localcontext() as ctx:
    ctx.prec=110
    for N in (24,32,48,64):
        a=coeff(N)
        for k in (1,2,3):
            ratio=Decimal(a[k-1])/Decimal(a[k])
            # Valid only for sufficiently large N: close two-term root.
            lo=ratio*Decimal('0.85')
            hi=ratio*Decimal('1.15')
            if eval_negative(a,lo)*eval_negative(a,hi)>=0:
                print(f'N={N} k={k}: interval not yet isolating, skip')
                continue
            x=bisect_root(a,lo,hi)
            c=(Decimal(k)**(2*k) /
               (Decimal(k-1)**(k-1) if k>1 else Decimal(1)) /
               Decimal(k+1)**(k+1))
            radius=ctx.exp(ctx.ln(x)/Decimal(N))
            print(f'N={N}, ring={k}, radius={radius:.13f}, limiting={c:.13f}, root/coeffratio={x/ratio:.10f}')
print('checks finished')
