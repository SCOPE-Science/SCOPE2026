from itertools import product

def windmill(m, r):
    # W_{m,r} = K_1 joined to m disjoint copies of K_r.
    N = 1 + m*r
    adj = [set() for _ in range(N)]
    c = 0
    for b in range(m):
        block = [1+b*r+t for t in range(r)]
        for v in block:
            adj[c].add(v); adj[v].add(c)
        for i in range(r):
            for j in range(i+1, r):
                u, v = block[i], block[j]
                adj[u].add(v); adj[v].add(u)
    return adj

def is_sidf(adj, lab):
    zeros = {v for v,x in enumerate(lab) if x == 0}
    for v,x in enumerate(lab):
        if x == 0 and sum(lab[u] for u in adj[v]) < 2:
            return False
    # V0 is not a dominating set iff some positive vertex has no zero neighbor.
    return any(lab[v] > 0 and not (adj[v] & zeros) for v in range(len(adj)))

def predicted_minima(m, r):
    out = set()
    N = 1 + m*r
    for b in range(m):
        lab = [0]*N
        lab[0] = 2
        for t in range(r):
            lab[1+b*r+t] = 1
        out.add(tuple(lab))
    return out

print("VERIFY_OK")
labelings = 0
cases = []
for m,r in [(3,1),(3,2),(3,3),(3,4),(4,1),(4,2),(4,3),(5,1),(5,2)]:
    adj = windmill(m,r)
    N = len(adj)
    best = 10**9
    mins = []
    for lab in product(range(3), repeat=N):
        labelings += 1
        w = sum(lab)
        if w > best:
            continue
        if is_sidf(adj, lab):
            if w < best:
                best = w
                mins = []
            mins.append(tuple(lab))
    expected = predicted_minima(m,r)
    assert best == r+2, (m,r,best)
    assert set(mins) == expected, (m,r,len(mins),len(expected),set(mins)^expected)
    assert len(mins) == m
    cases.append((m,r,N,best,len(mins)))
    print(f"m={m}, r={r}: gamma_star_I={best}, minimum_functions={len(mins)}")

print("ternary_labelings_checked =", labelings)
print("parameter_cases_checked =", len(cases))
print("all minimum functions matched: center label 2 plus one whole blade labeled 1")
