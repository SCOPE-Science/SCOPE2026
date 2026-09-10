"""Brute-force cross-check: |U_n|,|C1_n|,|C2_n| for n<=8 by direct pattern matching."""
import itertools

def std(p):
    s = sorted(p)
    r = {v: i+1 for i, v in enumerate(s)}
    return tuple(r[v] for v in p)

P2413 = (2,4,1,3); P3142 = (3,1,4,2)
T1 = (1,2,3,6,5,4); T2 = (3,2,1,6,5,4)

def avoids(p, pats):
    n = len(p)
    for q in pats:
        k = len(q)
        if k > n: continue
        for idx in itertools.combinations(range(n), k):
            if std([p[i] for i in idx]) == q:
                return False
    return True

for n in range(1, 9):
    u = c1 = c2 = 0
    for p in itertools.permutations(range(1, n+1)):
        if not avoids(p, [P2413, P3142]): continue
        u += 1
        if avoids(p, [T1]): c1 += 1
        if avoids(p, [T2]): c2 += 1
    print(f"n={n}: U={u} C1={c1} C2={c2}", flush=True)
