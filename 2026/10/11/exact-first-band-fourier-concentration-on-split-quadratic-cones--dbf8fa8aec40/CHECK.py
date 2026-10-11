#!/usr/bin/env python3
"""Reproduce finite-field Fourier and exact block identities for the split quadratic cone.

Requires Python 3 standard library only.  This is corroboration; unrestricted
prime-power and dimension statements follow from the character-sum proof.
"""
import cmath
from fractions import Fraction as Q
from itertools import product
from math import pi, sqrt


def frequency_set(q, m):
    n = 2*m
    E = [tuple([0]*n)]
    for i in range(n):
        for a in range(1, q):
            x = [0]*n; x[i] = a; E.append(tuple(x))
    return E


def predicted_matrix(q, m, E):
    a = Q(1,q); b = Q(q-1,q**(m+1)); c = Q(1,q**m)
    K = []
    for i, s in enumerate(E):
        row=[]
        for j, t in enumerate(E):
            paired = any((s[h]-t[h])%q and (s[m+h]-t[m+h])%q for h in range(m))
            row.append((a if i == j else 0)+b-(c if paired else 0))
        K.append(row)
    return K


def direct_gram(q,m,E):
    n=2*m
    accum=[[0j]*len(E) for _ in E]
    for z in product(range(q),repeat=n):
        if sum(z[j]*z[m+j] for j in range(m))%q: continue
        vals=[cmath.exp(2j*pi*sum(e[k]*z[k] for k in range(n))/q) for e in E]
        for i in range(len(E)):
            for j in range(len(E)):
                accum[i][j]+=vals[j]*vals[i].conjugate()
    denom=q**n
    return [[v/denom for v in row] for row in accum]


def mm(K, v):
    return [sum(K[i][j]*v[j] for j in range(len(v))) for i in range(len(v))]


def exact_blocks(q,m,E,K):
    N=len(E); r=q-1; a=Q(1,q); c=Q(1,q**m); b=r*c/q
    L=2*m*r
    assert N==L+1
    assert sum(K[i][i] for i in range(N))==N*(a+b)
    # The zero-frequency basis and the normalized sum of all nonzero basis
    # vectors span the single 2x2 exceptional block.
    v0=[0]*N; v0[0]=1
    vu=[0]+[1]*(N-1)
    K0=mm(K,v0); Ku=mm(K,vu)
    assert K0[0]==a+b and all(K0[j]==b for j in range(1,N))
    assert Ku[0]==b*L and all(Ku[j]==a-r*c+b*L for j in range(1,N))
    # q-1 label contrasts: 2m blocks, each of dimension q-2.
    contrast=0
    for block in range(2*m):
        first=1+block*r
        for k in range(1,r):
            v=[0]*N;v[first]=1;v[first+k]=-1
            assert mm(K,v)==[a*x for x in v]
            contrast+=1
    assert contrast==2*m*(q-2)
    # Partner anti-symmetries (one for each x-y pair).
    for h in range(m):
        v=[0]*N
        for j in range(r):
            v[1+h*r+j]=1;v[1+(m+h)*r+j]=-1
        assert mm(K,v)==[(a+r*c)*x for x in v]
    # Differences of pairs among the symmetric partner modes.
    for h in range(1,m):
        v=[0]*N
        for j in range(r):
            for block, sign in ((h,1),(m+h,1),(0,-1),(m,-1)):
                v[1+block*r+j]=sign
        assert mm(K,v)==[(a-r*c)*x for x in v]
    # Characteristic polynomial of the exact 2x2 compression in the
    # orthonormal basis (e_0, L^-1/2 1_{E\\{0}}).
    trace=2*a-r*c+b*(1+L)
    det=(a+b)*(a-r*c+b*L)-b*b*L
    disc=trace*trace-4*det
    assert disc>0
    lam_lo=(float(trace)-sqrt(float(disc)))/2
    lam_hi=(float(trace)+sqrt(float(disc)))/2
    if m==1:
        assert trace==1+Q(1,q*q) and det==Q(1,q*q)
    else:
        assert 0<float(a-r*c)<lam_lo<float(a)<float(a+r*c)<lam_hi<1
    # Dimension check for full spectral decomposition.
    assert 2+m+(m-1)+2*m*(q-2)==N
    return lam_lo,lam_hi


def run():
    total=0; peak=0
    for q,m in ((3,1),(3,2),(3,3),(5,1),(5,2),(7,1),(7,2),(11,1)):
        E=frequency_set(q,m)
        K=predicted_matrix(q,m,E)
        lo,hi=exact_blocks(q,m,E,K)
        D=direct_gram(q,m,E)
        err=max(abs(D[i][j]-complex(K[i][j])) for i in range(len(E)) for j in range(len(E)))
        assert err<1e-12,(q,m,err)
        total+=len(E)**2;peak=max(peak,err)
        print(f'q={q} m={m} dim={len(E)} lambda_min2={lo:.12g} lambda_max={hi:.12g} Gram_error={err:.2e}')
    print(f'VERIFY_OK prime_field_cases=8 Fourier_matrix_entries={total} complete_block_decompositions=8 max_error={peak:.3e}')

if __name__ == '__main__': run()
