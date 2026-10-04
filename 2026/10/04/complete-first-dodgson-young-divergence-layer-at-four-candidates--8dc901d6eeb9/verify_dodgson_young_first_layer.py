#!/usr/bin/env python3
from itertools import permutations, product
from collections import Counter

C=(0,1,2,3)
ORDERS=tuple(permutations(C))
CPERMS=tuple(permutations(C))

def strong_cw(profile,c):
    n=len(profile)
    return all(2*sum(v.index(c)<v.index(o) for v in profile)>n for o in C if o!=c)

def weak_cw(profile,c):
    n=len(profile)
    return all(2*sum(v.index(c)<v.index(o) for v in profile)>=n for o in C if o!=c)

def dodgson_dp(profile,c):
    n=len(profile)
    opp=[x for x in C if x!=c]
    idx={x:i for i,x in enumerate(opp)}
    base=[2*sum(v.index(c)<v.index(o) for v in profile)-n for o in opp]
    dp={(0,0,0):0}
    for v in profile:
        pos=v.index(c)
        gain=[0,0,0]
        opts=[((0,0,0),0)]
        for k in range(1,pos+1):
            gain[idx[v[pos-k]]] += 2
            opts.append((tuple(gain),k))
        nd={}
        for g,cost in dp.items():
            for h,cc in opts:
                z=tuple(g[i]+h[i] for i in range(3))
                nc=cost+cc
                if nc<nd.get(z,99):
                    nd[z]=nc
        dp=nd
    return min(cost for g,cost in dp.items()
               if all(base[i]+g[i]>0 for i in range(3)))

def dodgson_direct(profile,c):
    menus=[]
    for v in profile:
        pos=v.index(c)
        local=[]
        for k in range(pos+1):
            w=list(v)
            w.pop(pos)
            w.insert(pos-k,c)
            local.append((tuple(w),k))
        menus.append(local)
    best=99
    for choices in product(*menus):
        q=tuple(x[0] for x in choices)
        cost=sum(x[1] for x in choices)
        if strong_cw(q,c):
            best=min(best,cost)
    return best

def young_subsets(profile,c):
    n=len(profile)
    best=0
    for mask in range(1,1<<n):
        q=tuple(profile[i] for i in range(n) if (mask>>i)&1)
        if weak_cw(q,c):
            best=max(best,len(q))
    return n-best

def young_three_voter_formula(profile,c):
    if strong_cw(profile,c):
        return 0
    for i in range(3):
        for j in range(i+1,3):
            if weak_cw((profile[i],profile[j]),c):
                return 1
    if any(v[0]==c for v in profile):
        return 2
    return 3

def winner_data(profile):
    ds=tuple(dodgson_dp(profile,c) for c in C)
    assert ds==tuple(dodgson_direct(profile,c) for c in C)
    ys=tuple(young_subsets(profile,c) for c in C)
    assert ys==tuple(young_three_voter_formula(profile,c) for c in C)
    D=frozenset(i for i,x in enumerate(ds) if x==min(ds))
    Y=frozenset(i for i,x in enumerate(ys) if x==min(ys))
    return D,Y,ds,ys

def relabel_profile(profile,p):
    return tuple(sorted(tuple(p[x] for x in v) for v in profile))

def canonical(profile):
    q=tuple(sorted(profile))
    return min(relabel_profile(q,p) for p in CPERMS)

# One voter: both rules select the top-ranked candidate.
for v in ORDERS:
    c=v[0]
    assert strong_cw((v,),c)
    assert young_subsets((v,),c)==0
    assert dodgson_dp((v,),c)==0

hist=Counter()
relations=Counter()
classes=Counter()
details={}
for profile in product(ORDERS,repeat=3):
    D,Y,ds,ys=winner_data(profile)
    hist[(len(D),len(Y),D==Y)] += 1
    if D!=Y:
        assert D < Y
        relations["dodgson_subset_young"] += 1
        c=canonical(profile)
        classes[c]+=1
        details.setdefault(c,winner_data(c))

assert sum(hist.values())==24**3==13824
assert hist==Counter({
    (1,1,True):12288,
    (3,3,True):528,
    (2,3,False):144,
    (2,4,False):576,
    (3,4,False):288,
})
assert relations==Counter({"dodgson_subset_young":1008})
assert len(classes)==7
assert Counter(classes.values())==Counter({144:7})

expected={
((0,1,2,3),(1,2,0,3),(3,2,0,1)):
    (frozenset({0,1,2}),frozenset({0,1,2,3}),(1,1,1,3),(1,1,1,1)),
((0,1,2,3),(1,2,3,0),(2,3,0,1)):
    (frozenset({1,2}),frozenset({0,1,2}),(2,1,1,3),(1,1,1,3)),
((0,1,2,3),(1,2,3,0),(3,0,2,1)):
    (frozenset({0,1}),frozenset({0,1,2,3}),(1,1,2,2),(1,1,1,1)),
((0,1,2,3),(1,2,3,0),(3,2,0,1)):
    (frozenset({1,2}),frozenset({0,1,2,3}),(2,1,1,2),(1,1,1,1)),
((0,1,2,3),(1,3,0,2),(2,3,0,1)):
    (frozenset({0,1}),frozenset({0,1,2,3}),(1,1,2,2),(1,1,1,1)),
((0,1,2,3),(1,3,0,2),(3,2,0,1)):
    (frozenset({0,1,3}),frozenset({0,1,2,3}),(1,1,3,1),(1,1,1,1)),
((0,1,2,3),(1,3,2,0),(2,3,0,1)):
    (frozenset({1,2}),frozenset({0,1,2,3}),(2,1,1,2),(1,1,1,1)),
}
assert set(classes)==set(expected)
for c,exp in expected.items():
    assert classes[c]==144
    assert winner_data(c)==exp

print("VERIFY_OK")
print("profiles",13824)
print("histogram",dict(hist))
print("divergence",1008,"probability","7/96")
print("relation","Dodgson proper subset of Young on every divergent profile")
print("isomorphism_classes",7,"orbit_sizes",sorted(classes.values()))
for c in sorted(expected):
    print(c,expected[c],"orbit",classes[c])
