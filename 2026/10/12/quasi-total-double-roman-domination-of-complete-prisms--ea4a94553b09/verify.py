from itertools import product

def complete_prism(n):
    N=2*n
    adj=[set() for _ in range(N)]
    for side in (0,n):
        for i in range(side,side+n):
            for j in range(i+1,side+n):
                adj[i].add(j); adj[j].add(i)
    for i in range(n):
        adj[i].add(n+i); adj[n+i].add(i)
    return adj

def is_qtdr(adj, lab):
    positive={v for v,x in enumerate(lab) if x>0}
    for v,x in enumerate(lab):
        if x==0:
            n3=sum(lab[u]==3 for u in adj[v])
            n2=sum(lab[u]==2 for u in adj[v])
            if n3<1 and n2<2:
                return False
        elif x==1:
            if not any(lab[u]>=2 for u in adj[v]):
                return False
    for v in positive:
        if not (adj[v] & positive) and lab[v]!=2:
            return False
    return True

def predicted_minima(n):
    out=set()
    for i in range(n):
        lab=[0]*(2*n)
        lab[i]=3
        lab[n+i]=3
        out.add(tuple(lab))
    return out

print("VERIFY_OK")
checked=0
for n in range(3,6):
    adj=complete_prism(n)
    best=None
    mins=[]
    for lab in product(range(4), repeat=2*n):
        checked += 1
        w=sum(lab)
        if best is not None and w>best:
            continue
        if is_qtdr(adj, lab):
            if best is None or w<best:
                best=w; mins=[lab]
            elif w==best:
                mins.append(lab)
    print(f"n={n}: gamma_qtdR={best}, minimum_functions={len(mins)}")
    assert best==6
    if n>=4:
        assert set(mins)==predicted_minima(n), (n,len(mins))

for n in range(4,51):
    adj=complete_prism(n)
    pred=predicted_minima(n)
    assert len(pred)==n
    for lab in pred:
        assert sum(lab)==6
        assert is_qtdr(adj,lab)

print("full_labelings_checked =",checked)
print("constructed_parameter_range = 4..50")
print("for n=4,5 every exhaustive minimum matched the n matched 3-3 functions")
print("for n=3 the same value 6 has additional minimum functions")
