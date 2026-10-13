from itertools import product

def half_adj(n):
    adj=[set() for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            if i <= j:
                adj[i].add(n+j)
                adj[n+j].add(i)
    return adj

def is_oitr(n, lab):
    adj=half_adj(n)
    zeros=[v for v,x in enumerate(lab) if x==0]
    for u in zeros:
        if any(v in adj[u] for v in zeros):
            return False
    for u in zeros:
        if not any(lab[v]==2 for v in adj[u]):
            return False
    for u,x in enumerate(lab):
        if x>0 and not any(lab[v]>0 for v in adj[u]):
            return False
    return True

def predicted_minima(n):
    out=[]
    out.append(tuple([1]+[0]*(n-1)+[1]*(n-1)+[2]))
    for t in range(1,n):
        A=[2]+[1]*(t-1)+[0]*(n-t)
        B=[0]*t+[1]*(n-t-1)+[2]
        out.append(tuple(A+B))
    out.append(tuple([2]+[1]*(n-1)+[0]*(n-1)+[1]))
    if n==2:
        out.append(tuple([1]*(2*n)))
    return set(out)

total=0
print("VERIFY_OK")
for n in range(2,8):
    best=10**9
    mins=[]
    for lab in product(range(3), repeat=2*n):
        total += 1
        w=sum(lab)
        if w>best:
            continue
        if is_oitr(n,lab):
            if w<best:
                best=w
                mins=[]
            mins.append(tuple(lab))
    expected=predicted_minima(n)
    assert best==n+2
    assert set(mins)==expected
    assert len(mins)==(4 if n==2 else n+1)
    print(f"n={n}: gamma_oitR={best}, minimum_functions={len(mins)}")
print("ternary_labelings_checked =", total)
print("all minimum functions matched the staircase classification")
