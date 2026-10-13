from itertools import product

def chain_adj(degs, t):
    s=len(degs)
    adj=[set() for _ in range(s+t)]
    for i,d in enumerate(degs):
        for j in range(d):
            adj[i].add(s+j); adj[s+j].add(i)
    return adj

def is_tdr(adj, lab):
    pos={v for v,x in enumerate(lab) if x>0}
    if any(not (adj[v] & pos) for v in pos):
        return False
    for v,x in enumerate(lab):
        if x==0:
            if not (any(lab[u]==3 for u in adj[v]) or sum(lab[u]==2 for u in adj[v])>=2):
                return False
        elif x==1 and not any(lab[u]>=2 for u in adj[v]):
            return False
    return True

def universal_sets(degs,t):
    s=len(degs)
    ux={i for i,d in enumerate(degs) if d==t}
    uy={s+j for j in range(t) if all(d>j for d in degs)}
    return ux,uy

def predicted_minimum(degs,t,lab):
    s=len(degs)
    ux,uy=universal_sets(degs,t)
    xs=[i for i,x in enumerate(lab[:s]) if x]
    ys=[s+j for j,x in enumerate(lab[s:]) if x]
    return sum(lab)==6 and len(xs)==len(ys)==1 and lab[xs[0]]==3 and lab[ys[0]]==3 and xs[0] in ux and ys[0] in uy

types=0
labelings=0
minimums=0
print("VERIFY_OK")
for s in range(3,5):
    for t in range(3,5):
        for degs in product(range(1,t+1), repeat=s):
            if tuple(sorted(degs))!=degs or degs[-1]!=t:
                continue
            types+=1
            adj=chain_adj(degs,t)
            best=10**9
            mins=[]
            for lab in product(range(4), repeat=s+t):
                labelings+=1
                w=sum(lab)
                if w>best:
                    continue
                if is_tdr(adj,lab):
                    if w<best:
                        best=w; mins=[]
                    mins.append(lab)
            ux,uy=universal_sets(degs,t)
            assert best==6,(s,t,degs,best)
            assert len(mins)==len(ux)*len(uy),(s,t,degs,len(mins),len(ux),len(uy))
            assert all(predicted_minimum(degs,t,m) for m in mins)
            minimums += len(mins)
print("chain_types_checked =",types)
print("quaternary_labelings_checked =",labelings)
print("minimum_functions_checked =",minimums)
print("all minima were exactly universal opposite-side pairs labeled 3")
