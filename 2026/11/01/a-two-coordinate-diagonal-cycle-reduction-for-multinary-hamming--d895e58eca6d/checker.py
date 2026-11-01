#!/usr/bin/env python3
"""Independent finite test of the diagonal cyclic fixed-Rips orbit criterion.

For q>=3, n>=2, and integer r, directly reconstruct all C_q vertex
orbits of the q-ary n-cube and check clique conditions against the
proposed lower-dimensional Rips criterion.  No external dependencies.
"""
from itertools import product, combinations


def hdist(x, y):
    return sum(a != b for a, b in zip(x,y))


def check(q,n):
    assert q>=3 and n>=2
    m=n-2
    # Entire orbits under (x_0,x_1) -> (x_0+1,x_1+1).
    verts = list(product(range(q),repeat=m+1))
    orbit={v: tuple((t,(v[0]+t)%q)+v[1:] for t in range(q)) for v in verts}
    assert len(verts)==q**(n-1)
    for r in range(n+1):
        good={v: all(hdist(a,b)<=r for a,b in combinations(orbit[v],2)) for v in verts}
        assert all(v_good == (r>=2) for v_good in good.values()),(q,n,r,'orbit diameter')
        if r<2:
            continue
        for v,w in combinations(verts,2):
            d=max(hdist(a,b) for a in orbit[v] for b in orbit[w])
            expected=2+hdist(v[1:],w[1:])
            assert d==expected,(q,n,r,v,w,d,expected)
            assert (d<=r)==(hdist(v[1:],w[1:])<=r-2)
    print('PASS q=%d n=%d orbit_vertices=%d max_r=%d' %(q,n,len(verts),n))

if __name__=='__main__':
    for q,n in [(3,2),(3,3),(3,4),(3,5),(4,2),(4,3),(4,4),(5,2),(5,3),(5,4)]:
        check(q,n)
    print('ALL_EXACT_ORBIT_COMPARISONS_PASSED')


def gf2_rank(vectors):
    pivots={}
    for v in vectors:
        while v:
            p=v.bit_length()-1
            if p in pivots:
                v^=pivots[p]
            else:
                pivots[p]=v
                break
    return len(pivots)


def quotient_homology_mod2(q,n,r):
    # Enumerate all orbit vertices and all faces of the actual fixed-point complex.
    reps=list(product(range(q),repeat=n-1))
    orbits=[[(t,(t+v[0])%q)+v[1:] for t in range(q)] for v in reps]
    if r<2: return None
    adj=[set() for _ in reps]
    for i in range(len(reps)):
        for j in range(i+1,len(reps)):
            if all(hdist(a,b)<=r for a in orbits[i] for b in orbits[j]):
                adj[i].add(j);adj[j].add(i)
    # enumerate graph cliques by increasing vertex labels, without using projection.
    faces={0:[]}
    def grow(tup,common):
        if tup: faces.setdefault(len(tup)-1,[]).append(tup)
        for v in sorted(common):
            grow(tup+(v,), {w for w in common if w>v and w in adj[v]})
    grow((),set(range(len(reps))))
    ranks={}
    for k in range(1,max(faces)+1):
        prev={s:i for i,s in enumerate(faces[k-1])}
        columns=[]
        for s in faces[k]:
            col=0
            for i in range(len(s)):
                col ^= 1<<prev[s[:i]+s[i+1:]]
            columns.append(col)
        ranks[k]=gf2_rank(columns)
    betti={}
    for k,ff in faces.items():
        b=len(ff)-ranks.get(k,0)-ranks.get(k+1,0)
        if k==0:b-=1
        if b:betti[k]=b
    return betti, {str(k):len(v) for k,v in faces.items()}


if __name__=='__main__':
    for r,expected in ((2,{0:8}),(3,{1:4})):
        got, f=quotient_homology_mod2(3,4,r)
        assert got==expected,(r,got,expected)
        print('MOD2_OK ternary-n4 r=%d betti=%s f=%s'%(r,got,f))
    print('ALL_HOMOLOGY_CHECKS_PASSED')


def check_binary_boundary():
    # Sharp boundary: with q=2,n=3,r=2, four orbit vertices form C_4,
    # whereas the lower-dimensional r=0 complex has two isolated vertices.
    q,n,r=2,3,2
    reps=list(product(range(q),repeat=n-1))
    orbits=[[(t,(t+v[0])%q,v[1]) for t in range(q)] for v in reps]
    adj={i:set() for i in range(4)}
    for i,j in combinations(range(4),2):
        if all(hdist(a,b)<=r for a in orbits[i] for b in orbits[j]):
            adj[i].add(j);adj[j].add(i)
    assert all(len(s)==2 for s in adj.values())
    assert len({frozenset((i,j)) for i in adj for j in adj[i]})==4
    assert not any(all(b in adj[a] for a,b in combinations(trip,2)) for trip in combinations(range(4),3))
    print('BINARY_BOUNDARY_OK q=2 n=3 r=2 fixed_orbit_graph=C4')


if __name__=='__main__':
    check_binary_boundary()
