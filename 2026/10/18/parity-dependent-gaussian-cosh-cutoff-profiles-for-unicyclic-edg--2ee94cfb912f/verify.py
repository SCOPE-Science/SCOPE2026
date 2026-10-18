#!/usr/bin/env python3
"""Exact finite checks for a binary edge-toggle walk on unicyclic graphs.

No simulation is used. All finite-state probabilities use fractions.
"""
from fractions import Fraction
from math import comb


def edges(m, ell):
    """An ell-cycle with m-ell pendant edges, attached as a path at vertex zero."""
    assert m >= ell >= 3
    E = [(j, (j + 1) % ell) for j in range(ell)]
    E.extend((j - 1, j) if j > ell else (0, ell) for j in range(ell, m))
    return E


def projected(mask, E):
    y = 0
    for i, (u,v) in enumerate(E):
        if mask >> i & 1:
            y ^= (1 << u) | (1 << v)
    return y


def walk(Q, moves):
    N = len(moves)
    out = {}
    for x, v in Q.items():
        for s in moves:
            y = x ^ s
            out[y] = out.get(y, Fraction(0)) + v / N
    return out


def chi2(Q, target_count):
    return sum((v * target_count - 1)**2 for v in Q.values()) / target_count + Fraction(target_count - len(Q), target_count)


def spectral_chi2(m, ell, t):
    # Characters orthogonal to the unique cycle vector. In even-cycle
    # case, complements represent the same character on a parity sector.
    if ell % 2:
        return sum(Fraction(comb(m,k), 2) * Fraction(m - 2*k, m)**(2*t)
                   for k in range(m+1)) - 1
    return sum(Fraction(comb(ell,j)*comb(m-ell,k), 2) *
               Fraction(m - 2*(j+k), m)**(2*t)
               for j in range(0,ell+1,2)
               for k in range(m-ell+1)) - 1


def run():
    checks = 0
    for m in range(3, 9):
        for ell in range(3,m+1):
            E=edges(m,ell)
            assert len(E)==m
            cycles=(1<<ell)-1
            assert projected(cycles,E)==0
            assert all(projected(a,E)!=0 for a in range(1,1<<m) if a!=cycles)
            checks += (1<<m)-1
            # Test the exact push-forward from edge-parity bits.
            Q={0:Fraction(1)}
            P={0:Fraction(1)}
            for t in range(0,5):
                got={}
                for x,v in Q.items():
                    y=projected(x,E)
                    got[y]=got.get(y,Fraction(0))+v
                assert got==P, (m,ell,t,got,P)
                # For odd ell, each parity layer maps bijectively to the
                # 2^(m-1) even-vertex-parity states; otherwise to 2^(m-2).
                target_count=2**(m-(1 if ell%2 else 2))
                assert chi2(P,target_count)==spectral_chi2(m,ell,t), (m,ell,t)
                checks+=2
                if t<4:
                    Q=walk(Q,[1<<i for i in range(m)])
                    P=walk(P,[(1<<u)|(1<<v) for u,v in E])
    print('PASS',checks,'exact checks; all unicyclic graph sizes 3..8, cycle lengths, times 0..4')

if __name__=='__main__':
    run()
