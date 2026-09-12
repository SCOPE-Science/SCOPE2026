"""Prove the >=30 depth-2 hexagon-ball bound via exact invariant certificates.

For a starter cyclic STS(19), take the first hexagon-switch child N1, enumerate ALL
hexagon switches of N1, and certify distinct isomorphism classes by pairwise-distinct
exact invariant tuples (Pasch count, hexagon-record count, mitre count).
Distinct tuples => rigorously non-isomorphic. No heuristic iso tester is used.

Run for BOTH anti-Pasch cyclic candidates so the literal A4 claim follows
regardless of residual MPR-naming risk.
"""
import json, sys, time
from itertools import combinations
sys.path.insert(0, '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1132/output/artifacts')
from ball import gen, hex_records, do_switch

V = 19


def check_valid_sts(B):
    assert len(B) == 57, len(B)
    pairs = set()
    for blk in B:
        for p in combinations(sorted(blk), 2):
            assert p not in pairs, p
            pairs.add(p)
    assert len(pairs) == 171


def check_difference_family(bases):
    from collections import Counter
    c = Counter()
    for (a, b, d) in bases:
        for x, y in ((a, b), (a, d), (b, d)):
            c[(y - x) % V] += 1
            c[(x - y) % V] += 1
    assert sorted(c.items()) == [(i, 1) for i in range(1, V)], sorted(c.items())


def pasch_count(B):
    bl = list(B)
    n = 0
    for six in combinations(range(V), 6):
        s = set(six)
        if sum(1 for b in bl if s.issuperset(b)) == 4:
            from collections import Counter
            deg = Counter()
            for b in bl:
                if s.issuperset(b):
                    for x in b:
                        deg[x] += 1
            if all(deg[x] == 2 for x in six):
                n += 1
    return n


def mitre_count(B):
    bl = list(B)
    n = 0
    for seven in combinations(range(V), 7):
        s = set(seven)
        if sum(1 for b in bl if s.issuperset(b)) == 5:
            n += 1
    return n


def key(B):
    return (pasch_count(B), len(hex_records(B)), mitre_count(B))


def run_case(name, bases):
    t0 = time.time()
    check_difference_family(bases)
    B = gen([tuple(b) for b in bases])
    check_valid_sts(B)
    k0 = key(B)
    assert k0[0] == 0, (name, k0)  # anti-Pasch starter
    recs = hex_records(B)
    assert len(recs) > 0
    a, b, c, cy = recs[0]
    N1 = do_switch(B, a, b, cy)
    check_valid_sts(N1)
    k1 = key(N1)
    assert k1 != k0, (name, k0, k1)  # depth-1 child is a genuinely new class
    r2 = hex_records(N1)
    reps = {}  # key -> (blocks, switch)
    for (a2, b2, c2, cy2) in r2:
        M = do_switch(N1, a2, b2, cy2)
        check_valid_sts(M)
        k = key(M)
        if k in (k0, k1):
            continue  # back-edge / duplicate of a known class; excluded
        if k not in reps:
            reps[k] = (sorted(M), [a2, b2, list(cy2)])
    total = 2 + len(reps)
    # pairwise-distinct keys by construction => pairwise non-isomorphic
    assert len({k0, k1} | set(reps)) == 2 + len(reps)
    dt = time.time() - t0
    print(f'{name}: starter_key={k0} child_key={k1} '
          f'n_hex_starter={len(recs)} n_hex_child={len(r2)} '
          f'novel_depth2_keys={len(reps)} TOTAL={total} t={dt:.1f}s', flush=True)
    return {'starter': sorted(B), 'starter_key': list(k0),
            'child': sorted(N1), 'child_key': list(k1),
            'child_switch': [a, b, list(cy)],
            'reps': [{'key': list(k), 'blocks': v[0], 'switch': v[1]}
                     for k, v in sorted(reps.items(), key=lambda kv: kv[0])],
            'total': total}


if __name__ == '__main__':
    out = {}
    out['netto_B'] = run_case('netto_B', [(0, 1, 8), (0, 2, 5), (0, 4, 13)])
    out['alt_A'] = run_case('alt_A', [(0, 1, 4), (0, 2, 12), (0, 5, 13)])
    assert out['netto_B']['total'] >= 30 and out['alt_A']['total'] >= 30
    p = '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1132/output/artifacts/roster_cert.json'
    with open(p, 'w') as f:
        json.dump(out, f)
    print('wrote', p, 'OK >=30 for both starters', flush=True)
