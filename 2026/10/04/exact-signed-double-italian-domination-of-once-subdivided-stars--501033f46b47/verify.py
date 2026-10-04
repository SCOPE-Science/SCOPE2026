from itertools import product
from math import comb

VALUES=(-1,1,2,3)

def subdivided_star(q):
    n=1+2*q
    adj=[set() for _ in range(n)]
    c=0
    for i in range(q):
        v=1+2*i
        u=v+1
        adj[c].add(v); adj[v].add(c)
        adj[v].add(u); adj[u].add(v)
    return adj

def is_sdidf(adj, lab):
    for v in range(len(adj)):
        if lab[v] + sum(lab[u] for u in adj[v]) < 1:
            return False
        pos = sum(max(lab[u],0) for u in adj[v])
        if lab[v] == -1 and pos < 3:
            return False
        if lab[v] == 1 and pos < 2:
            return False
    return True

def brute(q):
    adj=subdivided_star(q)
    n=len(adj)
    best=10**9
    count=0
    for lab in product(VALUES, repeat=n):
        w=sum(lab)
        if w>best:
            continue
        if is_sdidf(adj,lab):
            if w<best:
                best=w
                count=0
            count+=1
    return best,count

def arm_states(center):
    out=[]
    for v,u in product(VALUES, repeat=2):
        # leaf u
        if u+v < 1:
            continue
        if u==-1 and max(v,0)<3:
            continue
        if u==1 and max(v,0)<2:
            continue
        # support v
        if center+v+u < 1:
            continue
        pos=max(center,0)+max(u,0)
        if v==-1 and pos<3:
            continue
        if v==1 and pos<2:
            continue
        out.append((v,u,v+u))
    return out

def dp_exact(q):
    best=10**9
    count=0
    for c in VALUES:
        states=arm_states(c)
        # DP keyed by (sum_v, sum_positive_v) -> (min arm weight, count)
        dp={(0,0):(0,1)}
        for _ in range(q):
            nd={}
            for (sv,sp),(w,cnt) in dp.items():
                for v,u,cost in states:
                    key=(sv+v, sp+max(v,0))
                    nw=w+cost
                    if key not in nd or nw<nd[key][0]:
                        nd[key]=(nw,cnt)
                    elif nw==nd[key][0]:
                        nd[key]=(nw,nd[key][1]+cnt)
            dp=nd
        for (sv,sp),(w,cnt) in dp.items():
            if c+sv < 1:
                continue
            if c==-1 and sp<3:
                continue
            if c==1 and sp<2:
                continue
            total=c+w
            if total<best:
                best=total; count=cnt
            elif total==best:
                count+=cnt
    return best,count

def formula(q):
    assert q>=4
    val=q+(q+3)//4+1
    if q%4==1:
        k=(q-1)//4
        cnt=comb(q,k+1)+comb(q,k)
    else:
        cnt=comb(q,(q+3)//4)
    return val,cnt

# Direct full-label exhaustive checks where feasible.
for q in (4,5):
    got=brute(q)
    exp=formula(q)
    assert got==exp,(q,got,exp)

# Independent exact DP from the defining local constraints over a much wider range.
for q in range(4,61):
    got=dp_exact(q)
    exp=formula(q)
    assert got==exp,(q,got,exp)

print("VERIFY_OK")
print("full_label_bruteforce_q = 4,5")
print("direct_labelings_checked =", 4**9 + 4**11)
print("exact_arm_state_DP_q = 4..60")
print("all optimum values matched q+ceil(q/4)+1")
print("all optimum counts matched the residue-class formula")
