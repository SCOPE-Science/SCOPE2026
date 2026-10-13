from itertools import combinations
import sympy as sp


def spider_power_graph(m, ell, k):
    # vertex 0 is center; (i,a) -> 1+i*ell+(a-1), i=0..m-1, a=1..ell
    n = 1 + m * ell
    adj = [set() for _ in range(n)]
    def idx(i,a): return 1+i*ell+(a-1)
    for i in range(m):
        for a in range(1, ell+1):
            u=idx(i,a)
            if a <= k:
                adj[0].add(u); adj[u].add(0)
            for b in range(a+1, ell+1):
                if b-a <= k:
                    v=idx(i,b); adj[u].add(v); adj[v].add(u)
            for j in range(i+1,m):
                for b in range(1,ell+1):
                    if a+b <= k:
                        v=idx(j,b); adj[u].add(v); adj[v].add(u)
    return adj


def forces_all(adj, initial):
    black=set(initial)
    while True:
        move=None
        for u in tuple(black):
            white=[v for v in adj[u] if v not in black]
            if len(white)==1:
                move=white[0]; break
        if move is None:
            return len(black)==len(adj)
        black.add(move)


def zero_forcing_number(adj, upper):
    n=len(adj)
    for s in range(upper+1):
        for S in combinations(range(n),s):
            if forces_all(adj,S):
                return s
    return None


def certificate_matrix(m,ell,k):
    # W columns are indicators of consecutive windows of length k+1.
    W=sp.zeros(ell,ell-k)
    for c in range(ell-k):
        for a in range(c,c+k+1):
            W[a,c]=1
    D=W*W.T
    C=sp.zeros(ell,ell)
    for a in range(1,ell+1):
        for b in range(1,ell+1):
            if a+b <= k:
                C[a-1,b-1]=1
    B=D+C
    d=sp.Matrix([1 if a<=k else 0 for a in range(1,ell+1)])
    n=1+m*ell
    X=sp.zeros(n,n)
    for i in range(m):
        s=1+i*ell
        X[0,s:s+ell]=d.T
        X[s:s+ell,0]=d
        for j in range(m):
            t=1+j*ell
            X[s:s+ell,t:t+ell]=B if i==j else C
    return W,D,C,B,X


def support_ok(adj,X):
    n=len(adj)
    for i in range(n):
        for j in range(i+1,n):
            if (X[i,j] != 0) != (j in adj[i]):
                return False,(i,j,X[i,j],j in adj[i])
    return True,None

profiles=[]
for m in range(2,5):
    for k in range(1,4):
        for ell in range(k+1,6):
            if 1+m*ell <= 13:
                profiles.append((m,ell,k))

matrix_checks=0
brute_profiles=0
subset_tests=0
for m,ell,k in profiles:
    adj=spider_power_graph(m,ell,k)
    W,D,C,B,X=certificate_matrix(m,ell,k)
    assert W.rank()==ell-k
    assert D.rank()==ell-k
    ok,bad=support_ok(adj,X)
    assert ok,bad
    nullity=X.rows-X.rank()
    assert nullity==(m-1)*k,(m,ell,k,nullity)
    matrix_checks += 1
    target=(m-1)*k
    z=zero_forcing_number(adj,target)
    assert z==target,(m,ell,k,z,target)
    brute_profiles += 1

# A larger constructive sweep checks support and exact certificate nullity without brute force.
constructive=0
for m in range(2,7):
    for k in range(1,5):
        for ell in range(k+1,k+6):
            adj=spider_power_graph(m,ell,k)
            W,D,C,B,X=certificate_matrix(m,ell,k)
            ok,bad=support_ok(adj,X)
            assert ok,bad
            assert X.rows-X.rank()==(m-1)*k
            constructive += 1

print('ALL CHECKS PASSED')
print(f'bruteforce_profiles={brute_profiles}')
print(f'matrix_profiles_small={matrix_checks}')
print(f'constructive_profiles={constructive}')
print('small_order_limit=13')
