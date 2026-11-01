#!/usr/bin/env python3
"""Exact finite chain/character checks for three unordered points on K_{3,4}.

Python 3.9+ standard library; no external input. Modular ranks are certified
lower bounds on characteristic-zero ranks; the rational rank upper bound uses
the established H_1 theorem of Ko and Park (2011). Nothing here mistakes
modular dimensions for a proof of integral homology.
"""
from itertools import combinations, combinations_with_replacement, permutations, product

P, Q, N = 3, 4, 7
EDGES = tuple((i, j) for i in range(P) for j in range(P, N))
EDGE_ID = {e: i for i, e in enumerate(EDGES)}
INC = tuple(tuple(k for k, e in enumerate(EDGES) if v in e) for v in range(N))


def build_complex():
    basis = {}
    pos = {}
    for d in range(4):
        basis[d] = tuple((vs, hs, mon)
                         for vs in combinations(range(N), d)
                         for hs in product(*(range(len(INC[v])-1) for v in vs))
                         for mon in combinations_with_replacement(range(len(EDGES)), 3-d))
        pos[d] = {b: k for k,b in enumerate(basis[d])}
    diff = {}
    for d in range(1,4):
        cols = []
        for vs, hs, mon in basis[d]:
            col={}
            for k, v in enumerate(vs):
                for e, coeff in ((INC[v][hs[k]+1], 1), (INC[v][0], -1)):
                    target=(vs[:k]+vs[k+1:],hs[:k]+hs[k+1:],tuple(sorted(mon+(e,))))
                    r=pos[d-1][target]
                    col[r]=col.get(r,0)+((-1)**k)*coeff
            cols.append({r:c for r,c in col.items() if c})
        diff[d]=tuple(cols)
    return basis,pos,diff


def apply_boundary(vec,degree,diff):
    out={}
    for col,a in vec.items():
        for row,b in diff[degree][col].items():out[row]=out.get(row,0)+a*b
    return {r:c for r,c in out.items() if c}


def rank_mod(cols,prime):
    pivots={}
    for col in cols:
        v={i:c%prime for i,c in col.items() if c%prime}
        while v:
            i=min(v)
            if i not in pivots:
                inv=pow(v[i],-1,prime)
                pivots[i]={j:c*inv%prime for j,c in v.items()}
                break
            t=v[i]
            for j,c in pivots[i].items():
                z=(v.get(j,0)-t*c)%prime
                if z:v[j]=z
                else:v.pop(j,None)
    return len(pivots)


def group():
    for a in permutations(range(P)):
        for b in permutations(range(Q)):
            g=tuple(a)+tuple(P+x for x in b)
            yield a,b,g


def edge_action(g):
    return tuple(EDGE_ID[tuple(sorted((g[i],g[j])))] for i,j in EDGES)


def action_basis(b,degree,g,ge,pos):
    vs,hs,mon=b
    mapped=tuple(g[v] for v in vs)
    newvs=tuple(sorted(mapped))
    newmon=tuple(sorted(ge[e] for e in mon))
    crossings=sum(mapped[i]>mapped[j] for i in range(degree) for j in range(i+1,degree))
    terms={():-1 if crossings%2 else 1}
    for v,h in zip(vs,hs):
        local={}
        for edge,sign in ((ge[INC[v][h+1]],1),(ge[INC[v][0]],-1)):
            if edge!=INC[g[v]][0]:
                c=INC[g[v]].index(edge)-1
                local[c]=local.get(c,0)+sign
        terms={partial+(choice,):coeff*scalar
               for partial,coeff in terms.items() for choice,scalar in local.items() if scalar}
    out={}
    for choices_in_old_order,c in terms.items():
        new_hs=tuple(choices_in_old_order[mapped.index(v)] for v in newvs)
        r=pos[degree][(newvs,new_hs,newmon)]
        out[r]=out.get(r,0)+c
    return {r:c for r,c in out.items() if c}


def act_vec(vec,degree,basis,pos,g,ge):
    out={}
    for col,c in vec.items():
        for row,a in action_basis(basis[degree][col],degree,g,ge,pos).items():
            out[row]=out.get(row,0)+a*c
    return {r:a for r,a in out.items() if a}


def sg(p):
    return -1 if sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2 else 1


def irreps3(p):return (1,sg(p),sum(i==p[i] for i in range(3))-1)


def irreps4(p):
    fix=sum(i==p[i] for i in range(4))
    standard=fix-1
    on_pairs=sum(set((p[i],p[j]))==set((i,j)) for i,j in combinations(range(4),2))
    shape22=on_pairs-fix
    return (1,sg(p),shape22,standard,sg(p)*standard)


def main():
    basis,pos,diff=build_complex()
    dims=tuple(len(basis[d]) for d in range(4))
    assert dims==(364,1326,1476,491)
    print('chain_dimensions',dims)
    print('differential_nonzero_entries',tuple(sum(map(len,diff[d])) for d in range(1,4)))
    for d in (2,3):
        for col in diff[d]:assert not apply_boundary(col,d-1,diff)
    print('boundary_squared_zero',True)
    ranks={p:tuple(rank_mod(diff[d],p) for d in range(1,4)) for p in (2,3,5,101)}
    assert ranks[2]==(363,956,491)
    assert all(ranks[p]==(363,957,491) for p in (3,5,101))
    print('exact_finite_field_ranks',ranks)
    # The rank of d_1 is 363: in degree zero the differential spans
    # the differences between all degree-three monomials in connected
    # edge variables; their augmentation kernel has rank 364 - 1.
    # Ko--Park's theorem gives rank_Q H_1(B_3(K3,4))=6. The F3 rank
    # lower bound and the H1 rank upper bound force rank_Q d_2=957.
    # The F3 full rank d_3=491 forces the same over Q.
    betti=(1,6,28,0)
    assert all(x>=0 for x in betti)
    assert sum((-1)**d*dims[d] for d in range(4))==sum((-1)**d*betti[d] for d in range(4))
    print('rational_betti_from_rank_bounds_and_known_H1',betti)
    allg=list(group());assert len(allg)==144
    chars=[]
    for a,b,g in allg:
        ge=edge_action(g)
        traces=tuple(sum(action_basis(x,d,g,ge,pos).get(j,0)
                         for j,x in enumerate(basis[d])) for d in range(4))
        # Graph-cycle character is the natural equivariant rational H1:
        # H1(K3,4) = augmentation(S3) tensor augmentation(S4).
        h1=(sum(i==a[i] for i in range(3))-1)*(sum(j==b[j] for j in range(4))-1)
        # Independent alternating graph cellular trace formula.
        edge_trace=sum(g[i]==i and g[j]==j for i,j in EDGES)
        vertex_trace=sum(g[i]==i for i in range(N))
        assert h1==edge_trace-vertex_trace+1
        h2=sum((-1)**d*traces[d] for d in range(4))-1+h1
        chars.append((a,b,h1,h2))
    assert chars[0][2:]==(6,28)
    target2={(1,2):2,(1,3):1,(1,4):1,(2,1):1,(2,2):1,(2,3):1,(2,4):1}
    for i in range(3):
        for j in range(5):
            h1num=sum(h1*irreps3(a)[i]*irreps4(b)[j] for a,b,h1,h2 in chars)
            h2num=sum(h2*irreps3(a)[i]*irreps4(b)[j] for a,b,h1,h2 in chars)
            assert h1num==(144 if (i,j)==(2,3) else 0),(i,j,'H1',h1num)
            assert h2num==144*target2.get((i,j),0),(i,j,'H2',h2num)
    assert sum(h1 for a,b,h1,h2 in chars)==0
    assert sum(h2 for a,b,h1,h2 in chars)==0
    print('automorphisms_and_exact_character_inner_products',len(chars))
    print('H1_irreducibles_S3_index_S4_index_multiplicity',[(2,3,1)])
    print('H2_irreducibles_S3_index_S4_index_multiplicity',sorted((i,j,m) for (i,j),m in target2.items()))
    print('full_group_invariant_dimensions_H1_H2',(0,0))
    # For S3 generators and S4 generators verify chain map identity on
    # every basis vector in all three positive homological degrees.
    aI=(0,1,2);bI=(0,1,2,3)
    gens={( (1,0,2), bI ),((1,2,0),bI),(aI,(1,0,2,3)),(aI,(1,2,3,0))}
    chosen=[(a,b,g) for a,b,g in allg if (a,b) in gens]
    assert len(chosen)==4
    for a,b,g in chosen:
        ge=edge_action(g)
        for d in (1,2,3):
            for j,bas in enumerate(basis[d]):
                lhs=apply_boundary(action_basis(bas,d,g,ge,pos),d,diff)
                rhs=act_vec(diff[d][j],d-1,basis,pos,g,ge)
                assert lhs==rhs,('chain_map',d,j,a,b)
    print('chain_map_identity_all_basis_vectors_four_generators',True)
    print('PASS')

if __name__=='__main__':main()
