from itertools import combinations

def crown_adj(n):
    adj=[set() for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                adj[i].add(n+j); adj[n+j].add(i)
    return adj

def is_doids(n, S):
    adj=crown_adj(n); S=set(S)
    comp=set(range(2*n))-S
    if any(adj[v] & comp for v in comp):
        return False
    return all((v in S) + len(adj[v] & S) >= 2 for v in range(2*n))

def predicted_minima(n):
    out=set()
    A=set(range(n)); B=set(range(n,2*n))
    if n==3:
        for i in range(n):
            out.add(frozenset(set(range(2*n))-{i,n+i}))
        return out
    for T in combinations(A,2): out.add(frozenset(B|set(T)))
    for T in combinations(B,2): out.add(frozenset(A|set(T)))
    if n==4:
        for i in range(n):
            out.add(frozenset(set(range(2*n))-{i,n+i}))
    return out

total=0
print("VERIFY_OK")
for n in range(3,9):
    best=2*n+1; mins=[]
    for mask in range(1<<(2*n)):
        total += 1
        w=mask.bit_count()
        if w>best: continue
        S=[v for v in range(2*n) if (mask>>v)&1]
        if is_doids(n,S):
            if w<best:
                best=w; mins=[]
            mins.append(frozenset(S))
    target=4 if n==3 else n+2
    expected=predicted_minima(n)
    assert best==target,(n,best,target)
    assert set(mins)==expected,(n,len(mins),len(expected),set(mins)^expected)
    print(f"n={n}: gamma_doi={best}, minimum_sets={len(mins)}")
print("subsets_checked =", total)
print("all minimum sets matched the piecewise classification")
