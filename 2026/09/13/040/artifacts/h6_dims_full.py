import itertools
from collections import defaultdict
import sympy as sp
# Assemble H6 twisted dims: inv(A6xW) rank (computed 4 for k>=4) minus rank(D(inv V)) (2 for k>=4).
# Need inv(A6xW) for k=2,3 as well, and image rank for k=3 (D|_I rank 0 from stab_maps).
exec(open('output/artifacts/h6_check.py').read().split("# Enumerate")[0].split("import sympy")[0])
import sympy as sp
from collections import defaultdict
import itertools
exec(open('output/artifacts/h5_explore.py').read().split("def orbit_sum_C5")[0])

def orbit_sum_A6W(k, rep, maps):
    w_index,wlist,dW,s_index,slist,nS,a6_index,a6list=maps
    atype, avals, (p0,q0) = rep
    if atype in ('PA','PB'):
        S=sorted(set([avals[0],avals[1],p0,q0]))
    else:
        S=sorted(set([avals[0],avals[1],avals[2],p0,q0]))
    acc=defaultdict(int)
    for img in itertools.permutations(range(k), len(S)):
        phi=dict(zip(S,img))
        if atype in ('PA','PB'):
            gi=a6_index.get((atype,phi[avals[0]],phi[avals[1]]),None)
            if gi is None: continue
        else:
            i,j,l=phi[avals[0]],phi[avals[1]],phi[avals[2]]
            order=sorted([(i,avals[3]),(j,avals[4]),(l,avals[5])])
            key=('T',order[0][0],order[1][0],order[2][0],order[0][1],order[1][1],order[2][1])
            gi=a6_index.get(key,None)
            if gi is None: continue
        wres=wedge_image_dict(p0,q0,phi[p0],phi[q0],k)
        base=gi*dW
        for (r,s),c in wres.items():
            acc[base+w_index[(r,s)]]+=c
    return dict(acc)

def ddot(a,b):
    if len(a)>len(b): a,b=b,a
    s=0
    for kk,v in a.items():
        w=b.get(kk,0)
        if w: s+=v*w
    return s

def gen_A6_reps():
    allr=[]
    for at in ('PA','PB'):
        for i in range(5):
            for j in range(5):
                if i==j: continue
                for p in range(5):
                    for q in range(5):
                        if not (p<q): continue
                        allr.append((at,(i,j),(p,q)))
    for c in itertools.product((0,1),repeat=3):
        for (p,q) in [(0,1),(0,2),(0,3),(1,2),(2,3),(3,4)]:
            allr.append(('T',(0,1,2,c[0],c[1],c[2]),(p,q)))
    def canon_T(rep):
        at,av,(p,q)=rep
        if at in ('PA','PB'):
            i,j=av
            best=None
            for (pp,qq) in ((p,q),(q,p)):
                roles=[i,j,pp,qq]
                mp={};nxt=0;code=[]
                for v in roles:
                    if v not in mp: mp[v]=nxt;nxt+=1
                    code.append(mp[v])
                code=tuple(code)
                if best is None or code<best: best=code
            return (at,best)
        else:
            i,j,l,c1,c2,c3=av
            best=None
            for perm in itertools.permutations([0,1,2]):
                pos=[i,j,l]; lab=[c1,c2,c3]
                pi=[pos[perm[t]] for t in range(3)]
                la=[lab[perm[t]] for t in range(3)]
                for (pp,qq) in ((p,q),(q,p)):
                    roles=pi+[pp,qq]
                    mp={};nxt=0;code=[]
                    for v in roles:
                        if v not in mp: mp[v]=nxt;nxt+=1
                        code.append(mp[v])
                    key=(tuple(code),tuple(la))
                    if best is None or key<best: best=key
            return ('T',best)
    seen={}
    for rep in allr:
        c=canon_T(rep)
        if c not in seen: seen[c]=rep
    return list(seen.values())

reps=gen_A6_reps()
# image ranks from quotient runs: k=3: 0; k>=4: 2 (rank(D|_I)).
imgrank={3:0,4:2,5:2,6:2}
for k in [2,3,4,5,6]:
    maps=build_index_maps(k)
    vecs=[orbit_sum_A6W(k,r,maps) for r in reps]
    r=len(vecs)
    G=sp.zeros(r)
    for i in range(r):
        for j in range(i,r):
            v=ddot(vecs[i],vecs[j])
            G[i,j]=v; G[j,i]=v
    rk=G.rank()
    print(f"k={k} inv(A6xW)={rk} imgrank={imgrank.get(k,'?')} => dimH6={rk-imgrank.get(k,0) if k in imgrank else '?'}")
