"""Full character table of H^2 = E3_20 + E3_11, fit weight-3 polynomial, find N*."""
import itertools
import numpy as np
from characters import (P, build_F11_data, char_H2, char_H3, S_H1, S_G, S_Hexterior,
                        subspace_trace, kernel_trace, perm_from_cycle_type, cycle_counts,
                        partitions_upto, modinv)
from explore_dims import pairs_list, rank_mod
from math import comb

cache = {n: build_F11_data(n) for n in range(2, 8)}

def full_char(n, sigma):
    pairs = pairs_list(n)
    gindex = {pp: k for k, pp in enumerate(pairs)}
    SG = S_G(sigma, pairs, gindex, P)
    trE01 = int(np.trace(SG) % P)
    trH2 = char_H2(n, sigma, P)
    trE20 = (trH2 - trE01) % P
    D = cache[n]
    H1, H3, ng, d1 = D['H1'], D['H3'], D['ng'], D['d1']
    R, fmat = D['R'], D['fmat']
    SH1 = S_H1(sigma, n, P)
    SF = np.kron(SH1, SG) % P
    SH3 = S_Hexterior(sigma, [m for m in H3], n, P) if H3 else np.zeros((0, 0), dtype=np.int64)
    # row-space basis of R
    M = R.copy() % P
    m_, d_ = M.shape
    row = 0
    for col in range(d_):
        piv = -1
        for i in range(row, m_):
            if M[i, col] % P != 0:
                piv = i; break
        if piv < 0:
            continue
        M[[row, piv]] = M[[piv, row]]
        inv = modinv(M[row, col])
        M[row] = (M[row]*inv) % P
        for i in range(m_):
            if i != row and M[i, col] != 0:
                M[i] = (M[i] - M[i, col]*M[row]) % P
        row += 1
    Brow = M[:row]
    trR = subspace_trace(SF, Brow) if row else 0
    A = fmat.T % P  # H3 x F
    trkerF = kernel_trace(A, SF, SH3, P)
    trE11 = (trkerF - trR) % P
    trH3 = char_H3(n, sigma, P)
    return dict(E20=trE20, E11=trE11, TOT=(trE20+trE11) % P, kerF=trkerF,
                R=trR, H2=trH2, E01=trE01, H3=trH3,
                F=int(np.trace(SF) % P))

def sgn(x):
    x = int(x) % P
    return x if x <= P//2 else x - P

rows = []
for n in range(2, 8):
    print(f"=== n={n} ===")
    for ct in partitions_upto(n):
        sigma = perm_from_cycle_type(ct)
        cc = cycle_counts(sigma)
        c = full_char(n, sigma)
        print(f"  type={ct} X1={cc.get(1,0)} X2={cc.get(2,0)} X3={cc.get(3,0)} "
              f"E20={sgn(c['E20'])} E11={sgn(c['E11'])} TOT={sgn(c['TOT'])}")
        rows.append((n, tuple(ct), cc, sgn(c['TOT']), sgn(c['E20']), sgn(c['E11'])))
