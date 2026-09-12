"""Clean two-prime verification with fixed modular arithmetic (fresh process)."""
import sys
sys.path.insert(0, 'output/artifacts')
import numpy as np
from characters import build_F11_data, char_H2, S_H1, S_G, S_Hexterior, kernel_trace, subspace_trace, perm_from_cycle_type, modinv
from explore_dims import pairs_list

P1, P2 = 1000003, 1000033

def full(n, sigma, p):
    D = build_F11_data(n, p)
    pairs = pairs_list(n)
    gindex = {pp: k for k, pp in enumerate(pairs)}
    SG = S_G(sigma, pairs, gindex, p)
    trE01 = int(np.trace(SG) % p)
    trH2 = char_H2(n, sigma, p)
    trE20 = (trH2 - trE01) % p
    H1, H3 = D['H1'], D['H3']
    R = D['R'] % p
    fmat = D['fmat'] % p
    SH1 = S_H1(sigma, n, p)
    SF = np.kron(SH1, SG) % p
    SH3 = S_Hexterior(sigma, [m for m in H3], n, p) if len(H3) else np.zeros((0, 0), dtype=np.int64)
    M = R.copy() % p
    m_, d_ = M.shape
    row = 0
    for col in range(d_):
        piv = -1
        for i in range(row, m_):
            if M[i, col] % p != 0:
                piv = i
                break
        if piv < 0:
            continue
        M[[row, piv]] = M[[piv, row]]
        inv = pow(int(M[row, col]), p - 2, p)
        M[row] = (M[row] * inv) % p
        for i in range(m_):
            if i != row and M[i, col] != 0:
                M[i] = (M[i] - (M[i, col] * M[row]) % p) % p
        row += 1
    trR = subspace_trace(SF, M[:row], p) if row else 0
    A = fmat.T % p
    trkerF = kernel_trace(A, SF, SH3, p)
    return (trE20 + (trkerF - trR)) % p

def sgned(x, p):
    x = int(x) % p
    return x if x <= p // 2 else x - p

tests = [(2, [2]), (2, [1, 1]), (3, [3]), (3, [2, 1]), (3, [1]*3),
         (4, [4]), (4, [2, 2]), (4, [1]*4), (5, [3, 1, 1]), (5, [1]*5),
         (6, [3, 2, 1]), (6, [1]*6), (7, [2, 1, 1, 1, 1, 1]), (7, [1]*7)]
ok = True
for n, ct in tests:
    sg = perm_from_cycle_type(ct)
    a = sgned(full(n, sg, P1), P1)
    b = sgned(full(n, sg, P2), P2)
    flag = 'OK' if a == b else 'MISMATCH'
    if a != b:
        ok = False
    print(f"n={n} {ct}: p1={a} p2={b} {flag}")
print("ALL OK" if ok else "FAILURES PRESENT")
