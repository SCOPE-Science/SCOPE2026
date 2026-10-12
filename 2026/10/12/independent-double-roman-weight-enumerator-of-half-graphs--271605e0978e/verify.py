from itertools import product
from collections import Counter

def half_adj(n):
    adj=[set() for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            if i <= j:
                adj[i].add(n+j); adj[n+j].add(i)
    return adj

def is_idrd(n, lab):
    adj=half_adj(n)
    pos={v for v,x in enumerate(lab) if x>0}
    if any(adj[u] & pos for u in pos):
        return False
    for v,x in enumerate(lab):
        if x==0:
            if not (any(lab[u]==3 for u in adj[v]) or sum(lab[u]==2 for u in adj[v])>=2):
                return False
        elif x==1:
            if not any(lab[u]>=2 for u in adj[v]):
                return False
    return True

def predicted(n, lab):
    pos={v for v,x in enumerate(lab) if x>0}
    for t in range(n+1):
        S=set(range(t,n)) | {n+j for j in range(t)}
        if pos != S:
            continue
        if any(lab[v] not in (2,3) for v in S): return False
        if any(lab[v]!=0 for v in range(2*n) if v not in S): return False
        if t==0: return lab[0]==3
        if t==n: return lab[2*n-1]==3
        return lab[n+t-1]==3 and lab[t]==3
    return False

def expected_hist(n):
    c=Counter()
    for mask in range(1<<(n-1)):
        w=3+sum(3 if (mask>>i)&1 else 2 for i in range(n-1))
        c[w]+=2
    for t in range(1,n):
        for mask in range(1<<(n-2)):
            w=6+sum(3 if (mask>>i)&1 else 2 for i in range(n-2))
            c[w]+=1
    return c

total=feasible=0
print("VERIFY_OK")
for n in range(2,6):
    hist=Counter()
    for lab in product(range(4), repeat=2*n):
        total += 1
        actual=is_idrd(n,lab)
        expect=predicted(n,lab)
        assert actual==expect,(n,lab,actual,expect)
        if actual:
            hist[sum(lab)]+=1
            feasible += 1
    assert hist==expected_hist(n)
    minw=min(hist)
    assert minw==2*n+1 and hist[minw]==2
    print(f"n={n}: i_dR={minw}, minimum_functions={hist[minw]}, total_IDRDFs={sum(hist.values())}, histogram={dict(sorted(hist.items()))}")
print("quaternary_labelings_checked =",total)
print("feasible_IDRDFs_checked =",feasible)
print("all feasible functions matched the n+1 support-family classification")
