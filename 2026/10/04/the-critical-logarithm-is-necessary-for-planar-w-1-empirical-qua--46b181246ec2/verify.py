#!/usr/bin/env python3
import math

def construction(N):
    K = math.floor(math.log(N)/(4*math.log(8)))
    assert K >= 1
    rows = []
    Lsum = 0
    moment_numerator = 0.0
    match_lb = 0.0
    for j in range(K):
        R = 8**j
        A = math.sqrt(N/(64*K*R*R))
        m = math.floor(A)
        assert m >= 2
        L = 2*m*m
        s = R/(2*m)
        Lsum += L
        moment_numerator += L*R*R
        match_lb += 0.5*L*s
        assert s <= R/4
        assert m*R >= (1/16)*math.sqrt(N/K) - 1e-12
        rows.append((j,R,m,L,s))
    assert Lsum < 2*N
    moment_bound = 4*moment_numerator/N
    assert moment_bound <= 1/8 + 1e-12
    assert match_lb >= (1/32)*math.sqrt(N*K) - 1e-10
    e_lb = match_lb/(2*N)
    return K, moment_bound, e_lb

# These values are chosen so that the asymptotic floor conditions are safely active.
for N in (10**8, 10**10, 10**12, 10**16, 10**20):
    K, moment, lb = construction(N)
    assert lb > 0
    print(f"N={N} K={K} moment<={moment:.12g} lower={lb:.12g}")
print("VERIFY_OK")
