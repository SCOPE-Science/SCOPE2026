"""Finite-window satisfiability for per-pair Z-invariant graphs (diversity rescues Rado).

Universe: orbits 0..K-1 x positions 0..P-1, edges Z-invariant per pair:
E((i,m),(j,n)) depends on (i,j,n-m), not just (1_{i=j},n-m).
Variables identified under symmetry M[i,j,d]=M[j,i,-d], M[i,i,d]=M[i,i,-d],
M[i,i,0]=False. Small case K=3,P=3 with requirements
R1=(U={(0,0)},V={}) and R2=(U={(0,0),(1,0)},V={(2,0)}).
Result: satisfiable (witness assignment found), contrasting uniform impossibility.
Generalizes to full existence proof by finite extensions (see DRAFT.md).
"""
K, P = 3, 3


def canon(i, j, d):
    if i > j:
        return (j, i, -d)
    return (i, j, d)


def edge_key(i, m, j, n):
    if (i, m) == (j, n):
        return None
    return canon(i, j, n - m)


pairs = [((i, m), (j, n)) for i in range(K) for m in range(P)
         for j in range(K) for n in range(P) if not (i == j and m == n)]
keys = set(edge_key(i, m, j, n) for (i, m), (j, n) in pairs)
keys.discard(None)

parent = {}


def find(a):
    while parent.get(a, a) != a:
        a = parent[a]
    return a


for k in list(keys):
    i, j, d = k
    if i == j:
        a = find(k)
        b = find(canon(i, j, -d))
        if a != b:
            parent[a] = b

reps = {}
for k in keys:
    r = find(k)
    reps.setdefault(r, []).append(k)
rep_list = list(reps.keys())
print("orbits of vars:", len(rep_list))

R1 = ({(0, 0)}, set())
R2 = ({(0, 0), (1, 0)}, {(2, 0)})
reqs = [R1, R2]

sat = None
for mask in range(2 ** len(rep_list)):
    val = {r: bool((mask >> t) & 1) for t, r in enumerate(rep_list)}
    if any(val[r] for r in rep_list if r[0] == r[1] and r[2] == 0):
        continue

    def adj(a, b):
        return val[find(edge_key(a[0], a[1], b[0], b[1]))]

    good = True
    for (U, V) in reqs:
        found = False
        for kk in range(K):
            for w in range(P):
                x = (kk, w)
                if x in U or x in V:
                    continue
                if all(adj(x, u) for u in U) and all(not adj(x, v) for v in V):
                    found = True
                    break
            if found:
                break
        if not found:
            good = False
            break
    if good:
        sat = val
        break
print("satisfiable:", sat is not None)
assert sat is not None
print("PER-PAIR SATISFIABILITY CONFIRMED.")
