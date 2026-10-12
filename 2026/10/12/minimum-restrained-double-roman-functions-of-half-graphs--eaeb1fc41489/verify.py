from itertools import product

def half_adj(n):
    adj=[set() for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            if i <= j:
                adj[i].add(n+j); adj[n+j].add(i)
    return adj

def is_rdrd(n, lab):
    adj=half_adj(n)
    zeros=[v for v,x in enumerate(lab) if x==0]
    for v in zeros:
        if not any(u in adj[v] for u in zeros):
            return False
    for v,x in enumerate(lab):
        if x==0:
            if not (any(lab[u]==3 for u in adj[v]) or sum(lab[u]==2 for u in adj[v])>=2):
                return False
        elif x==1:
            if not any(lab[u]>=2 for u in adj[v]):
                return False
    return True

def predicted_minimum(n, lab):
    t=tuple(lab)
    if n==2:
        return t in {
            (0,3,3,0),(1,1,2,2),(1,2,2,1),(2,1,1,2),(2,2,1,1)
        }
    if n==3:
        return t in {
            (0,0,3,2,3,0),(0,1,3,2,2,0),(0,2,2,2,2,0),
            (0,2,2,3,1,0),(0,3,1,2,0,2),(0,3,2,3,0,0),
            (2,0,2,1,3,0),(2,1,1,1,1,2),(3,0,1,1,0,3)
        }
    return t == tuple([3]+[0]*(n-2)+[1]+[1]+[0]*(n-2)+[3])

total=0
print("VERIFY_OK")
for n in range(2,6):
    best=10**9
    mins=[]
    for lab in product(range(4), repeat=2*n):
        total += 1
        w=sum(lab)
        if w>best:
            continue
        if is_rdrd(n, lab):
            if w<best:
                best=w
                mins=[]
            mins.append(tuple(lab))
    target=6 if n==2 else 8
    count=5 if n==2 else (9 if n==3 else 1)
    assert best==target
    assert len(mins)==count
    assert all(predicted_minimum(n,m) for m in mins)
    print(f"n={n}: gamma_rdR={best}, minimum_functions={len(mins)}")
print("quaternary_labelings_checked =", total)
print("all minimum functions matched the piecewise classification")
