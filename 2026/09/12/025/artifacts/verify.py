"""Independent replay of roster_cert.json: revalidates STS property, switch legality,
key recomputation, and pairwise key-distinctness. Stdlib only."""
import json, sys
sys.path.insert(0, '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1132/output/artifacts')
from ball import gen, hex_records, do_switch
from prove_ball import pasch_count, mitre_count, check_valid_sts, key

P = '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1132/output/artifacts/roster_cert.json'
d = json.load(open(P))
for name in ('netto_B', 'alt_A'):
    c = d[name]
    S = set(tuple(b) for b in c['starter'])
    check_valid_sts(S)
    assert key(S) == tuple(c['starter_key']), name
    assert pasch_count(S) == 0, name
    C = set(tuple(b) for b in c['child'])
    check_valid_sts(C)
    assert key(C) == tuple(c['child_key']), name
    # child reachable by one legal hexagon switch from starter
    a, b, cy = c['child_switch']
    assert tuple(sorted(cy)) and len(cy) == 6
    assert do_switch(S, a, b, tuple(cy)) == C, name
    # each rep reachable by one legal switch from child, keys distinct
    keys = {tuple(c['starter_key']), tuple(c['child_key'])}
    assert len(c['reps']) + 2 == c['total'], name
    for r in c['reps']:
        M = set(tuple(x) for x in r['blocks'])
        check_valid_sts(M)
        k = key(M)
        assert list(k) == r['key'], (name, k, r['key'])
        assert tuple(k) not in keys, (name, k)
        keys.add(tuple(k))
        a2, b2, cy2 = r['switch']
        assert do_switch(C, a2, b2, tuple(cy2)) == M, (name, r['key'])
    assert c['total'] >= 30, name
    print(name, 'OK total=', c['total'], 'keys=', len(keys))
print('ALL VERIFIED')
