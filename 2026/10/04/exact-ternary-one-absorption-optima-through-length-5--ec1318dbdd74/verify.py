from itertools import product
import json
import numpy as np
import scipy
import scipy.sparse as sp
from scipy.optimize import milp, LinearConstraint, Bounds

Q = 3
EXPECTED = {2:3, 3:6, 4:13, 5:29}

def ball(x):
    x = tuple(x)
    n = len(x)
    out = {x[:-1]}
    for i in range(n-1):
        out.add(x[:i] + (min(2, x[i] + x[i+1]),) + x[i+2:])
    return out

def solve_set_packing(n):
    words = list(product(range(Q), repeat=n))
    outputs = list(product(range(Q), repeat=n-1))
    oi = {y:i for i,y in enumerate(outputs)}
    rows, cols = [], []
    for j,x in enumerate(words):
        for y in ball(x):
            rows.append(oi[y]); cols.append(j)
    A = sp.coo_matrix((np.ones(len(rows)), (rows, cols)), shape=(len(outputs), len(words))).tocsr()
    r = milp(-np.ones(len(words)), integrality=np.ones(len(words)),
             bounds=Bounds(np.zeros(len(words)), np.ones(len(words))),
             constraints=LinearConstraint(A, -np.inf*np.ones(len(outputs)), np.ones(len(outputs))),
             options={'mip_rel_gap':0.0})
    assert r.success and r.mip_gap == 0.0
    return int(round(-r.fun)), int(r.mip_node_count)

def solve_conflict_graph(n):
    words = list(product(range(Q), repeat=n))
    inv = {}
    for i,x in enumerate(words):
        for y in ball(x):
            inv.setdefault(y, []).append(i)
    edges = set()
    for ids in inv.values():
        for a in range(len(ids)):
            for b in range(a+1, len(ids)):
                if ids[a] != ids[b]:
                    edges.add((min(ids[a],ids[b]), max(ids[a],ids[b])))
    edges = sorted(edges)
    rows = np.repeat(np.arange(len(edges)), 2)
    cols = np.array([v for e in edges for v in e], dtype=int)
    A = sp.coo_matrix((np.ones(len(cols)), (rows, cols)), shape=(len(edges), len(words))).tocsr()
    r = milp(-np.ones(len(words)), integrality=np.ones(len(words)),
             bounds=Bounds(np.zeros(len(words)), np.ones(len(words))),
             constraints=LinearConstraint(A, -np.inf*np.ones(len(edges)), np.ones(len(edges))),
             options={'mip_rel_gap':0.0})
    assert r.success and r.mip_gap == 0.0
    return int(round(-r.fun)), len(edges), int(r.mip_node_count)

def check_witnesses():
    data = json.load(open('optimal_codes.json', encoding='utf-8'))
    for ns, code in data['codes'].items():
        n = int(ns)
        assert len(code) == EXPECTED[n]
        bs = []
        for s in code:
            assert len(s) == n and set(s) <= set('012')
            b = ball(tuple(map(int,s)))
            for old in bs:
                assert b.isdisjoint(old)
            bs.append(b)

check_witnesses()
print('scipy', scipy.__version__)
for n in range(2,6):
    a, nodes_a = solve_set_packing(n)
    b, edges, nodes_b = solve_conflict_graph(n)
    print(f'n={n} set_packing={a} nodes={nodes_a} conflict={b} edges={edges} nodes={nodes_b}')
    assert a == b == EXPECTED[n]
print('VERIFY_OK')
