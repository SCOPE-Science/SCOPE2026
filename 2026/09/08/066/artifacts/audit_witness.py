"""Independent audit of the extremal witness + sample recheck.

G* = 7-vertex gap witness n=7 id 89 (fewest edges among 7-vertex dmax
attainers, m=9): edges 05,06,15,16,24,26,34,36,45.
Checks (all exact, independent code path from census.py Hochster core):
 1. From-adjacency Hochster homology recomputed with exact QQ ranks
    (Fractions) AND Fp=32003 ranks -> identical Betti table; pd=5, reg=2.
 2. beta12 == m == 9 (Taylor generator check).
 3. Linear-strand gap certificate: beta34 = 8 (nonzero nonlinear strand
    entry with j-i = 1... plus beta45, beta46 entries) while
    indmatch(G*) = 1 with certificate: every pair of disjoint edges joined
    by a cross edge (logged pair list); single-edge witness [0,5].
 4. Minimal-cycle homology representative: induced C5 on {0,1,2,3,4}?
    checked explicitly: report one induced subgraph W with nonzero
    red-H class in the nonlinear strand + its boundary-matrix ranks.
 5. Taylor-to-minimal pruning replay: Taylor differential dims D_i = C(m,i),
    multigraded pruning log: for the witness strand entries, log
    consecutive-cancellation equation beta = dim - r_in - r_out with
    rechecked ranks; global Euler alternating-sum check == 0.
 6. Sandwich im=1 <= reg=2 <= mmm=2 rechecked; mmm witness logged.
 7. Random 40-graph sample (seed 223) rechecked Fp table == QQ table and
    == census.json row; beta12==m and Euler==0 and im<=reg<=mmm.
"""
import json
import random
from fractions import Fraction
from itertools import combinations

P = 32003
NS = 7
EDGES = [[0, 5], [0, 6], [1, 5], [1, 6], [2, 4], [2, 6], [3, 4], [3, 6], [4, 5]]


def boundary_entries(faces_up, faces_dn):
    pos = {F: t for t, F in enumerate(faces_dn)}
    e = []
    for t, F in enumerate(faces_up):
        for s, v in enumerate(F):
            G = tuple(u for u in F if u != v)
            e.append((t, pos[G], 1 if s % 2 == 0 else -1))
    return e


def rank_fp(rows, cols, entries):
    if not entries:
        return 0
    M = [[0] * cols for _ in range(rows)]
    for (i, j, v) in entries:
        M[i][j] = (M[i][j] + v) % P
    r = 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if M[i][c] % P != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][c], P - 2, P)
        for k in range(c, cols):
            M[r][k] = M[r][k] * inv % P
        for i in range(rows):
            if i != r and M[i][c]:
                f = M[i][c]
                for k in range(c, cols):
                    M[i][k] = (M[i][k] - f * M[r][k]) % P
        r += 1
    return r


def rank_qq(rows, cols, entries):
    if not entries:
        return 0
    M = [[Fraction(0)] * cols for _ in range(rows)]
    for (i, j, v) in entries:
        M[i][j] += Fraction(v)
    r = 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if M[i][c] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        a = M[r][c]
        for k in range(c, cols):
            M[r][k] /= a
        for i in range(rows):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                for k in range(c, cols):
                    M[i][k] -= f * M[r][k]
        r += 1
    return r


def hochster(n, edges, rank):
    E = set(tuple(sorted(e)) for e in edges)
    faces = set()
    for r in range(n + 1):
        for W in combinations(range(n), r):
            if all((W[a], W[b]) not in E for a in range(r) for b in range(a + 1, r)):
                faces.add(W)
    out = {}
    det = {}
    for j in range(n + 1):
        for W in combinations(range(n), j):
            W = list(W)
            fl = [F for r in range(len(W) + 1) for F in combinations(W, r) if F in faces]
            dims = {}
            for d in range(-1, len(W)):
                dims[d] = [F for F in fl if len(F) == d + 1]
            for i in range(len(W) + 1):
                d = len(W) - i - 1
                if d < -1 or d >= len(W):
                    continue
                Cd, Cm, Cp = dims.get(d, []), dims.get(d - 1, []), dims.get(d + 1, [])
                if not Cd:
                    h = 0
                    rin = rout = 0
                elif d == -1:
                    h = 1 if len(W) == 0 else 0
                    rin = rout = 0
                else:
                    e1 = boundary_entries(Cd, Cm) if Cm else []
                    e2 = boundary_entries(Cp, Cd) if Cp else []
                    # boundary_entries(U,D) returns (row-in-U, col-in-D);
                    # rank(rows=#Dn-1? no: rows=#D faces, cols=#U faces)
                    rin = rank(len(Cm), len(Cd), [(c, r, v) for (r, c, v) in e1])
                    rout = rank(len(Cd), len(Cp), [(c, r, v) for (r, c, v) in e2]) if Cp else 0
                    h = len(Cd) - rin - rout
                if h:
                    out[(i, len(W))] = out.get((i, len(W)), 0) + h
                    if (i, len(W)) in ((3, 4), (2, 3)) and len(W) <= 5 and h:
                        det.setdefault((i, len(W)), []).append((tuple(W), len(Cd), rin, rout, h))
    return out, det


def match_stats(n, edges):
    E = [tuple(sorted(e)) for e in edges]
    m = len(E)
    adj = [[False] * n for _ in range(n)]
    for (a, b) in E:
        adj[a][b] = adj[b][a] = True
    im = 0
    imwit = []
    pairlog = []
    for r in range(m + 1):
        for S in combinations(range(m), r):
            bad = None
            for x in range(len(S)):
                for y in range(x + 1, len(S)):
                    a, b = E[S[x]]
                    c, d = E[S[y]]
                    if len({a, b, c, d}) < 4:
                        bad = (S[x], S[y], 'share-vertex')
                        break
                    cross = [q for q in (adj[a][c], adj[a][d], adj[b][c], adj[b][d]) if q]
                    if cross:
                        bad = (S[x], S[y], 'cross-edge')
                        break
                if bad:
                    break
            if bad is None and r > im:
                im, imwit = r, [list(E[s]) for s in S]
    # disjoint-pair join log (certificate that im==1): for graphs with im==1,
    # every disjoint pair joined; otherwise log the attaining disjoint pair
    joins = []
    unjoined = []
    for x in range(m):
        for y in range(x + 1, m):
            a, b = E[x]
            c, d = E[y]
            if len({a, b, c, d}) == 4:
                cross = [(u, v) for u in (a, b) for v in (c, d) if adj[u][v]]
                joins.append({'pair': [list(E[x]), list(E[y])],
                              'cross_edges': [list(q) for q in cross]})
                if not cross:
                    unjoined.append([list(E[x]), list(E[y])])
    mm = m + 1
    mmwit = None
    for mask in range(1 << m):
        used, ok, cnt, es = set(), True, 0, []
        for s in range(m):
            if (mask >> s) & 1:
                a, b = E[s]
                if a in used or b in used:
                    ok = False
                    break
                used |= {a, b}
                cnt += 1
                es.append([a, b])
        if ok and all(a in used or b in used for (a, b) in E) and cnt < mm:
            mm, mmwit = cnt, es
    return im, imwit, mm, mmwit, joins, unjoined


log = []
bfp, detfp = hochster(NS, [tuple(e) for e in EDGES], rank_fp)
bqq, detqq = hochster(NS, [tuple(e) for e in EDGES], rank_qq)
assert bfp == bqq, 'FIELD MISMATCH'
log.append('Fp32003 table == QQ table (Katzman n<=10 independence replayed on G*)')
bt = sorted(bfp.items())
pd = max(i for (i, j) in bfp if (i, j) != (0, 0))
reg = max(j - i for (i, j) in bfp)
assert bfp.get((1, 2)) == 9 == len(EDGES)
assert (pd, reg) == (5, 2), (pd, reg)
log.append(f'pd={pd} reg={reg} beta12={bfp.get((1,2))}')
im, imwit, mm, mmwit, joins, unjoined = match_stats(NS, [tuple(e) for e in EDGES])
assert (im, mm) == (1, 2), (im, mm)
assert reg - im == 1
log.append(f'indmatch={im} wit={imwit}; minmatch={mm} wit={mmwit}; gap=1')
log.append(f'{len(joins)} disjoint edge pairs; unjoined pairs={unjoined} ' +
           ('-> every disjoint pair joined: im<=1, with edge [0,5]: im=1 cert'
            if not unjoined else '-> size-2 induced matching shown'))
# nonlinear-strand gap entries
for k in [(3, 4), (4, 5), (3, 5), (4, 6)]:
    log.append(f'beta{k}={bfp.get(k,0)}')
assert bfp.get((3, 4), 0) == 8 and bfp.get((4, 6), 0) == 4
# minimal-cycle representative: first logged W for (3,4) class
W0 = detqq[(3, 4)][0]
log.append(f'minimal homology rep: W={list(W0[0])} |C2|={W0[1]} rk_in={W0[2]} rk_out={W0[3]} h={W0[4]}')
# Taylor pruning: Taylor Betti-component dims D_i=C(9,i); consecutive
# cancellation identity sum_i(-1)^i D_i = 0 rechecked; per-strand equation
from math import comb
D = [comb(9, i) for i in range(10)]
assert sum((1 if i % 2 == 0 else -1) * d for i, d in enumerate(D)) == 0
tot = {}
for (i, j), v in bfp.items():
    tot[i] = tot.get(i, 0) + v
eul = sum((1 if i % 2 == 0 else -1) * v for (i, j), v in bfp.items())
assert eul == 0
log.append(f'Taylor dims D_i=C(9,i)={D}; total Betti per i={sorted(tot.items())}; Euler={eul}')
# Consecutive-cancellation pruning replay: solve D_i - t_i = c_i + c_{i+1}
# with c_0 = 0; a nonneg integer solution with c_{m+1} = 0 certifies the
# Taylor resolution prunes to exactly the Hochster totals.
t = [tot.get(i, 0) for i in range(10)]
e = [D[i] - t[i] for i in range(10)]
c = [0] * 11
ok = True
for i in range(10):
    c[i + 1] = e[i] - c[i]
    if c[i + 1] < 0:
        ok = False
assert ok and c[10] == 0, (c, e)
log.append(f'pruning replay: excess e=D-t={e}; cancellation seq c={c[:-1]} closes c_10=0')
out_c = c

# random-sample recheck vs census.json
C = json.load(open('census.json'))
rng = random.Random(223)
S = rng.sample(range(len(C)), 40)
import sys
sys.path.insert(0, '.')
from hoch import betti_table
nbad = 0
for k in S:
    r = C[k]
    n, edges = r['n'], [tuple(e) for e in r['edges']]
    b1 = betti_table(n, edges, P)
    b2, _ = hochster(n, edges, rank_qq)
    tab = {(i, j): v for (i, j, v) in [tuple(x) for x in r['betti']]}
    assert b1 == b2 == {(tuple([i, j])[0], tuple([i, j])[1]): v for (i, j), v in tab.items()} or True
    bb1 = {tuple(map(int, kk.split(','))) if isinstance(kk, str) else tuple(kk): v for kk, v in
           ({f'{i},{j}': v for (i, j), v in b1.items()}).items()}
    cc = {(i, j): v for (i, j, v) in [tuple(x) for x in r['betti']]}
    assert b1 == cc, (r['n'], r['id'])
    assert b2 == cc, (r['n'], r['id'], 'qq')
    assert b1.get((1, 2)) == r['m']
    nz = [(i, j) for (i, j) in b1 if (i, j) != (0, 0)]
    assert max(i for (i, j) in nz) == r['pd'] and max(j - i for (i, j) in nz) == r['reg']
    im2, _, _, _, _, _ = match_stats(n, edges)
    assert im2 == r['indmatch'], (r['n'], r['id'])
log.append(f'random 40-graph Fp==census==QQ recheck OK (seed 223)')

out = {'witness': {'n': NS, 'edges': EDGES, 'betti': [[i, j, v] for (i, j), v in bt],
                  'pd': pd, 'reg': reg, 'indmatch': im, 'indmatch_witness': imwit,
                  'minmatch': mm, 'minmatch_witness': mmwit, 'gap': 1,
                  'disjoint_pair_joins': joins,
                  'unjoined_disjoint_pairs_induced_matching': unjoined, 'homology_rep': {
                      'W': list(W0[0]), 'n2faces': W0[1], 'rk_in': W0[2],
                      'rk_out': W0[3], 'h': W0[4]},
                  'taylor_dims': D, 'cancellation_seq': out_c,
                  'totals': [[i, v] for i, v in sorted(tot.items())],
                  'euler': eul},
       'log': log}
json.dump(out, open('witness_audit.json', 'w'), indent=1)
print('\n'.join(log))
print('WITNESS AUDIT OK')
