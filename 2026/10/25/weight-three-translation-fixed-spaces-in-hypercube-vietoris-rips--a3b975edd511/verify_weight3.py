"""Standalone finite checks for translation-fixed weight-three hypercube Rips complexes."""
from itertools import combinations, product
from math import comb


def cube_edges(m):
    return [(u,u^(1<<k)) for u in range(1<<m) for k in range(m) if not ((u>>k)&1)]


def representatives():
    # Representatives of F_2^3 / <111>, canonical leading bit zero.
    return [0,1,2,3]


def orbit_vertices(n):
    m=n-3
    return [(u,w) for u in range(1<<m) for w in representatives()]


def distances_compatible(a,b):
    (u,w),(v,z)=a,b
    d=(u^v).bit_count()
    # An orbit is represented by (u,w) and (u,w xor 7).
    return d+max((w^z).bit_count(),(w^z^7).bit_count())<=3


def facets_predicted(n):
    m=n-3
    out=set()
    for u,v in cube_edges(m):
        for choices in product([u,v],repeat=4):
            out.add(frozenset((choices[w],w) for w in range(4)))
    return out


def boundary_rank(faces_low,faces_high):
    idx={f:i for i,f in enumerate(faces_low)}
    basis={}
    for f in faces_high:
        z=0
        for i in range(len(f)):
            z ^= 1<<idx[f[:i]+f[i+1:]]
        while z:
            p=z.bit_length()-1
            if p in basis:z ^= basis[p]
            else:
                basis[p]=z
                break
    return len(basis)


def maximal_cliques(vertices):
    """Exhaustive bitset Bron-Kerbosch enumeration without dependencies."""
    count=len(vertices)
    adjacent=[0]*count
    for a in range(count):
        for b in range(a+1,count):
            if distances_compatible(vertices[a],vertices[b]):
                adjacent[a] |= 1<<b
                adjacent[b] |= 1<<a
    result=[]
    def rec(chosen,p,x):
        if not p and not x:
            result.append(frozenset(vertices[i] for i in chosen))
            return
        pool=p|x
        if pool:
            u=max((i for i in range(count) if pool>>i&1),
                  key=lambda i:(adjacent[i]&p).bit_count())
            options=p & ~adjacent[u]
        else:
            options=p
        while options:
            bit=options & -options
            v=bit.bit_length()-1
            rec(chosen+(v,),p&adjacent[v],x&adjacent[v])
            p &= ~bit
            x |= bit
            options &= ~bit
    rec((),(1<<count)-1,0)
    return set(result)


def inspect(n):
    m=n-3
    verts=orbit_vertices(n)
    maximal=maximal_cliques(verts)
    expected=facets_predicted(n)
    assert maximal==expected, (n,len(maximal),len(expected),len(maximal^expected))
    assert all(len(c)==4 for c in maximal)
    simplices=[set() for i in range(4)]
    for f in maximal:
        seq=tuple(sorted(f))
        for k in range(1,5):
            for s in combinations(seq,k):simplices[k-1].add(s)
    faces=[sorted(x) for x in simplices]
    ranks=[0]+[boundary_rank(faces[k-1],faces[k]) for k in range(1,4)]+[0]
    betti=[len(faces[k])-ranks[k]-ranks[k+1] for k in range(4)]
    # Convert unreduced beta0 to reduced beta0
    betti[0]-=1
    v=1<<m
    e=m*(1<<(m-1))
    assert betti==[0,e-v+1,0,e], (n,betti,e,v)
    assert len(maximal)==14*e+v
    print(f'n={n}: {v} outside vertices, {e} outside edges; '
          f'{len(verts)} orbit vertices, {len(maximal)} tetrahedra; '
          f'face-counts={[len(x) for x in faces]}, reduced Betti={betti}')


if __name__=='__main__':
    for n in (4,5,6,7):inspect(n)
    print('WEIGHT3_TRANSLATION_FIXED_COMPLEX_VERIFIED')
