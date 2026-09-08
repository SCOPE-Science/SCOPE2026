"""Independent verifier: enumerates all 6-sets x 60 cycles from edge lists alone."""
import json, itertools, os
_HERE = os.path.dirname(os.path.abspath(__file__))
W = json.load(open(os.path.join(_HERE, 'witnesses.json')))
def check(n, edges):
    S = set()
    for a, b in edges:
        if a > b: a, b = b, a
        S.add((a, b))
    assert len(S) == len(edges), "duplicate/loop"
    for a, b in edges:
        assert 0 <= a < b < n
        assert a != b
    # girth + C6 enumeration
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b); adj[b].append(a)
    nc6 = 0
    for vs in itertools.combinations(range(n), 6):
        v0 = vs[0]
        for perm in itertools.permutations(vs[1:]):
            cyc = (v0,) + perm
            if cyc[1] > cyc[-1]: continue
            ok = True
            for t in range(6):
                a, b = cyc[t], cyc[(t+1) % 6]
                if a > b: a, b = b, a
                if (a, b) not in S: ok = False; break
            if ok: nc6 += 1
    # BFS girth
    best = 10**9
    for s in range(n):
        dist = [-1]*n; par = [-1]*n
        dist[s] = 0; q = [s]
        for u in q:
            for w in adj[u]:
                if dist[w] == -1:
                    dist[w] = dist[u]+1; par[w] = u; q.append(w)
                elif par[u] != w and par[w] != u:
                    best = min(best, dist[u]+dist[w]+1)
    girth = best if best < 10**9 else None
    return nc6, girth
for k, v in W.items():
    nc6, g = check(v['n'], v['edges'])
    print(f"n={v['n']} m={v['m']} C6count={nc6} girth={g} C6free={nc6==0}")
