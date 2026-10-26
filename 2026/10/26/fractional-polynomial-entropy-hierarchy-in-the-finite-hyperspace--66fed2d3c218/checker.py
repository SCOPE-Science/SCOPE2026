#!/usr/bin/env python3
"""Finite exact-height checks for rational rotating-disk configurations.

The asymptotic polynomial-entropy statements require the analytic argument.
"""
from fractions import Fraction
from math import ceil, cos, pi, hypot


def heights(alpha, j_max):
    return sorted({Fraction(1, int(j**alpha)) for j in range(1, j_max+1) if int(j**alpha)>0})


def greedy_gap(seq, N, cap=Fraction(1, 8)):
    chosen=[]
    for a in seq:
        if a > cap:
            continue
        if not chosen or a-chosen[-1]>=Fraction(1,N):
            chosen.append(a)
    return chosen


def phase_certificate(N, seq):
    count=0
    for i,a in enumerate(seq):
        for b in seq[:i]:
            d=a-b
            assert Fraction(1,N)<=d<=Fraction(1,8)
            t=ceil(Fraction(1,4)/d)
            assert 0<=t<N
            assert Fraction(1,4)<=t*d<=Fraction(3,8)
            count+=1
    return count


def sample_hausdorff_lower(N, seq):
    # A few two-radius configurations: Euclidean positions in two planes.
    # Different radius bands prevent relabelling across the two particles.
    rs=(Fraction(1,3),Fraction(2,3))
    indices=(0,len(seq)//2,len(seq)-1)
    tested=0
    for i in indices:
        for j in indices:
            if i==j:continue
            d=abs(seq[i]-seq[j]);t=ceil(Fraction(1,4)/d)
            assert 0<=t<N
            r=float(rs[0]);s=float(rs[1]);
            # Same-band distance at the distinguishing time.
            p=(float(seq[i]),r*cos(2*pi*t*float(seq[i])),r*__import__('math').sin(2*pi*t*float(seq[i])))
            q=(float(seq[j]),r*cos(2*pi*t*float(seq[j])),r*__import__('math').sin(2*pi*t*float(seq[j])))
            ds=((p[0]-q[0])**2+(p[1]-q[1])**2+(p[2]-q[2])**2)**.5
            assert ds > float(rs[0])
            assert rs[1]-rs[0]==Fraction(1,3)
            tested+=1
    return tested


if __name__=='__main__':
    for N in (100,1000,10000,100000):
        H=heights(2, max(1000,10*int(N**(1/3))))
        S=greedy_gap(H,N)
        assert len(S)>=3
        checked=phase_certificate(N,S)
        tested=sample_hausdorff_lower(N,S)
        print(f'RATIONAL_LEVEL_PACKING N={N} count={len(S)} pair_phase_checks={checked} sample_two_radius_checks={tested}')
    print('ALL_FINITE_ROTATION_SEPARATION_CHECKS_PASS')
    print('UNBOUNDED_PACKING_AND_ENTROPY_FORMULAS_REQUIRE_ANALYTICAL_PROOF')
