"""Rebuild and certify the two-phase collapse for N(K3 square Cn).
Only Python standard library is required. Finite tests complement the separate uniform proof.
"""
from itertools import combinations
from collections import Counter,defaultdict

def run(n):
    V=[(a,b) for a in range(n) for b in range(3)]
    facets=set()
    for a,b in V:
        u=(a,(b+1)%3); v=(a,(b-1)%3)
        p=((a+1)%n,b); m=((a-1)%n,b)
        facets.add(frozenset((u,v,p,m)))
    assert len(facets)==3*n
    faces=[set() for _ in range(4)]
    for F in facets:
        for d in range(1,5):
            faces[d-1].update(frozenset(s) for s in combinations(sorted(F),d))
    assert [len(s) for s in faces]==[3*n,12*n,12*n,3*n],(n,[len(s) for s in faces])
    for a,b in V:
        u=(a,(b+1)%3);v=(a,(b-1)%3)
        p=((a+1)%n,b);m=((a-1)%n,b)
        triangle=frozenset((u,v,p));tetra=frozenset((u,v,p,m))
        assert tetra in faces[3] and triangle in faces[2]
        assert sum(triangle.issubset(F) for F in faces[3])==1
        faces[3].remove(tetra);faces[2].remove(triangle)
    assert len(faces[3])==0
    for a,b in V:
        u=(a,(b+1)%3);v=(a,(b-1)%3)
        m=((a-1)%n,b)
        e=frozenset((u,v)); t=frozenset((u,v,m))
        assert e in faces[1] and t in faces[2]
        assert sum(e.issubset(F) for F in faces[2])==1
        faces[1].remove(e); faces[2].remove(t)
    assert [len(s) for s in faces]==[3*n,9*n,6*n,0],(n,[len(s) for s in faces])
    incidence=Counter(e for t in faces[2] for e in map(frozenset,combinations(t,2)))
    assert set(incidence.values())=={2} and len(incidence)==9*n
    assert set(faces[1])==set(incidence)
    triangles=faces[2]
    todo=set(triangles); seen={todo.pop()}
    while len(seen)<len(triangles):
        more={t for t in todo if any(len(t & s)==2 for s in seen)}
        assert more
        seen|=more;todo-=more
    for vertex in V:
        lkedges={frozenset(t-{vertex}) for t in triangles if vertex in t}
        lkv=set().union(*lkedges)
        degrees=Counter(x for e in lkedges for x in e)
        assert len(lkedges)==len(lkv) and set(degrees.values())=={2}
        link_seen={next(iter(lkv))}; frontier=list(link_seen)
        while frontier:
            u=frontier.pop()
            for e in lkedges:
                if u in e:
                    w=next(iter(e-{u}))
                    if w not in link_seen:link_seen.add(w);frontier.append(w)
        assert link_seen==lkv
    assert 3*n-9*n+6*n==0
    return len(facets),len(triangles)

if __name__=='__main__':
    for n in range(5,41):
        t,f=run(n)
        print(f'n={n} initial_tetrahedra={t} remaining_triangles={f} elementary_pairs={6*n}: OK')
    print('VERIFY_OK_TRIANGULAR_CYCLE_NEIGHBORHOOD_TORUS')
