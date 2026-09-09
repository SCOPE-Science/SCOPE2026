"""Independent replay: rebuilds refined M8 unit model, rechecks D* rank==2 (stdlib only)."""
import itertools
a = {i: f"a{i}" for i in range(1,7)}
b = {i: f"b{i}" for i in range(1,7)}
V = []
for i in range(1,7): V += [a[i], b[i]]
V += ["c1","c2","c4","c5","dL","dR","vs"]
for i in range(1,7): V += [f"m{i}a", f"m{i}b"]
idx = {v:k for k,v in enumerate(V)}
n = len(V)
assert n == 31
adj = [[0]*n for _ in range(n)]
def add_edge(u,v,m=1):
    i,j = idx[u], idx[v]
    adj[i][j]+=m; adj[j][i]+=m
for i in range(1,7):
    add_edge(a[i], f"m{i}a"); add_edge(f"m{i}a", b[i])
    add_edge(a[i], f"m{i}b"); add_edge(f"m{i}b", b[i])
add_edge(b[1],"c1"); add_edge("c1",a[2])
add_edge(b[2],"c2"); add_edge("c2",a[3])
add_edge(b[3],"dL"); add_edge("dL","vs")
add_edge("vs","dR"); add_edge("dR",a[4])
add_edge(b[4],"c4"); add_edge("c4",a[5])
add_edge(b[5],"c5"); add_edge("c5",a[6])
deg = [sum(r) for r in adj]
E = sum(deg)//2
g = E-n+1
def q_reduced(D, q):
    D = list(D)
    for _ in range(10000):
        neg = next((v for v in range(n) if v != q and D[v] < 0), None)
        if neg is not None:
            v = neg
            D[v] += deg[v]
            for u in range(n):
                if adj[v][u]: D[u] -= adj[v][u]
            continue
        burned = [False]*n
        burned[q] = True
        changed = True
        while changed:
            changed = False
            for v in range(n):
                if burned[v]: continue
                c = sum(adj[v][u] for u in range(n) if burned[u])
                if D[v] < c:
                    burned[v] = True; changed = True
        if all(burned): return D
        S = [v for v in range(n) if not burned[v]]
        inS = set(S)
        for v in S:
            D[v] -= sum(adj[v][u] for u in range(n) if u not in inS)
        for u in range(n):
            if u in inS: continue
            D[u] += sum(adj[u][v] for v in S)
    raise RuntimeError("no convergence")
def show(D): return {V[i]: D[i] for i in range(n) if D[i] != 0}
D = [0]*n
D[idx["vs"]] += 2
for s in ["a1","a2","b4","a5"]: D[idx[s]] += 1
assert sum(D) == 6
npair = 0
for E2 in itertools.combinations_with_replacement(range(n), 2):
    D2 = list(D)
    for v in E2: D2[v] -= 1
    if not all(x >= 0 for x in q_reduced(D2, 0)):
        print("PAIR_FAIL", [V[v] for v in E2]); print("FAIL"); raise SystemExit(1)
    npair += 1
T = [idx["b2"], idx["b3"], idx["b4"]]
DT = list(D)
for v in T: DT[v] -= 1
if all(x >= 0 for x in q_reduced(DT, 0)):
    print("TRIPLE_UNEXPECTEDLY_WINNABLE"); print("FAIL"); raise SystemExit(1)
print(f"graph_genus={g} pairs_verified={npair} triple=b2+b3+b4 unwinnable")
print("VERIFY_OK")
