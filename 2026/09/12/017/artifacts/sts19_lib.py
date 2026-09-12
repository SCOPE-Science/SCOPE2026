"""Core library for cyclic STS(19) Pasch-neighbourhood ledger."""
import itertools

V = 19

def blocks_from_bases(bases, v=V):
    blocks = set()
    for (a, b) in bases:
        for t in range(v):
            blocks.add(tuple(sorted(((t) % v, (t + a) % v, (t + b) % v))))
    return sorted(blocks)

def check_sts(blocks, v=V):
    if len(blocks) != v * (v - 1) // 6:
        return False
    seen = set()
    for bl in blocks:
        for p in itertools.combinations(bl, 2):
            if p in seen:
                return False
            seen.add(p)
    return len(seen) == v * (v - 1) // 2

def third_table(blocks, v=V):
    third = [[-1] * v for _ in range(v)]
    for (a, b, c) in blocks:
        third[a][b] = third[b][a] = c
        third[a][c] = third[c][a] = b
        third[b][c] = third[c][b] = a
    return third

def block_index(blocks):
    return {b: i for i, b in enumerate(blocks)}

def find_pasches(blocks, v=V):
    """Return list of Pasches, each a frozenset of 4 block-tuples. Uses shared-point pair method."""
    third = third_table(blocks, v)
    by_point = [[] for _ in range(v)]
    for bl in blocks:
        for x in bl:
            by_point[x].append(bl)
    pasches = set()
    for x in range(v):
        bls = by_point[x]
        for i in range(len(bls)):
            for j in range(i + 1, len(bls)):
                b1, b2 = bls[i], bls[j]
                a, bb = [p for p in b1 if p != x]
                c, d = [p for p in b2 if p != x]
                # pairing (a,c)|(bb,d)
                e = third[a][c]
                if third[bb][d] == e:
                    t3 = tuple(sorted((a, c, e)))
                    t4 = tuple(sorted((bb, d, e)))
                    pasches.add(frozenset((b1, b2, t3, t4)))
                # pairing (a,d)|(bb,c)
                e = third[a][d]
                if third[bb][c] == e:
                    t3 = tuple(sorted((a, d, e)))
                    t4 = tuple(sorted((bb, c, e)))
                    pasches.add(frozenset((b1, b2, t3, t4)))
    return sorted(pasches)

def pasch_switch(blocks, pasch):
    """Return new block list after switching the given Pasch. Generic trade completion."""
    bset = set(blocks)
    old = set(pasch)
    pts = sorted({p for bl in old for p in bl})
    assert len(pts) == 6 and len(old) == 4
    covered = set()
    for bl in old:
        for p in itertools.combinations(sorted(bl), 2):
            covered.add(p)
    assert len(covered) == 12
    tris = [t for t in itertools.combinations(pts, 3)
            if all(tuple(sorted(p)) in covered for p in itertools.combinations(t, 2))]
    # find partitions of covered pairs into 4 triples
    parts = []
    def backtrack(rem, chosen):
        if not rem:
            parts.append(tuple(chosen))
            return
        e = next(iter(rem))
        for t in tris:
            if e[0] in t and e[1] in t:
                tp = set(itertools.combinations(sorted(t), 2))
                if tp <= rem:
                    backtrack(rem - tp, chosen + [tuple(sorted(t))])
                    if len(parts) >= 3:
                        return
    backtrack(set(covered), [])
    assert len(parts) == 2, f"expected 2 partitions, got {len(parts)}"
    oldkey = tuple(sorted(tuple(sorted(b)) for b in old))
    alt = [p for p in parts if tuple(sorted(p)) != oldkey]
    assert len(alt) == 1
    newb = (bset - old) | set(alt[0])
    out = sorted(newb)
    assert check_sts(out, V)
    return out

def count_mitres(blocks, v=V):
    """Count labelled mitre copies: root r (unique degree-3 point) + 3 blocks through r
    + 2 disjoint transversal triples on the 6 arm points."""
    third = third_table(blocks, v)
    by_point = [[] for _ in range(v)]
    for bl in blocks:
        for x in bl:
            by_point[x].append(set(bl))
    total = 0
    for r in range(v):
        through = [s - {r} for s in by_point[r]]  # 9 pairs
        for combo in itertools.combinations(range(len(through)), 3):
            arms = [through[i] for i in combo]
            six = sorted(set().union(*arms))
            if len(six) != 6:
                continue
            sixset = set(six)
            found = set()
            for x, y in itertools.combinations(six, 2):
                e = third[x][y]
                if e in sixset:
                    found.add(tuple(sorted((x, y, e))))
            # check partition of six into two present triples
            ok = False
            for t in found:
                rest = tuple(sorted(sixset - set(t)))
                if rest in found:
                    ok = True
                    break
            if ok:
                total += 1
    return total

# ---- exact isomorphism via backtracking with propagation ----

def _propagate(fa, fb, thirdA, thirdB, v, queue):
    while queue:
        a, b = queue.pop()
        d = thirdB[fa[a]][fa[b]]
        c = thirdA[a][b]
        if fa[c] == -1 and fb[d] == -1:
            fa[c] = d
            fb[d] = c
            for a2 in range(v):
                if fa[a2] != -1 and a2 != c:
                    queue.append((min(c, a2), max(c, a2)))
        elif fa[c] != d:
            return False
    return True

def _seed_queue(fa, v):
    mapped = [a for a in range(v) if fa[a] != -1]
    q = []
    for i in range(len(mapped)):
        for j in range(i + 1, len(mapped)):
            a, b = mapped[i], mapped[j]
            q.append((min(a, b), max(a, b)))
    return q

def iso_exists(thirdA, thirdB, v=V):
    """Decide isomorphism A->B. Fix A-block {0,x,y}: use first block of A."""
    # find a block in A containing 0
    x = y = None
    for b in range(1, v):
        c = thirdA[0][b]
        if c > b:
            x, y = b, c
            break
    for b0 in range(v):
        for b1 in range(v):
            if b1 == b0:
                continue
            b2 = thirdB[b0][b1]
            for (i0, i1, i2) in ((b0, b1, b2), (b0, b2, b1)):
                fa = [-1] * v
                fb = [-1] * v
                fa[0] = i0
                fa[x] = i1
                fa[y] = i2
                fb[i0] = 0
                fb[i1] = x
                fb[i2] = y
                if not _propagate(fa, fb, thirdA, thirdB, v, _seed_queue(fa, v)):
                    continue
                # branch if incomplete
                stack = [(fa, fb)]
                done = False
                while stack:
                    fa0, fb0 = stack.pop()
                    if all(z != -1 for z in fa0):
                        return True
                    a = fa0.index(-1)
                    for d in range(v):
                        if fb0[d] == -1:
                            fa1 = list(fa0)
                            fb1 = list(fb0)
                            fa1[a] = d
                            fb1[d] = a
                            if _propagate(fa1, fb1, thirdA, thirdB, v, _seed_queue(fa1, v)):
                                stack.append((fa1, fb1))
                                if all(z != -1 for z in fa1):
                                    return True
                                break
                    else:
                        continue
                    # actually need to try all d; redo properly below
                # fallback full branch below
                return _iso_branch(fa, fb, thirdA, thirdB, v)
    return False

def _iso_branch(fa, fb, thirdA, thirdB, v):
    if all(z != -1 for z in fa):
        return True
    a = fa.index(-1)
    for d in range(v):
        if fb[d] == -1:
            fa1 = list(fa)
            fb1 = list(fb)
            fa1[a] = d
            fb1[d] = a
            if _propagate(fa1, fb1, thirdA, thirdB, v, _seed_queue(fa1, v)):
                if _iso_branch(fa1, fb1, thirdA, thirdB, v):
                    return True
    return False

def iso_exists_full(thirdA, thirdB, v=V):
    x = y = None
    for b in range(1, v):
        c = thirdA[0][b]
        if c > b:
            x, y = b, c
            break
    for b0 in range(v):
        for b1 in range(v):
            if b1 == b0:
                continue
            b2 = thirdB[b0][b1]
            for (i0, i1, i2) in ((b0, b1, b2), (b0, b2, b1)):
                fa = [-1] * v
                fb = [-1] * v
                fa[0] = i0
                fa[x] = i1
                fa[y] = i2
                fb[i0] = 0
                fb[i1] = x
                fb[i2] = y
                if _propagate(fa, fb, thirdA, thirdB, v, _seed_queue(fa, v)):
                    if _iso_branch(fa, fb, thirdA, thirdB, v):
                        return True
    return False

def aut_order(third, v=V):
    return count_isos(third, third, v)

def count_isos(thirdA, thirdB, v=V):
    x = y = None
    for b in range(1, v):
        c = thirdA[0][b]
        if c > b:
            x, y = b, c
            break
    n = [0]
    for b0 in range(v):
        for b1 in range(v):
            if b1 == b0:
                continue
            b2 = thirdB[b0][b1]
            for (i0, i1, i2) in ((b0, b1, b2), (b0, b2, b1)):
                fa = [-1] * v
                fb = [-1] * v
                fa[0] = i0
                fa[x] = i1
                fa[y] = i2
                fb[i0] = 0
                fb[i1] = x
                fb[i2] = y
                if _propagate(fa, fb, thirdA, thirdB, v, _seed_queue(fa, v)):
                    _count_branch(fa, fb, thirdA, thirdB, v, n)
    return n[0]

def _count_branch(fa, fb, thirdA, thirdB, v, n):
    if all(z != -1 for z in fa):
        n[0] += 1
        return
    a = fa.index(-1)
    for d in range(v):
        if fb[d] == -1:
            fa1 = list(fa)
            fb1 = list(fb)
            fa1[a] = d
            fb1[d] = a
            if _propagate(fa1, fb1, thirdA, thirdB, v, _seed_queue(fa1, v)):
                _count_branch(fa1, fb1, thirdA, thirdB, v, n)
