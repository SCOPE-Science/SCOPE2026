# Verify d^2=0 and d(relations) in ideal at cochain level for k=3 (small, exact), plus D(R)=0 in A6 (already checked for k>=4).
# Use Kriz model: d(G_ij)=D_ij in H^4; d(x)=0. Relations: R1: G_ij=G_ji, G_ij^2=0 (degree reasons? |G|=3 so G^2 has degree 6; not automatically 0 in free tensor? Actually G_ij^2 may be nonzero a priori; Kriz relation says square zero), R2: (x_i-x_j)G_ij=0, R3: G_ij G_jl + G_jl G_li + G_li G_ij =0 (Arnold).
# Check d(R2)=(x_i-x_j)D_ij = 0 in H^6 (done: D(R)=0). Check d(R3)= D_ij G_jl + ... : lands in H^4 \otimes G + ...? Must vanish mod R2? Verify numerically that d(R3) is in span of R2-type elements within C7 = H^4 \otimes G^{\otimes 2}? For degree-5-relevant? Actually Arnold relation is degree 6 (G^2 terms); its differential is degree 9: D_ij G_... + cyclic. For H^5/H^6 computation we only need C5,C6 = H^2\otimes G, A6 (no G^2). Arnold doesn't affect H^5/H^6? Arnold relation involves G^2 (two G factors) with H^0 coefficients: total degree 6. Its span intersected with A6 (zero G factors)? No. So Arnold irrelevant for H^6 quotient? H^6 classes with G factors: H^0\otimes G^2 (degree 6) exist! Wait H^6(F_k) has contributions: H^6(M^k) [A6], H^3\otimes G (0), H^0\otimes G^2 (sym^2 G / Arnold). We omitted the G^2 piece!
# Compute its twisted invariants: inv(Sym^2(G)/Arnold \otimes W). Character of Sym^2(G)? Need full computation. Let's compute orbit sums for G^2 x W and Arnold quotient.
import itertools
from collections import defaultdict
import sympy as sp

exec(open('output/artifacts/h5_explore.py').read().split("def orbit_sum_C5")[0])

def gen_G2_reps():
    # G^2 monomials: ordered pairs (s,t) of 2-subsets, modulo s,t swap (graded commutative, |G| odd => antisymmetric? |G|=3 odd, so G_ij G_lm = -G_lm G_ij; squares zero). Basis: s<t (in sorted order) with disjoint-or-not supports, excluding s==t.
    # Orbit types classified by overlap pattern of 4 positions + W pair overlap. Enumerate abstractly.
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
        # symmetries: swap within s? (s is a set, already unordered), swap within t, swap s<->t (with sign, but support same), swap p,q
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

reps=gen_G2_reps()
print(f"num G2xW orbit types: {len(reps)}")

def orbit_sum_G2W(k, rep, maps):
    w_index,wlist,dW,s_index,slist,nS,a6_index,a6list=maps
    # index G2 basis: ordered s<t pairs -> gid; N2 = C(nS,2)
    s,t,(p0,q0)=rep
    # canonicalize sign? rep has s<t in enumeration order; image may have s'>t'; antisymmetry: G_s'G_t' = sign * G_sorted. Track sign.
    # Build gid map
    gid={}
    gl=[]
    for i,a in enumerate(slist):
        for b in slist[i+1:]:
            gid[(a,b)]=len(gl); gl.append((a,b))
    n2=len(gl)
    S=sorted(set([s[0],s[1],t[0],t[1],p0,q0]))
    acc=defaultdict(int)
    for img in itertools.permutations(range(k), len(S)):
        phi=dict(zip(S,img))
        a,b=phi[s[0]],phi[s[1]]
        sa=(a,b) if a<b else (b,a)
        c,d=phi[t[0]],phi[t[1]]
        ta=(c,d) if c<d else (d,c)
        if sa==ta: continue  # square zero
        # order
        ia=slist.index(sa); ib=slist.index(ta)
        if ia<ib: gi=gid[(sa,ta)]; sgn=1
        else: gi=gid[(ta,sa)]; sgn=-1
        wres=wedge_image_dict(p0,q0,phi[p0],phi[q0],k)
        base=gi*dW
        for (r,ss),cc in wres.items():
            acc[base+w_index[(r,ss)]]+=sgn*cc
    return dict(acc), n2*dW

def ddot(a,b):
    if len(a)>len(b): a,b=b,a
    s=0
    for kk,v in a.items():
        w=b.get(kk,0)
        if w: s+=v*w
    return s

for k in [4,5,6]:
    maps=build_index_maps(k)
    vecs=[orbit_sum_G2W(k,r,maps)[0] for r in reps]
    r=len(vecs)
    G=sp.zeros(r)
    for i in range(r):
        for j in range(i,r):
            v=ddot(vecs[i],vecs[j])
            G[i,j]=v; G[j,i]=v
    print(f"k={k} inv(G^2_free x W) rank={G.rank()}")
