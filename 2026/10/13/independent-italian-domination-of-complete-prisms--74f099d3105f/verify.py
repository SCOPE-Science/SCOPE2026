from itertools import product

def complete_prism(n):
    # Vertices 0,...,n-1 form layer A, n,...,2n-1 form layer B.
    # Each layer is a clique, and i is matched to n+i.
    adj=[set() for _ in range(2*n)]
    for base in (0,n):
        for i in range(n):
            for j in range(i+1,n):
                u=base+i
                v=base+j
                adj[u].add(v)
                adj[v].add(u)
    for i in range(n):
        adj[i].add(n+i)
        adj[n+i].add(i)
    return adj

def is_iidf(adj, lab):
    # Independent Italian domination:
    # positive support is independent, and every zero vertex sees label sum at least 2.
    pos={v for v,x in enumerate(lab) if x>0}
    for v in pos:
        if adj[v] & pos:
            return False
    for v,x in enumerate(lab):
        if x==0 and sum(lab[u] for u in adj[v]) < 2:
            return False
    return True

def predicted(n):
    out=set()
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            lab=[0]*(2*n)
            lab[i]=2
            lab[n+j]=2
            out.add(tuple(lab))
    return out

print("VERIFY_OK")
checked=0
for n in range(2,7):
    adj=complete_prism(n)
    feasible=[]
    best=None
    mins=[]
    for lab in product(range(3), repeat=2*n):
        checked += 1
        if not is_iidf(adj, lab):
            continue
        feasible.append(lab)
        w=sum(lab)
        if best is None or w<best:
            best=w
            mins=[lab]
        elif w==best:
            mins.append(lab)
    print(f"n={n}: feasible={len(feasible)}, i_I={best}, minima={len(mins)}")
    if n>=3:
        pred=predicted(n)
        assert set(feasible)==pred, (n, len(feasible), len(pred))
        assert best==4
        assert len(mins)==n*(n-1)

for n in range(3,51):
    adj=complete_prism(n)
    pred=predicted(n)
    assert len(pred)==n*(n-1)
    for lab in pred:
        assert sum(lab)==4
        assert is_iidf(adj, lab)

print("ternary_labelings_checked =", checked)
print("construction_checked_n = 3..50")
print("for every exhaustive n>=3, all feasible functions matched the ordered anti-matching 2-2 classification")
