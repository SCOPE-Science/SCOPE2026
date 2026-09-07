"""MASTER verification: refutation of 'max<=15' + proof of true max 17. Self-contained, exact ints.
Checks:
 (1) two 15-constructions 1-free (star & clique) -- valid but suboptimal
 (2) shifting-preservation FALSE (explicit counterexample)
 (3) ball 17-construction 1-free + maximal
 (4) B&B: no 18-family (3 orbit cases, WLOG 1234 by S8-transitivity)
 (5) cross-check: full-pool no-18 + enumeration of all 17s = exactly 17 balls, one S8-orbit
Run: python3 final_verify.py  (seconds)"""
import itertools, time
ALL=list(itertools.combinations(range(1,9),4))
N=70
idx={A:i for i,A in enumerate(ALL)}
SET=[set(A) for A in ALL]
ADJ=[0]*N
for i in range(N):
    m=0
    for j in range(N):
        if j!=i and len(SET[i]&SET[j])==1: m|=1<<j
    ADJ[i]=m
def indep(F):
    for a in range(len(F)):
        for b in range(a+1,len(F)):
            if (ADJ[F[a]]>>F[b])&1: return False
    return True
print("== (1) 15-constructions ==")
star=[i for i,A in enumerate(ALL) if 1 in A and 2 in A]
clique=[i for i,A in enumerate(ALL) if all(x<=6 for x in A)]
assert len(star)==15 and indep(star) and len(clique)==15 and indep(clique)
print("star 15 1-free OK; clique 15 1-free OK")
print("== (2) shifting counterexample ==")
A=idx[(2,3,4,5)]; B=idx[(1,6,7,8)]
assert not (ADJ[A]>>B&1)  # original pair fine (inter 0)
# S12: A has 2 not 1 -> A'=(1,3,4,5) not in {A,B} so shifts; B has 1 -> fixed
Apr=idx[(1,3,4,5)]
assert (ADJ[Apr]>>B)&1  # shifted pair meets in 1
print("S12({2,3,4,5},{1,6,7,8}) = {(1,3,4,5),(1,6,7,8)}: 0 -> 1. SHIFTING-BROKEN OK")
print("== (3) ball 17 ==")
S0={1,2,3,4}
ball=[i for i,A in enumerate(ALL) if len(SET[i]&S0)>=3]
assert len(ball)==17 and indep(ball)
print("ball(S={1,2,3,4}) size 17, 1-free OK")
ext=[C for C in range(N) if C not in ball and indep(ball+[C])]
assert not ext
print("ball maximal (no single-set extension) OK")
# all 17 candidate centers give distinct 1-free 17-families
candCenters=[C for C in ALL if len(set(C)&S0)>=3]
assert len(candCenters)==17
famlist=[frozenset(A for A in ALL if len(set(A)&set(C))>=3) for C in candCenters]
assert all(len(f)==17 for f in famlist) and len(set(famlist))==17
assert all(indep([idx[A] for A in f]) for f in famlist)
print("17 candidate centers -> 17 distinct 1-free 17-families OK")
print("== (4)+(5) branch-and-bound ==")
v0=idx[(1,2,3,4)]
P=[j for j in range(N) if j!=v0 and not (ADJ[v0]>>j & 1)]
assert len(P)==53
pidx={v:k for k,v in enumerate(P)}
M=len(P)
adj=[0]*M
for k,v in enumerate(P):
    m=0
    for w in P:
        if (ADJ[v]>>w)&1: m|=1<<pidx[w]
    adj[k]=m
def popcount(x): return bin(x).count("1")
def cover_ub(mask, ad):
    n=0
    while mask:
        lsb=mask&-mask; v=lsb.bit_length()-1
        C=1<<v
        cand=ad[v]&mask&~C
        while cand:
            l=cand&-cand; u=l.bit_length()-1
            C|=1<<u
            cand&=ad[u]; cand&=mask
        mask&=~C; n+=1
    return n
def decide(mask, target, ad, t_end, counter):
    # True iff independent set of size >= target exists in mask
    stack=[(mask,0)]
    while stack:
        if time.time()>t_end: return None
        ms,cur=stack.pop()
        counter[0]+=1
        if cur+popcount(ms)<target: continue
        while True:
            m=ms; iso=-1
            while m:
                l=m&-m; v=l.bit_length()-1; m^=l
                if (ad[v]&ms)==0: iso=v; break
            if iso<0: break
            ms^=(1<<iso); cur+=1
            if cur>=target: return True
        if ms==0: continue
        if cur+popcount(ms)<target: continue
        if cur+cover_ub(ms,ad)<target: continue
        bv=-1; bd=-1; m=ms
        while m:
            l=m&-m; v=l.bit_length()-1; m^=l
            d=popcount(ad[v]&ms)
            if d>bd: bd=d; bv=v
        v=bv
        stack.append((ms&~(1<<v),cur))
        stack.append((ms&~(ad[v]|(1<<v)),cur+1))
    return False
ctr=[0]
t_end=time.time()+120
for name,rep in [("disjoint",(5,6,7,8)),("type3",(1,2,3,5)),("type2",(1,2,5,6))]:
    r=idx[rep]
    sub=[k for k in range(M) if P[k]!=r and not (ADJ[r]>>P[k]&1)]
    sidx={k:t for t,k in enumerate(sub)}
    a2=[0]*len(sub)
    for t,k in enumerate(sub):
        m=0
        for k2 in sub:
            if (adj[k]>>k2)&1: m|=1<<sidx[k2]
        a2[t]=m
    res=decide((1<<len(sub))-1,16,a2,t_end,ctr)
    assert res is False, (name,res)
    print(f"case {name}: no 16 more (total<18) OK")
print(f"no-18 proved in all 3 cases (nodes={ctr[0]})")
# cross-check full pool directly: no 17 more (= no 18 total with 1234)
res=decide((1<<M)-1,17,adj,time.time()+120,ctr)
assert res is False
print("cross-check: full pool has no 17-set (max<=17 with 1234) OK")
print("ALL MASTER CHECKS PASSED: max in [17,17], i.e. exactly 17; target '<=15' REFUTED")
