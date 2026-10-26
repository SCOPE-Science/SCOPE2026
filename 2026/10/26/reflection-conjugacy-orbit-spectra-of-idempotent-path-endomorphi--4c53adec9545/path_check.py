#!/usr/bin/env python3
"""Direct finite verification of strict path-graph endomorphism idempotent orbit formulas."""
from collections import Counter
from math import comb

def walk_counts(k, length):
    curr = [0]*k
    curr[0] = 1
    for _ in range(length):
        nxt = [0]*k
        for i, c in enumerate(curr):
            if i: nxt[i-1] += c
            if i+1<k: nxt[i+1] += c
        curr = nxt
    return sum(curr)

def formula(n):
    hist, fixed = {}, {}
    for k in range(2,n+1):
        d=n-k
        hist[k]=sum(walk_counts(k,a)*walk_counts(k,d-a) for a in range(d+1))
        fixed[k]=walk_counts(k,d//2) if d%2==0 else 0
    return hist,fixed

def check(n):
    hist=Counter(); fixed=Counter(); sets=set()
    def rec(path):
        if len(path)==n:
            t=tuple(path)
            if all(t[t[i]-1]==t[i] for i in range(n)):
                rank=len(set(t)); hist[rank]+=1; sets.add(t)
                refl=tuple(n+1 - t[n-1-i] for i in range(n))
                if refl==t: fixed[rank]+=1
            return
        for target in (path[-1]-1,path[-1]+1):
            if 1<=target<=n:
                rec(path+[target])
    for v in range(1,n+1):rec([v])
    h,f=formula(n)
    assert h==dict(hist), (n,'rank',h,hist)
    assert f==dict((k,fixed[k]) for k in h), (n,'fixed',f,fixed)
    visited=set(); orbit_hist=Counter()
    for t in sets:
        if t in visited: continue
        refl=tuple(n+1 - t[n-1-i] for i in range(n))
        assert refl in sets
        orb={t,refl}
        visited.update(orb)
        orbit_hist[(len(set(t)),len(orb))]+=1
    for k in h:
        assert orbit_hist[(k,1)]==f[k]
        assert orbit_hist[(k,2)]==(h[k]-f[k])//2
    return len(sets),sum(f.values()),len(visited),sum(orbit_hist.values()),sum(h.values()),hist,fixed

if __name__=='__main__':
    total=0
    for n in range(2,15):
        size, fix, vis, norbits, sums, hist,fixed=check(n)
        assert size==vis==sums
        total+=size
        print(f'n={n} total={size} reflection_fixed={fix} conjugacy_orbits={norbits} rank_counts={dict(sorted(hist.items()))}')
    for d in range(0,11):
        stable=sum(comb(a,a//2)*comb(d-a,(d-a)//2) for a in range(d+1))
        fixed_stable=comb(d//2,(d//2)//2) if d%2==0 else 0
        for n in (2*d+1,2*d+2,3*d+5):
            if n<2: continue
            k=n-d
            if k<2: continue
            h,f=formula(n)
            assert h[k]==stable,(n,d,h[k],stable)
            assert f[k]==fixed_stable,(n,d,f[k],fixed_stable)
    print(f'ALL_PATH_RETRACTION_REFLECTION_CHECKS_PASSED cases=13 total_idempotents={total} stable_deficiencies=11')
