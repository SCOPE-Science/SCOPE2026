from itertools import product

def half_adj(n):
    adj=[set() for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            if i <= j:
                adj[i].add(n+j)
                adj[n+j].add(i)
    return adj

def is_qtitalian(n, lab):
    adj=half_adj(n)
    for v,x in enumerate(lab):
        if x==0:
            if sum(lab[u] for u in adj[v]) < 2:
                return False
        elif x==2:
            if not any(lab[u]>0 for u in adj[v]):
                return False
    return True

def predicted_minimum(n, lab):
    if n==2:
        return tuple(lab) in {(0,1,1,1),(1,1,1,0)}
    if n==3:
        return tuple(lab) in {
            (0,0,1,1,1,1),
            (0,1,1,1,1,0),
            (1,1,1,1,0,0),
            (2,0,0,0,0,2),
        }
    return tuple(lab)==tuple([2]+[0]*(n-1)+[0]*(n-1)+[2])

total=0
print("VERIFY_OK")
for n in range(2,8):
    best=10**9
    mins=[]
    for lab in product(range(3), repeat=2*n):
        total+=1
        w=sum(lab)
        if w>best:
            continue
        if is_qtitalian(n,lab):
            if w<best:
                best=w
                mins=[]
            mins.append(tuple(lab))
    target=3 if n==2 else 4
    assert best==target
    expected_count=2 if n==2 else (4 if n==3 else 1)
    assert len(mins)==expected_count
    assert all(predicted_minimum(n,m) for m in mins)
    print(f"n={n}: gamma_qtI={best}, minimum_functions={len(mins)}")
print("ternary_labelings_checked =", total)
print("all minimum functions matched the piecewise classification")
