"""Corrected lingering-path + fixed-chip analysis for (6,1,5), l=12,m=1,N=13.
Enforces p0 in C (d0>=1). Computes fixed chip coords and hunts intersection circles."""
from itertools import product
g,r,d=6,1,5
N=13
def paths():
    out=[]
    for d0 in range(0,d+1):
        if d0<1: continue  # p0=(d0,) must be in C={y>0}
        for steps in product([-1,0,1],repeat=g):
            p=d0; ok=True
            for s in steps:
                p+=s
                if p<1: ok=False;break
            if not ok: continue
            if steps.count(-1)!=g-d+d0: continue
            out.append((d0,steps))
    return out
P=paths()
print("valid paths:",len(P))
comp=[x for x in P if x[1].count(0)==2]
print("components (2 lingers):",len(comp))
# chip coords: for each path, fixed x_i (None if linger)
def chips(d0,steps):
    p=d0; xs=[]
    for i,s in enumerate(steps):
        if s==-1: xs.append(0)
        elif s==1: xs.append((p+1)%N)  # (p_{i-1}+1)*m mod N, m=1
        else: xs.append(None)
        p+=s
    return tuple(xs)
from collections import defaultdict
byL=defaultdict(list)
for d0,s in comp:
    L=tuple(i+1 for i,v in enumerate(s) if v==0)
    byL[L].append((d0,s,chips(d0,s)))
print("linger pairs:",len(byL))
for L in sorted(byL): print(L, len(byL[L]))
# hunt intersections: pairs of paths with linger sets sharing exactly loop 3,
# fixed coords agreeing on all loops where both fixed
def agree(c1,c2):
    for a,b in zip(c1,c2):
        if a is not None and b is not None and a!=b: return False
    return True
cands=[]
Ls=sorted(byL)
for i in range(len(Ls)):
    for j in range(i+1,len(Ls)):
        if 3 not in Ls[i] or 3 not in Ls[j]: continue
        if set(Ls[i])==set(Ls[j]): continue
        for A in byL[Ls[i]]:
            for B in byL[Ls[j]]:
                if agree(A[2],B[2]):
                    # free loops: union of linger sets; shared fixed elsewhere
                    cands.append((Ls[i],A,Ls[j],B))
print("agreeing cross-pairs sharing loop3:",len(cands))
for L1,A,L2,B in cands[:20]:
    print(L1,"d0=",A[0],"steps=",A[1],"chips=",A[2])
    print(L2,"d0=",B[0],"steps=",B[1],"chips=",B[2])
    print("---")
