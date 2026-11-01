#!/usr/bin/env python3
"""Exact finite checks for the integral hexagonal-chain homology theorem.

No third-party dependencies. Finite tests corroborate, but do not replace, the
all-parameter proof given separately.
"""
from collections import defaultdict


def hex_edges(n):
    width = 2*n + 1
    edges = set()
    for r in range(2):
        for j in range(width-1):
            edges.add(frozenset((r*width+j, r*width+j+1)))
    for j in range(0, width, 2):
        edges.add(frozenset((j, width+j)))
    return edges


def independent_faces(n):
    N = 4*n+2
    adj = [0]*N
    for edge in hex_edges(n):
        i,j = tuple(edge)
        adj[i] |= 1 << j
        adj[j] |= 1 << i
    faces = defaultdict(list)
    def dfs(avail, selected):
        faces[len(selected)].append(tuple(selected))
        while avail:
            bit = avail & -avail
            v = bit.bit_length() - 1
            avail ^= bit
            dfs(avail & ~adj[v], selected+[v])
    dfs((1<<N)-1, [])
    return {k: sorted(v) for k,v in faces.items()}


def echelon_add(vector, pivots):
    while vector:
        lead = vector.bit_length()-1
        if lead in pivots:
            vector ^= pivots[lead]
        else:
            pivots[lead] = vector
            return True
    return False


def reduce_all(vector, boundaries, homology):
    for lead in sorted(set(boundaries)|set(homology), reverse=True):
        if (vector>>lead)&1:
            vector ^= (boundaries[lead] if lead in boundaries else homology[lead][0])
    return vector


def quotient_coords(vector, boundaries, homology):
    coords = 0
    for lead in sorted(set(boundaries)|set(homology), reverse=True):
        if (vector>>lead)&1:
            if lead in boundaries:
                vector ^= boundaries[lead]
            else:
                representative, bit = homology[lead]
                vector ^= representative
                coords ^= bit
    assert vector == 0, 'cycle is not spanned by boundaries and homology basis'
    return coords


def homology_actions(n):
    faces = independent_faces(n)
    k=n+1
    curr=faces[k]
    lower={f:i for i,f in enumerate(faces[k-1])}
    upper=faces.get(k+1, [])
    curr_idx={f:i for i,f in enumerate(curr)}
    boundaries={}
    for face in upper:
        d=0
        for j in range(len(face)):
            d ^= 1 << curr_idx[face[:j]+face[j+1:]]
        echelon_add(d,boundaries)
    derivative={}
    cycles=[]
    for i,face in enumerate(curr):
        v=0
        for j in range(len(face)):
            v ^= 1 << lower[face[:j]+face[j+1:]]
        carrier=1<<i
        while v:
            p=v.bit_length()-1
            if p in derivative:
                v0,c0=derivative[p]
                v ^= v0
                carrier ^= c0
            else:
                derivative[p]=(v,carrier)
                break
        else:
            cycles.append(carrier)
    hom={}
    representatives=[]
    for cycle in cycles:
        reduced=reduce_all(cycle,boundaries,hom)
        if reduced:
            p=reduced.bit_length()-1
            assert p not in hom
            hom[p]=(reduced,1<<len(representatives))
            representatives.append(cycle)
    assert len(representatives)==2, ('homology dimension',n,len(representatives))
    width=2*n+1
    symmetries={
        'row': lambda i:(1-i//width)*width+i%width,
        'end': lambda i:(i//width)*width+(width-1-i%width),
    }
    matrices={}
    for name,act in symmetries.items():
        permutation=[curr_idx[tuple(sorted(act(i) for i in face))] for face in curr]
        cols=[]
        for cycle in representatives:
            moved=0
            while cycle:
                least=cycle & -cycle
                j=least.bit_length()-1
                cycle ^= least
                moved ^= 1<<permutation[j]
            cols.append(quotient_coords(moved,boundaries,hom))
        assert len(cols)==2
        matrices[name]=cols
    def rank_tminus1(cols):
        piv={}
        for j,col in enumerate(cols):
            echelon_add(col^(1<<j),piv)
        return len(piv)
    assert rank_tminus1(matrices['row'])==1, (n,matrices)
    assert rank_tminus1(matrices['end'])==(n%2), (n,matrices)
    return {k:len(v) for k,v in faces.items()}, matrices


def fold_polynomial(n):
    # Fixed-orbit graph of the end reversal: two path rails at columns
    # 0,...,n, and vertical rungs in even columns.
    state={(0,0,0):1}  # unused; kept separate from the direct oracle below
    a,b,c=1,0,0
    for j in range(n+1):
        a,b,c = a+2*b+c, -(a+b), (a if j%2 else 0)
    return a+2*b+c


def folded_direct(n):
    width=n+1
    N=2*width
    adj=[0]*N
    edges=[]
    for r in range(2):
        for j in range(width-1):
            edges.append((r*width+j, r*width+j+1))
    for j in range(0,width,2):
        edges.append((j,width+j))
    for i,j in edges:
        adj[i]|=1<<j
        adj[j]|=1<<i
    total=0
    for mask in range(1<<N):
        if all(not (mask>>i&1) or not (mask & adj[i]) for i in range(N)):
            total += -1 if mask.bit_count()%2 else 1
    return total


def primitive_cross_cycle_check(n):
    width=2*n+1
    vertical=[(2*i,width+2*i) for i in range(n+1)]
    selected={edge[i%2] for i,edge in enumerate(vertical)}
    assert len(selected)==n+1
    edge_set=hex_edges(n)
    assert all(not e.issubset(selected) for e in edge_set)
    for other in set(range(4*n+2)) - selected:
        assert any(frozenset((other,u)) in edge_set for u in selected), (n,other)
    # Every choice of one endpoint on each rung occurs with coefficient +/-1
    # in the cross-polytope fundamental cycle. The selected simplex is a
    # maximal face; evaluation by its facet cochain is +/-1.
    return True


def main():
    for n in range(1,41):
        predicted = 0 if n%2 else 2*(-1)**(n//2+1)
        assert fold_polynomial(n)==predicted, (n,fold_polynomial(n),predicted)
    for n in range(1,8):
        assert fold_polynomial(n)==folded_direct(n), n
    for n in range(1,15):
        primitive_cross_cycle_check(n)
    for n in range(1,6):
        faces, action=homology_actions(n)
        print('n',n,'faces',sum(faces.values()),'top_H_mod2',2,'row',action['row'],'end',action['end'])
    print('VERIFY_OK: 40 transfer checks; 7 independent orbit enumerations; '
          '14 primitive facets; 5 exact mod-2 homology action checks')


if __name__=='__main__':
    main()
