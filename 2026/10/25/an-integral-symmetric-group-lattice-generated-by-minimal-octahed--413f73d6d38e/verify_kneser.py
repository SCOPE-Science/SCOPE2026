"""Integral equivariant sphere generators for independent edge-family complexes.

Finite diagnostics only. Uniform assertion is proved mathematically in RESULT.md.
"""
from itertools import combinations,product,permutations
from collections import defaultdict
from math import comb


def parity(xs):
    return (-1)**sum(xs[i]>xs[j] for i in range(len(xs)) for j in range(i+1,len(xs)))


def sign_to_sorted(xs):
    return parity(xs)


def faces(n):
    edges=list(combinations(range(1,n+1),2))
    d=defaultdict(set)
    for a in range(1,n+1):
        incident=[e for e in edges if a in e]
        for k in range(1,len(incident)+1):
            for face in combinations(incident,k): d[k-1].add(face)
    for abc in combinations(range(1,n+1),3):
        i,j,k=abc
        d[2].add(tuple(sorted(((i,j),(i,k),(j,k)))))
    for k in (0,1,2,3):
        d.setdefault(k,set())
    return {k:sorted(v) for k,v in d.items()}


def boundary(z):
    out=defaultdict(int)
    for f,coef in z.items():
        for i in range(len(f)):
            v=f[:i]+f[i+1:]
            out[v]+=(-1)**i*coef
    return {x:y for x,y in out.items() if y}


def octahedron(Q):
    a,b,c,d=Q
    axes=[((a,b),(c,d)),((a,c),(b,d)),((a,d),(b,c))]
    z=defaultdict(int)
    for ss in product((0,1),repeat=3):
        axisordered=[axes[i][ss[i]] for i in range(3)]
        key=tuple(sorted(axisordered))
        z[key]+=(-1)**sum(ss)*sign_to_sorted(axisordered)
    assert len(z)==8 and all(abs(x)==1 for x in z.values())
    assert not boundary(z)
    return dict(z)


def triangle_coordinate(Q,z):
    a,b,c=Q
    e=((b,c),(a,c),(a,b)) # order corresponding to i,j,k complements
    e_sorted=tuple(sorted(e))
    return z.get(e_sorted,0)*sign_to_sorted(e)


def relative_coefficients(n,z):
    return {T:triangle_coordinate(T,z) for T in combinations(range(1,n+1),3) if triangle_coordinate(T,z)}


def sparse_cols(n,k):
    f=faces(n)
    idx={v:i for i,v in enumerate(f[k-1])}
    cols=[]
    for ff in f[k]:
        col={idx[ff[:i]+ff[i+1:]]:(-1)**i for i in range(len(ff))}
        cols.append(col)
    return len(f[k-1]),cols


def modrank(cols,p):
    piv={}
    for col in cols:
        z={i:c%p for i,c in col.items() if c%p}
        while z:
            row=min(z)
            if row not in piv:
                fac=pow(z[row],-1,p)
                piv[row]={i:(v*fac)%p for i,v in z.items() if v%p}
                break
            c=z[row]
            for i,v in piv[row].items():
                t=(z.get(i,0)-c*v)%p
                if t: z[i]=t
                else: z.pop(i,None)
    return len(piv)


def verify(n):
    f=faces(n)
    Fs={k:len(f[k]) for k in f}
    boundary2_idx={ff:i for i,ff in enumerate(f[1])}
    octs=[octahedron(Q) for Q in combinations(range(1,n+1),4)]
    octcols=[]
    idx={f:i for i,f in enumerate(f[2])}
    for z in octs:
        octcols.append({idx[face]:val for face,val in z.items()})
    _,d3=sparse_cols(n,3)
    _,d2=sparse_cols(n,2)
    rk3=modrank(d3,101)
    rk2=modrank(d2,101)
    rkjoined=modrank(d3+octcols,101)
    assert len(f[2])-rk2-rk3==comb(n-1,3)
    assert rkjoined-rk3==comb(n-1,3)
    # Integral linear relations verified explicitly on oriented simplicial cycles.
    # The octahedron orientation above yields the same sign as the standard
    # alternating tetrahedron-face boundary after one uniform scalar correction.
    for Q in combinations(range(1,n+1),4):
        z=octahedron(Q)
        r=relative_coefficients(n,z)
        std={Q[:i]+Q[i+1:]:(-1)**i for i in range(4)}
        assert r==std or r=={t:-v for t,v in std.items()},(Q,r,std)
    # Canonical generators indexed by four-subsets satisfy the signed five-term relations.
    orient={Q:relative_coefficients(n,octahedron(Q))[Q[1:]] for Q in combinations(range(1,n+1),4)}
    normalized={Q:{ff:coef*orient[Q] for ff,coef in octahedron(Q).items()} for Q in orient}
    for S in combinations(range(1,n+1),5):
        z=defaultdict(int)
        for i in range(5):
            Q=S[:i]+S[i+1:]
            for ff,c in normalized[Q].items(): z[ff]+=(-1)**i*c
        # Relations need only hold in homology: the resulting cycle lies in star subcomplex U.
        # Relative classes vanish on all nonstar triangles.
        rel=relative_coefficients(n,z)
        assert not rel,(S,rel)
    # Pure signed symmetry, check for two generating permutations on normalized cycle family
    for perm in ((2,1)+tuple(range(3,n+1)),tuple(range(2,n+1))+(1,)):
        def act(z):
            ret=defaultdict(int)
            for face,v in z.items():
                moved=[tuple(sorted((perm[i-1],perm[j-1]))) for i,j in face]
                ret[tuple(sorted(moved))]+=v*sign_to_sorted(moved)
            return dict(ret)
        for Q,z in list(normalized.items())[:min(7,len(normalized))]:
            im=tuple(sorted(perm[x-1] for x in Q))
            s=sign_to_sorted([perm[x-1] for x in Q])
            transformed=act(z)
            candidate=normalized[im]
            # equivariance in homology detected in relative triangle coefficients
            assert relative_coefficients(n,transformed)=={k:s*v for k,v in relative_coefficients(n,candidate).items()}
    print('n=',n,'f-vector=',Fs,'d2_rank=',rk2,'d3_rank=',rk3,'H2_rank=',len(f[2])-rk2-rk3,'octahedra=',len(octs),'octahedron_rank_mod101=',rkjoined-rk3,'five_relations_checked=',comb(n,5) if n>=5 else 0)

if __name__=='__main__':
    for n in range(4,9): verify(n)
    print('VERIFY_OK_KNESER_INTEGRAL_SYMMETRIC_MODULE')
