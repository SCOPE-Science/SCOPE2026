import itertools
from collections import defaultdict
import sympy as sp
exec(open('output/artifacts/h5_explore.py').read().split("def gen_reps")[0])

def ddot(a,b):
    if len(a)>len(b): a,b=b,a
    s=0
    for kk,v in a.items():
        w=b.get(kk,0)
        if w: s+=v*w
    return s

def gram_rank(dicts):
    r=len(dicts)
    G=sp.zeros(r)
    for i in range(r):
        for j in range(i,r):
            v=ddot(dicts[i],dicts[j])
            G[i,j]=v; G[j,i]=v
    return G.rank(), G

# ---- H4: A4xW orbit sums (support<=3) at k=10,11 ----
def build_A4(k):
    idx={}; lst=[]
    for i in range(k):
        idx[('P',i)]=len(lst); lst.append(('P',i))
    for i in range(k):
        for j in range(i+1,k):
            idx[('A',i,j)]=len(lst); lst.append(('A',i,j))
    for i in range(k):
        for j in range(i+1,k):
            idx[('B',i,j)]=len(lst); lst.append(('B',i,j))
    for i in range(k):
        for j in range(k):
            if i==j: continue
            idx[('C',i,j)]=len(lst); lst.append(('C',i,j))
    widx={}; wl=[]
    d=k-1
    for p in range(d):
        for q in range(p+1,d):
            widx[(p,q)]=len(wl); wl.append((p,q))
    return idx,lst,widx,wl

def orbit_sum_A4W(k, rep, cache):
    Aidx,Alst,widx,wl=cache
    dW=len(wl)
    (gtype,gvals),(p0,q0)=rep
    if gtype=='P': S=sorted(set([gvals,p0,q0]))
    else: S=sorted(set([gvals[0],gvals[1],p0,q0]))
    acc=defaultdict(int)
    for img in itertools.permutations(range(k), len(S)):
        phi=dict(zip(S,img))
        if gtype=='P': gi=Aidx[('P',phi[gvals])]
        elif gtype in ('A','B'):
            a,b=phi[gvals[0]],phi[gvals[1]]
            if a>b: a,b=b,a
            gi=Aidx[(gtype,a,b)]
        else: gi=Aidx[('C',phi[gvals[0]],phi[gvals[1]])]
        wres=wedge_image_dict(p0,q0,phi[p0],phi[q0],k)
        base=gi*dW
        for (r,s),c in wres.items():
            kk=widx.get((r,s))
            if kk is not None: acc[base+kk]+=c
    return dict(acc)

reps4=[(('P',0),(0,1)),(('P',0),(1,2)),
 (('A',(0,1)),(0,1)),(('A',(0,1)),(0,2)),(('A',(0,1)),(2,3)),
 (('B',(0,1)),(0,1)),(('B',(0,1)),(0,2)),(('B',(0,1)),(2,3)),
 (('C',(0,1)),(0,1)),(('C',(0,1)),(0,2)),(('C',(0,1)),(1,2)),(('C',(0,1)),(2,3))]
# G3 reps for H3 check
def orbit_sum_G3W(k, rep, cache):
    Aidx,Alst,widx,wl=cache
    # G3 index
    gidx={}; gl=[]
    for i in range(k):
        for j in range(i+1,k):
            gidx[(i,j)]=len(gl); gl.append((i,j))
    dW=len(wl)
    (i0,j0),(p0,q0)=rep
    S=sorted(set([i0,j0,p0,q0]))
    acc=defaultdict(int)
    for img in itertools.permutations(range(k), len(S)):
        phi=dict(zip(S,img))
        a,b=phi[i0],phi[j0]
        if a>b: a,b=b,a
        gi=gidx[(a,b)]
        wres=wedge_image_dict(p0,q0,phi[p0],phi[q0],k)
        base=gi*dW
        for (r,s),c in wres.items():
            kk=widx.get((r,s))
            if kk is not None: acc[base+kk]+=c
    return dict(acc)
reps3=[((0,1),(0,1)),((0,1),(0,2)),((0,1),(2,3))]

for k in [10,11]:
    cache=build_A4(k)
    v4=[orbit_sum_A4W(k,r,cache) for r in reps4]
    rk4,_=gram_rank(v4)
    v3=[orbit_sum_G3W(k,r,cache) for r in reps3]
    rk3,_=gram_rank(v3)
    print(f"k={k} inv(H4xW)={rk4} (expect 1) inv(GxW)={rk3} (expect 0) => dimH4tw={rk4-rk3}", flush=True)
