#!/usr/bin/env python3
"""Exact finite checks for abundant integers of the form 2^a p^2 and phase statistics."""
from math import isqrt, log, sqrt

def sieve(N):
    p = bytearray(b'\x01') * (N + 1)
    p[0:2] = b'\x00\x00'
    for d in range(2, isqrt(N)+1):
        if p[d]:p[d*d::d] = b'\x00' * (((N-d*d)//d)+1)
    return p

def count_formula(X, isp=None):
    if isp is None:
        mx=0
        for a in range(1,X.bit_length()):
            q=X//(1<<a)
            if q<9: break
            mx=max(mx,min((1<<(a+1))-1,isqrt(q)))
        isp=sieve(mx+3)
    N = len(isp)-1
    pi = [0]*(N+1)
    for i in range(1,N+1):pi[i]=pi[i-1]+isp[i]
    total=0
    for a in range(1,X.bit_length()):
        q=X//(1<<a)
        if q<9: break
        top=min((1<<(a+1))-1,isqrt(q))
        if top>=3:total+=pi[top]-1
    return total

def main():
    bound=250000
    isp=sieve(isqrt(bound)+5)
    sigma=list(range(bound+1))
    # Exact divisor sum by divisors
    sigma=[0]*(bound+1)
    for d in range(1,bound+1):
        for k in range(d,bound+1,d): sigma[k]+=d
    good=[];bad=[]; cases=0
    for a in range(1,bound.bit_length()):
        pow2=1<<a
        if pow2*9>bound:break
        for p in range(3,isqrt(bound//pow2)+1,2):
            if not isp[p]:continue
            n=pow2*p*p
            actual=sigma[n]>2*n
            predicted=p<2*pow2
            assert actual==predicted,(n,a,p,actual,predicted)
            cases+=1
            if actual:good.append(n)
            else:bad.append(n)
    assert len(good)==count_formula(bound), (len(good),count_formula(bound))
    print('EXACT_CLASSIFICATION_OK', 'bound='+str(bound),'tested='+str(cases),'abundant='+str(len(good)),'deficient='+str(len(bad)), 'first='+str(sorted(good)[:12]))
    def phase(s):return 3*2**(1/3)*s**(-1/3)*(2+(1+sqrt(2))*sqrt(s))
    cmin=9*(1+sqrt(2))**(2/3)
    cmax=3*2**(1/3)*(3+sqrt(2))
    smin=16*(3-2*sqrt(2))
    assert 1<smin<8
    print('PHASE_CONSTANTS',f'smin={smin:.12f}',f'liminf={cmin:.12f}',f'limsup={cmax:.12f}',f'boundary={phase(1):.12f}/{phase(8):.12f}')
    for m in (8,11,14,17):
        for s in (1, smin, 7.9):
            X=int((1<<(3*m+2))*s)
            cnt=count_formula(X)
            normalized=cnt*log(X)/X**(1/3)
            print(f'PHASE_SAMPLE m={m:2d} s={s:.9f} count={cnt:8d} norm={normalized:.7f} expected={phase(s):.7f}')
if __name__=='__main__':main()
