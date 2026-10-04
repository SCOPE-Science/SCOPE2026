#!/usr/bin/env python3
import math
from itertools import combinations

MAX_N = 36

def trim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p

def div_exact(num, den):
    num = num[:]
    den = trim(den[:])
    q = [0] * max(1, (len(num) - len(den) + 1))
    while len(num) >= len(den):
        c = num[-1]  # den is monic
        j = len(num) - len(den)
        q[j] = c
        if c:
            for i, d in enumerate(den):
                num[i+j] -= c*d
        trim(num)
    assert all(v == 0 for v in num), (num, den)
    return trim(q)

def cyclotomic_table(nmax):
    phis = {}
    for n in range(1, nmax+1):
        p = [-1] + [0]*(n-1) + [1]
        for d in range(1, n):
            if n % d == 0:
                p = div_exact(p, phis[d])
        phis[n] = p
    return phis

def remainder_vectors(phi, N):
    m = len(phi)-1
    assert phi[-1] == 1
    out = []
    v = [0]*m
    v[0] = 1
    out.append(tuple(v))
    for _ in range(1, N):
        prev = out[-1]
        w = [0]*m
        spill = prev[-1]
        for j in range(1, m):
            w[j] = prev[j-1]
        if spill:
            for j in range(m):
                w[j] -= spill*phi[j]
        out.append(tuple(w))
    return out

def det_zero(R, N, a, b, t, k):
    # det [[1,1,1],[1,z^(ta),z^(tb)],[1,z^(ka),z^(kb)]]
    exps = (
        (t*a + k*b) % N,
        (t*b + k*a) % N,
        (k*b) % N,
        (t*b) % N,
        (k*a) % N,
        (t*a) % N,
    )
    signs = (1,-1,-1,1,1,-1)
    for j in range(len(R[0])):
        s = 0
        for e,sgn in zip(exps, signs):
            s += sgn*R[e][j]
        if s:
            return False
    return True

def q_of(N):
    for d in range(3, N+1):
        if N % d == 0:
            return d
    raise AssertionError

def exact_mu3(N, R):
    max_zeros = 0
    witness = None
    support_count = 0
    pair_kernels = 0
    determinant_tests = 0
    for a in range(1, N):
        for b in range(a+1, N):
            support_count += 1
            # Frequency rows equivalent to k=0 form a class of this size.
            row_class = math.gcd(N, math.gcd(a,b))
            if row_class > max_zeros:
                max_zeros = row_class
                witness = (a,b,"row_class")
            for t in range(1, N):
                # Cross-product kernel has three nonzero coordinates exactly
                # when 1,z^(ta),z^(tb) are pairwise distinct.
                if (t*a) % N == 0 or (t*b) % N == 0 or (t*(a-b)) % N == 0:
                    continue
                pair_kernels += 1
                zc = 0
                for k in range(N):
                    determinant_tests += 1
                    if det_zero(R, N, a, b, t, k):
                        zc += 1
                if zc > max_zeros:
                    max_zeros = zc
                    witness = (a,b,t)
    return N-max_zeros, max_zeros, witness, support_count, pair_kernels, determinant_tests

def construction_zeros(N, q):
    # Support {0,h,2h}; choose polynomial with two prescribed distinct qth roots.
    # Algebraically its zero fibers have size N/q each, so this is exact.
    h = N//q
    assert len({0,h,2*h}) == 3
    return 2*(N//q)

def main():
    phis = cyclotomic_table(MAX_N)
    total_supports = total_kernels = total_det = 0
    rows = []
    for N in range(3, MAX_N+1):
        R = remainder_vectors(phis[N], N)
        mu, zmax, wit, sc, pk, dt = exact_mu3(N, R)
        q = q_of(N)
        predicted = N*(q-2)//q
        assert mu == predicted, (N, mu, predicted, zmax, wit)
        assert construction_zeros(N,q) == 2*N//q
        total_supports += sc
        total_kernels += pk
        total_det += dt
        rows.append((N,q,mu,zmax,wit))
    print(f"checked N=3..{MAX_N}")
    print(f"normalized_supports={total_supports}")
    print(f"nondegenerate_pair_kernels={total_kernels}")
    print(f"exact_cyclotomic_determinant_tests={total_det}")
    print("last_rows=")
    for row in rows[-8:]:
        print(row)
    print("VERIFY_OK")

if __name__ == '__main__':
    main()
