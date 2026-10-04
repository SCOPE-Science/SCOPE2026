from itertools import combinations
from math import ceil
from functools import lru_cache
def parts(n,lo=1):
    if n==0: yield (); return
    for a in range(lo,n+1):
        for q in parts(n-a,a): yield (a,)+q
def graph(P):
    lab=[]
    for i,s in enumerate(P): lab += [i]*s
    E=[(u,v) for u in range(len(lab)) for v in range(u+1,len(lab)) if lab[u]!=lab[v]]
    return lab,E
def geos(P):
    lab,E=graph(P); I={e:i for i,e in enumerate(E)}; gs=[1<<i for i in range(len(E))]
    for a,c in combinations(range(len(lab)),2):
        if lab[a]!=lab[c]: continue
        for b in range(len(lab)):
            if lab[b]==lab[a]: continue
            gs.append((1<<I[tuple(sorted((a,b)))])|(1<<I[tuple(sorted((b,c))) ]))
    return len(E),sorted(set(gs))
def opt(P,partition):
    m,gs=geos(P); full=(1<<m)-1; C=[[] for _ in range(m)]
    for g in gs:
        for e in range(m):
            if g>>e&1: C[e].append(g)
    @lru_cache(None)
    def dp(mask):
        if mask==full:return 0
        e=next(i for i in range(m) if not(mask>>i&1))
        cand=C[e] if not partition else [g for g in C[e] if not(mask&g)]
        return 1+min(dp(mask|g) for g in cand)
    return dp(0)
def formula(P):
    return sum(ceil(P[i]*P[j]/2) for i in range(len(P)) for j in range(i+1,len(P)))
checked=0
for n in range(2,7):
    for P in parts(n):
        if len(P)<2: continue
        f=formula(P); assert opt(P,False)==f==opt(P,True)
        o=sum(x%2 for x in P)
        E=sum(P[i]*P[j] for i in range(len(P)) for j in range(i+1,len(P)))
        assert f==(E+o*(o-1)//2)//2
        checked+=1
print("VERIFY_OK")
print("multipartite_types_exhaustively_checked =",checked)
print("orders = 2..6")
print("both edge-geodesic cover and partition optimized by definition")
