#!/usr/bin/env python3
"""Standalone integer checks for a degree-one cubical/simplicial comparison.

Input hyperedges are sets of supported vertices. The checker independently
constructs the singular squares of the radius-one-ball cube and the simplex
boundary relations; it never assumes the theorem in constructing a cube.
"""
from itertools import combinations, product
from collections import Counter
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form, hermite_normal_form


def select_projective_plane_facets():
    """Find a six-vertex closed surface with every edge of K6 in two faces."""
    tri = list(combinations(range(6),3))
    ed = list(combinations(range(6),2))
    col={e:i for i,e in enumerate(ed)}
    t_edges=[tuple(col[e] for e in combinations(t,2)) for t in tri]
    from itertools import combinations as choose
    for I in choose(range(len(tri)),10):
        counts=[0]*15
        for i in I:
            for j in t_edges[i]:counts[j]+=1
        if counts==[2]*15:
            return [tri[i] for i in I]
    raise AssertionError('No closed 6-vertex triangulation found')


def simplicial_data(hyperedges):
    verts=sorted(set().union(*map(set,hyperedges)))
    edges=sorted({tuple(sorted(e)) for h in hyperedges for e in combinations(h,2)})
    tris=sorted({tuple(sorted(t)) for h in hyperedges for t in combinations(h,3)})
    idx={e:i for i,e in enumerate(edges)}
    tmat=Matrix.zeros(len(edges),len(tris))
    for j,(a,b,c) in enumerate(tris):
        tmat[idx[(a,b)],j]=1
        tmat[idx[(b,c)],j]=1
        tmat[idx[(a,c)],j]=-1
    return verts,edges,tris,tmat


def gamma_2_data(hyperedges):
    verts,edges,tris,tmat=simplicial_data(hyperedges)
    E={frozenset(x) for x in hyperedges}
    def supported(s):
        z=frozenset(s)
        return any(z<=h for h in E)
    directed=[(a,b) for a in verts for b in verts if a!=b and supported((a,b))]
    pos={e:i for i,e in enumerate(directed)}
    balls=((0,1,2),(1,0,3),(2,0,3),(3,1,2))
    relations=set()
    squares=0
    for a,b,c,d in product(verts,repeat=4):
        if (a==b and c==d) or (a==c and b==d):continue
        v=(a,b,c,d)
        if not all(supported(v[i] for i in ball) for ball in balls):continue
        squares+=1
        vec=[0]*len(directed)
        for u,w,sgn in ((a,b,1),(b,d,1),(a,c,-1),(c,d,-1)):
            if u!=w:vec[pos[(u,w)]]+=sgn
        if any(vec):relations.add(tuple(vec))
    mat=Matrix.hstack(*(Matrix(v) for v in sorted(relations))) if relations else Matrix.zeros(len(directed),0)
    return directed,mat,squares


def is_manifold_rp2(tris):
    edges=Counter(tuple(sorted(e)) for t in tris for e in combinations(t,2))
    assert len(edges)==15 and set(edges.values())=={2}
    for v in range(6):
        lk=Counter(tuple(sorted(x for x in t if x!=v)) for t in tris if v in t)
        assert len(lk)==5 and len(set.union(*(set(e) for e in lk)))==5
        deg=Counter(x for e in lk for x in e)
        assert len(deg)==5 and set(deg.values())=={2}
    return True


def snf_invariants(mat):
    di=smith_normal_form(mat,domain=ZZ)
    return [abs(int(di[i,i])) for i in range(min(di.rows,di.cols)) if di[i,i]!=0]


def compute_h1_simp(hyperedges):
    verts,edges,tris,tmat=simplicial_data(hyperedges)
    # Choose a spanning tree in the one-skeleton and put each cycle in the basis
    # of chords. Kernel of the graph boundary is a unimodular graph cycle lattice.
    parent={u:u for u in verts}
    def find(x):
        while parent[x]!=x:x=parent[x]
        return x
    tree=[];chords=[]
    for e in edges:
        u,v=e;ru,rv=find(u),find(v)
        if ru!=rv:parent[ru]=rv;tree.append(e)
        else:chords.append(e)
    assert len(tree)==len(verts)-len({find(x) for x in verts})
    inds={e:i for i,e in enumerate(edges)}
    d=Matrix([[tmat[inds[e],j] for j in range(len(tris))] for e in chords])
    invariants=snf_invariants(d)
    free=len(chords)-len(invariants)
    torsion=[z for z in invariants if z>1]
    return free,torsion,len(chords),len(tris)


def check_exact_relations(hyperedges):
    verts,edges,tris,tmat=simplicial_data(hyperedges)
    directed,gmat,ng=gamma_2_data(hyperedges)
    di={e:i for i,e in enumerate(directed)}
    # Independently build the inverse images of simplicial triangular relations
    # plus reversal relations, and compare integer column lattices via Hermite NF.
    cols=[]
    for a,b in edges:
        v=Matrix.zeros(len(directed),1)
        v[di[(a,b)]]=1;v[di[(b,a)]]=1;cols.append(v)
    for a,b,c in tris:
        v=Matrix.zeros(len(directed),1)
        v[di[(a,b)]]=1;v[di[(b,c)]]=1;v[di[(a,c)]]=-1;cols.append(v)
    basis=Matrix.hstack(*cols)
    assert hermite_normal_form(basis)==hermite_normal_form(gmat), 'integer image mismatch'
    return len(verts),len(edges),len(tris),ng,gmat.cols


def main():
    samples={
      'graph triangle':[(0,1),(0,2),(1,2)],
      'graph square':[(0,1),(1,2),(2,3),(0,3)],
      'filled triangle':[(0,1,2)],
      'nonuniform cycle':[(0,1,2),(1,4),(2,3),(3,4)],
      'two filled triangles':[(0,1,2),(0,2,3)],
      'complete tetrahedral boundary':[(0,1,2),(0,1,3),(0,2,3),(1,2,3)],
    }
    samples['six-vertex projective plane']=select_projective_plane_facets()
    print('RP2 FACETS',samples['six-vertex projective plane'])
    assert is_manifold_rp2(samples['six-vertex projective plane'])
    expected={
      'graph triangle':(1,[]), 'graph square':(1,[]),
      'filled triangle':(0,[]), 'nonuniform cycle':(1,[]),
      'two filled triangles':(0,[]), 'complete tetrahedral boundary':(0,[]),
      'six-vertex projective plane':(0,[2])
    }
    for name,h in samples.items():
        h1=compute_h1_simp(h)
        assert h1[:2]==expected[name],(name,h1)
        counts=check_exact_relations(h)
        print('PASS',name,'simplicial H1:',h1[:2],'(vertices,edges,triangles,2-cubes,distinct boundaries):',counts)
    print('ALL EXACT INTEGRAL RELATION-LATTICE COMPARISONS PASSED')
if __name__=='__main__':main()
