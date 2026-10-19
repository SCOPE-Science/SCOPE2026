#!/usr/bin/env python3
"""Exact-rational checks for first entrances to three-point ordinal cells of the dyadic map.

No third-party dependencies. This is a finite consistency check, not a substitute
for the transition-matrix proof of the generating functions.
"""
from fractions import Fraction as Q
from math import factorial

B = [Q(0), Q(1,4), Q(1,3), Q(1,2), Q(2,3), Q(3,4), Q(1)]
LABELS = ['012', '201', '021', '120', '102', '210']
A = ((0, 1, 2), (3,), (4, 5), (0, 1), (2,), (3, 4, 5))
P = [[Q(0) for _ in range(6)] for _ in range(6)]
for i in range(6):
    u = B[i]; v = B[i+1]
    m = (u + v)/2
    triplet = (m, (2*m)%1, (4*m)%1)
    label = ''.join(str(k) for k in sorted(range(3), key=lambda j: triplet[j]))
    assert label == LABELS[i], (i, triplet, label)
    for j in A[i]:
        P[i][j] = (B[j+1] - B[j]) / (2*(v-u))
    assert sum(P[i]) == 1

# [numerator coefficients], [denominator coefficients] in increasing degree.
RATIONAL = {
    0: ([0, 0, 0, 1], [8, -8, 0, 1]),
    1: ([0, 0, 4, -2, -1], [16, -16, 0, 2, -1]),
    2: ([0, 0, 1], [4, -2, -1]),
}

def power_coefficients(numerator, denominator, upto):
    a = []
    for n in range(upto+1):
        rhs = Q(numerator[n]) if n < len(numerator) else Q(0)
        for k in range(1, min(n,len(denominator)-1)+1):
            rhs -= denominator[k]*a[n-k]
        a.append(rhs / denominator[0])
    return a

def preimage_of_interval(a, b, n):
    scale = 2**n
    return [(Q(k+a, scale), Q(k+b, scale)) for k in range(scale)]

def exact_first_entrances(cell, cutoff):
    # Survivors are initial-coordinate intervals with the Boolean:
    # was the previous symbol in the given cell?
    remain = [(B[cell], B[cell+1], True)]
    masses = [Q(0)]*(cutoff+1)
    for n in range(1, cutoff+1):
        hits = preimage_of_interval(B[cell], B[cell+1], n)
        new = []
        idx = 0
        for left, right, prev in remain:
            cur = left
            while cur < right:
                while idx < len(hits) and hits[idx][1] <= cur:
                    idx += 1
                if idx < len(hits) and hits[idx][0] <= cur:
                    in_cell = True
                    end = min(right, hits[idx][1])
                else:
                    in_cell = False
                    end = min(right, hits[idx][0]) if idx < len(hits) else right
                assert end > cur
                if in_cell and not prev:
                    masses[n] += end-cur
                else:
                    if new and new[-1][1]==cur and new[-1][2]==in_cell:
                        new[-1] = (new[-1][0], end, in_cell)
                    else:
                        new.append((cur,end,in_cell))
                cur = end
        remain = new
        mass = B[cell+1]-B[cell]
        assert sum(masses)+sum(v-u for u,v, _ in remain) == mass
    return [m / (B[cell+1]-B[cell]) for m in masses]

# Exact interval geometry, independently of the Markov-chain rational functions.
for cell in range(6):
    cat = min(cell,5-cell)
    # labels pair 0,5; 1,4; 2,3
    predicted = power_coefficients(*RATIONAL[cat], 10)
    observed = exact_first_entrances(cell, 10)
    assert observed == predicted, (cell, observed, predicted)
    print(LABELS[cell], 'first-entrance n=1..10:', [str(x) for x in observed[1:]])

# First two PGF derivatives at z=1, computed from the defining polynomial identity.
def moment_polynomial(num, den):
    def deriv_at_one(c,k):
        return sum(Q(c[n])*factorial(n)//factorial(n-k) for n in range(k,len(c)))
    # N= D*G, at z=1, G(1)=1.
    d0=deriv_at_one(den,0); n0=deriv_at_one(num,0)
    assert d0 != 0 and n0 == d0
    d1=deriv_at_one(den,1); n1=deriv_at_one(num,1)
    mean=(n1-d1)/d0
    d2=deriv_at_one(den,2); n2=deriv_at_one(num,2)
    factorial_second=(n2-d2-2*d1*mean)/d0
    variance=factorial_second+mean-mean*mean
    return mean,variance
expected=((Q(8),Q(24)),(Q(12),Q(188)),(Q(6),Q(22)))
for i in range(3):
    assert moment_polynomial(*RATIONAL[i]) == expected[i]
    print('category',i,'mean/variance:', expected[i])

# Independent entrance frequencies: by invariance, each entrance is a transition
# from complement to the cell, of stationary intensity |I_i|(1-P_ii).
for i in range(6):
    mean = expected[min(i,5-i)][0]
    assert mean == 1 / ((B[i+1]-B[i])*(1-P[i][i]))
print('All exact tests passed.')
