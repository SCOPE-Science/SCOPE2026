# Identify explicit invariant vectors and the D map on them via orbit-sum inner products / Reynolds, exact rational arithmetic.
# Use full-group Reynolds for small k to get invariant basis + matrix of D.
# To keep it exact and feasible, work with sparse dict vectors and compute Reynolds-projected vectors via averaging over group using orbit enumeration by support (exact), then compute Gram matrices exactly with sympy.
import itertools
from collections import defaultdict
from math import factorial, comb
import sympy as sp

def V_image_dict(pi, k):
    d=k-1
    if pi < d:
        return {pi:1}
    else:
        return {t:-1 for t in range(d)}

def wedge_image_dict(p, q, pi, qi, k):
    from collections import defaultdict
    Ap=V_image_dict(pi,k); Aq=V_image_dict(qi,k)
    res={}
    for a,ca in Ap.items():
        for b,cb in Aq.items():
            if a==b: continue
            c=ca*cb
            if a<b: key=(a,b); res[key]=res.get(key,0)+c
            else: key=(b,a); res[key]=res.get(key,0)-c
    # remove zeros
    return {kk:v for kk,v in res.items() if v!=0}

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
    # W basis
    widx={}; wl=[]
    d=k-1
    for p in range(d):
        for q in range(p+1,d):
            widx[(p,q)]=len(wl); wl.append((p,q))
    return idx,lst,widx,wl

def orbit_sum_A4W(k, rep):
    # rep: (gkey, (p,q)) abstract labels; labels assumed in 0..L-1 small ints
    Aidx,Alst,widx,wl=build_A4(k)
    dW=len(wl)
    gtype,gvals=rep[0]
    (p0,q0)=rep[1]
    if gtype=='P':
        S=sorted(set([gvals,p0,q0]))
    elif gtype in ('A','B'):
        S=sorted(set([gvals[0],gvals[1],p0,q0]))
    else:
        S=sorted(set([gvals[0],gvals[1],p0,q0]))
    acc=defaultdict(int)
    for img in itertools.permutations(range(k), len(S)):
        phi=dict(zip(S,img))
        # G image
        if gtype=='P':
            gi=Aidx[('P',phi[gvals])]
        elif gtype in ('A','B'):
            a,b=phi[gvals[0]],phi[gvals[1]]
            if a>b: a,b=b,a
            gi=Aidx[(gtype,a,b)]
        else:
            gi=Aidx[('C',phi[gvals[0]],phi[gvals[1]])]
        wres=wedge_image_dict(p0,q0,phi[p0],phi[q0],k)
        base=gi*dW
        for (r,s),c in wres.items():
            acc[base+widx[(r,s)]]+=c
    return dict(acc)

def dot(a,b):
    if len(a)>len(b): a,b=b,a
    s=0
    for kk,v in a.items():
        w=b.get(kk)
        if w: s+=v*w
    return s

def gram_rank(dicts):
    r=len(dicts)
    G=sp.zeros(r)
    for i in range(r):
        for j in range(i,r):
            v=dot(dicts[i],dicts[j])
            G[i,j]=v; G[j,i]=v
    return G.rank(), G

# Candidate reps for A4xW invariants
reps=[
    (('P',0),(0,1)),
    (('P',0),(1,2)),
    (('A',(0,1)),(0,1)),
    (('A',(0,1)),(0,2)),
    (('A',(0,1)),(2,3)),
    (('B',(0,1)),(0,1)),
    (('B',(0,1)),(0,2)),
    (('B',(0,1)),(2,3)),
    (('C',(0,1)),(0,1)),
    (('C',(0,1)),(0,2)),
    (('C',(0,1)),(1,2)),
    (('C',(0,1)),(2,3)),
]
for k in [5,6]:
    vecs=[orbit_sum_A4W(k,r) for r in reps]
    rk,G=gram_rank(vecs)
    print(f"k={k} rank={rk}")
    if k==5:
        print("Gram="); sp.pprint(G)
        # find pivot columns
        # nullspace to express dependencies
        ns=G.nullspace()
        print(f"null dim={len(ns)}")
        for v in ns:
            print(list(v))
        # which single vector spans? find nonzero diagonal
        for i,r in enumerate(reps):
            d=dot(vecs[i],vecs[i])
            print(i,r,"selfdot=",d)
