#!/usr/bin/env python3
"""Exact finite checks for zero contacts and squared energy in simple random-walk bridges.

Run with Python 3, using only the standard library. All moment comparisons use
integer or rational arithmetic; no random sampling is involved.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def bridge_moments(n):
    """Enumerate every bridge with n upsteps and n downsteps."""
    N = 2*n
    count = comb(N, n)
    sums = [0, 0, 0, 0, 0] # R,Q,R^2,Q^2,RQ
    pin_count = [0]*(n+1)
    pin_energy = [0]*(n+1)
    pair_count = {(a, b): 0 for a in range(1,n) for b in range(a+1,n)}
    pair_energy = {k:0 for k in pair_count}
    enumerated = 0
    for places in combinations(range(N), n):
        up = set(places)
        height = 0
        hits = []
        Q = 0
        for t in range(1,N):
            height += 1 if t-1 in up else -1
            Q += height*height
            if t%2 == 0 and height == 0:
                hits.append(t//2)
        R = len(hits)
        sums[0] += R
        sums[1] += Q
        sums[2] += R*R
        sums[3] += Q*Q
        sums[4] += R*Q
        for k in hits:
            pin_count[k] += 1
            pin_energy[k] += Q
        for a,b in combinations(hits,2):
            pair_count[(a,b)] += 1
            pair_energy[(a,b)] += Q
        enumerated += 1
    assert enumerated == count
    ER, EQ, ER2, EQ2, ERQ = [Fraction(a, count) for a in sums]
    return ER, EQ, ER2-ER*ER, EQ2-EQ*EQ, ERQ-ER*EQ, pin_count, pin_energy, pair_count, pair_energy, count


def formulas(n):
    B = Fraction(4**n, comb(2*n,n))
    return (B-2,
            Fraction(n*(2*n+1),3),
            4*n+2-B-B*B,
            Fraction(8*n*n*(n-1)*(2*n+1),45),
            -Fraction(n*(n-1),6)*B)


def check():
    total_paths = 0
    assertions = 0
    for n in range(2,10):
        er, eq, vr, vq, crq, pc, pe, ppc, ppe, count = bridge_moments(n)
        total_paths += count
        for observed, target in zip((er,eq,vr,vq,crq),formulas(n)):
            assert observed == target, (n,observed,target)
            assertions += 1
        for k in range(1,n):
            target = Fraction(k*(2*k+1)+(n-k)*(2*(n-k)+1),3)
            assert pc[k] and Fraction(pe[k],pc[k]) == target,(n,k)
            assertions += 1
        for (a,b),c in ppc.items():
            x = (a,b-a,n-b)
            target = Fraction(sum(z*(2*z+1) for z in x),3)
            assert c and Fraction(ppe[(a,b)],c) == target, (n,a,b)
            assertions += 1
    # Independent exact coefficient convolution checks.
    for n in range(2,101):
        c = lambda k: comb(2*k,k)
        lhs=sum(k*(n-k)*c(k)*c(n-k) for k in range(1,n))
        rhs=(4**(n-1))*n*(n-1)//2
        assert lhs == rhs
        assertions += 1
    # Direct checks of the weighted-pair sums in the fourth-moment variance proof.
    for N in range(4,61,2):
        w={(i,j): N-j for j in range(2,N+1) for i in range(1,j)}
        W=sum(w.values()); U=sum(v*v for v in w.values())
        adj=sum(a*b for (i,j),a in w.items() for (k,l),b in w.items()
                if (i,j)<(k,l) and (i==k or i==l or j==k or j==l))
        assert W == N*(N-1)*(N-2)//6
        assert U == N*(N-2)*(N-1)**2//12
        assert adj == N*(N-3)*(N-2)*(N-1)*(8*N-7)//120
        assertions += 3
    print('PASS exact enumeration of',total_paths,'bridges for n=2..9;')
    print('PASS',assertions,'exact arithmetic assertions including prescribed-contact energies,')
    print('convolution identities through n=100, and fourth-moment coefficient sums.')


if __name__ == '__main__':
    check()
