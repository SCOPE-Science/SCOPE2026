#!/usr/bin/env python3
from itertools import permutations, product
from collections import Counter

def ranks(pref):
    n=len(pref)
    out=[[0]*n for _ in range(n)]
    for i,row in enumerate(pref):
        for r,x in enumerate(row,1):
            out[i][x]=r
    return out

def stable_direct(mp,wp,M):
    n=len(mp)
    mr=ranks(mp); wr=ranks(wp)
    inv=[0]*n
    for m,w in enumerate(M): inv[w]=m
    for m in range(n):
        for w in range(n):
            if w==M[m]: continue
            if mr[m][w] < mr[m][M[m]] and wr[w][m] < wr[w][inv[w]]:
                return False
    return True

def stable_listpos(mp,wp,M):
    n=len(mp)
    inv=[0]*n
    for m,w in enumerate(M): inv[w]=m
    for m in range(n):
        cur=M[m]
        for w in mp[m]:
            if w==cur: break
            husband=inv[w]
            if wp[w].index(m) < wp[w].index(husband):
                return False
    return True

def metrics_dict(mp,wp,M):
    n=len(mp); mr=ranks(mp); wr=ranks(wp)
    rs=[]
    for m,w in enumerate(M):
        rs.extend((mr[m][w],wr[w][m]))
    prof=tuple(rs.count(r) for r in range(1,n+1))
    return prof,max(rs),tuple(rs)

def metrics_pos(mp,wp,M):
    n=len(mp); rs=[]
    for m,w in enumerate(M):
        rs.extend((mp[m].index(w)+1,wp[w].index(m)+1))
    prof=tuple(sum(1 for x in rs if x==r) for r in range(1,n+1))
    return prof,max(rs),tuple(rs)

def classify(n):
    P=list(permutations(range(n)))
    Ms=P
    rel=Counter(); stable_count=Counter(); bad=[]
    for profile in product(P, repeat=2*n):
        mp=profile[:n]; wp=profile[n:]
        st=[]
        for M in Ms:
            a=stable_direct(mp,wp,M)
            b=stable_listpos(mp,wp,M)
            assert a==b
            if a:
                x=metrics_dict(mp,wp,M)
                y=metrics_pos(mp,wp,M)
                assert x==y
                st.append((M,)+x)
        stable_count[len(st)]+=1
        bp=max(x[1] for x in st)
        rg=min(x[2] for x in st)
        R={x[0] for x in st if x[1]==bp}
        G={x[0] for x in st if x[2]==rg}
        if R==G: k="equal"
        elif R < G: k="rank_subset"
        elif G < R: k="regret_subset"
        elif R & G: k="overlap_nonnested"
        else: k="disjoint"
        rel[k]+=1
        if k=="disjoint": bad.append((profile,st,R,G))
    return rel,stable_count,bad

def transform(profile,pm,pw,swap=False):
    n=len(profile)//2
    mp=profile[:n]; wp=profile[n:]
    nm=[None]*n; nw=[None]*n
    if not swap:
        for om in range(n):
            nm[pm[om]]=tuple(pw[w] for w in mp[om])
        for ow in range(n):
            nw[pw[ow]]=tuple(pm[m] for m in wp[ow])
    else:
        # pm maps old women to new men; pw maps old men to new women
        for ow in range(n):
            nm[pm[ow]]=tuple(pw[m] for m in wp[ow])
        for om in range(n):
            nw[pw[om]]=tuple(pm[w] for w in mp[om])
    return tuple(nm+nw)

def canonical(profile):
    n=len(profile)//2
    P=list(permutations(range(n)))
    return min(transform(profile,pm,pw,s) for pm in P for pw in P for s in (False,True))

r2,s2,b2=classify(2)
assert r2==Counter({"equal":16})
assert s2==Counter({1:14,2:2})
assert not b2

r3,s3,b3=classify(3)
assert r3==Counter({"equal":37716,"rank_subset":6984,"disjoint":1956}),r3
assert s3==Counter({1:34080,2:11484,3:1092}),s3
assert len(b3)==1956

# Every disjoint instance has a unique minimum-regret optimizer.
assert all(len(G)==1 for _,_,_,G in b3)
assert Counter(len(st) for _,st,_,_ in b3)==Counter({2:1728,3:228})
assert Counter(len(R) for _,_,R,_ in b3)==Counter({1:1872,2:84})

orbits=Counter(canonical(p) for p,_,_,_ in b3)
assert len(orbits)==29
assert Counter(orbits.values())==Counter({72:26,36:2,12:1})
assert sum(orbits.values())==1956

# Canonical human-readable witness.
mp=((0,1,2),(0,1,2),(0,2,1))
wp=((0,1,2),(2,1,0),(1,2,0))
st=[]
for M in permutations(range(3)):
    if stable_direct(mp,wp,M):
        prof,reg,ranksv=metrics_dict(mp,wp,M)
        st.append((M,prof,reg,ranksv))
assert st==[
    ((0,1,2),(2,4,0),2,(1,1,2,2,2,2)),
    ((0,2,1),(4,0,2),3,(1,1,3,1,3,1)),
]
# first is unique minimum-regret; second is unique rank-maximal
assert max(x[1] for x in st)==(4,0,2)
assert min(x[2] for x in st)==2

print("VERIFY_OK")
print("n2_relations",dict(r2))
print("n3_relations",dict(r3))
print("n3_stable_count_distribution",dict(sorted(s3.items())))
print("disjoint_profiles",len(b3),"incidence","1956/46656=163/3888")
print("disjoint_stable_counts",dict(Counter(len(st) for _,st,_,_ in b3)))
print("rank_optimizer_sizes",dict(Counter(len(R) for _,_,R,_ in b3)))
print("regret_optimizer_sizes",dict(Counter(len(G) for _,_,_,G in b3)))
print("orbits",len(orbits),"orbit_size_distribution",dict(Counter(orbits.values())))
print("witness_stable_matchings",st)
