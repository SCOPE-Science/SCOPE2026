#!/usr/bin/env python3
"""Exact CRT weights and weighted-cycle optimization for divisor sums."""
from math import gcd

def factor(n):
    out=[];p=2
    while p*p<=n:
        if n%p==0:
            a=0
            while n%p==0: n//=p;a+=1
            out.append((p,a))
        p+=1
    if n>1: out.append((n,1))
    return out

def scaled_weights(m):
    fs=factor(m); den=1
    for p,a in fs:den*=p**(a+1)
    W=[]
    for r in range(m):
        z=1
        for p,a in fs:
            if r%p**a==0: z*=(a+1)*p-a
            else:
                e=0;s=r
                while s%p==0:e+=1;s//=p
                z*=(e+1)*(p-1)
        W.append(z)
    assert sum(W)==den, (m,sum(W),den)
    return W,den

def cycle_opt(weights, backtrace=False):
    m=len(weights)
    if m==1:return 0,[]
    B=(-1,[])
    for first in (0,1):
        dp={(first):(weights[0]*first,[0] if first else [])}
        for i in range(1,m):
            nxt={}
            for old,(val,sel) in dp.items():
                for bit in (0,1):
                    if old and bit:continue
                    if i==m-1 and bit and first:continue
                    v=val+bit*weights[i]
                    if bit not in nxt or v>nxt[bit][0]:
                        nxt[bit]=(v,sel+[i] if bit else sel)
            dp=nxt
        cand=max(dp.values(),key=lambda x:x[0]);
        if cand[0]>B[0]:B=cand
    return B

def brute_cycle(weights):
    n=len(weights)
    best=0
    for mask in range(1<<n):
        if any(((mask>>i)&1) and ((mask>>((i+1)%n))&1) for i in range(n)):
            continue
        score=sum(w for i,w in enumerate(weights) if mask>>i&1)
        if score>best:best=score
    return best

if __name__ == '__main__':
    from fractions import Fraction
    vals=[]
    for m in range(1,91):
        weights,den=scaled_weights(m)
        num,sel=cycle_opt(weights)
        assert num==sum(weights[r] for r in sel)
        assert all((r+1)%m not in sel and (r-1)%m not in sel for r in sel)
        if m<=15: assert brute_cycle(weights)==num
        vals.append((m,num,den))
        if m<90:assert 4*num<=3*den, (m,num,den)
    m,num,den=vals[-1]
    assert m==90 and Fraction(num,den)==Fraction(34,45)
    weights,den=scaled_weights(90)
    num,selected=cycle_opt(weights)
    parity=sum(weights[r] for r in range(0,90,2))
    assert den==2700 and parity==2025 and num==2040
    assert (set(range(0,90,2))-set(selected))=={44,46}
    assert set(selected)-set(range(0,90,2))=={45}
    assert weights[45]==63 and weights[44]==weights[46]==24
    import pathlib
    location=pathlib.Path(__file__).parent/'values_through_90.tsv'
    expected='modulus\tinteger_optimum\tinteger_denominator\n'+''.join(f'{m}\t{n}\t{d}\n' for m,n,d in vals)
    if location.exists(): assert location.read_text(encoding='utf8')==expected
    else:location.write_text(expected,encoding='utf8')
    print('VERIFY_OK checked_moduli=90 direct_bruteforce_moduli=15 first_excess=90 alpha90=34/45')
    print('parity=3/4 exact_gain=1/180 witness_exchange=remove_44_46_add_45')
