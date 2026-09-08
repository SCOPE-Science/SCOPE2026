"""Injection audit: f(pi) = append n+1 at END preserves inv; test avoidance + injectivity per k.
Certify for which (n,k) right-end insertion is safe."""
import json
from itertools import combinations
PATS = {(1,3,2,4),(1,2,4,3),(1,4,3,2)}
def std4(a,b,c,d):
    s=sorted((a,b,c,d)); r={v:i+1 for i,v in enumerate(s)}
    return (r[a],r[b],r[c],r[d])
def avoids(p):
    for i,j,k,l in combinations(range(len(p)),4):
        if std4(p[i],p[j],p[k],p[l]) in PATS: return False
    return True
def invnum(p):
    c=0
    for i in range(len(p)):
        for j in range(i+1,len(p)):
            if p[i]>p[j]: c+=1
    return c
def load(n):
    rows=[]
    with open(f"biv/surv_n{n}.txt") as f:
        for line in f:
            rows.append(tuple(map(int,line.strip().split(","))))
    return rows
if __name__=="__main__":
    import sys
    n=int(sys.argv[1]); kmax=int(sys.argv[2]) if len(sys.argv)>2 else 20
    rows=load(n)
    from collections import defaultdict
    byk=defaultdict(list)
    for p in rows: byk[invnum(p)].append(p)
    imgs=set(); ok=True; bad=[]
    for k in range(kmax+1):
        for p in byk.get(k,[]):
            q=p+(n+1,)
            if not avoids(q): ok=False; bad.append((k,p)); break
            if q in imgs: ok=False; bad.append((k,p)); break
            imgs.add(q)
        # injectivity within k automatic (distinct inputs -> distinct outputs), cross-k impossible (inv differs)
    print(f"n={n} right-end-append: {'SAFE all k<=%d'%kmax if not bad else 'FAILURES '+str(len(bad))}")
    for k,p in bad[:10]: print("fail k=",k,"pi=",p)
    # also verify image inv equals k and image in Av_{n+1}
    surv11=set()
    try:
        with open(f"biv/surv_n{n+1}.txt") as f:
            for line in f: surv11.add(tuple(map(int,line.strip().split(","))))
        miss=[q for q in imgs if q not in surv11]
        print("image-subset-of-Av:", len(miss)==0, "miss:", len(miss))
    except FileNotFoundError:
        print("(Av_{n+1} file not yet available; subset check deferred)")
