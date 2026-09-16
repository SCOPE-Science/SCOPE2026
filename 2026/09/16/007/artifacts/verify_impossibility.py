"""Numerical verification for universal cut-and-glue impossibility (D=2 hPEPS).

Checks:
1. Cat-family contraction: homogeneous D=2 tensor A(v1,v2) on 2x3 torus == |v1>^Tn + |v2>^Tn.
2. Dichotomy for any fixed non-zero patch operator C (m=4 qubits, dim 16):
   (a) generic C has rank>=2 on Sym^m -> explicit pair (v,w) with C|v>^Tm, C|w>^Tm
       linearly independent (wedge norm>0), and filtered cat has rank-2 patch marginal.
   (b) rank-1 C on Sym^m -> binary-form root v* with C|v*>^Tm = 0 (kill).
   (c) rank-0 C on Sym^m -> kills every product.
All deterministic (fixed seed). Uses only numpy.
"""
import numpy as np

rng = np.random.default_rng(0)
TOL = 1e-8

def kron_pow(v, m):
    r = np.array([1.0 + 0j])
    for _ in range(m):
        r = np.kron(r, v)
    return r

def sym_basis(m):
    """Orthonormal Dicke basis of Sym^m(C^2): dim m+1. Returns 2^m x (m+1) matrix."""
    from itertools import product
    d = 2 ** m
    S = np.zeros((d, m + 1), dtype=complex)
    for k in range(m + 1):
        vec = np.zeros(d, dtype=complex)
        for bits in product([0, 1], repeat=m):
            if sum(bits) == k:
                idx = 0
                for b in bits:
                    idx = idx * 2 + b
                vec[idx] += 1.0
        vec /= np.linalg.norm(vec)
        S[:, k] = vec
    return S

def cat_amplitude(phys, v1, v2):
    a1 = 1.0 + 0j
    a2 = 1.0 + 0j
    for s, v in zip(phys, [v1] * len(phys)):
        pass
    # amplitude = prod_s v1[s] + prod_s v2[s]
    p1, p2 = 1.0 + 0j, 1.0 + 0j
    for s in phys:
        p1 *= v1[s]
        p2 *= v2[s]
    return p1 + p2

def contract_torus(W, H, v1, v2):
    """Brute-force contraction of homogeneous cat tensor on W x H torus.
    Tensor: A[p,l,r,u,d] = v1[p] if l=r=u=d=0; v2[p] if all 1; else 0.
    Bond edges: horizontal W*H edges + vertical W*H edges (periodic)."""
    n = W * H
    # index sites row-major; right-neighbor and down-neighbor bonds
    n_h = n  # horizontal bonds (one per site: right edge)
    n_v = n  # vertical bonds (one per site: down edge)
    n_bonds = n_h + n_v
    psi = np.zeros(2 ** n, dtype=complex)
    # iterate over all bond configs (2^12=4096 for 2x3)
    for bc in range(2 ** n_bonds):
        bits = [(bc >> k) & 1 for k in range(n_bonds)]
        h = bits[:n_h]  # h[site] = bond to right neighbor
        vv = bits[n_h:]  # vv[site] = bond to down neighbor
        ok = True
        # for each site, left=right-neighbor-bond of left neighbor etc; need consistency:
        # l = h[left(site)], r = h[site], u = vv[up(site)], d = vv[site]; require l==r==u==d else A=0
        site_vecs = []
        for y in range(H):
            for x in range(W):
                s = y * W + x
                ls = y * W + (x - 1) % W
                us = ((y - 1) % H) * W + x
                l, r = h[ls], h[s]
                u, d = vv[us], vv[s]
                if l == r == u == d == 0:
                    site_vecs.append(v1)
                elif l == r == u == d == 1:
                    site_vecs.append(v2)
                else:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            continue
        # add product vector tensor site_vecs
        full = np.array([1.0 + 0j])
        for sv in site_vecs:
            full = np.kron(full, sv)
        psi += full
    return psi

def wedge_norm(a, b):
    return float(np.sqrt(max(0.0, (np.vdot(a, a) * np.vdot(b, b) - abs(np.vdot(a, b)) ** 2).real)))

def patch_rdm_eigs(a1, b1, a2, b2):
    """State |P> = |a1>|b1> + |a2>|b2>; patch marginal eigenvalues (normalized)."""
    P = np.kron(a1, b1) + np.kron(a2, b2)
    nrm = np.vdot(P, P).real
    P /= np.sqrt(nrm)
    da, db = len(a1), len(b1)
    M = P.reshape(da, db)
    sv = np.linalg.svd(M, compute_uv=False)
    return (sv ** 2), float(nrm)

def find_root_of_binary_form(coef):
    """coef[k] for monomial x^{m-k} y^k. Return projective root v*=(x,y) with f=0."""
    m = len(coef) - 1
    # try affine chart x=1: poly in z=y
    poly = coef[::-1]  # coef for z^k
    # strip leading zeros for numpy.roots
    p = np.trim_zeros(np.array(poly[::-1]), 'f')  # highest-degree first trimmed
    if len(p) == 0:
        raise AssertionError("zero polynomial has no isolated root (rank-0 case)")
    if len(p) == 1:
        # f = c*x^m -> root (0,1)
        return np.array([0.0, 1.0], dtype=complex)
    roots = np.roots(p[::-1]) if False else np.roots(p)
    # np.roots expects highest first; p is highest-first after trim? ensure:
    z = roots[0]
    return np.array([1.0, z], dtype=complex)

print("=== 1. cat contraction on 2x3 torus ===")
v1 = np.array([1.0, 0.0], dtype=complex)
v2 = np.array([1.0, 1.0], dtype=complex) / np.sqrt(2)
W, H, n = 2, 3, 6
psi = contract_torus(W, H, v1, v2)
from itertools import product as iprod
mx = 0.0
for bits in iprod([0, 1], repeat=n):
    idx = sum(b << (n - 1 - i) for i, b in enumerate(bits))
    mx = max(mx, abs(psi[idx] - cat_amplitude(bits, v1, v2)))
print(f"max |contracted - cat| = {mx:.2e}")
assert mx < 1e-8, "cat contraction mismatch"
print("PASS: homogeneous D=2 tensor contracts to |v1>^Tn + |v2>^Tn")

print("\n=== 2a. generic C: rank>=2 on Sym, violating pair ===")
m = 4
d = 2 ** m
S = sym_basis(m)
X = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
Cgen = X  # generic invertible
M = Cgen @ S
svals = np.linalg.svd(M, compute_uv=False)
rank = int((svals > 1e-6).sum())
print(f"rank(C|_Sym) = {rank} (dim Sym = {m+1}), top sv = {svals[:3]}")
assert rank >= 2
best = (0, None, None)
for _ in range(4000):
    a = rng.standard_normal(2) + 1j * rng.standard_normal(2)
    b = rng.standard_normal(2) + 1j * rng.standard_normal(2)
    a /= np.linalg.norm(a)
    b /= np.linalg.norm(b)
    w = wedge_norm(Cgen @ kron_pow(a, m), Cgen @ kron_pow(b, m))
    if w > best[0]:
        best = (w, a.copy(), b.copy())
w, va, vb = best
print(f"best wedge ||C|va>^m ^ C|vb>^m|| = {w:.4f}")
assert w > 0.1
a1, a2 = Cgen @ kron_pow(va, m), Cgen @ kron_pow(vb, m)
b1, b2 = kron_pow(va, n - m), kron_pow(vb, n - m)
eigs, nrm = patch_rdm_eigs(a1, b1, a2, b2)
print(f"filtered norm^2 = {nrm:.4f} (nonzero); patch RDM eigs = {eigs}")
assert nrm > TOL and (eigs > 1e-6).sum() == 2
print("PASS: filtered cat entangled across R|complement -> R marginal mixed (rank 2)")

print("\n=== 2b. rank-1 C = |e><s|, s=<0|^Tm: collinear but kills a product ===")
e = np.zeros(d, dtype=complex); e[0] = 1.0
s = np.zeros(d, dtype=complex); s[0] = 1.0
C1 = np.outer(e, s.conj())
M1 = C1 @ S
r1 = int((np.linalg.svd(M1, compute_uv=False) > 1e-6).sum())
print(f"rank(C1|_Sym) = {r1}")
assert r1 == 1
vstar = np.array([0.0, 1.0])  # f(v)=x^m root
kill = np.linalg.norm(C1 @ kron_pow(vstar, m))
print(f"||C1|v*>^m|| = {kill:.2e} for v*=(0,1)")
assert kill < TOL
print("PASS: rank-1 filter annihilates product hPEPS |1>^Tn (zero, not a pure state)")

print("\n=== 2c. rank-1 C with random bra: FTA root kills ===")
sr = (rng.standard_normal(d) + 1j * rng.standard_normal(d))
sr /= np.linalg.norm(sr)
er = (rng.standard_normal(d) + 1j * rng.standard_normal(d)); er /= np.linalg.norm(er)
Cr = np.outer(er, sr.conj())
Mr = Cr @ S
rr = int((np.linalg.svd(Mr, compute_uv=False) > 1e-8).sum())
print(f"rank(Cr|_Sym) = {rr}")
assert rr == 1
# binary form coefficients: f(x,y)=sum_k coef[k] x^{m-k} y^k via Dicke coeffs
t = S.conj().T @ sr  # components of s in Dicke basis (up to norm factors)
# |v>^Tm Dicke components: sqrt(C(m,k)) x^{m-k} y^k / ... account: (S[:,k] unit) overlap:
# f = sum_k conj(sr).S[:,k]-component... directly: f(v) = sr* . kron_pow(v)
import math
coef = np.zeros(m + 1, dtype=complex)
for k in range(m + 1):
    coef[k] = math.sqrt(math.comb(m, k)) * (S[:, k].conj() @ sr).conj() * 0 + 1  # placeholder
# simpler: evaluate f on (1,z) on m+1 points and interpolate coefficients
zs = np.exp(2j * np.pi * np.arange(m + 1) / (m + 1)) * 0.7
V = np.vander(zs, m + 1, increasing=True)  # V[j,k]=zs[j]^k
fv = np.array([np.vdot(sr, kron_pow(np.array([1.0, z]), m)) for z in zs])
ck = np.linalg.solve(V, fv)  # coef of z^k in f(1,z)
p = ck[::-1]  # highest-first
p_trim = np.trim_zeros(p, 'f')
if len(p_trim) <= 1:
    vstar2 = np.array([0.0, 1.0], dtype=complex)
else:
    zr = np.roots(p_trim)[0]
    vstar2 = np.array([1.0, zr], dtype=complex)
res = abs(np.vdot(sr, kron_pow(vstar2, m)))
print(f"|f(v*)| = {res:.2e}, v* = {vstar2}")
assert res < 1e-6
print("PASS: generic rank-1 filter has projective root -> zero post-selection")

print("\n=== 2d. Sym-killer C = I - P_sym ===")
Psym = S @ S.conj().T
Ck = np.eye(d) - Psym
rk = (np.linalg.svd(Ck @ S, compute_uv=False) > 1e-8).sum()
print(f"rank(Ck|_Sym) = {rk}")
assert rk == 0
for vt in [np.array([1.0, 0.0]), np.array([0.0, 1.0]), np.array([1.0, 1.0]) / np.sqrt(2)]:
    assert np.linalg.norm(Ck @ kron_pow(vt, m)) < 1e-8
print("PASS: Sym-killer annihilates every product hPEPS")

print("\nALL CHECKS PASSED")
