#!/usr/bin/env python3
"""Finite combinatorial checks for a six-label one-factor-disjointness complex.
Requires Python 3 standard library only. No assertion about novelty or external review.
"""
import itertools, json
from collections import Counter

V=tuple(range(6))

def matchings(v):
    if not v:
        yield ()
        return
    a=v[0]
    for i in range(1,len(v)):
        for z in matchings(v[1:i]+v[i+1:]):
            yield ((a,v[i]),)+z

P=[frozenset(tuple(sorted(e)) for e in M) for M in matchings(V)]
assert len(P)==15 and len(set(P))==15
Pindex={p:i for i,p in enumerate(P)}
E=[set(p) for p in P]
fac={k:[] for k in range(1,6)}
for k in range(1,6):
    for comb in itertools.combinations(range(15),k):
        if len(set().union(*(E[i] for i in comb)))==3*k:
            fac[k].append(comb)
assert [len(fac[k]) for k in range(1,6)]==[15,60,80,30,6]
face_sets={k:set(fac[k]) for k in fac}

# Pentads are 1-factorizations of the original complete graph.
pentads=[t for t in itertools.combinations(range(15),5)
         if len(set().union(*(E[i] for i in t)))==15]
assert len(pentads)==6
assert all(sum(j in pentad for pentad in pentads)==2 for j in range(15))
edge_to_match={tuple(i for i,p in enumerate(pentads) if j in p):j for j in range(15)}
assert len(edge_to_match)==15
match_to_edge={j:edge for edge,j in edge_to_match.items()}
assert len(match_to_edge)==15
for i in range(15):
    for j in range(i+1,15):
        disjoint=E[i].isdisjoint(E[j])
        incident=bool(set(match_to_edge[i]).intersection(match_to_edge[j]))
        assert disjoint==incident

A=set()
for p in pentads:
    for k in range(1,6):
        A.update(t for t in itertools.combinations(p,k))
assert A.issubset(set().union(*face_sets.values()))
relative=sorted(set().union(*face_sets.values())-A)
assert len(relative)==20 and all(len(t)==3 for t in relative)
for a,b,c in itertools.combinations(range(6),3):
    tri=tuple(sorted([edge_to_match[(a,b)],edge_to_match[(a,c)],edge_to_match[(b,c)]]))
    assert tri in relative

# Finite-field rank provides an independent homology-dimension check.
def rank_modp(rows,ncols,p):
    pivots={}
    for raw in rows:
        row={j:x%p for j,x in raw.items() if x%p}
        while row:
            c=min(row)
            if c not in pivots:
                u=pow(row[c],-1,p)
                pivots[c]={j:v*u%p for j,v in row.items() if v*u%p}
                break
            a=row[c]
            for j,v in pivots[c].items():
                new=(row.get(j,0)-a*v)%p
                if new:row[j]=new
                else:row.pop(j,None)
    return len(pivots)

def rank_boundary(k,p):
    lo={s:i for i,s in enumerate(fac[k])}
    cols=[]
    for s in fac[k+1]:
        cols.append({lo[s[:i]+s[i+1:]]:(-1)**i for i in range(len(s))})
    return rank_modp(cols,len(fac[k]),p)

ranks={str(p):[rank_boundary(k,p) for k in range(1,5)] for p in (2,3,101)}
assert all(x==[14,46,24,6] for x in ranks.values())
assert (15-1-14,60-14-46,80-46-24,30-24-6,6-6)==(0,0,10,0,0)

# Full permutation action and signed-chain Lefschetz traces.
def action(perm):
    pm=[Pindex[frozenset(tuple(sorted((perm[a],perm[b]))) for a,b in M)] for M in P]
    pent=[pentads.index(tuple(sorted(pm[j] for j in T))) for T in pentads]
    return pm,pent

def orientation_sign(order):
    return -1 if sum(order[i]>order[j] for i in range(len(order)) for j in range(i+1,len(order)))%2 else 1

def cycle_type(perm):
    seen=set();parts=[]
    for i in V:
        if i not in seen:
            j=i;count=0
            while j not in seen:
                seen.add(j);j=perm[j];count+=1
            parts.append(count)
    return tuple(sorted(parts,reverse=True))

def exterior_character(perm,k):
    # det(I+t g on augmentation) = product_c (1-(-t)^c)/(1+t).
    f=[1]
    for length in cycle_type(perm):
        new=[0]*(len(f)+length)
        for i,v in enumerate(f):
            new[i]+=v
            new[i+length]+=v*(-1)**(length-1)
        f=new
    q=[]
    for i in range(len(f)-1):
        q.append(f[i]-(q[-1] if q else 0))
    return q[k]

def signed_trace(pm,s):
    total=0
    for f in fac[s]:
        transformed=[pm[j] for j in f]
        if set(transformed)==set(f):
            total+=orientation_sign(transformed)
    return total

seen_actions=set()
classes={}
for perm in itertools.permutations(V):
    pm,pent=action(perm)
    assert tuple(sorted(pent))==V
    seen_actions.add(tuple(pent))
    # A critical orientation test: a free triangle on the three
    # factorization edges carries the same signed action as its triple.
    for u in itertools.combinations(range(6),3):
        src_edges=[edge_to_match[(u[0],u[1])],edge_to_match[(u[0],u[2])],edge_to_match[(u[1],u[2])]]
        dst=tuple(sorted(pent[i] for i in u))
        dst_edges=[edge_to_match[(dst[0],dst[1])],edge_to_match[(dst[0],dst[2])],edge_to_match[(dst[1],dst[2])]]
        moved=[pm[i] for i in src_edges]
        edge_sign=orientation_sign([dst_edges.index(i) for i in moved])
        pent_sign=orientation_sign([dst.index(pent[i]) for i in u])
        assert edge_sign==pent_sign
    tr=-1+sum((-1)**(s-1)*signed_trace(pm,s) for s in range(1,6))
    assert tr==exterior_character(tuple(pent),3), (perm,pent,tr)
    assert tr==exterior_character(perm,2), (perm,pent,tr)
    ct=cycle_type(perm)
    if ct in classes:assert classes[ct]==tr
    else:classes[ct]=tr
assert len(seen_actions)==720 and len(classes)==11

# Matrices on integral augmentation bases w_i = e_i-e_5, and exterior powers.
def matrix_aug(perm):
    return [[(perm[i]==j)-(perm[5]==j) for i in range(5)] for j in range(5)]

def det_mod2(square):
    rows=[sum((v&1)<<j for j,v in enumerate(row)) for row in square]
    n=len(rows);rank=0
    for col in range(n):
        piv=next((i for i in range(rank,n) if rows[i]>>col&1),None)
        if piv is None:continue
        rows[rank],rows[piv]=rows[piv],rows[rank]
        for i in range(rank+1,n):
            if rows[i]>>col&1:rows[i]^=rows[rank]
        rank+=1
    return rank==n

def wedge_mod2(perm,k):
    m=matrix_aug(perm)
    subs=list(itertools.combinations(range(5),k))
    return [[int(det_mod2([[m[i][j] for j in col] for i in row]))
             for col in subs] for row in subs]

def rank_binary(rows):
    a=[sum((x&1)<<i for i,x in enumerate(r)) for r in rows]
    piv={}
    for b in a:
        while b:
            c=b.bit_length()-1
            if c in piv:b^=piv[c]
            else:piv[c]=b;break
    return len(piv)

def rank_minus_identity_mod2(perm,k):
    m=wedge_mod2(perm,k)
    return rank_binary([[m[i][j]^(i==j) for j in range(len(m))] for i in range(len(m))])

trans=(1,0,2,3,4,5)
_,pent_trans=action(trans)
assert cycle_type(tuple(pent_trans))==(2,2,2)
rank_actual=rank_minus_identity_mod2(tuple(pent_trans),3)
rank_naive=rank_minus_identity_mod2(trans,2)
assert (rank_actual,rank_naive)==(4,3)

report={
 'checks':'VERIFY_OK',
 'perfect_matchings':len(P),
 'pentads':len(pentads),
 'pentad_factorizations':[list(p) for p in pentads],
 'face_counts_dimension_0_to_4':[len(fac[k]) for k in range(1,6)],
 'star_union_faces':len(A),
 'nonstar_triangle_cells':len(relative),
 'boundary_ranks_mod_p_by_dimension_1_to_4':ranks,
 'integral_homology_from_exact_topological_relative_sequence':{'H2_rank':10,'other_reduced':0,'torsion':False},
 'checked_group_elements':len(seen_actions),
 'conjugacy_class_homology_characters':{','.join(map(str,k)):v for k,v in sorted(classes.items(),reverse=True)},
 'transposition_on_six_factorizations':pent_trans,
 'transposition_mod2_rank_on_exterior_cube_factorization_augmentation':rank_actual,
 'transposition_mod2_rank_on_exterior_square_original_augmentation':rank_naive,
}
print(json.dumps(report,sort_keys=True,indent=2))
