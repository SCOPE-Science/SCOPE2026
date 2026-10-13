from itertools import combinations
from collections import deque
from math import comb

def crown(n):
    adj=[set() for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                adj[i].add(n+j)
                adj[n+j].add(i)
    return adj

def all_dist(adj):
    N=len(adj)
    D=[]
    for s in range(N):
        d=[10**9]*N
        d[s]=0
        q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v] == 10**9:
                    d[v]=d[u]+1
                    q.append(v)
        D.append(d)
    return D

def geodesic_internal_masks(adj,D,u,v):
    L=D[u][v]
    out=[]
    path=[u]
    def rec(x):
        if x == v:
            m=0
            for w in path[1:-1]:
                m |= 1 << w
            out.append(m)
            return
        dx=D[u][x]
        for y in adj[x]:
            if D[u][y] == dx+1 and D[u][y] + D[y][v] == L:
                path.append(y)
                rec(y)
                path.pop()
    rec(u)
    return sorted(set(out))

def direct_total_visible(n,adj,D,Xmask,paths):
    N=2*n
    for u in range(N):
        for v in range(u+1,N):
            if not any((m & Xmask)==0 for m in paths[(u,v)]):
                return False
    return True

def predicted(n,Xmask):
    # A = 0..n-1, B = n..2n-1.
    a_out=sum(1 for i in range(n) if not ((Xmask>>i)&1))
    b_out=sum(1 for j in range(n) if not ((Xmask>>(n+j))&1))
    return a_out >= 3 and b_out >= 3

total_subsets=0
total_geodesic_families=0

for n in range(3,9):
    adj=crown(n)
    D=all_dist(adj)
    paths={}
    for u in range(2*n):
        for v in range(u+1,2*n):
            paths[(u,v)] = geodesic_internal_masks(adj,D,u,v)
            total_geodesic_families += len(paths[(u,v)])
    coeff=[0]*(2*n+1)
    maximal=[]
    valid_masks=[]
    for Xmask in range(1<<(2*n)):
        actual=direct_total_visible(n,adj,D,Xmask,paths)
        expect=predicted(n,Xmask)
        assert actual == expect, (n,Xmask,actual,expect)
        total_subsets += 1
        if actual:
            coeff[Xmask.bit_count()] += 1
            valid_masks.append(Xmask)
    # Product formula.
    side=[comb(n,k) if 0 <= k <= n-3 else 0 for k in range(n+1)]
    exp=[0]*(2*n+1)
    for i,a in enumerate(side):
        for j,b in enumerate(side):
            if i+j < len(exp):
                exp[i+j] += a*b
    assert coeff == exp, (n,coeff,exp)
    valid=set(valid_masks)
    for Xmask in valid_masks:
        ismax=True
        for v in range(2*n):
            if not ((Xmask>>v)&1):
                if (Xmask | (1<<v)) in valid:
                    ismax=False
                    break
        if ismax:
            maximal.append(Xmask)
    expected_max_count = comb(n,3)**2
    expected_max_size = 2*n-6
    assert len(maximal) == expected_max_count, (n,len(maximal),expected_max_count)
    assert all(m.bit_count()==expected_max_size for m in maximal)
    degree=max(i for i,c in enumerate(coeff) if c)
    assert degree == expected_max_size
    print(f"n={n}: valid_sets={sum(coeff)}, degree={degree}, maximal_sets={len(maximal)}")

print("VERIFY_OK")
print("n_range = 3..8")
print("vertex_subsets_checked =", total_subsets)
print("shortest_path_families_enumerated =", total_geodesic_families)
print("all direct total-visibility tests matched the complement-size criterion")
print("all polynomial coefficients, degrees, and maximal-set counts matched")
