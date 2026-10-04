#!/usr/bin/env python3
from itertools import permutations, product
from collections import Counter
import hashlib


def serial_dictatorship(profile):
    n=len(profile); avail=set(range(n)); out=[]
    for pref in profile:
        for o in pref:
            if o in avail:
                out.append(o); avail.remove(o); break
    return tuple(out)

def serial_dictatorship_replay(profile):
    n=len(profile); used=[False]*n; out=[None]*n
    for i in range(n):
        for rank in range(n):
            o=profile[i][rank]
            if not used[o]:
                used[o]=True; out[i]=o; break
    return tuple(out)

def signature(profile, matching):
    n=len(profile); c=[0]*n
    for i,o in enumerate(matching): c[profile[i].index(o)] += 1
    return tuple(c)

def rankmax_bruteforce(profile):
    n=len(profile); vals=[]
    for m in permutations(range(n)):
        vals.append((signature(profile,m),m))
    best=max(s for s,_ in vals)
    return {m for s,m in vals if s==best}, best

def rankmax_weight(profile):
    n=len(profile); B=n+1
    vals=[]
    for m in permutations(range(n)):
        score=0
        for i,o in enumerate(m):
            r=profile[i].index(o)
            score += B**(n-1-r)
        vals.append((score,m))
    best=max(s for s,_ in vals)
    winners={m for s,m in vals if s==best}
    sigs={signature(profile,m) for m in winners}
    assert len(sigs)==1
    return winners, next(iter(sigs))

def normalize_objects(profile):
    mp={profile[0][j]:j for j in range(len(profile))}
    return tuple(tuple(mp[x] for x in pref) for pref in profile)

# 2x2 predecessor.
R2=list(permutations(range(2)))
for P in product(R2, repeat=2):
    assert serial_dictatorship(P)==serial_dictatorship_replay(P)
    a=rankmax_bruteforce(P); b=rankmax_weight(P)
    assert a==b
    assert serial_dictatorship(P) in a[0]

R3=list(permutations(range(3)))
bad=[]; sigpairs=Counter(); rmsizes=Counter(); classes=Counter(); digest=[]
for P in product(R3, repeat=3):
    s1=serial_dictatorship(P); s2=serial_dictatorship_replay(P)
    assert s1==s2
    a=rankmax_bruteforce(P); b=rankmax_weight(P)
    assert a==b
    RM,bestsig=a
    if s1 not in RM:
        bad.append(P)
        sigpairs[(signature(P,s1), bestsig)] += 1
        rmsizes[len(RM)] += 1
        classes[normalize_objects(P)] += 1
        digest.append(repr((P,s1,signature(P,s1),tuple(sorted(RM)),bestsig)))

assert len(bad)==54
assert rmsizes==Counter({1:36,2:18})
assert sigpairs==Counter({
    ((2,0,1),(2,1,0)):24,
    ((1,1,1),(2,0,1)):6,
    ((1,2,0),(2,0,1)):6,
    ((1,1,1),(1,2,0)):6,
    ((1,1,1),(2,1,0)):6,
    ((1,2,0),(2,1,0)):6,
})
assert len(classes)==9 and set(classes.values())=={6}
expected={
((0,1,2),(0,1,2),(1,0,2)),
((0,1,2),(0,1,2),(1,2,0)),
((0,1,2),(0,2,1),(0,2,1)),
((0,1,2),(0,2,1),(2,0,1)),
((0,1,2),(0,2,1),(2,1,0)),
((0,1,2),(1,2,0),(1,0,2)),
((0,1,2),(2,0,1),(0,2,1)),
((0,1,2),(2,1,0),(0,2,1)),
((0,1,2),(2,1,0),(2,0,1)),
}
assert set(classes)==expected
h=hashlib.sha256('\n'.join(sorted(digest)).encode()).hexdigest()
print('VERIFY_OK')
print('n2_profiles',4)
print('n2_failures',0)
print('n3_profiles',216)
print('n3_failures',54)
print('incidence','1/4')
print('rankmax_set_size_hist',dict(rmsizes))
print('signature_pair_hist',{str(k):v for k,v in sorted(sigpairs.items())})
print('object_relabel_classes',9)
print('orbit_size_hist',{6:9})
print('canonical_classes',sorted(expected))
print('failure_digest',h)
