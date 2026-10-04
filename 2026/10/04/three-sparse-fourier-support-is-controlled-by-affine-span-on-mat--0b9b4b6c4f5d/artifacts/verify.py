#!/usr/bin/env python3
from itertools import combinations

# Gaussian integers as (real, imag).
U = [(1,0),(0,1),(-1,0),(0,-1)]

def gadd(a,b): return (a[0]+b[0], a[1]+b[1])
def gsub(a,b): return (a[0]-b[0], a[1]-b[1])
def gmul(a,b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def gscale(n,a): return (n*a[0], n*a[1])
def gzero(a): return a==(0,0)

def det2(r,s,i,j):
    return gsub(gmul(r[i],s[j]), gmul(r[j],s[i]))

def cross(r,s):
    return (
        det2(r,s,1,2),
        gsub(gmul(r[2],s[0]), gmul(r[0],s[2])),
        det2(r,s,0,1),
    )

def dot(r,c):
    z=(0,0)
    for a,b in zip(r,c): z=gadd(z,gmul(a,b))
    return z

def proportional(r,s):
    # all entries are nonzero; compare 2x2 minors
    return gzero(det2(r,s,0,1)) and gzero(det2(r,s,0,2)) and gzero(det2(r,s,1,2))

def point(n): return (n%4,n//4)
def enc(p): return p[0]+4*p[1]
def addp(a,b): return ((a[0]+b[0])%4,(a[1]+b[1])%4)
def subp(a,b): return ((a[0]-b[0])%4,(a[1]-b[1])%4)

def orderp(a):
    x=(0,0)
    for m in range(1,5):
        x=addp(x,a)
        if x==(0,0): return m
    raise AssertionError

def generated(ds):
    H={(0,0)}
    changed=True
    while changed:
        changed=False
        for h in list(H):
            for d in ds:
                z=addp(h,d)
                if z not in H:
                    H.add(z); changed=True
    return H

def htype(S):
    pts=[point(x) for x in S]
    base=pts[0]
    H=generated([subp(p,base) for p in pts[1:]])
    if len(H)==4:
        return 'C4' if any(orderp(h)==4 for h in H) else 'C2xC2'
    if len(H)==8: return 'C4xC2'
    if len(H)==16: return 'C4xC4'
    raise AssertionError((S,len(H)))

def chi(k,x):
    a,b=point(k); c,d=point(x)
    return U[(a*c+b*d)%4]

def rows_for(S):
    return [tuple(chi(k,x) for x in S) for k in range(16)]

def zero_count(rows,c):
    return sum(gzero(dot(r,c)) for r in rows)

def find_generic_no_zero(rows):
    for t in range(1,201):
        c=((1,0),(t,0),(t*t,0))
        if all(not gzero(dot(r,c)) for r in rows): return c
    raise AssertionError('generic witness not found')

def find_single_class_witness(rows,rep):
    # ker(rep): c = (rep1 + t rep2, -rep0, -t rep0)
    for t in range(1,65):
        c=(gadd(rep[1],gscale(t,rep[2])), gscale(-1,rep[0]), gscale(-t,rep[0]))
        if any(gzero(x) for x in c): continue
        zeros=[i for i,r in enumerate(rows) if gzero(dot(r,c))]
        if zeros and all(proportional(rows[i],rep) for i in zeros):
            return c, len(zeros)
    raise AssertionError('single-class witness not found')

def attainable_sizes(S):
    rows=rows_for(S)
    sizes={16}
    find_generic_no_zero(rows)
    reps=[]
    for r in rows:
        if not any(proportional(r,q) for q in reps): reps.append(r)
    # Rank-one zero sets (one projective row class).
    for r in reps:
        c,z=find_single_class_witness(rows,r)
        assert all(not gzero(x) for x in c)
        sizes.add(16-z)
    # Rank-two zero constraints determine a one-dimensional kernel.
    for r,s in combinations(reps,2):
        if proportional(r,s): continue
        c=cross(r,s)
        if any(gzero(x) for x in c): continue
        z=zero_count(rows,c)
        assert z>=2
        sizes.add(16-z)
    return sizes

pred={
    'C4': {8,12,16},
    'C2xC2': {12,16},
    'C4xC2': {12,14,16},
    'C4xC4': {14,15,16},
}
counts={k:0 for k in pred}
incidence={m:0 for m in [8,12,14,15,16]}
for S in combinations(range(16),3):
    typ=htype(S)
    got=attainable_sizes(S)
    if got != pred[typ]:
        raise AssertionError((S,typ,got,pred[typ]))
    counts[typ]+=1
    for m in got: incidence[m]+=1

assert counts == {'C4':96,'C2xC2':16,'C4xC2':192,'C4xC4':256}, counts
assert incidence == {8:96,12:304,14:448,15:256,16:560}, incidence
print('VERIFY_OK')
print('support_type_counts', counts)
print('support_incidence_by_fourier_size', incidence)
print('global_sizes', sorted(incidence))
