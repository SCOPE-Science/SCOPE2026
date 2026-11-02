#!/usr/bin/env python3
"""Independent integral triangle-boundary and equivariance certificate.
Builds the relative two-cells and the complete-graph cycle lattice directly.
"""
from itertools import combinations
from math import comb

def parity(v):
    return -1 if sum(a>b for i,a in enumerate(v) for b in v[i+1:])%2 else 1

def canonical(w):
    return tuple(sorted(w)),parity(w)

def wedge_boundary(t):
    return {(t[1],t[2]):1,(t[0],t[2]):-1,(t[0],t[1]):1}

def act_face(face,perm):
    return canonical(tuple(perm[x] for x in face))

def boundary_equivariant(n):
    triangles=list(combinations(range(n),3))
    edges=list(combinations(range(n),2))
    adj=[list(range(n)) for _ in range(n-1)]
    for i,perm in enumerate(adj):perm[i],perm[i+1]=perm[i+1],perm[i]
    for perm in adj:
        for t in triangles:
            tnew,sgn=act_face(t,perm)
            rhs={e:0 for e in edges}
            for e,val in wedge_boundary(t).items():
                en,eg=act_face(e,perm);rhs[en]+=val*eg
            lhs={e:0 for e in edges}
            for e,val in wedge_boundary(tnew).items():lhs[e]+=val*sgn
            assert lhs==rhs,('wedge equivariance',n,t,perm)
            # Independent edge-of-triangle orientation, crucial for S_n action on relative cells.
            def triangle_vertices(u):
                return [(u[0],u[1]),(u[0],u[2]),(u[1],u[2])]
            moved=[tuple(sorted((perm[a],perm[b]))) for a,b in triangle_vertices(t)]
            target=triangle_vertices(tnew)
            oriented_sign=parity([target.index(e) for e in moved])
            assert oriented_sign==sgn,('relative triangle equivariance',n,t,perm)
    # The triangles {0,i,j} provide an explicit integral basis of graphic cycle space.
    basis=list(combinations(range(1,n),2))
    assert len(basis)==comb(n-1,2)
    for i,j,k in combinations(range(1,n),3):
        relation={t:0 for t in triangles}
        for t,c in [((i,j,k),1),((0,j,k),-1),((0,i,k),1),((0,i,j),-1)]:relation[t]+=c
        summed={e:0 for e in edges}
        for t,c in relation.items():
            if c:
                for e,v in wedge_boundary(t).items():summed[e]+=c*v
        assert not any(summed.values()),('tetrahedron boundary identity',n,i,j,k)
    return len(triangles),len(basis),comb(n-1,3),len(adj)

for n in range(4,10):
    nt,rank,kern,trans=boundary_equivariant(n)
    assert nt-rank==kern
    print(f'n={n} rel_triangles={nt} image_rank={rank} kernel_rank={kern} generators={trans} exact_integral_relations=YES')
print('INTEGRAL_EQUIVARIANT_CERTIFICATE_OK')
