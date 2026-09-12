"""Totaro E2 exploration for F_n(T*) over Fp.
M = once-punctured torus: H^0=Q, H^1=<a,b>, H^2=0.
H*(M^n) = exterior(a_i,b_i)/(a_i b_i).
G_ij symmetric odd, Arnold + sliding, d(G_ij)=a_i b_j - b_i a_j.
Computes dim E3 in total degree 2.
"""
import itertools, numpy as np

def prime_mod_inv(a, p):
    return pow(int(a), p-2, p)

def rank_mod(A, p):
    """rank of m x n matrix over Fp via Gaussian elimination (numpy-assisted)."""
    if A.size == 0:
        return 0
    M = A.copy() % p
    m, n = M.shape
    r = 0
    row = 0
    for col in range(n):
        # find pivot
        piv = -1
        for i in range(row, m):
            if M[i, col] % p != 0:
                piv = i; break
        if piv < 0:
            continue
        M[[row, piv]] = M[[piv, row]]
        inv = prime_mod_inv(M[row, col], p)
        M[row] = (M[row]*inv) % p
        for i in range(m):
            if i != row and M[i, col] != 0:
                M[i] = (M[i] - M[i, col]*M[row]) % p
        row += 1; r += 1
        if row == m:
            break
    return r

def nullspace_mod(A, p):
    """Nullspace (right kernel) of m x n matrix A over Fp. Returns (k, N) with N k x n basis rows."""
    m, n = A.shape
    M = A.copy() % p
    pivots = []
    pivcol_of_row = {}
    row = 0
    col2row = {}
    for col in range(n):
        piv = -1
        for i in range(row, m):
            if M[i, col] % p != 0:
                piv = i; break
        if piv < 0:
            continue
        M[[row, piv]] = M[[piv, row]]
        inv = prime_mod_inv(M[row, col], p)
        M[row] = (M[row]*inv) % p
        for i in range(m):
            if i != row and M[i, col] != 0:
                M[i] = (M[i] - M[i, col]*M[row]) % p
        col2row[col] = row
        pivots.append(col)
        row += 1
        if row == m:
            # continue to identify pivots? still need reduced form for remaining cols
            pass
    free = [c for c in range(n) if c not in col2row]
    k = len(free)
    N = np.zeros((k, n), dtype=np.int64)
    for idx, f in enumerate(free):
        N[idx, f] = 1
        for c, r in col2row.items():
            N[idx, c] = (-M[r, f]) % p
    return k, N

# ---------- cohomology monomials ----------
def build_H(n):
    # generators: 0..2n-1, even=a_i, odd=b_i
    N = 2*n
    mons_by_deg = {}
    for mask in range(1 << N):
        # bitmask over generators present
        deg = bin(mask).count('1')
        gens = [g for g in range(N) if mask >> g & 1]
        # check forbidden a_i b_i
        bad = False
        for i in range(n):
            if (mask >> (2*i) & 1) and (mask >> (2*i+1) & 1):
                bad = True; break
        if bad:
            continue
        mons_by_deg.setdefault(deg, []).append(tuple(gens))
    # sort for determinism
    for d in mons_by_deg:
        mons_by_deg[d].sort()
    index = {}
    for d, lst in mons_by_deg.items():
        for k, m in enumerate(lst):
            index[(d, m)] = k
    return mons_by_deg, index, N

def mul_sign(m1, m2):
    # merge two sorted tuples, return (sign, tuple) or (0, None) if overlap
    s = set(m1) & set(m2)
    if s:
        return 0, None
    inv = 0
    for x in m1:
        for y in m2:
            if x > y:
                inv += 1
    return (-1)**inv, tuple(sorted(m1+m2))

def cup(m1, m2, index_of, n):
    s, m = mul_sign(m1, m2)
    if s == 0:
        return None
    # check forbidden
    present = set(m)
    for i in range(n):
        if (2*i in present) and (2*i+1 in present):
            return None
    return (len(m), m, s)

def pairs_list(n):
    return [(i, j) for i in range(n) for j in range(i+1, n)]

P = 1000003

for n in range(2, 8):
    mons, index_of, N = build_H(n)
    H1 = mons.get(1, [])
    H2 = mons.get(2, [])
    H3 = mons.get(3, [])
    d1 = len(H1); d2 = len(H2); d3 = len(H3)
    pairs = pairs_list(n)
    ng = len(pairs)
    gindex = {p: k for k, p in enumerate(pairs)}
    # diagonal Delta_ij as vector in H2 coords
    # Delta = a_i b_j - b_i a_j ; generators: a_i=2i, b_i=2i+1
    Delta = np.zeros((ng, d2), dtype=np.int64)
    h2idx = {m: k for k, m in enumerate(H2)}
    for k, (i, j) in enumerate(pairs):
        m_a = tuple(sorted([2*i, 2*j+1]))  # a_i b_j
        m_b = tuple(sorted([2*i+1, 2*j]))  # b_i a_j
        Delta[k, h2idx[m_a]] = (Delta[k, h2idx[m_a]] + 1)
        Delta[k, h2idx[m_b]] = (Delta[k, h2idx[m_b]] - 1)
    # d01: E2^{0,1} -> E2^{2,0}: matrix ng x d2? map G -> Delta. rank?
    r01 = rank_mod(Delta % P, P)
    dim_E30_20 = d2 - r01
    # ---- E2^{1,1} ----
    # F11 = H1 x G, dim d1*ng
    F = d1*ng
    h1idx = {m: k for k, m in enumerate(H1)}
    def f11_idx(hi, gi):
        return hi*ng + gi
    # relations R11: 2*ng rows in F coords
    R = np.zeros((2*ng, F), dtype=np.int64)
    ab = [0, 1]  # 0=a-type,1=b-type
    for k, (i, j) in enumerate(pairs):
        for t, gval in [(0, 2*i), (0, 2*j), (1, 2*i+1), (1, 2*j+1)]:
            pass
        # relation (a_i - a_j) G_ij
        # a_i is monomial (2i,), a_j is (2j,)
        rrow_a = k*2; rrow_b = k*2+1
        R[rrow_a, f11_idx(h1idx[(2*i,)], k)] += 1
        R[rrow_a, f11_idx(h1idx[(2*j,)], k)] -= 1
        R[rrow_b, f11_idx(h1idx[(2*i+1,)], k)] += 1
        R[rrow_b, f11_idx(h1idx[(2*j+1,)], k)] -= 1
    rR = rank_mod(R % P, P)
    dimQ11 = F - rR
    # map f: F11 -> H3, f(h x G_ij) = h cup Delta_ij
    h3idx = {m: k for k, m in enumerate(H3)}
    fmat = np.zeros((F, d3), dtype=np.int64)
    for hi, h in enumerate(H1):
        for k in range(ng):
            row = f11_idx(hi, k)
            for c, m2 in enumerate(H2):
                coef = int(Delta[k, c])
                if coef == 0:
                    continue
                r = cup(h, m2, None, n)
                if r is None:
                    continue
                _, m3, s = r
                fmat[row, h3idx[m3]] = (fmat[row, h3idx[m3]] + coef*s)
    # kernel of induced map Q11 -> H3: ker = {v in F : fmat v =0} containing R.
    # dim ker(Q) = dim ker(F->H3) - rank(R)  [since R subset ker? verify]
    # check R subset ker: R*fmat should be 0
    check = (R % P) @ (fmat % P) % P
    is_sub = np.all(check == 0)
    # stacked matrix [fmat^T? ] compute dim ker F->H3 = F - rank(fmat)
    rf = rank_mod(fmat % P, P)
    dimkerF = F - rf
    dimkerQ = dimkerF - rR
    print(f"n={n} H1={d1} H2={d2} H3={d3} ng={ng} rank(d01)={r01} dimE3_20={dim_E30_20} dimQ11={dimQ11} rankR={rR} Rinker={is_sub} rankf={rf} dimkerQ(E3_11)={dimkerQ}")
    # ---- E2^{0,2} ---- Arnold algebra degree 2
    # basis: ordered pairs of G's modulo Arnold. Build via free exterior on ng generators modulo Arnold rels.
    # Free Lambda^2: pairs u<v of G-indices, dim C(ng,2). Arnold rels: for each triple i<j<k? Actually for each triple of points {i,j,k}: one relation G_ij G_jk + G_jk G_ki + G_ki G_ij = 0.
    # But careful: G indices are pairs; triple gives 3 G's; relation among the 3 wedge products.
    from math import comb
    Nfree = comb(ng, 2) if ng >= 2 else 0
    gpair_list = [(u, v) for u in range(ng) for v in range(u+1, ng)]
    gpidx = {p: k for k, p in enumerate(gpair_list)}
    # Arnold rows
    import itertools as it
    arn_rows = []
    for (i, j, k_) in it.combinations(range(n), 3):
        # the three G indices
        e1 = gindex[tuple(sorted([i, j]))]
        e2 = gindex[tuple(sorted([j, k_]) )]
        e3 = gindex[tuple(sorted([i, k_]))]
        row = np.zeros(Nfree, dtype=np.int64)
        for (u, v, s) in [ (e1,e2,1),(e2,e3,1),(e3,e1,1) ]:
            # wedge e_u ^ e_v with sign to sorted order
            if u == v:
                continue
            if u < v:
                row[gpidx[(u, v)]] += s
            else:
                row[gpidx[(v, u)]] -= s
        arn_rows.append(row)
    if arn_rows:
        Arn = np.array(arn_rows, dtype=np.int64) % P
        rA = rank_mod(Arn, P)
    else:
        rA = 0
    dimE02 = Nfree - rA
    print(f"   Arnold: free={Nfree} nrel={len(arn_rows)} rank={rA} dimE02={dimE02}")
