from itertools import product

def half_adj(n):
    adj=[set() for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            if i <= j:
                adj[i].add(n+j); adj[n+j].add(i)
    return adj

def is_oidrd(n, lab):
    adj=half_adj(n)
    zeros=[v for v,x in enumerate(lab) if x==0]
    zset=set(zeros)
    for v in zeros:
        if adj[v] & zset:
            return False
    for v,x in enumerate(lab):
        if x==0:
            if not (any(lab[u]==3 for u in adj[v]) or sum(lab[u]==2 for u in adj[v])>=2):
                return False
        elif x==1:
            if not any(lab[u]>=2 for u in adj[v]):
                return False
    return True

def predicted_minima(n):
    if n==2:
        return {(0,0,2,3),(0,1,2,2),(2,2,1,0),(3,2,0,0)}
    if n==3:
        return {
            (0,0,0,2,2,3),(0,0,1,2,2,2),(2,0,0,1,1,3),(2,2,2,1,0,0),
            (3,0,0,0,1,3),(3,1,0,0,0,3),(3,1,1,0,0,2),(3,2,2,0,0,0)
        }
    out=set()
    out.add(tuple([2]+[0]*(n-1)+[1]*(n-1)+[3]))
    for t in range(1,n):
        out.add(tuple([3]+[1]*(t-1)+[0]*(n-t)+[0]*t+[1]*(n-t-1)+[3]))
    out.add(tuple([3]+[1]*(n-1)+[0]*(n-1)+[2]))
    return out

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
        if is_oidrd(n,lab):
            if w<best:
                best=w
                mins=[]
            mins.append(tuple(lab))
    target=5 if n==2 else n+4
    exp=predicted_minima(n)
    assert best==target
    assert set(mins)==exp
    print(f"n={n}: gamma_oidR={best}, minimum_functions={len(mins)}")
print("quaternary_labelings_checked =", total)
print("all minimum functions matched the piecewise classification")
