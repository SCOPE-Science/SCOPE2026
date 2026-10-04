from itertools import product
from collections import defaultdict
from math import comb

def partitions(n, lo=1):
    if n==0:
        yield ()
        return
    for a in range(lo,n+1):
        for r in partitions(n-a,a):
            yield (a,)+r

def vertices(profile):
    return [(i,j) for i,n in enumerate(profile) for j in range(n)]

def direct(profile, vals):
    verts=vertices(profile)
    part=[i for i,j in verts]
    for idx,(i,j) in enumerate(verts):
        s=vals[idx]
        for k,(h,t) in enumerate(verts):
            if h!=i:
                s += vals[k]
        if s<1:return False
    return True

def criterion(profile, vals):
    offs=[]; p=0
    W=sum(vals)
    for n in profile:
        block=vals[p:p+n]; p+=n
        s=sum(block); m=min(block)
        if W-s+m<1:return False
    return True

def local_poly(n,w):
    d=defaultdict(int)
    for vals in product((-1,0,1), repeat=n):
        s=sum(vals); m=min(vals)
        if WTEST(w,s,m): d[s]+=1
    return dict(d)

def WTEST(w,s,m): return w-s+m>=1

def predicted(profile):
    N=sum(profile); out={}
    for w in range(1,N+1):
        cur={0:1}
        for n in profile:
            p=local_poly(n,w)
            nxt=defaultdict(int)
            for a,ca in cur.items():
                for b,cb in p.items(): nxt[a+b]+=ca*cb
            cur=dict(nxt)
        if cur.get(w,0): out[w]=cur[w]
    return out

profiles=labelings=valid=coeff=gamma=0
for N in range(2,10):
    for prof in partitions(N):
        if len(prof)<2: continue
        profiles+=1
        obs=defaultdict(int)
        for vals in product((-1,0,1), repeat=N):
            labelings+=1
            d=direct(prof, vals); c=criterion(prof, vals)
            if d!=c: raise AssertionError((prof,vals,d,c))
            if d:
                valid+=1; obs[sum(vals)]+=1
        pred=predicted(prof)
        for w in range(1,N+1):
            coeff+=1
            if obs.get(w,0)!=pred.get(w,0): raise AssertionError((prof,w,obs.get(w,0),pred.get(w,0)))
        g=min(obs)
        expected=1 if 1 in prof else 2
        gamma+=1
        if g!=expected: raise AssertionError((prof,g,expected))
print(f'VERIFY_OK profiles={profiles} labelings={labelings} valid_functions={valid} coefficient_checks={coeff} gamma_checks={gamma} max_order=9')
