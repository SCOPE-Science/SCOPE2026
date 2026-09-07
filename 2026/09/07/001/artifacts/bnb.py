"""Exact decision B&B: rule out independent set of size TARGET in subpool.
Usage: run cases (disjoint/type3/type2) with TARGET total. Bit-int, cover bound,
isolated reduction, max-degree branching, node budget + timeout."""
import itertools, time, sys
ALL=list(itertools.combinations(range(1,9),4))
N=70
idx={A:i for i,A in enumerate(ALL)}
inter=lambda a,b: len(set(a)&set(b))
ADJ=[0]*N
for i in range(N):
    m=0
    Ai=set(ALL[i])
    for j in range(N):
        if j!=i and len(Ai&set(ALL[j]))==1: m|=1<<j
    ADJ[i]=m
v0=idx[(1,2,3,4)]
P=[j for j in range(N) if j!=v0 and not (ADJ[v0]>>j & 1)]
pidx={v:k for k,v in enumerate(P)}
M=len(P)
adj=[0]*M
for k,v in enumerate(P):
    m=0
    row=ADJ[v]
    for w in P:
        if (row>>w)&1: m|=1<<pidx[w]
    adj[k]=m
def popcount(x): return bin(x).count("1")
def cover_ub(mask, adj):
    n=0
    while mask:
        lsb=mask&-mask; v=lsb.bit_length()-1
        C=1<<v
        cand=adj[v]&mask&~C
        while cand:
            l=cand&-cand; u=l.bit_length()-1
            C|=1<<u
            cand&=adj[u]; cand&=mask
        mask&=~C; n+=1
        if n>30:  # early stop, already weak
            # still must finish to be valid? No: partial count + popcount(rest) is valid UB
            return n+popcount(mask)
    return n
nodes=[0]
t0=time.time()
LIMIT=0
def search(mask, cur, target, adj, deadline):
    nodes[0]+=1
    if (nodes[0]&0xFFFFF)==0:
        print(f"  nodes={nodes[0]} cur={cur} pc={popcount(mask)} elapsed={time.time()-t0:.1f}s",flush=True)
    if time.time()>deadline:
        return None  # timeout unknown
    if cur+popcount(mask)<target:
        return False
    # isolated-vertex reduction: include all isolated (loop)
    while True:
        m=mask; iso=-1
        while m:
            l=m&-m; v=l.bit_length()-1; m^=l
            if (adj[v]&mask)==0:
                iso=v; break
        if iso<0: break
        mask^=(1<<iso); cur+=1
        if cur>=target: return True
    if mask==0:
        return cur>=target
    if cur+popcount(mask)<target:
        return False
    if cur+cover_ub(mask,adj)<target:
        return False
    # branch on max-degree vertex
    bestv=-1; bestd=-1
    m=mask
    while m:
        l=m&-m; v=l.bit_length()-1; m^=l
        d=popcount(adj[v]&mask)
        if d>bestd: bestd=d; bestv=v
    v=bestv
    # include v
    r=search(mask&~(adj[v]|(1<<v)), cur+1, target, adj, deadline)
    if r is True: return True
    if r is None: return None
    # exclude v
    return search(mask&~(1<<v), cur, target, adj, deadline)
def run_case(name, fixed_extra, target_total, budget_s):
    global nodes
    nodes[0]=0
    # subpool: in P, compatible with fixed_extra, excluding fixed_extra
    sub=[k for k in range(M) if P[k]!=fixed_extra and not (ADJ[fixed_extra]>>P[k]&1)]
    # reindex
    sidx={k:t for t,k in enumerate(sub)}
    n2=len(sub)
    a2=[0]*n2
    for t,k in enumerate(sub):
        m=0
        for k2 in sub:
            if (adj[k]>>k2)&1: m|=1<<sidx[k2]
        a2[t]=m
    full=(1<<n2)-1
    cur=2  # v0 + fixed_extra
    need=target_total-cur
    print(f"case {name}: subpool={n2} need>={need} more (target total {target_total})",flush=True)
    res=search(full, 0, need, a2, time.time()+budget_s)
    print(f"case {name}: result={res} nodes={nodes[0]} elapsed={time.time()-t0:.1f}s",flush=True)
    return res
if __name__=="__main__":
    target=int(sys.argv[1]) if len(sys.argv)>1 else 18
    budget=float(sys.argv[2]) if len(sys.argv)>2 else 240
    which=sys.argv[3] if len(sys.argv)>3 else "all"
    reps={"disjoint":idx[(5,6,7,8)],"type3":idx[(1,2,3,5)],"type2":idx[(1,2,5,6)]}
    for name,r in reps.items():
        if which!="all" and which!=name: continue
        run_case(name,r,target,budget)
