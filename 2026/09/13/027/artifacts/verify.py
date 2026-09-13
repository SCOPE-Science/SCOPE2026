"""Deduplicate block sets, test isomorphism, recount Pasches independently."""
import itertools, json

V = 21
data = json.load(open("work/sts21_scan.json"))

def blocks_of(rep):
    B = set()
    for t in range(V):
        B.add(tuple(sorted([(t) % V, (t + 7) % V, (t + 14) % V])))
    for base in rep:
        for t in range(V):
            B.add(tuple(sorted([(b + t) % V for b in base])))
    return frozenset(B)

systems = [(r, blocks_of(tuple(tuple(t) for t in r["rep"]))) for r in data["results"]]
print("num multiplier-class systems:", len(systems), flush=True)
uniq = {}
for r, B in systems:
    uniq.setdefault(B, []).append(r["rep"])
print("num distinct block sets:", len(uniq), flush=True)
ulist = list(uniq.items())

def make_pairmap(B):
    pm = {}
    for b in B:
        for a, c in itertools.combinations(b, 2):
            pm[(a, c)] = b
    return pm

def extend(f, B1, pm2, s2):
    f = dict(f)
    used = set(f.values())
    changed = True
    while changed:
        changed = False
        for b in B1:
            mapped = [x for x in b if x in f]
            if len(mapped) == 3:
                a, c = f[b[0]], f[b[1]]
                key = (a, c) if a < c else (c, a)
                if key not in pm2:
                    return None
                if f[b[2]] not in set(pm2[key]):
                    return None
            elif len(mapped) == 2:
                m0, m1 = [x for x in b if x in f]
                un = [x for x in b if x not in f][0]
                a, c = f[m0], f[m1]
                key = (a, c) if a < c else (c, a)
                blk = pm2.get(key)
                if blk is None:
                    return None
                z = [w for w in blk if w != a and w != c][0]
                if z in used:
                    return None
                f[un] = z
                used.add(z)
                changed = True
    if len(f) == V:
        for b in B1:
            if tuple(sorted(f[x] for x in b)) not in s2:
                return None
        return f
    x = min(p for p in range(V) if p not in f)
    for y in range(V):
        if y not in used:
            f2 = dict(f)
            f2[x] = y
            r = extend(f2, B1, pm2, s2)
            if r is not None:
                return r
    return None

def isomorphic(B1, B2):
    pm2 = make_pairmap(B2)
    s2 = set(B2)
    b0 = sorted(B1)[0]
    for tgt in B2:
        for perm in itertools.permutations(tgt):
            f = {b0[0]: perm[0], b0[1]: perm[1], b0[2]: perm[2]}
            r = extend(f, B1, pm2, s2)
            if r is not None:
                return r
    return None

n = len(ulist)
iso_class = list(range(n))
for i in range(n):
    for j in range(i + 1, n):
        if iso_class[j] != j:
            continue
        m = isomorphic(ulist[i][0], ulist[j][0])
        if m is not None:
            print(f"system {i} ~= system {j}", flush=True)
            iso_class[j] = iso_class[i]
print("iso class labels:", iso_class, flush=True)

def pasch_count2(B):
    bset = set(B)
    count = 0
    for X in itertools.combinations(range(V), 6):
        blks = [b for b in itertools.combinations(X, 3) if b in bset]
        if len(blks) == 4:
            deg = {p: 0 for p in X}
            for b in blks:
                for p in b:
                    deg[p] += 1
            assert all(v == 2 for v in deg.values()), (X, blks)
            count += 1
        elif len(blks) > 4:
            raise AssertionError(("too many", X, blks))
    return count

for i, (B, reps_) in enumerate(ulist):
    p2 = pasch_count2(set(B))
    print(i, "pasch:", p2, "nblocks:", len(B), "reps:", reps_, flush=True)
print("OK")
