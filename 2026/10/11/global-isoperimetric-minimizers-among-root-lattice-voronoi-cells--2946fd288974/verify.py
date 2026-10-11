from functools import lru_cache

h = (1,2,3,4,4,4,3,2)

# Complete residue multiplication table and equality criterion.
for a in range(8):
    for b in range(8):
        assert h[a]*h[b] >= h[(a+b) % 8]
        assert (h[a]*h[b] == h[(a+b) % 8]) == (a == 0 or b == 0)

def irreducibles(max_rank):
    out = []
    for m in range(1, max_rank + 1):
        out.append((f"A{m}", m, m + 1))
        if m >= 4:
            out.append((f"D{m}", m, 4))
    if max_rank >= 6:
        out.append(("E6", 6, 3))
    if max_rank >= 7:
        out.append(("E7", 7, 2))
    if max_rank >= 8:
        out.append(("E8", 8, 1))
    return sorted(out, key=lambda z:(z[1], z[0]))

MAX = 256
types = irreducibles(MAX)

@lru_cache(None)
def best(d):
    if d == 0:
        return 1
    ans = None
    for _, r, det in types:
        if r > d:
            break
        v = det * best(d-r)
        ans = v if ans is None or v < ans else ans
    return ans

for d in range(1, MAX + 1):
    assert best(d) == h[d % 8]

def predicted_types(d):
    k, r = divmod(d, 8)
    sols = set()
    if r == 0:
        sols.add(tuple(["E8"]*k))
    elif r == 1:
        sols.add(tuple(sorted(["E8"]*k + ["A1"])))
    elif r == 2:
        sols.add(tuple(sorted(["E8"]*k + ["A2"])))
    elif r == 6:
        sols.add(tuple(sorted(["E8"]*k + ["E6"])))
    elif r == 7:
        sols.add(tuple(sorted(["E8"]*k + ["E7"])))
    elif r == 3:
        sols.add(tuple(sorted(["E8"]*k + ["A3"])))
        for j in range(1, k+1):
            sols.add(tuple(sorted(["E8"]*(k-j) + [f"D{8*j+3}"])))
    elif r in (4,5):
        for j in range(0, k+1):
            sols.add(tuple(sorted(["E8"]*(k-j) + [f"D{8*j+r}"])))
    return sols

# Enumerate equality decompositions canonically for moderate rank.
small_types = irreducibles(80)

@lru_cache(None)
def enum_min(d, start):
    if d == 0:
        return 1, {()}
    val = None
    sols = set()
    for idx in range(start, len(small_types)):
        name, r, det = small_types[idx]
        if r > d:
            break
        subv, subs = enum_min(d-r, idx)
        if subv is None:
            continue
        cur = det*subv
        cand = {(name,)+s for s in subs}
        if val is None or cur < val:
            val, sols = cur, cand
        elif cur == val:
            sols |= cand
    return val, sols

for d in range(2, 81):
    val, sols = enum_min(d, 0)
    assert val == h[d % 8]
    assert {tuple(sorted(s)) for s in sols} == predicted_types(d)

print("VERIFY_OK")
print("residue_table=complete")
print("minimum_determinants=ranks_1..256")
print("equality_types=ranks_2..80")
