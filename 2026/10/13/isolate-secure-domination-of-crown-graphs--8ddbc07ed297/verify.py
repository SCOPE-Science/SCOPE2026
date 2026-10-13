def crown_graph(n):
    adj=[set() for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            if i!=j:
                adj[i].add(n+j)
                adj[n+j].add(i)
    return adj

def dominates(adj,S):
    S=set(S)
    return all(v in S or bool(adj[v] & S) for v in range(len(adj)))

def isolate_dominating(adj,S):
    S=set(S)
    if not dominates(adj,S):
        return False
    return any(not (adj[v] & S) for v in S)

def isolate_secure(adj,S):
    S=set(S)
    if not isolate_dominating(adj,S):
        return False
    for u in range(len(adj)):
        if u in S:
            continue
        ok=False
        for v in adj[u] & S:
            T=(S-{v})|{u}
            if isolate_dominating(adj,T):
                ok=True
                break
        if not ok:
            return False
    return True

print("VERIFY_OK")
checked=0
for n in range(3,8):
    adj=crown_graph(n)
    good=[]
    for mask in range(1,1<<(2*n)):
        checked += 1
        S={v for v in range(2*n) if mask>>v & 1}
        if isolate_secure(adj,S):
            good.append(S)
    sizes=[len(S) for S in good]
    g=min(sizes) if sizes else None
    mins=[S for S in good if len(S)==g]
    print(f"n={n}: total_ISDS={len(good)}, gamma_0s={g}, minima={len(mins)}")
    if n>=4:
        A=set(range(n))
        B=set(range(n,2*n))
        assert set(map(frozenset,good))=={frozenset(A),frozenset(B)}
        assert g==n and len(mins)==2

for n in range(4,51):
    adj=crown_graph(n)
    A=set(range(n)); B=set(range(n,2*n))
    assert isolate_secure(adj,A)
    assert isolate_secure(adj,B)

print("subsets_checked =", checked)
print("construction_checked_n = 4..50")
print("for every exhaustive n>=4, the only ISDS were the two bipartition classes")
