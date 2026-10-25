#!/usr/bin/env python3
"""Exact finite checks for a translation action on critical toroidal-grid Rips complexes.

Run: python3 verify.py  [with morse_certificate.json in the same directory]
No third-party dependencies.  The infinite-family character proof is mathematical;
the finite checks and the independent Morse certificate cover its first case.
"""
import collections
import itertools
import json
from pathlib import Path


def complex_faces(k):
    n = 3*k
    nv = n*n
    def distance(u,v):
        a,b = divmod(u,n)
        c,d = divmod(v,n)
        return min((a-c)%n,(c-a)%n)+min((b-d)%n,(d-b)%n)
    adj = [{v for v in range(nv) if v != u and distance(u,v) <= k} for u in range(nv)]
    faces = []
    def extend(prefix,candidates):
        for i,v in enumerate(candidates):
            f = prefix+(v,)
            faces.append(f)
            extend(f,[w for w in candidates[i+1:] if w in adj[v]])
    extend((),list(range(nv)))
    faces.sort(key=lambda f:(len(f),f))
    return faces


def check_morse(faces):
    cert = json.loads((Path(__file__).resolve().parent/'morse_certificate.json').read_text(encoding='utf-8'))
    pairs = cert['pairs']
    critical = cert['critical_indices']
    N=len(faces)
    assert len(pairs)==432 and len(critical)==24
    face_index={face:i for i,face in enumerate(faces)}
    used=[]
    matched = set()
    for lo,hi in pairs:
        assert isinstance(lo,int) and isinstance(hi,int)
        assert 0<=lo<N and 0<=hi<N
        assert len(faces[hi])==len(faces[lo])+1 and set(faces[lo]).issubset(faces[hi])
        assert lo not in matched and hi not in matched
        matched.update((lo,hi))
    assert set(critical)==set(range(N))-matched
    count=collections.Counter(len(faces[i])-1 for i in critical)
    assert count=={0:1,2:23},count
    paired_set={(lo,hi) for lo,hi in pairs}
    downstream=[[] for _ in faces]
    indeg=[0]*N
    for hi,f in enumerate(faces):
        if len(f)<2:continue
        for subface in itertools.combinations(f,len(f)-1):
            lo=face_index[subface]
            if (lo,hi) in paired_set:src,dst=lo,hi
            else:src,dst=hi,lo
            downstream[src].append(dst);indeg[dst]+=1
    queue=collections.deque(i for i,d in enumerate(indeg) if d==0)
    visited=0
    while queue:
        v=queue.popleft();visited+=1
        for w in downstream[v]:
            indeg[w]-=1
            if indeg[w]==0:queue.append(w)
    assert visited==N,('Morse directed cycle',visited,N)
    print('MORSE_K2_FACES',N,'MATCHED_PAIRS',len(pairs),'CRITICAL',dict(count),'ACYCLIC',visited==N)


def moved_face(face,k,a,b):
    n=3*k
    return tuple(sorted(((u//n+a)%n)*n+(u%n+b)%n for u in face))


def oriented_sign(face,new_vertices):
    position={v:j for j,v in enumerate(sorted(new_vertices))}
    p=[position[v] for v in new_vertices]
    inversions=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
    return -1 if inversions%2 else 1


def check_characters(faces,k):
    n=3*k
    fvector=collections.Counter(len(f)-1 for f in faces)
    euler=sum((-1)**i*v for i,v in fvector.items())
    assert euler==6*k*k,(k,euler)
    observed={}
    for a in range(n):
        for b in range(n):
            lef=0
            fixed={}
            for f in faces:
                moved=moved_face(f,k,a,b)
                if moved==f:
                    translated=[((u//n+a)%n)*n+(u%n+b)%n for u in f]
                    s=oriented_sign(f,translated)
                    dim=len(f)-1
                    fixed[dim]=fixed.get(dim,0)+1
                    lef+=(-1)**dim*s
            trace=lef-1
            expected=(6*k*k-1 if a==b==0 else
                      3*k*k-1 if ((a in (k,2*k) and b==0) or (a==0 and b in (k,2*k)))
                      else -1)
            assert trace==expected,(k,a,b,trace,expected,fixed)
            if (a,b)!=(0,0):
                if expected==-1:assert not fixed,(k,a,b,fixed)
                else:assert fixed=={2:3*k*k},(k,a,b,fixed)
            observed[(a,b)]=trace
    assert sum(observed.values())==n*n,('trivial multiplicity',k)
    assert sum((int(u%3==0)+int(v%3==0)-int((u,v)==(0,0))) for u in range(n) for v in range(n))==6*k*k-1
    print('K',k,'VERTICES',n*n,'SIMPLEX_COUNTS',dict(sorted(fvector.items())),
          'EULER',euler,'TRANSLATION_TRACE_HISTOGRAM',dict(sorted(collections.Counter(observed.values()).items())))


def main():
    for k in (2,3):
        faces=complex_faces(k)
        if k==2:check_morse(faces)
        check_characters(faces,k)
    print('VERIFY_OK_CRITICAL_TORUS_TRANSLATION_MODULE')


if __name__=='__main__':main()
