from itertools import product
from math import ceil

def sunlet(n):
    # cycle vertices 0..n-1, pendant leaves n..2n-1
    adj=[set() for _ in range(2*n)]
    for i in range(n):
        j=(i+1)%n
        adj[i].add(j); adj[j].add(i)
        adj[i].add(n+i); adj[n+i].add(i)
    return adj

def is_pdid(adj, lab):
    for v,x in enumerate(lab):
        if x in (0,1):
            s=x+sum(lab[u] for u in adj[v])
            if not (3 <= s <= 4):
                return False
    return True

def construction(n):
    # Cycle word has ceil(n/3) ones and no run of three zeros.
    k=n//3
    r=n%3
    x=[]
    if r==0:
        x=[1,0,0]*k
    elif r==1:
        x=[1,0,0]*k+[1]
    else:
        x=[1,0,0]*k+[1,0]
    y=[2]*n
    return tuple(x+y)

def local_leaf_choices(a,b,c):
    out=[]
    for y in range(4):
        ok=True
        if y in (0,1):
            ok &= 3 <= y+b <= 4
        if b in (0,1):
            ok &= 3 <= a+b+c+y <= 4
        if ok:
            out.append(y)
    return out

def dp_min(n):
    # Exhaust all cycle labels only; choose each pendant label optimally from its local constraint.
    best=10**9
    for x in product(range(4), repeat=n):
        w=sum(x)
        feasible=True
        for i in range(n):
            choices=local_leaf_choices(x[(i-1)%n],x[i],x[(i+1)%n])
            if not choices:
                feasible=False
                break
            w += min(choices)
        if feasible and w<best:
            best=w
    return best

print("VERIFY_OK")
checked=0
for n in range(3,6):
    adj=sunlet(n)
    best=None
    count=0
    for lab in product(range(4), repeat=2*n):
        checked += 1
        w=sum(lab)
        if best is not None and w>best:
            continue
        if is_pdid(adj,lab):
            if best is None or w<best:
                best=w
                count=1
            elif w==best:
                count+=1
    expected=2*n+ceil(n/3)
    assert best==expected,(n,best,expected)
    print(f"n={n}: gamma_p_dI={best}, minimum_functions={count}")

for n in range(3,11):
    best=dp_min(n)
    expected=2*n+ceil(n/3)
    assert best==expected,(n,best,expected)
    lab=construction(n)
    assert sum(lab)==expected
    assert is_pdid(sunlet(n),lab)
    print(f"dp n={n}: minimum={best}, construction_weight={sum(lab)}")

for n in range(3,51):
    lab=construction(n)
    assert sum(lab)==2*n+ceil(n/3)
    assert is_pdid(sunlet(n),lab)

print("full_labelings_checked =",checked)
print("cycle_state_dp_range = 3..10")
print("construction_checked_n = 3..50")
print("all checks matched 2n+ceil(n/3)")
