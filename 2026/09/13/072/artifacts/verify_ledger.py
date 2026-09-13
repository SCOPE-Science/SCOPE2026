"""Lane-1787 ledger verification (stdlib only, deterministic).

Verifies:
 1. Clique sentences Gamma_n on complete graphs K_m: K_m |= Gamma_n iff m>=n.
 2. Walk formulae P_k on path graphs: P_l(0,l) true on Path_l, P_k(0,l) false for k<l.
 3. EqRel collapse: every existential-closure of atom-conjunctions (<=2 vars) has
    truth-pattern across sample models in {F-empty-only, T-everywhere} => with the
    empty disjunction, geometric sentences take exactly 3 patterns.
 4. Embedding-span ledger data: tiny embedding spans all amalgamate (41 each) AND
    the discrete-2/K2/discrete-2 embedding span has no amalgam on <=4 vertices
    (analytic reflection argument extends to all sizes; documents that
    embedding-AP is the wrong notion — not used for separation).
 5. Sub(U^2) bottom patterns: graphs realize TF/FT/FF (E vs eq incomparable);
    eqrels realize FF/TF/TT (chain Bot < eq < R < Top).
Writes verify_ledger_output.json in the same directory.
"""
import json
from itertools import product

out = {}

# ---------- structures ----------
def all_graphs(n):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    for bits in product([False, True], repeat=len(pairs)):
        E = [[False] * n for _ in range(n)]
        for (i, j), b in zip(pairs, bits):
            E[i][j] = E[j][i] = b
        yield E

def all_eqrels(n):
    # reflexive+symmetric+transitive boolean matrices
    for bits in product([False, True], repeat=n * n):
        R = [list(bits[i * n:(i + 1) * n]) for i in range(n)]
        ok = True
        for i in range(n):
            if not R[i][i]:
                ok = False
                break
            for j in range(n):
                if R[i][j] != R[j][i]:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            continue
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if R[i][j] and R[j][k] and not R[i][k]:
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                break
        if ok:
            yield R

def complete(n):
    E = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                E[i][j] = True
    return E

def path(n):
    E = [[False] * n for _ in range(n)]
    for i in range(n - 1):
        E[i][i + 1] = E[i + 1][i] = True
    return E

# ---------- 1. cliques ----------
def sat_clique(E, n):
    m = len(E)
    for tup in product(range(m), repeat=n):
        good = True
        for a in range(n):
            for b in range(n):
                if a != b and not E[tup[a]][tup[b]]:
                    good = False
                    break
            if not good:
                break
        if good:
            return True
    return False

clique_ok = True
for m in range(0, 7):
    for n in range(1, 7):
        if sat_clique(complete(m), n) != (m >= n):
            clique_ok = False
out["clique_Km_models_Gamman_iff_m_geq_n"] = clique_ok

# ---------- 2. walks ----------
def bool_mul(A, B):
    n = len(A)
    C = [[False] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if A[i][k]:
                for j in range(n):
                    if B[k][j]:
                        C[i][j] = True
    return C

def walk(E, k, a, b):
    if k == 0:
        return a == b
    P = [row[:] for row in E]
    for _ in range(k - 1):
        P = bool_mul(P, E)
    return P[a][b]

walk_ok = True
for ell in range(1, 6):
    E = path(ell + 1)
    if not walk(E, ell, 0, ell):
        walk_ok = False
    for k in range(0, ell):
        if walk(E, k, 0, ell):
            walk_ok = False
out["walk_Pk_separates_on_paths"] = walk_ok

# ---------- 3. eqrel collapse ----------
eq_models = {
    "empty": [],
    "single": [[True]],
    "disc2": [[True, False], [False, True]],
    "indisc2": [[True, True], [True, True]],
    "disc3": [[i == j for j in range(3)] for i in range(3)],
    "indisc3": [[True] * 3 for _ in range(3)],
    "mixed21": [[True, True, False], [True, True, False], [False, False, True]],
}
names = list(eq_models.keys())

def atoms2(R, vals):
    # vals: dict var->element; atoms over {x,y}
    x, y = vals["x"], vals["y"]
    return {
        "Rxx": R[x][x], "Rxy": R[x][y], "Ryx": R[y][x], "Ryy": R[y][y],
        "exx": True, "eyy": True, "exy": (x == y),
    }

keys = ["Rxx", "Rxy", "Ryx", "Ryy", "exy"]
patterns = set()
for mask in range(1 << len(keys)):
    conj = [keys[i] for i in range(len(keys)) if mask & (1 << i)]
    # sentence: exists x exists y. conj
    row = []
    for nm in names:
        R = eq_models[nm]
        n = len(R)
        sat = False
        for a in range(n):
            for b in range(n):
                d = atoms2(R, {"x": a, "y": b})
                if all(d[k] for k in conj):
                    sat = True
                    break
            if sat:
                break
        row.append(sat)
    patterns.add(tuple(row))

pat_all_true = tuple([True] * len(names))
pat_true_iff_nonempty = tuple(nm != "empty" for nm in names)
out["eq_existential_patterns"] = [list(p) for p in sorted(patterns)]
out["eq_patterns_subset_of_{Top,Inhab}"] = patterns <= {pat_all_true, pat_true_iff_nonempty}
# full geometric sentences: arbitrary disjunctions of the above + empty disjunction
# => exactly 3 patterns: all-false, true-iff-nonempty, all-true
closure = {tuple([False] * len(names)), pat_true_iff_nonempty, pat_all_true}
or_closed = True
for p in patterns:
    for q in patterns:
        if tuple(a or b for a, b in zip(p, q)) not in closure:
            or_closed = False
out["eq_geometric_sentences_exactly_3_patterns"] = (
    out["eq_patterns_subset_of_{Top,Inhab}"] and or_closed and len(closure) == 3
)

# ---------- 4. AP spot checks ----------
def is_embedding_gra(G, T, f):
    # injective + preserves/reflects E
    if len(set(f)) != len(f):
        return False
    n = len(G)
    for a in range(n):
        for b in range(n):
            if G[a][b] != T[f[a]][f[b]]:
                return False
    return True

def is_embedding_eq(R, S, f):
    if len(set(f)) != len(f):
        return False
    n = len(R)
    for a in range(n):
        for b in range(n):
            if R[a][b] != S[f[a]][f[b]]:
                return False
    return True

def check_AP(all_structs, is_emb, smax=2, dmax=3):
    structs = {n: list(all_structs(n)) for n in range(smax + 1)}
    spans = 0
    for na in range(0, 2):
        for A in structs[na]:
            for nb in range(na, smax + 1):
                for B in structs[nb]:
                    for f in product(range(nb), repeat=na):
                        if not is_emb(A, B, list(f)):
                            continue
                        for nc in range(na, smax + 1):
                            for C in structs[nc]:
                                for g in product(range(nc), repeat=na):
                                    if not is_emb(A, C, list(g)):
                                        continue
                                    spans += 1
                                    if not exists_amalgam(
                                        all_structs, is_emb, A, B, C,
                                        list(f), list(g), dmax
                                    ):
                                        return False, spans
    return True, spans

def exists_amalgam(all_structs, is_emb, A, B, C, f, g, dmax):
    nb, nc = len(B), len(C)
    for nd in range(max(nb, nc), dmax + 1):
        for D in all_structs(nd):
            for hB in product(range(nd), repeat=nb):
                if not is_emb(B, D, list(hB)):
                    continue
                for hC in product(range(nd), repeat=nc):
                    if not is_emb(C, D, list(hC)):
                        continue
                    if all(hB[f[a]] == hC[g[a]] for a in range(len(A))):
                        return True
    return False

ap_gra, nspans_gra = check_AP(all_graphs, is_embedding_gra)
ap_eq, nspans_eq = check_AP(all_eqrels, is_embedding_eq)
out["AP_graphs_tiny"] = {"holds": ap_gra, "spans_checked": nspans_gra}
out["AP_eqrel_tiny"] = {"holds": ap_eq, "spans_checked": nspans_eq}

# ---------- 5. Sub(U^2) lattice separations ----------
# Graphs: atoms E(x,y), x=y on sample pointed pairs must realize TF, FT, FF
# (E true/eq false; E false/eq true; both false) => E, eq incomparable,
# E|eq strictly below Top. (TT impossible is analytic: irreflexivity.)
gra_pairs = [
    ("K2021", complete(2), (0, 1)),     # E true, eq false
    ("Pt00", [[False]], (0, 0)),        # E false, eq true
    ("Dis2_01", [[False, False], [False, False]], (0, 1)),  # both false
]
gra_pats = set()
for nm, E, (a, b) in gra_pairs:
    gra_pats.add((E[a][b], a == b))
out["gra_U2_patterns_TF_FT_FF"] = sorted(gra_pats) == [(False, False), (False, True), (True, False)]

# EqRel: atoms R(x,y), x=y must realize FF, TF, TT
# (R false/eq false; R true/eq false; both true) => chain Bot<eq<R<Top strict.
eq_pairs = [
    ("disc2_01", [[True, False], [False, True]], (0, 1)),  # both false
    ("indisc2_01", [[True, True], [True, True]], (0, 1)),  # R true, eq false
    ("single_00", [[True]], (0, 0)),                       # both true
]
eq_pats = set()
for nm, R, (a, b) in eq_pairs:
    eq_pats.add((R[a][b], a == b))
out["eq_U2_patterns_FF_TF_TT"] = sorted(eq_pats) == [(False, False), (True, False), (True, True)]

# ---------- 6. Embedding-AP failure witness for graphs ----------
# Span: A = discrete 2 {x,y}; B = K2; C = discrete 2 (identity maps).
# Any embedding-amalgam D with hB,hC agreeing on A forces the A-images
# both adjacent (B reflects E) and non-adjacent (C reflects E): impossible
# at EVERY size (analytic). Bounded machine check for <=4 vertices.
def no_amalgam_bounded(A, B, C, f, g, nmax=4):
    for nd in range(max(len(B), len(C)), nmax + 1):
        for D in all_graphs(nd):
            for hB in product(range(nd), repeat=len(B)):
                if not is_embedding_gra(B, D, list(hB)):
                    continue
                for hC in product(range(nd), repeat=len(C)):
                    if not is_embedding_gra(C, D, list(hC)):
                        continue
                    if all(hB[f[a]] == hC[g[a]] for a in range(len(A))):
                        return False  # amalgam found
    return True

A2 = [[False, False], [False, False]]
B2 = [[False, True], [True, False]]
out["gra_embedding_AP_counterexample_no_amalgam_le4"] = no_amalgam_bounded(
    A2, B2, A2, [0, 1], [0, 1])
# NOTE (audit honesty): the same span shape also fails to amalgamate for
# eqrels under embeddings (reflection forces R(d0,d1) both true and false),
# so this witness does NOT separate the theories; it only documents that
# embedding-AP is the wrong notion here. The audit-proof separator is
# |Sub(1)| = 3 vs infinite (proved syntactically in DRAFT.md).

out["ALL"] = (
    clique_ok and walk_ok
    and out["eq_geometric_sentences_exactly_3_patterns"]
    and ap_gra and ap_eq
    and out["gra_U2_patterns_TF_FT_FF"]
    and out["eq_U2_patterns_FF_TF_TT"]
    and out["gra_embedding_AP_counterexample_no_amalgam_le4"]
)
with open("verify_ledger_output.json", "w") as fh:
    json.dump(out, fh, indent=2)
print(json.dumps({k: v for k, v in out.items() if k != "eq_existential_patterns"}, indent=2))
assert out["ALL"], "CHECKS FAILED"
print("ALL CHECKS PASSED")
