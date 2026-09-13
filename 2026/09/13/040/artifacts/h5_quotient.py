import itertools
from collections import defaultdict
import sympy as sp

exec(open('output/artifacts/h5_explore.py').read().split("def gen_reps")[0])

def gen_reps():
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

def build_flat_index(k):
    maps=build_index_maps(k)
    w_index,wlist,dW,s_index,slist,nS,a6_index,a6list=maps
    # domain flat: ((etype,k? )) index: ((etype*k+j)*nS+si)*dW+wi ; size 2*k*nS*dW
    NC5 = 2*k*nS*dW
    return maps, NC5

def dict_to_dense(d, N):
    import numpy as np
    v=np.zeros(N,dtype=int)
    for kk,vv in d.items():
        v[kk]=vv
    return v

def compute_H5(k, verbose=True):
    maps, NC5 = build_flat_index(k)
    w_index,wlist,dW,s_index,slist,nS,a6_index,a6list=maps
    nA6=len(a6list)
    NA6W = nA6*dW
    reps=gen_reps()
    # Step 1: invariant subspace I = span of orbit sums in C5xW
    dom=[orbit_sum_C5(k,rep,maps) for rep in reps]
    # Gram rank = 4 (for k>=4). Find basis of I via independent orbit sums.
    # Use exact Gram + pick pivots.
    r=len(dom)
    G=sp.zeros(r)
    def ddot(a,b):
        if len(a)>len(b): a,b=b,a
        s=0
        for kk,v in a.items():
            w=b.get(kk,0)
            if w: s+=v*w
        return s
    for i in range(r):
        for j in range(i,r):
            v=ddot(dom[i],dom[j])
            G[i,j]=v; G[j,i]=v
    rk=G.rank()
    # pivot columns via columnspace? Use sympy columnspace on G? Instead greedy.
    piv=[]
    for i in range(r):
        # check if dom[i] linearly independent of previous pivots: rank of Gram of piv+[i] == len
        test=piv+[i]
        m=len(test)
        Gm=sp.zeros(m)
        for a in range(m):
            for b in range(a,m):
                v=ddot(dom[test[a]],dom[test[b]])
                Gm[a,b]=v; Gm[b,a]=v
        if Gm.rank()==m:
            piv=test
    if verbose:
        print(f"k={k} inv(C5) rank={rk} pivots={piv} reps={[reps[i] for i in piv]}")
    Ivecs=[dom[i] for i in piv]  # basis of I (as vectors in C)
    # Step 2: relation subspace Rsub: spanned by (x_l - x_m)G_lm \otimes w over all l<m, x in {a,b}, w in W basis.
    # Represent as dense? NC5 up to k=7: 2*7*21*15=4410. Manageable dense with sympy? Use sparse + linear algebra via projection onto I.
    # To compute I ∩ Rsub: x in I lies in Rsub iff x orthogonal to (Rsub)^\perp? Easier: solve: x = R*c? Use least squares over Q: build matrix R (NC5 x nR) and test each I vector in column space.
    # nR = (#relations)*(dW) = (2*nS)*dW. For k=7: 42*15=630 cols, rows 4410. Exact rank via sympy could be heavy but ok for k<=6.
    # Build R columns as dicts.
    Rcols=[]
    for (l,m) in slist:
        for etype in (0,1):
            # relation vector in C5: e_l G_lm - e_m G_lm (e=a if etype=0 else b)
            for w in wlist:
                # w=(p,q) basis element of W; R col = (basis_C5[(etype,l,(l,m))] - basis_C5[(etype,m,(l,m))]) \otimes w
                d={}
                # flat index function
                si=s_index[(l,m)]
                wi=w_index[w]
                idx1=((etype*k+l)*nS+si)*dW+wi
                idx2=((etype*k+m)*nS+si)*dW+wi
                d[idx1]=1; d[idx2]=-1
                Rcols.append(d)
    if verbose:
        print(f"  NC5={NC5} nRcols={len(Rcols)} NA6W={NA6W}")
    # Intersection: for each basis vector of I, test membership in span(Rcols).
    # Build matrix M = [Rcols | -I?] Solve R*c = v. Use sympy linear solve on augmented? NC5 rows large; reduce to support rows (union of supports of Rcols and Ivecs)? Supports: Rcols involve only s=(l,m) slices; Ivecs involve many. Union = all rows that appear. Could still be ~NC5.
    # Use rational least-squares via normal equations? Membership test: v in col(R) iff v - P v = 0 where P projects. Compute via sympy? Alternative: use integer Gaussian elimination with sage-like? Use numpy rational via fractions? Let's use sympy Matrix with reduced row set: restrict to rows in support union (which is most rows, but ok).
    # For k=5: NC5=2*5*10*6=600 rows, 2*10*6=120 cols. Fine.
    # Build dense matrices with sympy for exactness (600x120 ok).
    import numpy as np
    # collect row index set
    rows=set()
    for d in Rcols:
        rows.update(d.keys())
    for d in Ivecs:
        rows.update(d.keys())
    rows=sorted(rows)
    ridx={r:i for i,r in enumerate(rows)}
    nR=len(Rcols); nI=len(Ivecs)
    Rm=sp.zeros(len(rows), nR)
    for j,d in enumerate(Rcols):
        for kk,v in d.items():
            Rm[ridx[kk],j]=v
    # rank of R
    rR=Rm.rank()
    if verbose:
        print(f"  rank(Rsub)={rR}")
    # For each Iv, test membership: rank([R | v]) == rank(R)?
    inR=[]
    for i,d in enumerate(Ivecs):
        v=sp.zeros(len(rows),1)
        for kk,vv in d.items():
            v[ridx[kk]]=vv
        aug=Rm.row_join(v)
        rka=aug.rank()
        inR.append(rka==rR)
        if verbose:
            print(f"    I[{i}] in Rsub? {rka==rR} (aug rank {rka})")
    dim_inter = None
    # Intersection dimension: need full space I ∩ R, not just basis members. Since basis may mix, compute properly: find all coeffs c such that sum c_i I_i ∈ R.
    # Method: matrix [R | I] : find nullspace vectors' I-parts. Consider M = [R, I1,..,InI] (rows x (nR+nI)). Nullspace dimension = nR+nI - rank(M). Nullspace vectors (a,b): R a + I b =0. Map to b gives kernel of (I -> C/R), i.e., I∩R parametrized. dim(I∩R) = dim ker = nullity - nullity(R alone)? More directly: dim(I∩R) = rank(R)+rank(I)-rank([R I]) = rR + nI - rank(M).
    M = Rm.row_join(sp.zeros(len(rows), nI))
    for j,d in enumerate(Ivecs):
        for kk,vv in d.items():
            M[ridx[kk], nR+j]=vv
    rM=M.rank()
    dim_cap = rR + nI - rM
    if verbose:
        print(f"  rank([R I])={rM} => dim(I∩R)={dim_cap} => dim inv(V)={nI-dim_cap}")
    # Step 3: D map on quotient: compute D(Ivecs) images, and D(R)=0 check; then ker of induced map V->A6W restricted to inv(V).
    # Compute images
    imgs=[orbit_sum_Dimage(k,rep,maps) for rep in reps]
    # images corresponding to pivots
    Imgs=[imgs[i] for i in piv]
    # Check D(Rcols)=0? Each R col maps via D: D((e_l - e_m)G_lm \otimes w) should be 0 since D(e_l G)-D(e_m G)? Let's verify: D(e_l G_lm): terms? e_l*pt_l vanishes? Actually D(s) independent of e? D acts as D_G \otimes I on C5? D(e_j \otimes s_lm)= e_j * D(s_lm) (multiplication in H^*). Then D(r)= e_l D(s) - e_m D(s). Is that zero? e_l pt_l... vs e_m pt_l? Not obviously zero. Wait relation is (x_i - x_j)s_ij=0 in domain, and D respects relations? D((x_i-x_j)s_ij) = (x_i - x_j)D(s_ij)? Since D is H^*-linear? d is H^*-linear up to? Actually differential is H^*-linear? d(h * s) = h * d(s) since d(h)=0. So D(r) = (x_l - x_m) D(s_lm) in H^6. Is that zero in H^6? (x_l - x_m)(pt_l+pt_m+...) =? x_l pt_l =0, x_l pt_m = pt_l? Hmm x_l * pt_m = pt_l? No: pt_l is degree 4 at position l; x_l is degree2 at l. Product x_l pt_l =0 (degree 6 at single position, top class is degree4, so vanishes). x_l pt_m (l≠m) = pt_m x_l nonzero (degree 6 across two positions). Similarly x_m pt_l nonzero. So (x_l - x_m)(pt_l + pt_m) = x_l pt_m - x_m pt_l (nonzero generally). So D(r) ≠ 0?! That can't be — differential must descend to quotient. Hmm, maybe Kriz differential does NOT descend naively; quotient is by relations as differential ideal? Let's recall: relations generate an ideal, differential preserves ideal? d((x_i - x_j)s_ij) = (x_i - x_j) d(s_ij). For this to be in ideal, need (x_i-x_j)d(s_ij) ∈ ideal. Since d(s_ij)=Δ_ij involves ... (x_i - x_j)Δ_ij =0 in H^*(M^k)? Is (x_l - x_m)Δ_lm =0? Δ_lm = pt_l+pt_m + a_la_m + b_lb_m - ...? Multiply by (a_l - a_m): (a_l - a_m)(pt_l+pt_m) = a_l pt_m - a_m pt_l. And (a_l - a_m)(a_la_m) = a_l^2 a_m - a_l a_m^2 = pt_l a_m - a_l pt_m. Sum: (a_l pt_m - a_m pt_l) + (pt_l a_m - a_l pt_m) =0. Similarly b terms vanish? (a_l - a_m)(b_lb_m)= a_l b_l b_m - a_m b_l b_m =0-0=0 (since a_l b_l=0). So total zero. Good — D(r)=0 in H^6. Our D_image function must reflect this cancellation; check numerically.
    # Verify: compute D of each R col (as dict in A6W) and check zero.
    # Build D matrix on basis? Instead compute D_* on the specific vectors: for relation (etype,l,m) \otimes w, D = D_image_of_domain_basis(k, etype, l, l, m, {w:1}) - D_image_of_domain_basis(k, etype, m, l, m, {w:1}).
    from collections import defaultdict as dd
    def D_of_R(etype,l,m,w):
        maps2=maps
        w_index2,wlist2,dW2,s_index2,slist2,nS2,a6_index2,a6list2=maps2
        # w is (p,q); represent wcoeffs dict {(p,q):1}? But W part must be expanded? No, W part passes through; use basis element directly.
        # D_image_of_domain_basis expects wcoeffs keyed by (r,s) W basis pairs; pass {(w):1}.
        d1=D_image_of_domain_basis(k, etype, l, l, m, {w:1}, maps2)
        d2=D_image_of_domain_basis(k, etype, m, l, m, {w:1}, maps2)
        out=dict(d1)
        for kk,v in d2.items():
            out[kk]=out.get(kk,0)-v
        return {kk:v for kk,v in out.items() if v!=0}
    ok=True
    for (l,m) in slist[:3]:
        for etype in (0,1):
            for w in wlist[:2]:
                dd_=D_of_R(etype,l,m,w)
                if len(dd_)!=0:
                    ok=False
                    print(f"  D(R) nonzero! {(etype,l,m,w)} -> {dd_}")
                    break
    if verbose:
        print(f"  D(R)=0 check: {ok}")
    # Rank of D on I: Gram of Imgs
    def ddot2(a,b):
        if len(a)>len(b): a,b=b,a
        s=0
        for kk,v in a.items():
            w=b.get(kk,0)
            if w: s+=v*w
        return s
    nI2=len(Imgs)
    Gm=sp.zeros(nI2)
    for a in range(nI2):
        for b in range(a,nI2):
            v=ddot2(Imgs[a],Imgs[b])
            Gm[a,b]=v; Gm[b,a]=v
    rD=Gm.rank()
    if verbose:
        print(f"  rank(D|_I)={rD} Gram="); print(Gm)
        print(f"  => naive ker dim (unquotiented) = {nI2-rD}")
    # True H^5 twisted = ker(Dbar) on inv(V): dim = dim inv(V) - rank(Dbar on inv(V)).
    # rank(Dbar) = rank of images of I-basis in A6W (since D(R)=0, descends). That's rD' = rank of Imgs modulo? Actually images of I basis vectors; but if some I vector lies in R, its image is 0 automatically. So rank = rank(Imgs as vectors) but considered as map factoring through quotient: rank = rD (same). Then dim ker = (nI - dim_cap) - rD_adjusted? Careful: if I∩R nonzero, the induced map's rank could be less than rD? No: rD = rank of images of chosen basis; kernel of quotient map = {v∈I : Dv=0}/(I∩R)? dim = (dim ker(D|_I)) - dim_cap? Only if I∩R ⊆ ker(D|_I) (true since D(R)=0). So dim H5 = (nI - rD) - dim_cap.
    dimH5 = (nI2 - rD) - dim_cap
    if verbose:
        print(f"  => dim H^5 twisted (quotiented) = ({nI2}-{rD})-{dim_cap} = {dimH5}")
    return {"k":k,"invC":rk,"rankR":rR,"dimcap":dim_cap,"rankD":rD,"dimH5":dimH5}

for k in [4,5,6]:
    print("="*60)
    compute_H5(k)
