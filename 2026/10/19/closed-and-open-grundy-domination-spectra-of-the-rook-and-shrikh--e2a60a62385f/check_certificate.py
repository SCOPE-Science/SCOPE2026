"""Verify the full coverage-state certificate without importing its producer."""
import json
from itertools import combinations
from pathlib import Path

path = Path(__file__).with_name('coverage_certificate.json')
raw = path.read_bytes()
assert raw.endswith(b'\n')
data = json.loads(raw)
assert data['n'] == 16 and len(data['cases']) == 4
expected = {
 ('rook', 'closed'): {4: 11712, 5: 114048, 6: 266112},
 ('rook', 'open'): {4: 1920, 5: 103680, 6: 1658880},
 ('shrikhande', 'closed'): {3: 192, 4: 10176, 5: 127296, 6: 492480, 7: 48384},
 ('shrikhande', 'open'): {4: 1920, 5: 103680, 6: 1658880},
}
for case in data['cases']:
    name, kind = case['graph'], case['neighborhood']
    assert (name, kind) in expected
    edge_set = {tuple(edge) for edge in case['edges']}
    assert len(edge_set) == 48 and all(0 <= a < b < 16 for a, b in edge_set)
    adj = [set() for _ in range(16)]
    for a, b in edge_set:
        adj[a].add(b); adj[b].add(a)
    assert all(len(s) == 6 for s in adj)
    assert all(len(adj[a] & adj[b]) == 2 for a, b in combinations(range(16), 2))
    num_four_cliques = sum(all((min(a,b), max(a,b)) in edge_set for a,b in combinations(quad,2))
                           for quad in combinations(range(16), 4))
    assert num_four_cliques == (8 if name == 'rook' else 0)
    neighborhoods = [sum(1<<w for w in adj[v] | ({v} if kind == 'closed' else set()))
                     for v in range(16)]
    states = {m: p for m, p in case['state_polynomials']}
    assert len(states) == case['states']
    assert states[(1<<16)-1] == [1]
    for state, poly in states.items():
        if state == (1<<16)-1: continue
        rhs = [0] * len(poly)
        for mask in neighborhoods:
            nxt = mask | state
            if nxt == state: continue
            assert nxt in states
            for i, cnt in enumerate(states[nxt]):
                assert i + 1 < len(rhs)
                rhs[i+1] += cnt
        assert rhs == poly, (name, kind, state)
    assert {int(k): c for k,c in case['spectrum']} == expected[(name,kind)]
    assert {i: c for i,c in enumerate(states[0]) if c} == expected[(name,kind)]
    seen, x = set(), 0
    for v in case['max_witness']:
        assert v not in seen
        seen.add(v)
        y = x | neighborhoods[v]
        assert y != x
        x = y
    assert x == (1<<16)-1 and len(seen) == case['max_length']
    print(name, kind, 'VALID', 'reachable', len(states), '4-cliques', num_four_cliques)
print('CERTIFICATE_OK')
