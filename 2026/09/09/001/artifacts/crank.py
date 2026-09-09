"""Crank/witness audit, full encoding.
Overpartition = tuple over distinct values (desc) of (value, multiplicity, bit).
phi1 flips bit of largest value; psi flips all bits. Commuting f.p.f. involutions."""
from itertools import product as iproduct
from collections import Counter

def gen_partitions(n):
    out=[]
    def gen(rem, maxv, cur):
        if rem==0:
            out.append(tuple(cur)); return
        for v in range(min(maxv,rem),0,-1):
            if v%3==0: continue
            cur.append(v); gen(rem-v, v, cur); cur.pop()
    gen(n,n,[])
    return out

def overparts(n):
    res=[]
    for P in gen_partitions(n):
        vals=sorted(set(P),reverse=True)
        for mask in iproduct([0,1],repeat=len(vals)):
            cnt=Counter(P)
            res.append(tuple((v,cnt[v],b) for v,b in zip(vals,mask)))
    return res

def phi1(x): return tuple((v,c,1-b) if j==0 else (v,c,b) for j,(v,c,b) in enumerate(x))
def psi(x):  return tuple((v,c,1-b) for (v,c,b) in x)

def audit(m):
    OP=overparts(m)
    S=len(OP)
    assert len(set(OP))==S
    assert all(phi1(x)!=x for x in OP)
    assert all(psi(x)!=x for x in OP)
    assert all(phi1(psi(x))==psi(phi1(x)) for x in OP)
    assert all(phi1(phi1(x))==x and psi(psi(x))==x for x in OP)
    rect=[x for x in OP if len(x)==1]
    nonrect=[x for x in OP if len(x)>1]
    seen=set()
    for x in nonrect:
        if x in seen: continue
        orb={x,phi1(x),psi(x),phi1(psi(x))}
        assert len(orb)==4,(m,x)
        seen|=orb
    assert len(seen)==len(nonrect)
    A=sum(1 for x in OP if x[0][2]==0)
    return {"S":S,"rect":len(rect),"A":A,"B":S-A}

for m in [1,3,5,7,9,11,13,15,17,19,21,23,25]:
    r=audit(m)
    print("m=%d S=%d rect=%d phi1-classes=(%d,%d) Smod4=%d"%(
        m,r["S"],r["rect"],r["A"],r["B"],r["S"]%4))
print("WITNESS AUDIT OK")
