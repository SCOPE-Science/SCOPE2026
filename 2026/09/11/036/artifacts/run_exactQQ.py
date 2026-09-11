"""Exact-QQ full Betti table for H1 via Fraction ranks (n=9, 512 subsets)."""
import sys, json
sys.path.insert(0, "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-745/output/artifacts")
from engine import *
from fractions import Fraction
H = [(0,2,5),(0,2,6),(1,2,7),(1,3,4),(1,4,5),(1,5,8),(2,3,4),(2,5,7),
     (3,6,7),(3,6,8),(4,6,8),(4,7,8),(5,6,8),(6,7,8)]
n=9; E=edges_of(H); face=face_array(E,n)
def rank_qq(A):
    if A is None or A.size==0: return 0
    M=[[Fraction(int(x)) for x in row] for row in A.tolist()]
    r=len(M); c=len(M[0]) if r else 0; rk=0
    for j in range(c):
        piv=-1
        for i in range(rk,r):
            if M[i][j]!=0: piv=i; break
        if piv<0: continue
        M[rk],M[piv]=M[piv],M[rk]
        pv=M[rk][j]
        for i in range(r):
            if i!=rk and M[i][j]!=0:
                f=M[i][j]/pv
                for k in range(j,c): M[i][k]-=f*M[rk][k]
        rk+=1
    return rk
tab={}; N=1<<n; top_h=0; topW=[]
for W in range(1,N):
    m=popcount(W)
    by=faces_by_dim(W,face,n)
    if not by: continue
    top=max(by)
    rks={}
    for d in range(1,top+2):
        rks[d]=rank_qq(boundary_matrix(by,d))
    for h in range(1,top+1):
        nd=len(by.get(h,[]))
        hd=nd-rks.get(h,0)-rks.get(h+1,0)
        if hd:
            if h>top_h: top_h=h; topW=[(W,h,hd)]
            elif h==top_h: topW.append((W,h,hd))
            i=m-h-1; j=h+1
            if i>=0: tab[(i,j)]=tab.get((i,j),0)+hd
print("exact-QQ reg(S/I) =", top_h+1)
print("attaining (W,h,dim):", [(bin(w),h,d) for (w,h,d) in topW if h==top_h][:10])
print("--- exact-QQ Betti table ---")
for k in sorted(tab): print(f"beta_{k[0]},{k[1]} = {tab[k]}")
json.dump({"regQ_exact": top_h+1, "bettiQ_exact": {f"{k}":v for k,v in tab.items()},
           "attaining": topW}, open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-745/output/artifacts/H1_exactQQ.json","w"), indent=1)
print("wrote H1_exactQQ.json")
