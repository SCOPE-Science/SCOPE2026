"""Certify preset fallback H1: n<=10, tau=4, nu=1, reg(S/I;Q)=4 + Betti table + witness."""
import sys, itertools, json
sys.path.insert(0, "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-745/output/artifacts")
from engine import *

# First n=9 focus hit (t=101, seed 746 log)
H = [(0,2,5),(0,2,6),(1,2,7),(1,3,4),(1,4,5),(1,5,8),(2,3,4),(2,5,7),
     (3,6,7),(3,6,8),(4,6,8),(4,7,8),(5,6,8),(6,7,8)]
n = 9
E = edges_of(H)
print("edges:", H)
print("3-uniform:", all(len(t) == 3 for t in H))

# --- tau: explicit 4-cover + exhaustive no-3-cover ---
found4 = None
for C in itertools.combinations(range(n), 4):
    cm = mask_of(C)
    if all((e & cm) != 0 for e in E):
        found4 = C
        break
print("4-cover:", found4)
n3 = 0
bad3 = []
for C in itertools.combinations(range(n), 3):
    n3 += 1
    cm = mask_of(C)
    if all((e & cm) != 0 for e in E):
        bad3.append(C)
print(f"3-subsets checked: {n3}, 3-covers found: {len(bad3)}")
assert found4 is not None and not bad3

# --- nu=1: every disjoint pair witnessed ---
dp = disjoint_pairs(E)
bad = unwitnessed_disjoint_pairs(E)
print(f"disjoint pairs: {len(dp)}, unwitnessed: {len(bad)}")
assert len(E) > 0 and not bad
# log witnesses for first few
for (i, j) in dp[:5]:
    u = E[i] | E[j]
    wit = [tuple(sorted(v for v in range(n) if (E[k] >> v) & 1))
           for k in range(len(E)) if k != i and k != j and (E[k] | u) == u]
    print(f"  pair {H[i]},{H[j]} witnessed by {wit[0]}")

# --- reg over Q-proxy and F2 + full tables ---
face = face_array(E, n)
rF2, wF2 = regularity(E, n, "f2", verbose_witness=True)
rQ, wQ = regularity(E, n, "qp", verbose_witness=True)
print("regF2:", rF2, "regQp:", rQ)
tabQ = betti_table(E, n, "qp")
tab2 = betti_table(E, n, "f2")
print("--- Betti (Q-proxy) ---"); print(fmt_betti(tabQ))
print("--- Betti (F2) ---"); print(fmt_betti(tab2))
print("Q-witnesses:", [(bin(w), h, d) for (w, h, d) in wQ])
# cross-check second prime
rQ2 = regularity(E, n, "qp", p=10007)
print("regQp(p=10007):", rQ2)

# --- 2-collage ---
col, C = min_2collage(E)
print(f"2-collage: {col} cap={2*col} e.g. {[H[c] for c in C]}")

json.dump({"edges": H, "n": n, "cover4": found4, "regQ": rQ, "regF2": rF2,
           "bettiQ": {f"{k}": v for k, v in tabQ.items()},
           "bettiF2": {f"{k}": v for k, v in tab2.items()},
           "witQ": [(w, h, d) for (w, h, d) in wQ],
           "collage": col},
          open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-745/output/artifacts/H1_cert.json", "w"), indent=1)
print("wrote H1_cert.json")
