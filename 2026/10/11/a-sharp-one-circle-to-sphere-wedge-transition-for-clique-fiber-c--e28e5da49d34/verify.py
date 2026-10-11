"""Finite combinatorial checks for complete-fiber cyclic Vietoris--Rips theorem.
Run with Python >=3.9 standard library only: python verify.py
No unprovided data files are required.
"""
from itertools import combinations


def cyclic(a,b,n):
    d=abs(a-b)
    return min(d,n-d)


def complex_faces(m,n,r):
    vertices=[(i,j) for i in range(n) for j in range(m)]
    # Independent forward clique enumeration from the metric adjacency matrix.
    adj=[set() for _ in vertices]
    for u in range(len(vertices)):
        for v in range(u+1,len(vertices)):
            i,a=vertices[u];j,b=vertices[v]
            if cyclic(i,j,n)+(a!=b)<=r:
                adj[u].add(v)
                adj[v].add(u)
    faces=[]
    def explore(clique,candidates):
        for idx,v in enumerate(candidates):
            child=clique+(v,)
            faces.append(frozenset(child))
            explore(child,[w for w in candidates[idx+1:] if w in adj[v]])
    explore((),list(range(len(vertices))))
    assert len(faces)==len(set(faces))
    return vertices,faces


def model_cover(m,n,r):
    # B=complete-fiber lift of VR(C_n;r-1); F=one interval simplex per distance-r pair.
    cols=[{m*i+a for a in range(m)} for i in range(n)]
    B=[]
    # Build all maximal candidate carrier simplices, not their subfaces.
    # Every clique of columns at circular diameter <= r-1 is contained in a
    # consecutive r-column window when n>=3r, by elementary gap counting.
    B=[frozenset().union(*(cols[(i+j)%n] for j in range(r))) for i in range(n)]
    F=[]
    for i in range(n):
        for a in range(m):
            mask={m*i+a,m*((i+r)%n)+a}
            mask.update(v for j in range(1,r) for v in cols[(i+j)%n])
            F.append(frozenset(mask))
    T=[]
    if n==3*r:
        for i in range(r):
            for a in range(m):
                T.append(frozenset({m*i+a,m*((i+r)%n)+a,m*((i+2*r)%n)+a}))
    return B,F,T


def homology_mod2(faces):
    by_size={}
    for face in faces:by_size.setdefault(len(face),[]).append(tuple(sorted(face)))
    rank={0:0}
    for k in sorted(by_size):
        if k==1:continue
        pos={face:i for i,face in enumerate(by_size[k-1])}
        pivots={}
        for face in by_size[k]:
            bits=0
            for j in range(k):bits^=1<<pos[face[:j]+face[j+1:]]
            while bits:
                piv=bits.bit_length()-1
                if piv in pivots:bits^=pivots[piv]
                else:pivots[piv]=bits;break
        rank[k-1]=len(pivots)
    out={d-1:len(by_size[d])-rank.get(d-1,0)-rank.get(d,0) for d in by_size}
    out[0]-=1
    return {k:v for k,v in out.items() if v}


def test(m,r,n,check_homology):
    vertices, faces=complex_faces(m,n,r)
    B,F,T=model_cover(m,n,r)
    carriers=B+F+T
    for face in faces:
        assert any(face<=c for c in carriers),(m,r,n,face)
    # No carrier contains an illegal simplex.
    for carrier in carriers:
        assert all(cyclic(vertices[u][0],vertices[v][0],n) +
                   (vertices[u][1]!=vertices[v][1])<=r for u,v in combinations(carrier,2)),(m,r,n,carrier)
    # All faces containing a distance-r pair have a UNIQUE pair unless
    # they are one of the exceptional full equilateral triangles.
    equilateral={t for t in T}
    for face in faces:
        far=[]
        for u,v in combinations(face,2):
            a,i=vertices[u];b,j=vertices[v]
            if cyclic(a,b,n)==r:
                assert i==j
                far.append((u,v))
        if len(far)>1:assert face in equilateral,(m,r,n,face,far)
    if check_homology:
        observed=homology_mod2(faces)
        predicted={2:m*r-1} if n==3*r else {1:1}
        assert observed==predicted,(m,r,n,observed,predicted)
    return len(faces),len(B),len(F),len(T)


def main():
    tests=[(2,2,6),(3,2,6),(4,2,6),(2,2,7),(3,2,7),(4,2,7),
           (2,2,8),(3,2,8),(2,3,9),(3,3,9),(2,3,10),(3,3,10),
           (2,3,11),(3,3,11),(2,4,12),(2,4,13)]
    checks=0
    for m,r,n in tests:
        counts=test(m,r,n,True)
        print('OK',m,r,n,'faces',counts[0], 'B,F,T carriers',counts[1:],flush=True)
        checks+=1
    print('VERIFY_OK',checks,'exhaustive clique-cover and homology checks')

if __name__=='__main__':main()
