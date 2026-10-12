#!/usr/bin/env python3
from collections import Counter

M1 = [
[0,2,2,2,2,2,2,4],
[0,-1,-1,-1,0,0,0,-1],
[0,-1,0,0,-1,-1,0,-1],
[0,0,-1,0,-1,0,-1,-1],
[0,-1,0,0,-1,-1,0,-1],
[0,-1,-1,-1,0,0,0,-1],
[0,0,-1,0,-1,0,-1,-1],
[0,0,0,-1,0,-1,-1,-1],
[0,0,0,-1,0,-1,-1,-1],
[1,-1,-1,-1,-1,-1,-1,-3],
]
M2 = [
[1,1,1,1,3,3,3,3],
[-1,0,0,0,-1,-1,-1,0],
[0,-1,0,0,-1,-1,0,-1],
[0,0,-1,0,-1,0,-1,-1],
[0,-1,0,0,-1,-1,0,-1],
[-1,0,0,0,-1,-1,-1,0],
[0,0,-1,0,-1,0,-1,-1],
[0,0,0,-1,0,-1,-1,-1],
[0,0,0,-1,0,-1,-1,-1],
[0,0,0,0,-2,-2,-2,-2],
]
REPS=[tuple(row[j] for row in M1) for j in range(8)] + [tuple(row[j] for row in M2) for j in range(8)]

g1=(9,7,8,3,1,2,6,4,5)  # (195)(276)(384)
g2=(8,9,7,2,3,1,5,6,4)  # (186)(294)(375)
ID=tuple(range(1,10))
def compose(p,q):
    return tuple(p[q[i]-1] for i in range(9))
G={ID}
changed=True
while changed:
    changed=False
    for p in list(G):
        for g in (g1,g2):
            h=compose(g,p)
            if h not in G:
                G.add(h); changed=True
assert len(G)==9

def act(v,p):
    out=[0]*9
    for i,val in enumerate(v[1:],1):
        out[p[i-1]-1]=val
    return (v[0],*out)

curves=[]
for r in REPS:
    orb={act(r,p) for p in G}
    assert len(orb)==9
    curves.extend(orb)
curves=list(set(curves))
assert len(curves)==144
assert Counter(c[0] for c in curves)==Counter({2:54,1:36,3:36,0:9,4:9})

def ip(a,b):
    return a[0]*b[0]-sum(x*y for x,y in zip(a[1:],b[1:]))

assert {ip(c,c) for c in curves}=={-1}
cnt=Counter()
for i,a in enumerate(curves):
    for b in curves[i+1:]:
        cnt[ip(a,b)]+=1
assert cnt==Counter({0:2232,1:4320,2:2880,3:792,4:72})
assert sum(cnt.values())==144*143//2

cubics=[c for c in curves if c[0]==3]
quartics=[c for c in curves if c[0]==4]
def cubic_data(c):
    dbl=[i for i,x in enumerate(c[1:],1) if x==-2]
    omit=[i for i,x in enumerate(c[1:],1) if x==0]
    assert len(dbl)==1 and len(omit)==2
    return dbl[0],set(omit)
def quartic_triple(q):
    s=[i for i,x in enumerate(q[1:],1) if x==-3]
    assert len(s)==1
    return s[0]
for c in cubics:
    _,omit=cubic_data(c)
    partners=[q for q in quartics if ip(c,q)==4]
    assert len(partners)==2
    assert {quartic_triple(q) for q in partners}==omit
for q in quartics:
    assert sum(ip(c,q)==4 for c in cubics)==8

print("VERIFY_OK curves=144 pairs=10296 counts=0:2232,1:4320,2:2880,3:792,4:72 max=4 cubic_partners=2 quartic_partners=8")
