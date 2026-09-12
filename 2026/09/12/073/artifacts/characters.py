"""S_n characters of H^2(F_n(T*)) = E3^{2,0} + E3^{1,1} over Fp (p=1000003),
then fit weight-3 character polynomial and find minimal N*.

Character method: for permutation sigma, Lefschetz trace on H*(M^n) piece and on
free G piece, then quotient/kernel traces via induced-map trace formulas:
  tr(E3^{2,0}) = tr(H2) - tr(im d01) = tr(H2) - tr(E01)  [d01 injective]
  tr(E01) = trace of sigma on span{G}: # fixed edges (sigma acts by permuting edges, no signs: G_ij symmetric generators, permutation sends generator to generator).
  tr(E3^{1,1}) = tr(Q11) - tr(im f) = tr(Q11) - (tr(F11)-tr(kerF)) ... easier:
    tr(ker Q) = tr(Q11) - tr(H3) + tr(coker f). Need coker trace — instead compute
    tr via ranks: build explicit equivariant section? Alternative: compute characters
    of ker directly by Reynolds-projected nullspace: for each class rep, compute
    trace of sigma on ker f_Q by averaging: tr = (1/|C|) ... no.
  Direct approach: tr(sigma|ker(A)) for equivariant map A:V->W (V=Q11 realized as matrices?)
    Use formula with explicit matrices: pick basis, let S_V, S_W be matrices of sigma,
    A s.t. A S_V = S_W A. Then tr(ker) = tr(V) - tr(im), tr(im) = rank, but need character of image:
    tr(im) = trace of S_W restricted... use projector: tr(ker A) = sum over eigenvalues?
    Simplest robust: compute tr(ker) = (1/|G_sigma|) sum_{k} ... no, need centralizer average:
    tr(sigma|ker A) = mean_{tau in <sigma>} ... still needs projector onto ker.
    Cleanest: projector P = I - A^+ A needs pseudoinverse. Over finite field with
    symmetric averaging over cyclic group algebra: ker projector lies in span of ... no.
    PRAGMATIC: compute nullspace basis N (k x F), action matrix T on coefficients:
      N S_V = T N  => solve T = N S_V N^T (N N^T)^{-1}. Then tr = trace(T).
    This is exact and easy. Same for cokernel/image pieces if needed.

So: for each partition of n<=6 (and reps for n=7 partially), compute:
  S_H1, S_F11 (tensor), R relations (quotient): trace on Q11 = tr(F11)-tr(R_row)? For quotient
  V/R with equivariant inclusion R->V: tr(Q) = tr(V) - tr(row-space). Row-space trace again
  needs projector method. Alternative: tr(Q) = tr(V) - tr(R_rowspace); compute action on
  row-space via column-space dual: row-space of R (rows in F) is S_V-stable subspace;
  its character: use projector via N = basis of row space (from RREF), same formula.
  Then ker of f on quotient: lift to F: kerF contains R; T on kerF coeffs via nullspace basis;
  quotient out R: further quotient character via row-space projector inside kerF. Implementable
  but fiddly; SIMPLER: tr(E3_11) = tr(kerF) - tr(R) [as representations, R sits inside kerF].
  tr(R as rep) = trace on row-space. All three terms via projector formula. 

Also E3_20: tr = tr(H2) - tr(E01); E01 = span G, trace = #fixed edges. And H2 = Lambda^2(H1)/<a_i b_i>;
  compute S_H1 matrix explicitly (signed permutation), then induced action on H2 monomial basis
  with quotient projector for the n relations a_i b_i=0 (these span an invariant subspace isomorphic
  to trivial^n? check: sigma permutes the n forbidden monomials, so yes permutation rep; quotient trace
  = tr(Lambda^2 H1) - n_fixed... careful: quotient by subspace: tr = tr(whole)-tr(sub). Lambda^2 trace from
  eigenvalues; sub trace = #fixed points of sigma = X_1(sigma). Fine, or do projector uniformly.

Plan: implement generic helpers:
  - perm_matrix_on_H1(sigma): signed permutation (exterior signs are +1 on degree 1).
  - action_on_monoms(basis lists): for H2 exterior monomials: image of sorted tuple under sigma with sign.
  - subspace_trace(basis_action_matrix S (d x d), subspace_rows B (k x d) spanning stable subspace): T = B S B^+ with B^+ = B^T(BB^T)^{-1}; tr(T).
  - kernel_trace(A (m x d), S_V (d x d), S_W (m x m) with A S_V = S_W A): N=nullspace basis (k x d); T = N S_V N^T (N N^T)^{-1}; tr.
  All over Fp with p=1000003 (need |G| divisions? inverses exist as long as p junk denominators nonzero; verify by cross-checking two primes).

Then fit character polynomial: unknowns coeffs of weight<=3 basis:
  X1^3, X1 X2, X3, X1^2, X2, X1, 1 (weight: Xk has weight k).
Fit on all classes n=4..7 (overdetermined), verify exact on n=2..7 class-by-class, find minimal N*.
"""
import itertools
import numpy as np
from explore_dims import build_H, cup, pairs_list, rank_mod, nullspace_mod

P = 1000003

def modinv(a, p=P):
    return pow(int(a) % p, p-2, p)

def _mmul(*Ms, p):
    R = Ms[0] % p
    for M in Ms[1:]:
        R = (R @ (M % p)) % p
    return R

def minv(M, p=P):
    """Inverse of square matrix over Fp via Gauss-Jordan. Raises on singular."""
    n = M.shape[0]
    A = np.hstack([M % p, np.eye(n, dtype=np.int64)]).astype(np.int64)
    for col in range(n):
        piv = -1
        for i in range(col, n):
            if A[i, col] % p != 0:
                piv = i; break
        assert piv >= 0, "singular"
        A[[col, piv]] = A[[piv, col]]
        inv = modinv(A[col, col], p)
        A[col] = (A[col]*inv) % p
        for i in range(n):
            if i != col and A[i, col] != 0:
                A[i] = (A[i] - A[i, col]*A[col]) % p
    return A[:, n:] % p

def subspace_trace(S, B, p=P):
    """Trace of operator S (d x d) on subspace spanned by rows of B (k x d)."""
    k = B.shape[0]
    if k == 0:
        return 0
    G = (B @ B.T) % p
    Ginv = minv(G, p)
    T = _mmul(B, S, B.T, Ginv, p=p)
    return int(np.trace(T) % p)

def kernel_trace(A, S_V, S_W, p=P):
    """Trace of S_V on ker(A), given intertwining A S_V = S_W A. A: m x d."""
    m, d = A.shape
    k, N = nullspace_mod(A % p, p)
    if k == 0:
        return 0
    G = (N @ N.T) % p
    Ginv = minv(G, p)
    T = _mmul(N, S_V, N.T, Ginv, p=p)
    return int(np.trace(T) % p)

def partitions_upto(n):
    if n == 0:
        yield []
        return
    def rec(remaining, maxv, cur):
        if remaining == 0:
            yield list(cur); return
        for v in range(min(maxv, remaining), 0, -1):
            cur.append(v)
            yield from rec(remaining-v, v, cur)
            cur.pop()
    yield from rec(n, n, [])

def perm_from_cycle_type(ct):
    n = sum(ct)
    sigma = [0]*n
    i = 0
    for L in ct:
        for t in range(L):
            sigma[i+t] = i + (t+1) % L
        i += L
    return sigma

def cycle_counts(sigma):
    n = len(sigma)
    seen = [False]*n
    from collections import Counter
    c = Counter()
    for i in range(n):
        if not seen[i]:
            j = i; L = 0
            while not seen[j]:
                seen[j] = True; j = sigma[j]; L += 1
            c[L] += 1
    return c

def S_H1(sigma, n, p=P):
    # H1 basis order from build_H
    mons, _, _ = build_H(n)
    H1 = mons[1]
    h1idx = {m: k for k, m in enumerate(H1)}
    d = len(H1)
    S = np.zeros((d, d), dtype=np.int64)
    for j, m in enumerate(H1):
        g = m[0]
        pt, tp = g//2, g % 2
        img = 2*sigma[pt] + tp
        i = h1idx[(img,)]
        S[i, j] = 1
    return S

def S_Hexterior(sigma, mons_deg, n, p=P):
    # action on exterior monomials of fixed degree (before quotient): signed
    idx = {m: k for k, m in enumerate(mons_deg)}
    d = len(mons_deg)
    S = np.zeros((d, d), dtype=np.int64)
    for j, m in enumerate(mons_deg):
        # image generators
        imgs = []
        for g in m:
            pt, tp = g//2, g % 2
            imgs.append(2*sigma[pt] + tp)
        # sign of sort
        inv = 0
        for a in range(len(imgs)):
            for b in range(a+1, len(imgs)):
                if imgs[a] > imgs[b]:
                    inv += 1
        key = tuple(sorted(imgs))
        i = idx.get(key)
        if i is not None:
            S[i, j] = 1 if inv % 2 == 0 else p-1
    return S

def S_G(sigma, pairs, gindex, p=P):
    ng = len(pairs)
    S = np.zeros((ng, ng), dtype=np.int64)
    for j, (i, jj) in enumerate(pairs):
        key = tuple(sorted([sigma[i], sigma[jj]]))
        S[gindex[key], j] = 1
    return S

def char_H2(n, sigma, p=P):
    mons, _, _ = build_H(n)
    # all degree-2 exterior monomials incl forbidden
    N = 2*n
    allm2 = [tuple(sorted([a, b])) for a in range(N) for b in range(a+1, N)]
    S = S_Hexterior(sigma, allm2, n, p)
    idx = {m: k for k, m in enumerate(allm2)}
    forb = [idx[tuple(sorted([2*i, 2*i+1]))] for i in range(n)]
    B = np.zeros((n, len(allm2)), dtype=np.int64)
    for r, c in enumerate(forb):
        B[r, c] = 1
    tr_whole = int(np.trace(S) % p)
    tr_sub = subspace_trace(S, B)
    return (tr_whole - tr_sub) % p

def char_H3(n, sigma, p=P):
    mons, _, _ = build_H(n)
    N = 2*n
    allm3 = [tuple(sorted(t)) for t in itertools.combinations(range(N), 3)]
    S = S_Hexterior(sigma, allm3, n, p)
    idx = {m: k for k, m in enumerate(allm3)}
    # forbidden subspace: monomials containing some a_i b_i
    forb = [k for k, m in enumerate(allm3)
            if any((2*i in m) and (2*i+1 in m) for i in range(n))]
    tr_whole = int(np.trace(S) % p)
    if not forb:
        return tr_whole
    B = np.zeros((len(forb), len(allm3)), dtype=np.int64)
    for r, c in enumerate(forb):
        B[r, c] = 1
    tr_sub = subspace_trace(S, B)
    return (tr_whole - tr_sub) % p

def build_F11_data(n, p=P):
    mons, _, _ = build_H(n)
    H1 = mons[1]; H2 = mons[2]; H3 = mons.get(3, [])
    h1idx = {m: k for k, m in enumerate(H1)}
    h2idx = {m: k for k, m in enumerate(H2)}
    h3idx = {m: k for k, m in enumerate(H3)}
    pairs = pairs_list(n); ng = len(pairs)
    d1 = len(H1)
    F = d1*ng
    def f11(hi, gi):
        return hi*ng + gi
    R = np.zeros((2*ng, F), dtype=np.int64)
    for k, (i, j) in enumerate(pairs):
        R[2*k, f11(h1idx[(2*i,)], k)] += 1
        R[2*k, f11(h1idx[(2*j,)], k)] -= 1
        R[2*k+1, f11(h1idx[(2*i+1,)], k)] += 1
        R[2*k+1, f11(h1idx[(2*j+1,)], k)] -= 1
    R %= p
    Delta = np.zeros((ng, len(H2)), dtype=np.int64)
    for k, (i, j) in enumerate(pairs):
        Delta[k, h2idx[tuple(sorted([2*i, 2*j+1]))]] += 1
        Delta[k, h2idx[tuple(sorted([2*i+1, 2*j]))]] -= 1
    Delta %= p
    fmat = np.zeros((F, len(H3)), dtype=np.int64)
    for hi, h in enumerate(H1):
        for k in range(ng):
            row = f11(hi, k)
            for c, m2 in enumerate(H2):
                coef = int(Delta[k, c])
                if coef == 0:
                    continue
                r = cup(h, m2, None, n)
                if r is None:
                    continue
                _, m3, s = r
                fmat[row, h3idx[m3]] = (fmat[row, h3idx[m3]] + coef*s)
    return dict(H1=H1, H2=H2, H3=H3, pairs=pairs, ng=ng, d1=d1, R=R, fmat=fmat % p,
                h1idx=h1idx, f11=f11)

def char_E3(n, sigma, p=P, cache=None):
    pairs = pairs_list(n)
    gindex = {pp: k for k, pp in enumerate(pairs)}
    # E01 trace = # fixed edges
    SG = S_G(sigma, pairs, gindex, p)
    trE01 = int(np.trace(SG) % p)
    trH2 = char_H2(n, sigma, p)
    trE20 = (trH2 - trE01) % p
    # E11
    D = cache[n]
    H1, H3, ng, d1 = D['H1'], D['H3'], D['ng'], D['d1']
    R, fmat, h1idx, f11 = D['R'], D['fmat'], D['h1idx'], D['f11']
    SH1 = S_H1(sigma, n, p)
    # S on F11 = SH1 tensor SG
    SF = np.kron(SH1, SG) % p  # ordering hi*ng+gi matches kron? kron gives (hi,gi) row-major: yes
    # S on H3
    SH3 = S_Hexterior(sigma, [m for m in H3], n, p) if H3 else np.zeros((0, 0), dtype=np.int64)
    # traces
    trF = int(np.trace(SF) % p)
    # row-space trace of R
    # row space basis: row-reduce R to nonzero rows
    # get basis via RREF rows: use nullspace of orthogonal complement? simpler: row-space basis from SVD-like: take R, row-echelon nonzero rows
    M = R.copy() % p
    m_, d_ = M.shape
    row = 0
    for col in range(d_):
        piv = -1
        for i in range(row, m_):
            if M[i, col] % p != 0:
                piv = i; break
        if piv < 0:
            continue
        M[[row, piv]] = M[[piv, row]]
        inv = modinv(M[row, col])
        M[row] = (M[row]*inv) % p
        for i in range(m_):
            if i != row and M[i, col] != 0:
                M[i] = (M[i] - M[i, col]*M[row]) % p
        row += 1
    Brow = M[:row]  # row-space basis
    trR = subspace_trace(SF, Brow) if row else 0
    trQ = (trF - trR) % p
    trkerF = kernel_trace(fmat.T % p, SF, SH3, p)  # ker(fmat: F->H3): A=fmat.T? careful:
    # kernel_trace(A,S_V,S_W) expects A: m x d with A S_V = S_W A. Here map is fmat^T? We have fmat F x H3 acting on row vectors? Our convention: vectors are columns? Let's verify: f(v) = fmat^T v? Fix: define A = fmat.T (H3 x F): A (S_H3^T? ...). Since our S matrices act on column vecs on the left and intertwine as A S_V = S_W A, need A = fmat.T with S_V=SF, S_W=SH3.
    # Check: (fmat.T @ SF == SH3 @ fmat.T)?
    return dict(trE20=trE20, trF=trF, trR=trR, trQ=trQ, trkerF=trkerF,
                trH2=trH2, trE01=trE01, trH3=char_H3(n, sigma, p))

if __name__ == '__main__':
    import sys
    cache = {n: build_F11_data(n) for n in range(2, 8)}
    # verify intertwining on a sample
    for n in range(2, 8):
        D = cache[n]
        H1, H3, ng, d1 = D['H1'], D['H3'], D['ng'], D['d1']
        R, fmat = D['R'], D['fmat']
        pairs = pairs_list(n); gindex = {pp: k for k, pp in enumerate(pairs)}
        ct = [2] + [1]*(n-2) if n >= 2 else []
        sigma = perm_from_cycle_type(ct)
        SH1 = S_H1(sigma, n); SG = S_G(sigma, pairs, gindex)
        SF = np.kron(SH1, SG) % P
        SH3 = S_Hexterior(sigma, [m for m in H3], n) if H3 else np.zeros((0, 0), dtype=np.int64)
        A = fmat.T % P
        lhs = (A @ SF) % P
        rhs = (SH3 @ A) % P if H3 else np.zeros_like(lhs)
        print(f"n={n} intertwine_ok={np.array_equal(lhs, rhs)} F={A.shape[1]} H3={A.shape[0]}")
