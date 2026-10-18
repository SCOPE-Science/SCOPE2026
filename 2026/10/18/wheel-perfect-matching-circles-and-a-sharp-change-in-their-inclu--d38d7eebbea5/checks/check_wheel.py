"""Standalone finite verification for odd-rim wheel perfect-matching complexes.
No dependency on earlier calculations. Python 3 standard library only.
"""
from itertools import combinations
from collections import Counter

def wheel(r):
    N=2*r+1
    v=N  # hub
    edges=[(i,(i+1)%N) for i in range(N)]+[(i,v) for i in range(N)]
    edges=[tuple(sorted(e)) for e in edges]
    return N,edges

def perfect_matchings(nvertices,edges):
    inc={i:[] for i in range(nvertices)}
    for j,(a,b) in enumerate(edges):inc[a].append((b,j)); inc[b].append((a,j))
    def rec(rem,cur):
        if not rem:
            yield frozenset(cur);return
        u=min(rem)
        for v,j in inc[u]:
            if v in rem:
                yield from rec(rem-{u,v},cur+[j])
    return sorted(set(rec(set(range(nvertices)),[])))

def allfaces(facets):
    faces={frozenset()}
    for f in facets:
        for k in range(1,len(f)+1):
            faces.update(map(frozenset,combinations(sorted(f),k)))
    return faces

def nerve_from_facets(facets):
    m=len(facets)
    # all subsets sharing a graph edge
    maxnerve=[]
    for e in set().union(*facets):
        maximal=frozenset(i for i,f in enumerate(facets) if e in f)
        if maximal: maxnerve.append(maximal)
    return allfaces(maxnerve),maxnerve

def cyclicfaces(N,k):
    fs=[frozenset((i+j)%N for j in range(k)) for i in range(N)]
    return allfaces(fs),fs

def sgn(xs,ys):
    a=[ys.index(z) for z in xs]
    return (-1)**sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))

def lefschetz(faces,perm):
    L=0
    for face in faces:
        if not face:continue
        img=[perm[i] for i in sorted(face)]
        if set(img)==face:
            L+=(-1)**(len(face)-1)*sgn(img,sorted(face))
    return L

def run(lo=2,hi=8):
    for r in range(lo,hi+1):
        N,edges=wheel(r)
        f=perfect_matchings(N+1,edges)
        assert len(f)==N and all(len(x)==r+1 for x in f)
        spans=[]
        for i in range(N):
            pred={N+i}
            for j in range(r):
                a=(i+2*j+1)%N;b=(i+2*j+2)%N
                pred.add(edges.index(tuple(sorted((a,b)))))
            spans.append(frozenset(pred))
        assert set(f)==set(spans)
        Nf,ne=nerve_from_facets(spans)
        cf,fa=cyclicfaces(N,r)
        # Cyclic change of vertex names t -> i+2*t gives all length-r facets
        relab=lambda face:frozenset((2*t)%N for t in face)
        assert {relab(F) for F in cf}==Nf
        remaining=Nf
        for k in range(r,2,-1):
            shorter,_=cyclicfaces(N,k-1)
            short={relab(F) for F in shorter}
            endpointedges=[frozenset(((2*i)%N,(2*(i+k-1))%N)) for i in range(N)]
            assert len(set(endpointedges))==N
            for e in endpointedges:
                carriers=[F for F in remaining if e<=F]
                # every free endpoint pair occurs in exactly one maximal k-face
                carriers_max=[F for F in carriers if len(F)==k]
                assert len(carriers_max)==1
            removed={F for F in remaining if any(e<=F for e in endpointedges)}
            assert remaining-removed==short
            remaining=short
        assert len([F for F in remaining if len(F)==2])==N
        allf=allfaces(spans)
        fc=dict(sorted(Counter(len(x)-1 for x in allf if x).items()))
        chi=sum((-1)**i*v for i,v in fc.items())
        assert chi==0
        # use full alternating fixed-simplex traces of C_2r+1 symmetry
        def makeperm(vtrans):
            return [edges.index(tuple(sorted((vtrans(a),vtrans(b))))) for a,b in edges]
        rot=makeperm(lambda i:(i+1)%N if i<N else N)
        ref=makeperm(lambda i:(-i)%N if i<N else N)
        Lrot=lefschetz(allf,rot)
        Lref=lefschetz(allf,ref)
        assert (Lrot,Lref)==(0,2)
        # Independently check every rotation and reflection of the wheel.
        for a in range(N):
            rr=makeperm(lambda i:(i+a)%N if i<N else N)
            ss=makeperm(lambda i:(a-i)%N if i<N else N)
            assert lefschetz(allf,rr)==0, ('rotation',r,a)
            assert lefschetz(allf,ss)==2, ('reflection',r,a)
        if r==2:
            allordinary={frozenset()}|{frozenset((j,)) for j in range(len(edges))}
            allordinary.update(frozenset((j,k)) for j in range(len(edges)) for k in range(j+1,len(edges)) if len(set(edges[j]+edges[k]))==4)
            allordinary.update(F for F in allf if len(F)==3)
            assert all(F in allf for F in allordinary if len(F)==3)
            assert len({F for F in allordinary if len(F)==2}-allf)==5
            assert len(allordinary)==36
        print(f'r={r} rim={N} perfect_matchings={len(f)} faces={len(allf)-1} dimension={r} nerve_faces={len(Nf)-1} collapses={r-2} Euler={chi} rotation_L={Lrot} reflection_L={Lref}')
    print('ALL_WHEEL_CHECKS_PASS')
if __name__=='__main__':run()
