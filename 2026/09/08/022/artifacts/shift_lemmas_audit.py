"""Audit the two PROVED safe shift-maps on full enumerated sets:
 g1(pi) = (n+1) ++ pi            (prepend max; inv += n; SAFE by Lemma 1)
 g2(pi) = shift(pi,+1) ... check: append-min: q = (x+1 for x in pi) ++ (1,); inv += n; SAFE by Lemma 2?
 Lemma 2: new global min at LAST position; occurrence using last pos would need last value = pattern's
 last entry in {4,3,2}, but min value 1 is never the max-ish... precisely: pattern last values are 4,3,2
 (ranks among the 4); the last element being the global min has rank 1 among the 4. 4,3,2 != 1. Contradiction. SAFE.
 Verify avoidance + inv shift + injectivity on n=8,9,10 full sets."""
from itertools import combinations
PATS={(1,3,2,4),(1,2,4,3),(1,4,3,2)}
def std4(a,b,c,d):
    s=sorted((a,b,c,d)); r={v:i+1 for i,v in enumerate(s)}
    return (r[a],r[b],r[c],r[d])
def avoids(p):
    for i,j,k,l in combinations(range(len(p)),4):
        if std4(p[i],p[j],p[k],p[l]) in PATS: return False
    return True
def invnum(p):
    c=0
    L=len(p)
    for i in range(L):
        pi=p[i]
        for j in range(i+1,L):
            if pi>p[j]: c+=1
    return c
def load(n):
    rows=[]
    with open(f"biv/surv_n{n}.txt") as f:
        for line in f: rows.append(tuple(map(int,line.strip().split(","))))
    return rows
for n in [8,9,10]:
    rows=load(n); nxt=set(load(n+1))
    for name,g in [("prepend-max",lambda p:(n+1,)+p),
                   ("append-min",lambda p:tuple(x+1 for x in p)+(1,))]:
        seen=set(); ok=True
        for p in rows:
            q=g(p)
            if invnum(q)!=invnum(p)+n: ok=False; print(name,"INVSHIFT-FAIL",n,p,invnum(p),invnum(q)); break
            if q in seen: ok=False; print(name,"INJ-FAIL",n); break
            seen.add(q)
            if not avoids(q): ok=False; print(name,"AVOID-FAIL",n,p); break
            if q not in nxt: ok=False; print(name,"SUBSET-FAIL",n,p); break
        print(f"{name} n={n}->{n+1}: {'PASS' if ok else 'FAIL'} images={len(seen)}")
