#!/usr/bin/env python3
from itertools import permutations
from collections import Counter
import hashlib

R = list(permutations((0,1,2)))
IDX = {r:i for i,r in enumerate(R)}
POS = [{a:i for i,a in enumerate(r)} for r in R]

def comps(n,k=6):
    if k==1:
        yield (n,); return
    for x in range(n+1):
        for t in comps(n-x,k-1):
            yield (x,)+t

def bucklin_closed(p):
    n=sum(p)
    if n==0: return None
    first=[0,0,0]; last=[0,0,0]
    for r,c in zip(R,p):
        first[r[0]] += c
        last[r[-1]] += c
    maj=[a for a in range(3) if 2*first[a] > n]
    if len(maj)==1: return maj[0]
    m=min(last)
    ws=[a for a in range(3) if last[a]==m]
    return ws[0] if len(ws)==1 else None

def bucklin_literal(p):
    n=sum(p)
    if n==0: return None
    for depth in (1,2,3):
        scores=[0,0,0]
        for r,c in zip(R,p):
            for a in r[:depth]: scores[a]+=c
        eligible=[a for a in range(3) if 2*scores[a] > n]
        if eligible:
            mx=max(scores[a] for a in eligible)
            ws=[a for a in eligible if scores[a]==mx]
            return ws[0] if len(ws)==1 else None
    return None

def perm_profile(p,sigma):
    out=[0]*6
    for i,r in enumerate(R):
        rr=tuple(sigma[a] for a in r)
        out[IDX[rr]]=p[i]
    return tuple(out)

def canon(p):
    return min(perm_profile(p,s) for s in permutations((0,1,2)))

def profile_first(limit=6):
    events=set(); unique={}; totals={}
    for n in range(1,limit+1):
        u=0; t=0
        for p in comps(n):
            t+=1
            w1=bucklin_closed(p); w2=bucklin_literal(p)
            assert w1==w2
            if w1 is None: continue
            u+=1
            for i,r in enumerate(R):
                for k in range(1,p[i]+1):
                    q=list(p); q[i]-=k; q=tuple(q)
                    if sum(q)==0: continue
                    z1=bucklin_closed(q); z2=bucklin_literal(q)
                    assert z1==z2
                    if z1 is not None and z1!=w1 and POS[i][z1] < POS[i][w1]:
                        events.add((p,i,k,w1,z1))
        unique[n]=u; totals[n]=t
    return events,unique,totals

def event_first(limit=6):
    events=set()
    for m in range(1,limit):
        for q in comps(m):
            z=bucklin_literal(q)
            if z is None: continue
            for i,r in enumerate(R):
                for k in range(1,limit-m+1):
                    p=list(q); p[i]+=k; p=tuple(p)
                    if sum(p)>limit: break
                    w=bucklin_literal(p)
                    if w is not None and w!=z and POS[i][z] < POS[i][w]:
                        events.add((p,i,k,w,z))
    return events

ev,unique,totals=profile_first(6)
ev2=event_first(6)
assert ev==ev2
assert all(sum(p)==6 for p,_,_,_,_ in ev)
assert len(ev)==18
assert len({p for p,_,_,_,_ in ev})==18
assert Counter(k for _,_,k,_,_ in ev)==Counter({1:18})
assert totals[6]==462 and unique[6]==417
classes=Counter(canon(p) for p,_,_,_,_ in ev)
assert len(classes)==3 and Counter(classes.values())==Counter({6:3})

norm=set()
for p,i,k,w,z in ev:
    r=R[i]
    sigma=[None]*3
    for new,old in enumerate(r): sigma[old]=new
    sigma=tuple(sigma)
    norm.add((perm_profile(p,sigma),k,sigma[w],sigma[z]))
expected={
    ((1,0,0,3,2,0),1,2,1),
    ((1,1,0,3,1,0),1,2,1),
    ((1,2,0,3,0,0),1,2,1),
}
assert norm==expected
for p,k,w,z in expected:
    assert bucklin_closed(p)==2
    q=list(p); q[0]-=1; q=tuple(q)
    assert bucklin_closed(q)==1
    first=[0,0,0]; last=[0,0,0]
    for r,c in zip(R,p):
        first[r[0]]+=c; last[r[-1]]+=c
    assert first[1]==3 and sum(p)==6
    assert last==[3,2,1]
    qfirst=[0,0,0]
    for r,c in zip(R,q): qfirst[r[0]]+=c
    assert qfirst[1]==3 and sum(q)==5 and 2*qfirst[1]>5

digest=hashlib.sha256("\n".join(str(x) for x in sorted(ev)).encode()).hexdigest()
print('VERIFY_OK')
print('events_by_full_size', {n:sum(1 for e in ev if sum(e[0])==n) for n in range(1,7)})
print('total_profiles_n6', totals[6])
print('unique_outcome_profiles_n6', unique[6])
print('bad_profiles_n6', 18)
print('incidence_all_profiles', '3/77')
print('incidence_unique_profiles', '6/139')
print('abstention_size_hist', {1:18})
print('candidate_relabel_classes', 3)
print('orbit_size_hist', {6:3})
print('normalized_classes', sorted(expected))
print('event_set_sha256', digest)
