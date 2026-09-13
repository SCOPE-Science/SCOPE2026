import itertools
from collections import defaultdict
import sympy as sp
exec(open('output/artifacts/h5_explore.py').read().split("def orbit_sum_C5")[0])
exec(open('output/artifacts/verify_d2.py').read().split("def orbit_sum_G2W")[0].split("exec(")[0])

def build_G2(k, maps):
    w_index,wlist,dW,s_index,slist,nS,a6_index,a6list=maps
    gid={}; gl=[]
    for i,a in enumerate(slist):
        for b in slist[i+1:]:
            gid[(a,b)]=len(gl); gl.append((a,b))
    return gid,gl

def orbit_sum_G2W(k, rep, maps):
    w_index,wlist,dW,s_index,slist,nS,a6_index,a6list=maps
    gid,gl=build_G2(k,maps)
    s,t,(p0,q0)=rep
    S=sorted(set([s[0],s[1],t[0],t[1],p0,q0]))
    acc=defaultdict(int)
    for img in itertools.permutations(range(k), len(S)):
        phi=dict(zip(S,img))
        a,b=phi[s[0]],phi[s[1]]
        sa=(a,b) if a<b else (b,a)
        c,d=phi[t[0]],phi[t[1]]
        ta=(c,d) if c<d else (d,c)
        if sa==ta: continue
        ia=slist.index(sa); ib=slist.index(ta)
        if ia<ib: gi=gid[(sa,ta)]; sgn=1
        else: gi=gid[(ta,sa)]; sgn=-1
        wres=wedge_image_dict(p0,q0,phi[p0],phi[q0],k)
        base=gi*dW
        for (r,ss),cc in wres.items():
            acc[base+w_index[(r,ss)]]+=sgn*cc
    return dict(acc)

def gen_G2_reps():
    allr=[]
    pairs=[(a,b) for a in range(5) for b in range(a+1,5)]
    for i,s in enumerate(pairs):
        for t in pairs[i+1:]:
            for p in range(5):
                for q in range(p+1,5):
                    allr.append((s,t,(p,q)))
    def canon(rep):
        s,t,(p,q)=rep
        best=None
        for (ss,tt) in ((s,t),(t,s)):
            (a,b)=ss; (c,d)=tt
            for (aa,bb) in ((a,b),(b,a)):
                for (cc,dd_) in ((c,d),(d,c)):
                    for (pp,qq) in ((p,q),(q,p)):
                        roles=[aa,bb,cc,dd_,pp,qq]
                        mp={};nxt=0;code=[]
                        for v in roles:
                            if v not in mp: mp[v]=nxt;nxt+=1
                            code.append(mp[v])
                        code=tuple(code)
                        if best is None or code<best: best=code
        return best
    seen={}
    for rep in allr:
        c=canon(rep)
        if c not in seen: seen[c]=rep
    return list(seen.values())

def ddot(a,b):
    if len(a)>len(b): a,b=b,a
    s=0
    for kk,v in a.items():
        w=b.get(kk,0)
        if w: s+=v*w
    return s

def arnold_cols(k, maps):
    # Arnold relators x W basis: for each triple i<j<l and each w: R_ijl \otimes w, R = G_ij G_jl + G_jl G_li + G_li G_ij (with canonical order/signs).
    w_index,wlist,dW,s_index,slist,nS,a6_index,a6list=maps
    gid,gl=build_G2(k,maps)
    cols=[]
    for i in range(k):
        for j in range(i+1,k):
            for l in range(j+1,k):
                # canonical G2 basis elements (as ordered pairs in slist order):
                pairs_ij=(min(i,j),max(i,j)),(min(j,l),max(j,l)),(min(l,i),max(l,i))
                # each term G_ab G_cd with sign to canonical gid order
                terms=[]
                cyc=[(pairs_ij[0],pairs_ij[1]),(pairs_ij[1],pairs_ij[2]),(pairs_ij[2],pairs_ij[0])]
                for (sa,ta) in cyc:
                    ia=slist.index(sa); ib=slist.index(ta)
                    if ia<ib: terms.append((gid[(sa,ta)],1))
                    elif ia>ib: terms.append((gid[(ta,sa)],-1))
                    else: pass # square zero, shouldn't happen (distinct pairs)
                for w in wlist:
                    wi=w_index[w]
                    d={}
                    for (gi,sgn) in terms:
                        d[gi*dW+wi]=d.get(gi*dW+wi,0)+sgn
                    cols.append(d)
    return cols

def D_to_G2_cols(k, maps):
    # D: C5 -> A6 only; but differential C7? For H^6, incoming D: H^3\otimes G=0. Arnold quotient affects H^6 = (A6 \oplus G^2_free/Arnold... ) hmm also cross terms H^2\otimes G^2? degree 2+6=8 >6. So only A6 and G^2 pieces. No differential into G^2 from below (would come from H^3\otimes G=0). So H^6 twisted = (A6xW)/im(D) \oplus (G^2/Arnold \otimes W)^Sk.
    return []

reps=gen_G2_reps()
for k in [4,5,6,7,8]:
    maps=build_index_maps(k)
    w_index,wlist,dW,s_index,slist,nS,a6_index,a6list=maps
    gid,gl=build_G2(k,maps)
    N2=len(gl)*dW
    vecs=[orbit_sum_G2W(k,r,maps) for r in reps]
    # invariant subspace dimension (free)
    r=len(vecs)
    G=sp.zeros(r)
    for i in range(r):
        for j in range(i,r):
            v=ddot(vecs[i],vecs[j])
            G[i,j]=v; G[j,i]=v
    rkfree=G.rank()
    # Arnold subspace: intersect with invariants. Compute dim(I \cap Arnold) via [A | I] rank formula.
    Acols=arnold_cols(k,maps)
    # rank of Arnold span
    # Build matrices on support rows
    rows=set()
    for d in Acols: rows.update(d.keys())
    for d in vecs: rows.update(d.keys())
    rows=sorted(rows)
    ridx={x:i for i,x in enumerate(rows)}
    nA=len(Acols)
    Am=sp.zeros(len(rows),nA)
    for j,d in enumerate(Acols):
        for kk,v in d.items():
            Am[ridx[kk],j]=v
    rA=Am.rank()
    # pivots of I
    piv=[]
    for i in range(r):
        test=piv+[i]
        m=len(test)
        Gm=sp.zeros(m)
        for a in range(m):
            for b in range(a,m):
                v=ddot(vecs[test[a]],vecs[test[b]])
                Gm[a,b]=v; Gm[b,a]=v
        if Gm.rank()==m:
            piv=test
    Ivecs=[vecs[i] for i in piv]
    nI=len(Ivecs)
    M=Am.row_join(sp.zeros(len(rows),nI))
    for j,d in enumerate(Ivecs):
        for kk,v in d.items():
            M[ridx[kk],nA+j]=v
    rM=M.rank()
    dimcap=rA+nI-rM
    print(f"k={k} free_inv={rkfree} rankArn={rA} dim(I cap Arn)={dimcap} => quotient G2 inv dim={rkfree-dimcap}")
