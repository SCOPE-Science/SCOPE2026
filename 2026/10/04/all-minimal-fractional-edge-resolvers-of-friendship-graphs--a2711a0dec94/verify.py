from itertools import combinations
from collections import deque
from scipy.optimize import linprog

def friendship(k):
    # 0 is the common center; triangle i has outer vertices 2i-1,2i.
    n = 2*k + 1
    adj = [set() for _ in range(n)]
    edges = []
    for i in range(k):
        v, w = 2*i + 1, 2*i + 2
        for a,b in [(0,v),(0,w),(v,w)]:
            adj[a].add(b); adj[b].add(a)
            edges.append((min(a,b), max(a,b)))
    return adj, edges

def distances(adj):
    n = len(adj)
    D = [[10**9]*n for _ in range(n)]
    for s in range(n):
        D[s][s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if D[s][v] == 10**9:
                    D[s][v] = D[s][u] + 1
                    q.append(v)
    return D

def resolving_neighborhood(e, f, D):
    return tuple(
        z for z in range(len(D))
        if min(D[z][e[0]], D[z][e[1]]) != min(D[z][f[0]], D[z][f[1]])
    )

def solve_lp(n, neighborhoods):
    A=[]; b=[]
    for R in neighborhoods:
        row=[0.0]*n
        for v in R:
            row[v] = -1.0
        A.append(row); b.append(-1.0)
    res = linprog([1.0]*n, A_ub=A, b_ub=b,
                  bounds=[(0.0,1.0)]*n, method="highs")
    assert res.success
    return res.fun

def coord_range(n, neighborhoods, optimum, idx):
    A=[]; b=[]
    for R in neighborhoods:
        row=[0.0]*n
        for v in R:
            row[v] = -1.0
        A.append(row); b.append(-1.0)
    Aeq=[[1.0]*n]; beq=[optimum]
    c=[0.0]*n; c[idx]=1.0
    lo=linprog(c,A_ub=A,b_ub=b,A_eq=Aeq,b_eq=beq,
               bounds=[(0.0,1.0)]*n,method="highs")
    c[idx]=-1.0
    hi=linprog(c,A_ub=A,b_ub=b,A_eq=Aeq,b_eq=beq,
               bounds=[(0.0,1.0)]*n,method="highs")
    assert lo.success and hi.success
    return lo.fun, -hi.fun

def family_vector(k, distinguished, t):
    n=2*k+1
    g=[0.0]*n
    for v in range(1,n):
        g[v]=1.0-t
    g[distinguished]=t
    return g

def feasible(g, neighborhoods):
    return all(sum(g[v] for v in R) >= 1.0-1e-10 for R in neighborhoods)

def coordinatewise_minimal(g, neighborhoods):
    # For monotone constraints, a positive coordinate is non-decreasable
    # iff it belongs to at least one tight constraint.
    for v,x in enumerate(g):
        if x <= 1e-12:
            continue
        if not any(v in R and abs(sum(g[u] for u in R)-1.0) < 1e-9
                   for R in neighborhoods):
            return False
    return True

types=edge_pairs=coord_lps=family_checks=0
for k in range(2,9):
    adj, edges = friendship(k)
    D = distances(adj)
    neighborhoods=[]
    for e,f in combinations(edges,2):
        neighborhoods.append(resolving_neighborhood(e,f,D))
        edge_pairs += 1

    outer=set(range(1,2*k+1))
    size2={tuple(sorted(R)) for R in neighborhoods if len(R)==2}
    expected={tuple(p) for p in combinations(range(1,2*k+1),2)}
    assert size2 == expected, (k, len(size2), len(expected))

    # Every remaining edge-resolving neighborhood contains at least two
    # outer vertices, so the pair constraints imply all other constraints.
    assert all(len(set(R)&outer) >= 2 for R in neighborhoods)

    optimum=solve_lp(2*k+1, neighborhoods)
    assert abs(optimum-k) < 1e-9, (k,optimum)

    for v in range(2*k+1):
        lo,hi=coord_range(2*k+1, neighborhoods, optimum, v)
        coord_lps += 2
        target = 0.0 if v==0 else 0.5
        assert abs(lo-target) < 1e-8 and abs(hi-target) < 1e-8, (k,v,lo,hi)

    # Sample the complete symbolic family at rational parameters.
    for distinguished in range(1,2*k+1):
        for t in [0.0,0.125,0.25,0.375,0.5]:
            g=family_vector(k, distinguished, t)
            if t == 0.5:
                # all choices coincide with the uniform vector
                pass
            assert feasible(g, neighborhoods)
            assert coordinatewise_minimal(g, neighborhoods)
            family_checks += 1
    types += 1

print("VERIFY_OK")
print("friendship_graphs_checked =", types)
print("edge_pairs_checked =", edge_pairs)
print("coordinate_optimization_LPs =", coord_lps)
print("sampled_minimal_family_points =", family_checks)
print("k = 2..8")
print("all size-two resolving neighborhoods are exactly outer-vertex pairs")
print("every resolving neighborhood contains at least two outer vertices")
print("all LP optima equal k with unique optimum center=0, outer=1/2")
print("all sampled points of the classified minimal-function family are feasible and coordinatewise minimal")
