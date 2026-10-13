#!/usr/bin/env python3
"""Exact checks for triangular-cactus maximal-independent-set spectral identity.
Python 3 standard library only. Finite tests supplement the proof, not replace it.
"""
from collections import Counter
from fractions import Fraction

def trim(p):
    while len(p)>1 and p[-1]==0:p.pop()
    return p

def plus(a,b):
    c=[0]*max(len(a),len(b))
    for j,v in enumerate(a):c[j]+=v
    for j,v in enumerate(b):c[j]+=v
    return trim(c)

def shift(a):return [0]+a

def add_sub(a,b,c):
    out=plus(a,b)
    return trim(plus(out,[-v for v in c]))

def gf_polys(N):
    out=[[1], [0,3], [0,1,4]]
    for n in range(3,N+1):out.append(plus(shift(out[n-1]),shift(out[n-2])))
    return out[:N+1]

def characteristic_polys(N):
    out=[[Fraction(1)], [Fraction(0),Fraction(1)]]
    for n in range(2,N+1):
        a=Fraction(1,4) if n==2 else Fraction(3,4) if n==3 else Fraction(1)
        out.append(add_sub(shift(out[n-1]),[0], [v*a for v in out[n-2]]))
    return out[:N+1]

def spectral_coeffs(C,n):
    # [z^{n-2k}] char(J_n) = (-1)^k p_{n,k}/4;
    # D_n(y) = y^n p_n(1/y).
    ans=[0]*(n+1)
    for k in range(n//2+1):
        val=4*(-1)**k*C[n-2*k]
        assert val.denominator==1 and val.numerator>=0,(n,k,val)
        ans[n-k]=val.numerator
    return trim(ans)

def weighted_matching_poly(n):
    # Matching-to-tiling bijection: a tile of length 1 (monomer) contributes
    # x and boundary multiplicity 2, a tile of length 2 (dimer) contributes x.
    assert n>=2
    memo={n:[1],n-1:[0,2]}  # suffix starting at n+1 empty; pos n endpoint monomer
    for pos in range(n-2,-1,-1):
        i=pos+1
        mono=shift([w*(2 if i==1 else 1) for w in memo[pos+1]])
        dimer=shift(memo[pos+2])
        memo[pos]=plus(mono,dimer)
    return memo[0]

def chain(n):
    edges=[]; v=0; idx=1
    for _ in range(n):
        a,b=idx,idx+1;idx+=2
        edges.extend([(v,a),(a,b),(b,v)])
        v=a
    return idx,edges

def exhaustive_poly(n):
    nv,edges=chain(n)
    adj=[0]*nv
    for a,b in edges:adj[a]|=1<<b;adj[b]|=1<<a
    hist=[0]*(nv+1)
    for mask in range(1<<nv):
        independ=True
        for u in range(nv):
            if mask>>u&1 and mask&adj[u]:independ=False;break
        if not independ:continue
        if all((mask>>u&1) or (mask&adj[u]) for u in range(nv)):
            hist[mask.bit_count()]+=1
    return trim(hist)

def run():
    gf=gf_polys(80)
    char=characteristic_polys(80)
    graph_instances=0;tested_subsets=0
    for n in range(2,81):
        assert all(char[n][k]==0 for k in range(n+1) if (n-k)%2)
        asserted=spectral_coeffs(char[n],n)
        assert gf[n]==asserted,(n,gf[n],asserted)
        tiled=weighted_matching_poly(n)
        assert gf[n]==tiled,(n,gf[n],tiled)
        assert min(k for k,v in enumerate(gf[n]) if v)>0
        assert min(k for k,v in enumerate(gf[n]) if v)==(n+1)//2
        assert gf[n][-1]==4
    for n in range(1,10):
        observed=exhaustive_poly(n)
        assert observed==gf[n],(n,observed,gf[n])
        graph_instances+=1;tested_subsets+=1<<(2*n+1)
    for n in range(2,11):
        print('n=%02d total=%d min_size=%d roots_nonzero=%d coefficients=%s' % (n,sum(gf[n]),(n+1)//2,n//2,gf[n]))
    print('VERIFY_OK exhaustive_instances=%d candidate_vertex_subsets=%d determinant_checks_n=2..80' % (graph_instances,tested_subsets))
if __name__=='__main__':run()
