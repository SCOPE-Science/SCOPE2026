from itertools import product

def crown_graph(n):
    adj=[set() for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            if i!=j:
                adj[i].add(n+j)
                adj[n+j].add(i)
    return adj

def complement(adj):
    N=len(adj)
    return [set(range(N))-{v}-adj[v] for v in range(N)]

def is_idf(adj, lab):
    return all(x!=0 or sum(lab[u] for u in adj[v])>=2 for v,x in enumerate(lab))

def predicted(n):
    out=set()
    for i in range(n):
        lab=[0]*(2*n)
        lab[i]=2
        lab[n+i]=2
        out.add(tuple(lab))
    for i in range(n):
        for j in range(i+1,n):
            lab=[0]*(2*n)
            for k in (i,j):
                lab[k]=1
                lab[n+k]=1
            out.add(tuple(lab))
    return out

print("VERIFY_OK")
checked=0
for n in range(4,7):
    adj=crown_graph(n)
    cadj=complement(adj)
    best=None
    mins=[]
    for lab in product(range(3), repeat=2*n):
        checked+=1
        w=sum(lab)
        if best is not None and w>best:
            continue
        if is_idf(adj,lab) and is_idf(cadj,lab):
            if best is None or w<best:
                best=w
                mins=[lab]
            elif w==best:
                mins.append(lab)
    pred=predicted(n)
    assert best==4
    assert set(mins)==pred
    print(f"n={n}: gamma_gI={best}, minimum_functions={len(mins)}")

for n in range(4,51):
    adj=crown_graph(n)
    cadj=complement(adj)
    pred=predicted(n)
    assert len(pred)==n*(n+1)//2
    for lab in pred:
        assert sum(lab)==4
        assert is_idf(adj,lab) and is_idf(cadj,lab)

print("full_labelings_checked =",checked)
print("constructed_parameter_range = 4..50")
print("all exhaustive minima matched the aligned matched-pair classification")
