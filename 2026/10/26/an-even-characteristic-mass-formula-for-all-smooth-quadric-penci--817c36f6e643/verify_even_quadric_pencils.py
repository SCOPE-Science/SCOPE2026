#!/usr/bin/env python3
"""Exact finite-field checks for smooth quadric-pencil enumeration in characteristic 2.
Independent finite-field enumeration of Pfaffian-anisotropic planes (q=2,4)
and the canonical coefficient-discriminant tally (K=F4,F16).
No external dependencies.
"""
from itertools import product


def mul(a,b,m,poly):
    z=0
    while b:
        if b&1: z^=a
        b>>=1
        a<<=1
        if a & (1<<m): a ^=poly
    return z


def projective_points(q):
    for first in range(6):
        for tail in product(range(q),repeat=5-first):
            yield (0,)*first+(1,)+tail


def qpf(v, mult):
    return mult[v[0]][v[5]]^mult[v[1]][v[4]]^mult[v[2]][v[3]]


def anisotropic_planes(q):
    m=q.bit_length()-1
    poly={1:3,2:7}[m]
    mult=[[mul(a,b,m,poly) for b in range(q)] for a in range(q)]
    nonisotropic=[v for v in projective_points(q) if qpf(v,mult)!=0]
    valid_pairs=0
    for i,u in enumerate(nonisotropic):
        for v in nonisotropic[i+1:]:
            for t in range(1,q):
                w=tuple(u[k]^mult[t][v[k]] for k in range(6))
                if qpf(w,mult)==0: break
            else: valid_pairs+=1
    per_plane=q*(q+1)//2
    assert valid_pairs%per_plane==0
    return len(nonisotropic),valid_pairs//per_plane


def smooth_lifts(q):
    Q=q*q
    m=Q.bit_length()-1
    poly={2:7,4:19}[q]
    mult=[[mul(a,b,m,poly) for b in range(Q)] for a in range(Q)]
    sq=[mult[a][a] for a in range(Q)]
    smooth=0
    for a,b,c,d in product(range(Q),repeat=4):
        disc=mult[b][d]^sq[mult[a][d]]^sq[mult[c][b]]
        if disc: smooth+=1
    return smooth


def main():
    for q in (2,4):
        A=q**4*(q**3-1)*(q-1)//2
        npoint,nplane=anisotropic_planes(q)
        assert npoint==q*q*(q**3-1),(q,npoint)
        assert nplane==A,(q,nplane,A)
        smooth=smooth_lifts(q)
        expected=q*q*(q*q-1)**2*(q*q+1)
        assert smooth==expected,(q,smooth,expected)
        N=A*q**8
        S=A*smooth
        assert S==N*(q*q-1)*(q**4-1)//q**6
        print('q=%d anisotropic_points=%d anisotropic_polar_pencils=%d all_smooth_pencils=%d smooth_base_lifts_per_polar_pencil=%d smooth_base_pencils=%d' %(q,npoint,A,N,smooth,S))
    print('EVEN_QUADRIC_PENCIL_COUNTS_OK')

if __name__=='__main__': main()
