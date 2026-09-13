"""Enumerate Heffter difference families for cyclic STS(21) and count Pasches."""
import itertools, json, math

V = 21
UNITS = [u for u in range(1, 21) if math.gcd(u, 21) == 1]

def diffs(block):
    d = set()
    for a, b in itertools.combinations(block, 2):
        d.add((b - a) % V)
        d.add((a - b) % V)
    return d

def norm(block):
    cands = []
    for c in block:
        cands.append(tuple(sorted((x - c) % V for x in block)))
    return min(cands)

cands = []
need = set(range(1, 21)) - {7, 14}
for x in range(1, V):
    for y in range(x + 1, V):
        T = (0, x, y)
        d = diffs(T)
        if len(d) == 6 and not (d & {7, 14}):
            cands.append((T, d))

print("num candidates:", len(cands), flush=True)

need_list = sorted(need)
covers = {}
for i, (T, d) in enumerate(cands):
    for e in d:
        covers.setdefault(e, []).append(i)

families = []
def bt(chosen, covered):
    if len(chosen) == 3:
        if covered == need:
            families.append(tuple(chosen))
        return
    for e in need_list:
        if e not in covered:
            first = e
            break
    for i in covers[first]:
        T, d = cands[i]
        if d & covered:
            continue
        if chosen and i <= chosen[-1]:
            continue
        bt(chosen + [i], covered | d)

bt([], set())
print("num raw families:", len(families), flush=True)

def apply_mult(fam, u):
    out = []
    for i in fam:
        T = cands[i][0]
        img = {(u * t) % V for t in T}
        out.append(norm(img))
    return tuple(sorted(out))

def canon(fam):
    return min(apply_mult(fam, u) for u in UNITS)

classes = {}
for fam in families:
    c = canon(fam)
    classes.setdefault(c, []).append(fam)

print("num multiplier classes:", len(classes), flush=True)

def blocks_of(rep):
    B = set()
    for t in range(V):
        B.add(tuple(sorted([(t) % V, (t + 7) % V, (t + 14) % V])))
    for base in rep:
        for t in range(V):
            B.add(tuple(sorted([(b + t) % V for b in base])))
    return B

def check_sts(B):
    assert len(B) == 70, len(B)
    seen = set()
    for b in B:
        for a, c in itertools.combinations(b, 2):
            p = (a, c)
            assert p not in seen, f"pair {p} twice"
            seen.add(p)
    assert len(seen) == 210

def pasch_count(B):
    bset = set(B)
    count = 0
    for X in itertools.combinations(range(V), 6):
        n = 0
        for b in itertools.combinations(X, 3):
            if b in bset:
                n += 1
                if n > 4:
                    break
        if n == 4:
            count += 1
        elif n > 4:
            raise AssertionError("6-set with >4 blocks!")
    return count

results = []
for rep, fams in sorted(classes.items()):
    B = blocks_of(rep)
    check_sts(B)
    p = pasch_count(B)
    results.append({"rep": [list(t) for t in rep], "n_families": len(fams), "pasch": p})

results.sort(key=lambda r: -r["pasch"])
for r in results:
    print(r["pasch"], r["rep"], "x", r["n_families"], flush=True)

cmax = results[0]["pasch"]
print("C_max =", cmax, "attained by", sum(1 for r in results if r["pasch"] == cmax), "classes")
with open("work/sts21_scan.json", "w") as f:
    json.dump({"C_max": cmax, "results": results}, f, indent=1)
