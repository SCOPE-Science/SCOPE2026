"""Depth<=2 hexagon-switch ball around a named cyclic STS(19), with exact iso rejection.

Definitions follow Erskine-Griggs Section 2: for pair (a,b), cycle graph C_ab on
V\\{a,b,c} with a-edges B\\{a} and b-edges B\\{b}; each even cycle gives a switch
exchanging roles of a and b on its blocks. We enumerate 6-cycles only.

Isomorphism: exact backtracking tester in iso.py. To keep the hour feasible we
bucket by a cheap invariant (block-intersection profile + Pasch count + 6-cycle
count) and run exact tests only within buckets.

Output: roster.json with entries {id, depth, blocks, parent, switch, inv}.
"""
import json, sys, time
from itertools import combinations
sys.path.insert(0, '.')
from iso import are_isomorphic, block_set

V = 19


def gen(bases, v=V):
    B = set()
    for (a, b, c) in bases:
        for t in range(v):
            B.add(tuple(sorted([(a + t) % v, (b + t) % v, (c + t) % v])))
    return B


def pair_third(B):
    d = {}
    for b in B:
        for p in combinations(sorted(b), 2):
            d[p] = (set(b) - set(p)).pop()
    return d


def hex_records(B):
    idx = pair_third(B)
    recs = []
    for a in range(V):
        for b in range(a + 1, V):
            c = idx[(a, b)]
            nbrA, nbrB = {}, {}
            for blk in B:
                if a in blk and b not in blk:
                    x, y = [z for z in blk if z != a]
                    nbrA[x] = y; nbrB_dummy = 0
                    nbrA[y] = x
                if b in blk and a not in blk:
                    x, y = [z for z in blk if z != b]
                    nbrB[x] = y
                    nbrB[y] = x
            verts = [v for v in range(V) if v != a and v != b and v != c]
            seen = set()
            for s in verts:
                if s in seen:
                    continue
                path = [s]; cur = s; ok = True
                for step in range(40):
                    nxt = nbrA[cur] if step % 2 == 0 else nbrB[cur]
                    if nxt == s:
                        path.append(s); break
                    if nxt in path:
                        ok = False; break
                    path.append(nxt); cur = nxt
                else:
                    ok = False
                if ok:
                    for v in path[:-1]:
                        seen.add(v)
                    if len(path) - 1 == 6:
                        recs.append((a, b, c, tuple(path[:-1])))
    return recs


def do_switch(B, a, b, cy):
    S = set(cy)
    abl = [blk for blk in B if a in blk and set(blk) - {a} <= S]
    bbl = [blk for blk in B if b in blk and set(blk) - {b} <= S]
    assert len(abl) == 3 and len(bbl) == 3, (a, b, cy)
    N = set(B)
    for blk in abl + bbl:
        N.remove(blk)
    for blk in abl:
        x, y = [z for z in blk if z != a]
        N.add(tuple(sorted([b, x, y])))
    for blk in bbl:
        x, y = [z for z in blk if z != b]
        N.add(tuple(sorted([a, x, y])))
    # validity
    assert len(N) == 57
    pairs = set()
    for blk in N:
        for p in combinations(blk, 2):
            assert p not in pairs
            pairs.add(p)
    return N


def pasch_count(B):
    bl = list(B); n = 0
    for six in combinations(range(V), 6):
        s = set(six)
        cont = [b for b in bl if s.issuperset(b)]
        if len(cont) == 4:
            from collections import Counter
            deg = Counter()
            for b in cont:
                for x in b:
                    deg[x] += 1
            if all(deg[x] == 2 for x in six):
                n += 1
    return n


def invariant(B):
    bs = sorted(B)
    inter = []
    for i in range(len(bs)):
        si = set(bs[i])
        for j in range(i + 1, len(bs)):
            inter.append(len(si & set(bs[j])))
    from collections import Counter
    h = tuple(sorted(Counter(inter).items()))
    return (h, pasch_count(B), len(hex_records(B)))


def main(bases, out, max_depth1_tests=None):
    t0 = time.time()
    start = gen(bases)
    roster = [{'id': 0, 'depth': 0, 'blocks': sorted(start),
               'parent': None, 'switch': None, 'inv': None}]
    roster[0]['inv'] = [list(x) if isinstance(x, tuple) else x for x in invariant(start)]
    # depth 1
    recs = hex_records(start)
    print(f'starter hex records: {len(recs)}', flush=True)
    reps = []  # list of (blocks, parent, switch)
    ntests = [0]
    for (a, b, c, cy) in recs:
        N = do_switch(start, a, b, cy)
        placed = False
        for (R, _, _) in reps:
            ntests[0] += 1
            if are_isomorphic(N, R):
                placed = True
                break
        if not placed:
            reps.append((N, 0, [a, b, list(cy)]))
    print(f'depth1 classes: {len(reps)} iso-tests: {ntests[0]} t={time.time()-t0:.1f}s', flush=True)
    for i, (R, p, s) in enumerate(reps, start=1):
        roster.append({'id': i, 'depth': 1, 'blocks': sorted(R), 'parent': p,
                       'switch': s, 'inv': None})
    # depth 2: expand each depth-1 member; stop early once total >= 30 distinct
    nxt = len(roster)
    outer_tests = 0
    for i, (R, p, s) in enumerate(reps, start=1):
        recs2 = hex_records(R)
        for (a, b, c, cy) in recs2:
            N = do_switch(R, a, b, cy)
            # check against all roster members
            dup = False
            for e in roster:
                Eb = set(tuple(x) for x in e['blocks'])
                outer_tests += 1
                if are_isomorphic(N, Eb):
                    dup = True
                    break
            if not dup:
                roster.append({'id': nxt, 'depth': 2, 'blocks': sorted(N),
                               'parent': i, 'switch': [a, b, list(cy)], 'inv': None})
                nxt += 1
                if len(roster) >= 30:
                    break
        print(f'after expanding d1#{i}: roster={len(roster)} t={time.time()-t0:.1f}s', flush=True)
        if len(roster) >= 30:
            break
    print(f'FINAL roster={len(roster)} t={time.time()-t0:.1f}s', flush=True)
    with open(out, 'w') as f:
        json.dump({'bases': bases, 'roster': roster,
                   'starter_hex_records': len(hex_records(start))}, f)
    print('wrote', out, flush=True)


if __name__ == '__main__':
    bases = json.loads(sys.argv[1]) if len(sys.argv) > 1 else [[0, 1, 8], [0, 2, 5], [0, 4, 13]]
    out = sys.argv[2] if len(sys.argv) > 2 else 'roster_netto.json'
    main([tuple(b) for b in bases], out)
