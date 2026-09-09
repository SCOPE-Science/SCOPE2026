"""Step 2: count independent sets; exact Hochster regularity of S/I(G) over QQ-track.
Strategy: enumerate all independent sets; for each W subset compute reduced homology
of Ind(G[W]) over F_p (two primes) via numpy modular rank; max j-i-1+1 gives reg(S/I).
Then exact-rational recheck of witness subsets with sympy."""
import itertools
import numpy as np

n = 14
nbr = [set() for _ in range(n)]
for i in range(n):
    for d in (1, 3):
        nbr[i].add((i + d) % n)
        nbr[i].add((i - d) % n)

# enumerate independent sets as bitmasks
indsets = []
for mask in range(1 << n):
    ok = True
    for i in range(n):
        if mask >> i & 1:
            for w in nbr[i]:
                if w > i and (mask >> w & 1):
                    ok = False; break
            if not ok:
                break
    if ok:
        indsets.append(mask)
print("num independent sets:", len(indsets))

from math import comb
def popcount(m): return bin(m).count("1")

def mod_rank(mat, p):
    if mat.size == 0: return 0
    A = mat.astype(np.int64) % p
    r, c = A.shape
    rk = 0
    for j in range(c):
        piv = -1
        for i in range(rk, r):
            if A[i, j] % p != 0:
                piv = i; break
        if piv < 0: continue
        A[[rk, piv]] = A[[piv, rk]]
        inv = pow(int(A[rk, j]), -1, p)
        A[rk] = (A[rk]*inv) % p
        for i in range(r):
            if i != rk and A[i, j] % p != 0:
                A[i] = (A[i] - A[i, j]*A[rk]) % p
        rk += 1
    return rk

def homology_dims(faces_by_dim, p):
    # faces_by_dim[k] = list of k-dim faces (as sorted tuples), k=-1: [()] if nonempty
    maxd = len(faces_by_dim) - 2  # index shift: faces_by_dim[d+1] holds d-faces
    # build index maps
    idx = {}
    for d in range(-1, maxd + 1):
        for f in faces_by_dim[d + 1]:
            idx[(d, f)] = len([k for k in idx if k[0] == d])
    # simpler: per-dim index
    pos = {}
    for d in range(-1, maxd + 1):
        pos[d] = {f: k for k, f in enumerate(faces_by_dim[d + 1])}
    betti = {}
    ranks = {}
    # fbd[d+1] holds d-faces; ranks[d] = rank(C_d -> C_{d-1}), d=0..maxd+1
    ranks = {}
    for d in range(0, maxd + 2):
        rows = faces_by_dim[d] if d <= maxd + 1 else []       # (d-1)-faces
        cols = faces_by_dim[d + 1] if d + 1 <= maxd + 1 else []  # d-faces
        if not rows or not cols:
            ranks[d] = 0
            continue
        M = np.zeros((len(rows), len(cols)), dtype=np.int64)
        for j, f in enumerate(cols):
            for k in range(len(f)):
                g = f[:k] + f[k+1:]
                M[pos[d-1][g], j] = (-1)**k
        ranks[d] = mod_rank(M, p)
    for d in range(-1, maxd + 1):
        n_d = len(faces_by_dim[d + 1])
        b = n_d - ranks.get(d + 1, 0) - ranks.get(d, 0) if d >= 0 else n_d - ranks.get(0, 0)
        # careful: for d=-1, chain C_{-1} -> 0, ker = n_{-1} - rank(d_0)
        betti[d] = b
    return betti

def reg_of_quotient(p):
    best = 0; wit = []
    # group indsets by mask for face queries: precompute list
    for W in range(1 << n):
        j = popcount(W)
        if j == 0: continue
        # lower prune: max possible homological contribution: need j-i-1 >= ... ; track best j' - i'
        # faces: independent F subset of W
        # only need dims: for each possible i, check H_{j-i-1} != 0; i.e., any nonzero reduced homology dim t gives reg candidate j - (j - t - 1) ... let's just compute all
        faces = {}
        # collect by dim
        anyface = False
        maxd = -1
        for F in indsets:
            if F | W == W:  # F subset of W
                anyface = True
                t = popcount(F) - 1
                faces.setdefault(t, []).append(F)
        if not anyface:
            continue
        maxd = max(faces)
        # need vertex order for orientation: use sorted vertex tuple
        fbd = [[()]]  # index 0 = dim -1
        for d in range(0, maxd + 1):
            lst = []
            for F in faces.get(d, []):
                verts = tuple(i for i in range(n) if (F >> i) & 1 and (W >> i) & 1)
                lst.append(verts)
            fbd.append(lst)
        betti = homology_dims(fbd, p)
        for t, b in betti.items():
            if t >= 0 and b > 0:
                # j - i - 1 = t => (S/I) reg contribution: j - i = t + 1
                if t + 1 > best:
                    best = t + 1; wit = [(W, t, b)]
                elif t + 1 == best and len(wit) < 5:
                    wit.append((W, t, b))
    return best, wit

for p in (32003, 10007):
    best, wit = reg_of_quotient(p)
    print(f"p={p}: reg(S/I) = {best}")
    for W, t, b in wit[:5]:
        print(f"  W={W:014b} |W|={popcount(W)} H~_{t} dim={b}")
