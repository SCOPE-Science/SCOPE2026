"""Reconstruct and check explicit scale-two simplicial collapses of grid quotients.

Python 3, standard library only. Executes finite consistency checks, not a
substitute for the all-parameter local-combinatorial proof.
"""
from collections import Counter, deque
from itertools import combinations


def check(m, n, twisted):
    assert m >= 7 and n >= 7
    N = m*n
    def idx(i, j):
        j %= n
        if i == m:
            return n-1-j if twisted else j
        if i == -1:
            return (m-1)*n+(n-1-j if twisted else j)
        return i*n+j
    def uv(v):
        return divmod(v,n)
    def at(v, dx, dy):
        i,j=uv(v)
        return idx(i+dx,j+dy)
    V=set(range(N))
    neigh={v:{at(v,1,0),at(v,-1,0),at(v,0,1),at(v,0,-1)} for v in V}
    assert all(len(x)==4 for x in neigh.values())
    assert all(u in neigh[v] for u in V for v in neigh[u])
    squares=[]
    for v in sorted(V):
        i,j=uv(v)
        squares.append((v,idx(i+1,j),idx(i+1,j+1),idx(i,j+1)))
    assert len({frozenset(q) for q in squares})==N
    # Distance-two graph: enumerate its maximal cliques independently.
    dist2={v:set(neigh[v]) | {w for x in neigh[v] for w in neigh[x]}-{v} for v in V}
    for v in V:
        dist2[v].discard(v)
    maxima=[]
    def bronk(R,P,X):
        if not P and not X:
            maxima.append(frozenset(R));return
        pivot=max(P|X, key=lambda v:len(P & dist2[v])) if P|X else None
        for v in list(P - (dist2[pivot] if pivot is not None else set())):
            bronk(R|{v},P & dist2[v],X & dist2[v]);P.remove(v);X.add(v)
    bronk(set(),set(V),set())
    proposed={frozenset({v}|neigh[v]) for v in V}|{frozenset(q) for q in squares}
    assert set(maxima)==proposed, (m,n,twisted,'unexpected maximal cliques')
    faces=set()
    for M in proposed:
        for k in range(1,len(M)+1):
            faces.update(frozenset(q) for q in combinations(M,k))
    initial=Counter(map(len,faces))
    target=set()
    for v in V:target.add(frozenset({v}))
    for v in V:
        for w in neigh[v]:target.add(frozenset({v,w}))
    for a,b,c,d in squares:
        for q in ((a,b,c),(a,c,d)):
            for k in range(1,4):
                target.update(frozenset(t) for t in combinations(q,k))
    assert target <= faces
    pair_counts=[]
    def remove(lo,hi):
        f=frozenset(lo); h=frozenset(hi)
        assert f in faces and h in faces and len(h)==len(f)+1 and f<h,(f,h)
        covers=[f|{v} for v in V-f if f|{v} in faces]
        assert covers==[h],(m,n,twisted,'not free',f,covers)
        faces.remove(f);faces.remove(h)
    # A. Each five-vertex centered simplex and its noncentral facet.
    for v in sorted(V):remove(neigh[v],{v}|neigh[v])
    pair_counts.append(N)
    # B. Its four remaining tetrahedra and their three-neighbor facets.
    for v in sorted(V):
        for q in combinations(sorted(neigh[v]),3):remove(q,{v}|set(q))
    pair_counts.append(4*N)
    # C. Remove each quadrilateral tetrahedron along one off-diagonal face.
    for a,b,c,d in squares:remove((a,b,d),(a,b,c,d))
    pair_counts.append(N)
    # D. Remove the other off-diagonal triangle with its diagonal edge.
    for a,b,c,d in squares:remove((b,d),(b,c,d))
    pair_counts.append(N)
    # E. Remove the horizontal and vertical straight distance-two edges.
    for v in sorted(V):
        l,r=at(v,-1,0),at(v,1,0)
        u,d=at(v,0,1),at(v,0,-1)
        remove((l,r),(l,v,r))
        remove((u,d),(u,v,d))
    pair_counts.append(2*N)
    assert faces==target,(m,n,twisted,'residual',len(faces-target))
    assert pair_counts==[N,4*N,N,N,2*N]
    assert initial==Counter({1:N,2:6*N,3:10*N,4:6*N,5:N}),initial
    assert Counter(map(len,faces))==Counter({1:N,2:3*N,3:2*N})
    # Independent boundary computation on the resulting triangulation.
    edges=sorted((tuple(sorted(e)) for e in target if len(e)==2))
    triangles=sorted((tuple(sorted(t)) for t in target if len(t)==3))
    e_index={e:i for i,e in enumerate(edges)}
    assert len(edges)==3*N and len(triangles)==2*N
    def boundary_rank(p):
        pivots={}
        for a,b,c in triangles:
            col={e_index[(b,c)]:1,e_index[(a,c)]:p-1,e_index[(a,b)]:1}
            while col:
                j=min(col)
                if j not in pivots:
                    inv=pow(col[j],-1,p)
                    pivots[j]={k:(x*inv)%p for k,x in col.items() if (x*inv)%p}
                    break
                mult=col[j]
                for k,x in pivots[j].items():
                    z=(col.get(k,0)-mult*x)%p
                    if z:col[k]=z
                    else:col.pop(k,None)
        return len(pivots)
    r2=boundary_rank(2);r3=boundary_rank(3)
    b1_2=len(edges)-(N-1)-r2
    b2_2=len(triangles)-r2
    b1_3=len(edges)-(N-1)-r3
    b2_3=len(triangles)-r3
    assert (b1_2,b2_2)==(2,1)
    assert (b1_3,b2_3)==((1,0) if twisted else (2,1))
    print(f'm={m} n={n} twisted={twisted}: facets=({N} stars,{N} squares), '
          f'collapses={sum(pair_counts)}, final=(V={N},E={3*N},F={2*N}), '
          f'GF2-H=(2,1), GF3-H=({b1_3},{b2_3})')


if __name__=='__main__':
    for twisted in (True,False):
        for m,n in ((7,7),(7,8),(8,9),(9,10)):
            check(m,n,twisted)
    print('VERIFY_OK')
