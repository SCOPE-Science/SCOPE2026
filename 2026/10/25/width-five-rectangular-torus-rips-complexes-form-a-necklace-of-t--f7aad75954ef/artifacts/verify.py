"""Reproducible exact checks for width-five cyclic grid Vietoris--Rips complexes.
Run: python3 verify.py [max_n]; Python standard library only.
"""
from itertools import combinations
from collections import Counter
import sys

def build(n):
    vertices=list(range(5*n)); adj={v:set() for v in vertices}
    for v in vertices:
        a,j=divmod(v,n)
        for w in range(v+1,5*n):
            b,k=divmod(w,n)
            if min(abs(a-b),5-abs(a-b))+min(abs(j-k),n-abs(j-k))<=2:
                adj[v].add(w)
    faces=set()
    def grow(prefix,possible):
        for x in sorted(possible):
            f=prefix+(x,);faces.add(f)
            grow(f,possible&adj[x])
    grow((),set(vertices))
    return faces

def test(n):
    faces=build(n)
    counts=Counter(map(len,faces))
    assert counts=={1:5*n,2:30*n,3:55*n,4:35*n,5:6*n},(n,counts)
    slabs=[{f for f in faces if {v%n for v in f}<={j,(j+1)%n}} for j in range(n)]
    for j,s in enumerate(slabs):
        assert Counter(map(len,s))=={1:10,2:35,3:50,4:25,5:2}
        V=set(v for f in s for v in f)
        forbidden={frozenset((v,w)) for v,w in combinations(sorted(V),2) if tuple(sorted((v,w))) not in s}
        assert len(forbidden)==10
        degree=Counter(v for e in forbidden for v in e)
        assert set(degree.values())=={2} and len(degree)==10
        graph={v:{w for e in forbidden for w in e if v in e and w!=v} for v in V}
        seen=set();stack=[next(iter(V))]
        while stack:
            x=stack.pop()
            if x not in seen:seen.add(x);stack.extend(graph[x]-seen)
        assert seen==V  # forbidden-pair graph is C10, hence slab is Ind(C10)
        assert len(slabs[j]&slabs[(j+1)%n])==31
        for k in range(n):
            if k not in (j,(j-1)%n,(j+1)%n):assert not (s&slabs[k])
    targets=set().union(*slabs)
    assert len(faces-targets)==40*n
    pairs=0
    for j in range(n):
        for a in range(5):
            B={a*n+(j-1)%n,a*n+(j+1)%n}
            v=a*n+j;p=((a-1)%5)*n+j;q=((a+1)%5)*n+j
            for T in ((p,q),(p,),(q,),()):
                lo=frozenset(B.union(T));hi=lo|{v}
                lo=tuple(sorted(lo));hi=tuple(sorted(hi))
                assert lo in faces and hi in faces and lo not in targets
                cofaces=[f for f in faces if len(f)>len(lo) and set(lo).issubset(f)]
                assert cofaces==[hi],(n,j,a,T,cofaces)
                faces.remove(lo);faces.remove(hi);pairs+=1
    assert faces==targets and pairs==20*n
    return counts,pairs

if __name__=='__main__':
    bound=int(sys.argv[1]) if len(sys.argv)>1 else 12
    for n in range(7,bound+1):
        counts,pairs=test(n)
        print('EXACT_COLLAPSE_OK',n,'face_vector',[counts[k] for k in range(1,6)],'elementary_pairs',pairs,flush=True)
    print('VERIFY_OK_WIDTH_FIVE_RECTANGULAR_TORUS_RIPS',flush=True)
