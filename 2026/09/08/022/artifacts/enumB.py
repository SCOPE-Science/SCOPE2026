"""Enumerator B (independent): level-by-level hereditary generation.
Av(B*) is hereditary under point deletion, so every avoider of size m+1 is a
one-point extension (insert value m+1 at some site) of an avoider of size m.
Avoidance tested by NAIVE full check: all C(m,4) quadruples, order-isomorphism
via explicit standardization. No 'starts-with-1' lemma used."""
import sys, json
from itertools import combinations
PATS = {(1,3,2,4),(1,2,4,3),(1,4,3,2)}
def std4(a,b,c,d):
    s = sorted((a,b,c,d))
    r = {v:i+1 for i,v in enumerate(s)}
    return (r[a],r[b],r[c],r[d])
def avoids(p):
    for i,j,k,l in combinations(range(len(p)),4):
        if std4(p[i],p[j],p[k],p[l]) in PATS:
            return False
    return True
def invnum(p):
    c=0
    for i in range(len(p)):
        for j in range(i+1,len(p)):
            if p[i]>p[j]: c+=1
    return c
def run(n):
    cur = [()]
    dists = {}
    for m in range(1,n+1):
        nxt = []
        for pi in cur:
            L = list(pi)
            for s in range(len(L)+1):
                q = tuple(L[:s]+[m]+L[s:])
                if avoids(q):
                    nxt.append(q)
        cur = nxt
        d = {}
        for q in cur:
            k = invnum(q); d[k]=d.get(k,0)+1
        dists[m]=d
        print(f"B m={m} total={len(cur)}", flush=True)
    return dists
if __name__=="__main__":
    n=int(sys.argv[1])
    dists=run(n)
    json.dump({str(k):dists[n].get(k,0) for k in sorted(dists[n])}, open(f"biv/distB_n{n}.json","w"))
    print("wrote", f"biv/distB_n{n}.json", flush=True)
