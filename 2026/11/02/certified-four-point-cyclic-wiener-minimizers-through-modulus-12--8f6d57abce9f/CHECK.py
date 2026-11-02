#!/usr/bin/env python3
"""Exact-integer exhaustive certificate for four-point cyclic Wiener minima (8 <= N <= 128).

Only NumPy integer arithmetic is used for finite-object comparisons. Floating sqrt
suggests an integer square root, which is corrected until exact integer inequalities
are verified. Trigonometric table entries are rigorously enclosed by rational
Taylor bounds; no floating-point estimate is used to declare a comparison.
"""
from fractions import Fraction as F
from itertools import combinations
from math import gcd, factorial, isqrt
import json, sys, time
import numpy as np

LIMIT=128
Q=100000000

def arctan_trunc(recip,terms=20):
    x=F(1,recip)
    return sum(((-1)**i*x**(2*i+1)/ (2*i+1) for i in range(terms)),F(0))

PI0=16*arctan_trunc(5)-4*arctan_trunc(239)
PIERR=F(16,41*5**41)+F(4,41*239**41)
assert 3<PI0<4 and PIERR<F(1,10**20)
TERR=F(4**40,factorial(40))
assert PIERR+TERR < F(1,2*Q)

def rnd_fraction(x):
    # exact floor(x+1/2) (including negative x)
    return (x.numerator*2+x.denominator)//(2*x.denominator)

def trig_table(N):
    # nearest integer to Q times sine/cosine of angle 2*pi*j/N
    # rigorous individual coordinate error < 1/Q.
    c=np.empty(N,dtype=np.int64)
    s=np.empty(N,dtype=np.int64)
    for j in range(N//2+1):
        x=2*PI0*F(j,N)
        x2=x*x
        sm=F(0);cm=F(0)
        tp_s=x; tp_c=F(1)
        for h in range(20):
            if h:
                tp_s=-tp_s*x2/F((2*h)*(2*h+1))
                tp_c=-tp_c*x2/F((2*h-1)*(2*h))
            sm+=tp_s;cm+=tp_c
        c[j]=rnd_fraction(Q*cm)
        s[j]=rnd_fraction(Q*sm)
    for j in range(N//2+1,N):
        c[j]=c[N-j];s[j]=-s[N-j]
    assert np.all(np.abs(c)<=Q) and np.all(np.abs(s)<=Q)
    # half-turn coordinate table is exact by elementary identity
    if N%2==0: c[N//2]=-Q;s[N//2]=0
    c[0]=Q;s[0]=0
    return c,s

def expected_sets(N):
    if N%4==0:
        return {tuple(sorted((0,N//4,N//2,3*N//4)))}
    if N%2==0:
        h=N//2
        return {tuple(sorted((0,h,d,d+h))) for d in range(1,h) if gcd(d,h)==1}
    out=set()
    for d in range(1,N):
        if gcd(d,N)!=1: continue
        for j in range(4):
            out.add(tuple(sorted(((k-j)*d)%N for k in range(4))))
    return out

def certified_root_floor(q):
    # q>=0 int64, q< 2^63, sqrt(q) <2^31
    w=np.sqrt(q.astype(np.float64)).astype(np.int64)
    bad=w*w>q
    while np.any(bad):
        w[bad]-=1
        bad=w*w>q
    bad=(w+1)*(w+1)<=q
    while np.any(bad):
        w[bad]+=1
        bad=(w+1)*(w+1)<=q
    assert np.all(w*w <= q) and np.all((w+1)*(w+1)>q)
    return w

def integer_score(A,c,s,N):
    k=np.arange(1,N,dtype=np.int64)
    X=sum((c[(k*a)%N] for a in A),np.zeros(N-1,dtype=np.int64))
    Y=sum((s[(k*a)%N] for a in A),np.zeros(N-1,dtype=np.int64))
    assert np.all(np.abs(X)<=4*Q) and np.all(np.abs(Y)<=4*Q)
    z=X*X+Y*Y
    assert np.all(z>=0)
    return int(certified_root_floor(z).sum())

def verify_N(N,batch=2048):
    c,s=trig_table(N)
    expected=expected_sets(N)
    canonical=next(iter(expected))
    # verify every predicted minimum equals canonical exactly by translation
    # and dilation symmetries; the code checks only one representative value.
    ref=integer_score(canonical,c,s,N)
    k=np.arange(1,N,dtype=np.int64)[:,None]
    tests=0
    lowest_other=None
    min_margin=None
    count_expected=0
    # Every subset is translation-equivalent to a set anchored at zero.
    C=list(combinations(range(1,N),3))
    for i in range(0,len(C),batch):
        T=np.asarray(C[i:i+batch],dtype=np.int64)
        # every table index is in [0,N-1]; Q*4 <=4e8 hence squared norm <= 3.2e17
        idx1=k*T[:,0];idx2=k*T[:,1];idx3=k*T[:,2]
        x=c[0]+c[idx1%N]+c[idx2%N]+c[idx3%N]
        y=s[0]+s[idx1%N]+s[idx2%N]+s[idx3%N]
        assert np.all(np.abs(x)<=4*Q) and np.all(np.abs(y)<=4*Q)
        zz=x*x+y*y
        assert np.all(zz>=0)
        w=certified_root_floor(zz)
        totals=w.sum(axis=0,dtype=np.int64)
        for j,ab in enumerate(T):
            A=(0,int(ab[0]),int(ab[1]),int(ab[2]))
            if A in expected:
                count_expected+=1
            else:
                margin=int(totals[j])-ref
                if min_margin is None or margin<min_margin: min_margin=margin;lowest_other=A
                # true score non-expected >= (total-6*(N-1))/Q.
                # candidate true score <= (ref+7*(N-1))/Q.
                # strict verified separation when margin > 13*(N-1).
                assert margin>13*(N-1), f'not certified N={N}, set={A}, margin={margin}'
            tests+=1
    assert count_expected==len(expected), (N,count_expected,len(expected))
    assert tests==(N-1)*(N-2)*(N-3)//6
    return dict(N=N, candidate_score_units=ref, candidates_anchored=len(expected), others_checked=tests-len(expected), separation_margin_units=min_margin,
                closest_nonminimum=lowest_other, certificate_min_gap_lower=float(F(min_margin-13*(N-1),Q)) if min_margin is not None else None)

def main():
    start=time.monotonic();results=[]
    lower=int(sys.argv[1]) if len(sys.argv)>1 else 8
    upper=int(sys.argv[2]) if len(sys.argv)>2 else LIMIT
    assert 8<=lower<=upper<=LIMIT
    for N in range(lower,upper+1):
        res=verify_N(N)
        results.append(res)
        if N%10==0 or N==LIMIT:
            print('VERIFIED_TO',N,'elapsed',round(time.monotonic()-start,2),flush=True)
    assert len(results)==upper-lower+1
    assert all(r['separation_margin_units']>13*(r['N']-1) for r in results)
    summary={'range':[lower,upper],'limit':LIMIT,'moduli_checked':len(results),'subsets_anchored_checked':sum(r['others_checked']+r['candidates_anchored'] for r in results),
       'nonminimum_subsets_anchored':sum(r['others_checked'] for r in results),
       'min_verified_gap_lower':min(r['certificate_min_gap_lower'] for r in results),
       'min_gap_modulus':min(results,key=lambda r:r['certificate_min_gap_lower'])['N'],
       'q':Q,'all_separations_exact_integer':True,'seconds':round(time.monotonic()-start,2)}
    print('CHECK_OK',json.dumps(summary,sort_keys=True),flush=True)
    if len(sys.argv)>3:
        with open(sys.argv[3],'w',encoding='utf8') as f:json.dump({'summary':summary,'results':results},f,indent=2)
if __name__=='__main__': main()
