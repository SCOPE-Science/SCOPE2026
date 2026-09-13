import itertools
import numpy as np
from collections import defaultdict

# Cohomology ring of M=CP2#CP2: basis {1,a,b,pt}, a^2=b^2=pt, ab=0, apt=bpt=pt^2=0
# Represent monomial in A^{\otimes k} as tuple of factors per position: 0=1,1=a,2=b,3=pt
# Multiply by single factor at position j: helper

def build_index_maps(k):
    d=k-1
    # W basis index
    w_index={}
    wlist=[]
    for p in range(d):
        for q in range(p+1,d):
            w_index[(p,q)]=len(wlist); wlist.append((p,q))
    dW=len(wlist)
    # s basis index (l<m)
    s_index={}
    slist=[]
    for l in range(k):
        for m in range(l+1,k):
            s_index[(l,m)]=len(slist); slist.append((l,m))
    nS=len(slist)
    # A2 basis: (type,j): type 0=a,1=b
    # A6 basis: enumerate
    a6_index={}
    a6list=[]
    # type pt_i a_j, pt_i b_j (i!=j)
    for i in range(k):
        for j in range(k):
            if i==j: continue
            a6_index[('PA',i,j)]=len(a6list); a6list.append(('PA',i,j))
            a6_index[('PB',i,j)]=len(a6list); a6list.append(('PB',i,j))
    # triple 2's: positions i<j<l with choices c1,c2,c3 in {a,b}
    for i in range(k):
        for j in range(i+1,k):
            for l in range(j+1,k):
                for c1 in (0,1):
                    for c2 in (0,1):
                        for c3 in (0,1):
                            a6_index[('T',i,j,l,c1,c2,c3)]=len(a6list); a6list.append(('T',i,j,l,c1,c2,c3))
    return w_index,wlist,dW,s_index,slist,nS,a6_index,a6list

def V_image_dict(p_img, k):
    d=k-1
    if p_img < d:
        return {p_img:1}
    else:
        return {t:-1 for t in range(d)}

def wedge_image_dict(p, q, pi, qi, k):
    Ap=V_image_dict(pi,k); Aq=V_image_dict(qi,k)
    res={}
    for a,ca in Ap.items():
        for b,cb in Aq.items():
            if a==b: continue
            c=ca*cb
            if a<b: key=(a,b); res[key]=res.get(key,0)+c
            else: key=(b,a); res[key]=res.get(key,0)-c
    return res

def orbit_sum_C5(k, rep, maps):
    # rep: (etype, j0, (l0,m0), (p0,q0)) with labels in small set; support S sorted unique
    w_index,wlist,dW,s_index,slist,nS,a6_index,a6list=maps
    etype,j0,(l0,m0),(p0,q0)=rep
    S=sorted(set([j0,l0,m0,p0,q0]))
    t=len(S)
    # domain index: ((etype,j), (l,m), (p,q)) -> idx = ((etype*k+j)*nS + s)*dW + w
    # Use dict sparse accumulation then convert? For Gram we need full vectors; use dict per orbit sum then inner products via dicts (avoid dense huge)
    # Return dict {flat_idx: coeff}
    acc=defaultdict(int)
    Spos={v:n for n,v in enumerate(S)}
    # precompute w basis shift: need V_image expansions
    for img in itertools.permutations(range(k), t):
        phi=dict(zip(S,img))
        j=phi[j0]
        l,m=phi[l0],phi[m0]
        a,b=(l,m) if l<m else (m,l)
        si=s_index[(a,b)]
        pi,qi=phi[p0],phi[q0]
        wres=wedge_image_dict(p0,q0,pi,qi,k)
        base=((etype*k+j)*nS+si)*dW
        for (r,s),c in wres.items():
            wi=w_index[(r,s)]
            acc[base+wi]+=c
    return dict(acc)

def D_image_of_domain_basis(k, etype, j, l, m, wcoeffs, maps):
    # wcoeffs: dict {(r,s):c} expansion of W part (already in basis)
    # returns dict {target_flat: coeff} where target = A6 \otimes W
    w_index,wlist,dW,s_index,slist,nS,a6_index,a6list=maps
    nA6=len(a6list)
    out=defaultdict(int)
    # D(s_lm) = pt_l + pt_m + a_l a_m + b_l b_m
    # Multiply by e_j (a_j if etype=0 else b_j)
    # Four terms:
    # Term1: e_j * pt_l ; Term2: e_j*pt_m ; Term3: e_j*a_l a_m ; Term4: e_j*b_l b_m
    # Represent A6 basis element + coeff (+1)
    def add_A6(a6key, wdict):
        ai=a6_index.get(a6key, None)
        if ai is None: return
        base=ai*dW
        for (r,s),c in wdict.items():
            wi=w_index[(r,s)]
            out[base+wi]+=c
    # Precompute: factor values per position for each term is easier via per-position multiply rules.
    # Instead directly determine A6 key:
    # Terms 1-2: pt_l * e_j:
    for (ptpos, epos) in ((l,j),(m,j)):
        if ptpos==epos:
            # a*pt=0 at same position -> vanishes
            continue
        else:
            key=('PA' if etype==0 else 'PB', ptpos, epos)
            add_A6(key, wcoeffs)
    # Term3: a_l a_m * e_j
    # positions involved: l,m,j with factors a at l,m and e at j
    # if j==l: factor at l is e*a = a^2=pt (if e=a) or b*a=0 (if e=b); similarly j==m
    # if j distinct: triple (a,a,e)
    if etype==0: # e=a
        if j==l:
            # pt_l * a_m -> PA(l,m)
            add_A6(('PA',l,m), wcoeffs)
        elif j==m:
            add_A6(('PA',m,l), wcoeffs)
        else:
            i1,i2,i3=sorted([j,l,m])
            # need c's: all a
            # map positions to c: pos->0 for a
            dmap={j:0,l:0,m:0}
            key=('T',i1,i2,i3,dmap[i1],dmap[i2],dmap[i3])
            add_A6(key, wcoeffs)
    else: # e=b
        # b_j * a_l a_m
        if j==l or j==m:
            # b*a=0 at same position -> vanishes
            pass
        else:
            i1,i2,i3=sorted([j,l,m])
            dmap={j:1,l:0,m:0}
            key=('T',i1,i2,i3,dmap[i1],dmap[i2],dmap[i3])
            add_A6(key, wcoeffs)
    # Term4: b_l b_m * e_j
    if etype==1: # e=b
        if j==l:
            add_A6(('PB',l,m), wcoeffs)
        elif j==m:
            add_A6(('PB',m,l), wcoeffs)
        else:
            i1,i2,i3=sorted([j,l,m])
            dmap={j:1,l:1,m:1}
            key=('T',i1,i2,i3,dmap[i1],dmap[i2],dmap[i3])
            add_A6(key, wcoeffs)
    else: # e=a
        if j==l or j==m:
            pass
        else:
            i1,i2,i3=sorted([j,l,m])
            dmap={j:0,l:1,m:1}
            key=('T',i1,i2,i3,dmap[i1],dmap[i2],dmap[i3])
            add_A6(key, wcoeffs)
    return dict(out)

def orbit_sum_Dimage(k, rep, maps):
    w_index,wlist,dW,s_index,slist,nS,a6_index,a6list=maps
    etype,j0,(l0,m0),(p0,q0)=rep
    S=sorted(set([j0,l0,m0,p0,q0]))
    t=len(S)
    acc=defaultdict(int)
    for img in itertools.permutations(range(k), t):
        phi=dict(zip(S,img))
        j=phi[j0]; l=phi[l0]; m=phi[m0]
        pi,qi=phi[p0],phi[q0]
        wres=wedge_image_dict(p0,q0,pi,qi,k)
        if not wres: continue
        term=D_image_of_domain_basis(k, etype, j, l, m, wres, maps)
        for kk,v in term.items():
            acc[kk]+=v
    return dict(acc)

def dict_dot(a,b):
    if len(a)>len(b): a,b=b,a
    s=0
    for kk,v in a.items():
        w=b.get(kk,0)
        if w: s+=v*w
    return s

def rank_of_dicts(dicts):
    r=len(dicts)
    if r==0: return 0, None
    import sympy as sp
    G=sp.zeros(r)
    for i in range(r):
        for j in range(i,r):
            v=dict_dot(dicts[i],dicts[j])
            G[i,j]=v; G[j,i]=v
    return G.rank(), G

def gen_reps():
    # generate canonical reps with labels in 0..4 covering all overlap types
    # brute force all tuples then group by partition type; keep one per type
    reps=[]
    seen=set()
    for et in (0,1):
        for j0 in range(5):
            for l0 in range(5):
                for m0 in range(l0+1,5):
                    pass
    # Instead: iterate all and compute canonical partition code
    allreps=[]
    for etype in (0,1):
        for j0 in range(5):
            for l0 in range(5):
                for m0 in range(5):
                    if not (l0<m0): continue
                    for p0 in range(5):
                        for q0 in range(5):
                            if not (p0<q0): continue
                            allreps.append((etype,j0,(l0,m0),(p0,q0)))
    # group by isomorphism type: relabel labels by order of first appearance? Use partition of positions:
    # positions: [j, l, m, p, q] with l,m unordered and p,q unordered. Canonical code: compute set partition of {0..4 indices into 5 roles}?
    # Roles: 0=j,1=l,2=m,3=p,4=q with swaps 1<->2, 3<->4. Two reps equivalent iff exist bijection of label values preserving equalities.
    # Equality pattern: for each pair of roles, equal or not. Encode as frozenset of equal pairs (up to role swaps). Use brute force canonical: try all perms of label values? Simpler: compute canonical form by renaming labels in order of first appearance scanning roles in fixed order, but need to account for role swaps: take min over the 4 role-swap variants.
    def canon(rep):
        etype,j0,(l0,m0),(p0,q0)=rep
        best=None
        for (l,m) in ((l0,m0),(m0,l0)):
            for (p,q) in ((p0,q0),(q0,p0)):
                roles=[j0,l,m,p,q]
                mp={}; nxt=0; code=[]
                for v in roles:
                    if v not in mp: mp[v]=nxt; nxt+=1
                    code.append(mp[v])
                code=tuple(code)
                if best is None or code<best: best=code
        return (etype,best)
    seen={}
    for rep in allreps:
        c=canon(rep)
        if c not in seen:
            seen[c]=rep
    return list(seen.values())

reps=gen_reps()
print(f"num orbit types: {len(reps)}")
for k in [5,6,7,8,9,10]:
    maps=build_index_maps(k)
    w_index,wlist,dW,s_index,slist,nS,a6_index,a6list=maps
    print(f"=== k={k} dW={dW} nS={nS} nA6={len(a6list)}")
    dom=[orbit_sum_C5(k,rep,maps) for rep in reps]
    # filter zero dicts? keep for rank (zeros don't affect rank)
    nz=[d for d in dom if len(d)>0 and any(v!=0 for v in d.values())]
    # check zero vs nonzero via dot self
    rdom,Gdom=rank_of_dicts(dom)
    print(f"  inv(C5) rank={rdom} (num nonzero dicts={len(nz)}/{len(dom)})")
    imgs=[orbit_sum_Dimage(k,rep,maps) for rep in reps]
    rimg,_=rank_of_dicts(imgs)
    print(f"  rank(D(invC5))={rimg} => dim ker (H5 twisted) = {rdom-rimg}")
