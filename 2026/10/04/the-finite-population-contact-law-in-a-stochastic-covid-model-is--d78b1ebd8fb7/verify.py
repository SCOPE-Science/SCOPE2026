#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import combinations
from math import comb

def choose(n, k):
    if k < 0 or k > n:
        return 0
    return comb(n, k)

def beta_hg_formula(M, N, yI, yA, qI, qA):
    noinf = F(0)
    for i in range(N + 1):
        for a in range(N - i + 1):
            ways = choose(yI, i) * choose(yA, a) * choose(M-yI-yA, N-i-a)
            noinf += F(ways, choose(M, N)) * (1-qI)**i * (1-qA)**a
    return 1-noinf

def beta_hg_enumerate(M, N, yI, yA, qI, qA):
    # labels 0..yI-1 are I, next yA are A, remainder noninfectious.
    total = choose(M, N)
    noinf = F(0)
    for subset in combinations(range(M), N):
        i = sum(x < yI for x in subset)
        a = sum(yI <= x < yI+yA for x in subset)
        noinf += (1-qI)**i * (1-qA)**a / total
    return 1-noinf

def beta_src(M, N, yI, yA, qI, qA):
    return 1-(1-F(qI*yI + qA*yA, M))**N

# Saturation witness.
M=N=2
yI=1
yA=0
qI=F(1)
qA=F(0)
bh = beta_hg_formula(M,N,yI,yA,qI,qA)
be = beta_hg_enumerate(M,N,yI,yA,qI,qA)
bs = beta_src(M,N,yI,yA,qI,qA)
assert bh == be == F(1)
assert bs == F(3,4)

# Mixed two-class finite example.
M,N,yI,yA = 7,4,2,2
qI,qA = F(1,2),F(1,3)
bh = beta_hg_formula(M,N,yI,yA,qI,qA)
be = beta_hg_enumerate(M,N,yI,yA,qI,qA)
assert bh == be
assert bh != beta_src(M,N,yI,yA,qI,qA)

# One-infective closed form for a range of exact finite states.
for M in range(2,10):
    for N in range(1,M+1):
        for qI in (F(1,5), F(1,2), F(1)):
            bh = beta_hg_formula(M,N,1,0,qI,F(0))
            assert bh == F(N, M)*qI
            if N > 1:
                assert beta_src(M,N,1,0,qI,F(0)) < bh

# Large-population source-style early state: discrepancy is small but nonzero.
M,N,qI = 9999,10,F(1,5)
bh = beta_hg_formula(M,N,1,0,qI,F(0))
bs = beta_src(M,N,1,0,qI,F(0))
assert bh > bs
assert float((bh-bs)/bh) < 0.0001

print("VERIFY_OK")
print("saturation_beta_hypergeom", F(1))
print("saturation_beta_source", F(3,4))
print("mixed_beta_hypergeom", beta_hg_formula(7,4,2,2,F(1,2),F(1,3)))
print("mixed_beta_source", beta_src(7,4,2,2,F(1,2),F(1,3)))
print("early_relative_gap", float((bh-bs)/bh))
