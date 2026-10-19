#!/usr/bin/env python3
"""Explicit structural isomorphism of the optimum exchange graph with GP(12,5)^2."""
import itertools,collections,hashlib,json
U=tuple(range(12));V=tuple(range(12,24));
raw=set()
for i in range(12):
    for a,b in ((i,(i+1)%12),(i,i+12),(i+12,12+(i+5)%12)):
        raw.add(tuple(sorted((a,b))))
# Verified concrete isomorphism between GP(12,5) and the four-permutation star graph.
allperm=list(itertools.permutations(range(4)))
permid={p:i for i,p in enumerate(allperm)}
gp_to_star=(0,6,12,18,4,10,16,22,3,9,15,21,14,19,2,7,17,20,5,8,13,23,1,11)
assert sorted(gp_to_star)==list(range(24))
star_edges=set()
for a,p in enumerate(allperm):
    for k in range(1,4):
        q=list(p);q[0],q[k]=q[k],q[0]
        b=permid[tuple(q)];star_edges.add(tuple(sorted((a,b))))
assert {tuple(sorted((gp_to_star[a],gp_to_star[b])))for a,b in raw}==star_edges

r0=((0,4,8),(2,6,10),(13,17,21),(15,19,23))
c0=((0,6,15,21),(2,8,17,23),(4,10,13,19))
def rotate(blocks):
    return tuple(tuple((v+1)%12 if v<12 else 12+(v-12+1)%12 for v in group)for group in blocks)
components=((r0,c0),(rotate(r0),rotate(c0)))
lookup=[]
for rows,cols in components:
    assert all(len(set(row)&set(col))==1 for row in rows for col in cols)
    # Every permutation determines a unique independent triple: one cell per
    # column, three distinct rows. The first entry is the omitted row.
    perm_to_indep={}
    for p in allperm:
        subset=tuple(sorted((set(rows[p[j+1]])&set(cols[j])).pop()for j in range(3)))
        assert len(set(subset))==3
        perm_to_indep[p]=subset
    assert len(set(perm_to_indep.values()))==24
    lookup.append(perm_to_indep)

# Construct bases as complements of a pair of independent triples, and check
# that exactly a star move in one permutation coordinate produces a token jump.
allv=set(range(24))
bases={ (permid[p],permid[q]): frozenset(allv-set(lookup[0][p])-set(lookup[1][q]))
       for p in allperm for q in allperm }
assert len(bases)==576 and len(set(bases.values()))==576
for key,S in bases.items():
    for other,T in bases.items():
        diff=len(S-T)
        gp1,gp2=key;h1,h2=other
        edge=(gp1==h1 and tuple(sorted((gp2,h2)))in star_edges) or (gp2==h2 and tuple(sorted((gp1,h1)))in star_edges)
        if key==other:assert diff==0
        else:assert (diff==1)==edge

P=[1,3,6,9,5]
square=[sum(P[i]*P[k-i]for i in range(5)if 0<=k-i<5)for k in range(9)]
assert square==[1,6,21,54,100,138,141,90,25]
with open('product_isomorphism.json','w',encoding='utf8')as f:
    json.dump({'gp_vertex_to_star_permutation_index':gp_to_star,
     'perm_index_order':'lexicographically sorted permutations of (0,1,2,3)',
     'component_rook_rows':[[list(x)for x in cp[0]] for cp in components],
     'component_rook_columns':[[list(x)for x in cp[1]]for cp in components],
     'basis_key':'(lex-index of row-hole permutation in first SR component, same in second)',
     'distance_profile':square}, f,sort_keys=True,separators=(',',':'));f.write('\n')
print('STAR_OK: GP(12,5) explicitly isomorphic to star-transposition Cayley graph of S4.')
print('PRODUCT_OK: all 576 basis pairs obey exactly GP(12,5) Cartesian-square adjacency.')
print('PROFILE_OK: product distance profile',square)
print('ISOM_CERT_SHA256:',hashlib.sha256(open('product_isomorphism.json','rb').read()).hexdigest())
