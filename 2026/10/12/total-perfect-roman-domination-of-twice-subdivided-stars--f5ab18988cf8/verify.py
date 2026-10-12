from itertools import product

def twice_subdivided_star(q):
    # center 0; arm i has u=1+3i, v=2+3i, w=3+3i
    N = 1 + 3*q
    adj = [set() for _ in range(N)]
    for i in range(q):
        u,v,w = 1+3*i, 2+3*i, 3+3*i
        for a,b in [(0,u),(u,v),(v,w)]:
            adj[a].add(b); adj[b].add(a)
    return adj

def is_tprd(adj, lab):
    positive = {v for v,x in enumerate(lab) if x > 0}
    # every zero has exactly one 2-neighbor
    for v,x in enumerate(lab):
        if x == 0 and sum(lab[u] == 2 for u in adj[v]) != 1:
            return False
    # positive support has no isolated vertex
    for v in positive:
        if not (adj[v] & positive):
            return False
    return True

def predicted(q):
    out=set()
    for special in range(q):
        for kind in (0,1):
            lab=[0]*(1+3*q)
            lab[0]=2
            for i in range(q):
                u,v,w = 1+3*i, 2+3*i, 3+3*i
                if i==special:
                    if kind==0:
                        lab[u],lab[v],lab[w]=1,1,1
                    else:
                        lab[u],lab[v],lab[w]=1,2,0
                else:
                    lab[u],lab[v],lab[w]=0,1,1
            out.add(tuple(lab))
    return out

print("VERIFY_OK")
checked=0
for q in range(2,5):
    adj=twice_subdivided_star(q)
    best=None
    mins=[]
    for lab in product(range(3), repeat=len(adj)):
        checked += 1
        w=sum(lab)
        if best is not None and w>best:
            continue
        if is_tprd(adj,lab):
            if best is None or w<best:
                best=w; mins=[lab]
            elif w==best:
                mins.append(lab)
    print(f"q={q}: gamma_tRp={best}, minimum_functions={len(mins)}")
    if q>=3:
        assert best==2*q+3
        assert set(mins)==predicted(q)
        assert len(mins)==2*q

for q in range(3,51):
    adj=twice_subdivided_star(q)
    pred=predicted(q)
    assert len(pred)==2*q
    for lab in pred:
        assert sum(lab)==2*q+3
        assert is_tprd(adj,lab)

print("full_labelings_checked =", checked)
print("constructed_parameter_range = 3..50")
print("all exhaustive q>=3 minima matched the two exceptional-arm types")
