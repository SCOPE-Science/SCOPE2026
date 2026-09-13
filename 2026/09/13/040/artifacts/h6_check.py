import itertools
from collections import defaultdict
import sympy as sp
exec(open('output/artifacts/h5_explore.py').read().split("def orbit_sum_C5")[0])

# Enumerate C6 = H^3 \otimes G^{\otimes 2}? For M simply connected, H^3(M^k)=0 so C6 domain for H^6 is A6 (as used).
# But we need H^6 twisted = A6xW / im(D). We have inv(A6xW)=4 (char level) and rank(D(invC5))=2, so quotient dim = 2.
# Verify inv(A6xW) rank is really 4 via orbit sums (not just character), and image rank 2, for k>=4.
# Build A6 index (same as h5_explore build_index_maps a6) and orbit sums.

def orbit_sum_A6W(k, rep, maps):
    # rep: (atype, avals, (p,q)) where atype in 'PA','PB','T'
    w_index,wlist,dW,s_index,slist,nS,a6_index,a6list=maps
    atype, avals, (p0,q0) = rep
    if atype in ('PA','PB'):
        S=sorted(set([avals[0],avals[1],p0,q0]))
    else:
        S=sorted(set([avals[0],avals[1],avals[2],avals[3],avals[4],p0,q0]))  # avals=(i,j,l,c1,c2,c3)? support from positions only
        S=sorted(set([avals[0],avals[1],avals[2],p0,q0]))
    acc=defaultdict(int)
    for img in itertools.permutations(range(k), len(S)):
        phi=dict(zip(S,img))
        if atype in ('PA','PB'):
            gi=a6_index.get((atype,phi[avals[0]],phi[avals[1]]),None)
            if gi is None: continue
        else:
            i,j,l=phi[avals[0]],phi[avals[1]],phi[avals[2]]
            # sort positions, permute labels accordingly
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
    reps=[]
    # PA/PB x W overlaps: support partitions of {ptpos, epos, p, q}
    # types: all equal? ptpos==epos impossible (PA requires i!=j). So relations among (i,j,p,q) with i!=j, p<q abstract.
    # enumerate abstract label tuples then quotient by iso (same canon method with ordered pairs? PA ordered (i,j)).
    allr=[]
    for at in ('PA','PB'):
        for i in range(5):
            for j in range(5):
                if i==j: continue
                for p in range(5):
                    for q in range(5):
                        if not (p<q): continue
                        allr.append((at,(i,j),(p,q)))
    # T reps: positions i<j<l abstract fixed 0,1,2 with labelings; W pairs various overlaps
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
            # positions symmetric under S3 (with labels permuted), W pair unordered swap
            i,j,l,c1,c2,c3=av
            best=None
            for perm in itertools.permutations([0,1,2]):
                pos=[i,j,l]
                lab=[c1,c2,c3]
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
print(f"num A6 orbit types: {len(reps)}")
for k in [4,5,6,7]:
    maps=build_index_maps(k)
    vecs=[orbit_sum_A6W(k,r,maps) for r in reps]
    r=len(vecs)
    G=sp.zeros(r)
    for i in range(r):
        for j in range(i,r):
            v=ddot(vecs[i],vecs[j])
            G[i,j]=v; G[j,i]=v
    rk=G.rank()
    print(f"k={k} inv(A6xW) rank={rk}")
    # images: reuse D images from h5 reps? recompute here via exec of orbit_sum_Dimage
    exec(open('output/artifacts/h5_explore.py').read().split("def orbit_sum_Dimage")[1].split("def dict_dot")[0]) if False else None
