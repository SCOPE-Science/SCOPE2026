"""Standalone exact graph-Rips and elementary-collapse verification."""
from __future__ import annotations
import itertools,collections,json
from pathlib import Path

HERE=Path(__file__).resolve().parent

def distances_and_faces(n):
    m=2*n
    G=[{(i-1)%m,(i+1)%m,(i+n)%m} for i in range(m)]
    B=[{i}|G[i]|set().union(*(G[t] for t in G[i])) for i in range(m)]
    F=set()
    # Independent exhaustive clique generator, no graph packages.
    def visit(face,candidates):
        for i,v in enumerate(candidates):
            nxt=face+(v,)
            F.add(nxt)
            visit(nxt,[w for w in candidates[i+1:] if w in B[v]])
    visit((),list(range(m)))
    return G,B,F

def fixed_lefschetz(faces,n,a,b):
    m=2*n
    def act(v):return (a+(-v if b else v))%m
    total=0
    for s in faces:
        image=[act(v) for v in s]
        if set(image)!=set(s):continue
        inversions=sum(image[i]>image[j] for i in range(len(image)) for j in range(i+1,len(image)))
        total+=(-1 if inversions%2 else 1)*(-1 if (len(s)-1)%2 else 1)
    return total

def test_small():
    G,B,F=distances_and_faces(5)
    count=collections.Counter(len(s)-1 for s in F)
    assert dict(sorted(count.items()))=={0:10,1:35,2:50,3:25,4:2},count
    cert=json.loads((HERE/'collapse_n5.json').read_text())
    remaining=F.copy()
    for z,(sa,sb) in enumerate(cert['pairs']):
        a,b=tuple(sa),tuple(sb)
        assert len(a)+1==len(b) and a in remaining and b in remaining,(z,a,b)
        assert set(a)<set(b)
        cofaces=[t for t in remaining if set(a).issubset(t) and len(t)>len(a)]
        assert cofaces==[b],(z,a,b,cofaces)
        remaining.remove(a);remaining.remove(b)
    verts=cert['boundary_vertices'];opposite={tuple(e) for e in cert['opposite_pairs']}
    target={c for k in range(1,len(verts)+1) for c in itertools.combinations(verts,k)
            if all(pair not in opposite for pair in itertools.combinations(c,2))}
    assert remaining==target and len(remaining)==26,(len(remaining),len(target))
    assert len(cert['pairs'])==48
    for a in range(10):
        for b in (0,1):
            L=fixed_lefschetz(F,5,a,b)
            expected=1+(-1)**(a+b)
            assert L==expected,(a,b,L,expected)
    print('N5:',dict(sorted(count.items())),'48 exact collapses -> octahedral S2; 20 Lefschetz checks')

def validate_cover(n):
    G,B,F=distances_and_faces(n)
    def band(i):return {(i-1)%n,i%n,(i+1)%n}
    bands=[band(i) for i in range(n)]
    supports=[set(v%n for v in s) for s in F]
    assert all(any(s<=bb for bb in bands) for s in supports),(n,'coverage')
    # For all nonempty intersections, test the induced graph is complete.
    for c in itertools.chain.from_iterable(itertools.combinations(range(n),k) for k in range(1,5)):
        common=set.intersection(*(bands[i] for i in c))
        vertices=[v for v in range(2*n) if v%n in common]
        if not common or len(c)==1:continue
        assert all(w in B[v] for v,w in itertools.combinations(vertices,2)),(n,c,vertices)
    # Nerve exactly triangles of three consecutive centers and edges of distance <=2.
    nerve={c for k in range(1,n+1) for c in itertools.combinations(range(n),k)
           if set.intersection(*(bands[i] for i in c))}
    expected={c for k in (1,2) for c in itertools.combinations(range(n),k)
              if k==1 or min((c[1]-c[0])%n,(c[0]-c[1])%n)<=2}
    expected.update(tuple(sorted({(i-1)%n,i,(i+1)%n})) for i in range(n))
    assert nerve==expected,(n,len(nerve),len(expected))
    # Nerve elementary collapses along each distance-two chord.
    remains=nerve.copy()
    for i in range(n):
        edge=tuple(sorted({(i-1)%n,(i+1)%n}));triangle=tuple(sorted({(i-1)%n,i,(i+1)%n}))
        assert edge in remains and triangle in remains
        assert [c for c in remains if len(c)>2 and set(edge)<set(c)]==[triangle]
        remains.remove(edge);remains.remove(triangle)
    assert len(remains)==2*n
    assert all(len(t)<3 for t in remains)
    for t in remains:
        if len(t)==2:assert min(t[1]-t[0],n-(t[1]-t[0]))==1
    return len(F)

def main():
    for n in (3,4):
        G,B,F=distances_and_faces(n)
        assert all(v in B[u] for u in range(2*n) for v in range(2*n))
        assert len(F)==2**(2*n)-1
    print('N3,N4: diameter two, full simplices')
    test_small()
    for n in range(6,14):
        size=validate_cover(n)
        print('N',n, 'faces',size,'good cover and nerve collapse verified',sep='')
    print('ALL_CHECKS_PASS')
if __name__=='__main__':main()
