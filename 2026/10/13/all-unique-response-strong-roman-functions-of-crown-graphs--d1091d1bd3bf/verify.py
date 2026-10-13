from itertools import product
from math import ceil
from collections import Counter

def crown(n):
    adj=[set() for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            if i!=j:
                adj[i].add(n+j); adj[n+j].add(i)
    return adj

def is_urst(n, lab):
    adj=crown(n)
    V2={v for v,x in enumerate(lab) if x>=2}
    for v,x in enumerate(lab):
        q=sum(1 for u in adj[v] if u in V2)
        if x==0:
            if q>1: return False
        elif q!=0:
            return False
    V0={v for v,x in enumerate(lab) if x==0}
    for v in V0:
        if not any(lab[w]>=2 and lab[w]>=1+ceil(sum(1 for z in adj[w] if z in V0)/2) for w in adj[v]):
            return False
    return True

def predicted(n, lab):
    adj=crown(n)
    h=1+ceil((n-1)/2)
    V2=[v for v,x in enumerate(lab) if x>=2]
    if not V2:
        return all(x==1 for x in lab)
    if len(V2)==1:
        d=V2[0]
        if lab[d]!=h: return False
        return all((x==(0 if v in adj[d] else 1)) for v,x in enumerate(lab) if v!=d)
    if len(V2)==2:
        u,v=V2
        matched=(u<n and v==n+u) or (v<n and u==n+v)
        return matched and lab[u]==h and lab[v]==h and all(x==0 for j,x in enumerate(lab) if j not in V2)
    return False

total=0
feasible_total=0
print("VERIFY_OK")
for n in range(3,6):
    h=1+ceil((n-1)/2)
    counts=Counter()
    for lab in product(range(h+1), repeat=2*n):
        total+=1
        actual=is_urst(n,lab)
        expect=predicted(n,lab)
        assert actual==expect,(n,lab,actual,expect)
        if actual: counts[sum(lab)]+=1
    expected=Counter()
    expected[2*n]+=1
    expected[n+h]+=2*n
    expected[2*h]+=n
    assert counts==expected,(n,counts,expected)
    feasible_total+=sum(counts.values())
    print(f"n={n}: h={h}, weight_counts={dict(sorted(counts.items()))}, total_functions={sum(counts.values())}")
print("labelings_checked =", total)
print("URStRDFs_checked =", feasible_total)
print("all feasible functions matched the three-family classification and exact weight enumerator")
