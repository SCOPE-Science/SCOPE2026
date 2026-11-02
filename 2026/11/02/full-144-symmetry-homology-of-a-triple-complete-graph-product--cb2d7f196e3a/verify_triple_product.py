#!/usr/bin/env python3
"""Exact rational character of the independence complex of K2 x K3 x K3.

Uses signed Lefschetz traces, the published integral homotopy concentration,
and an independent finite-field homology diagnostic. Standard library only.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import permutations, product
from math import factorial

N=18
P=tuple(permutations(range(3)))
VERTICES=tuple(product(range(2),range(3),range(3)))
INDEX={v:i for i,v in enumerate(VERTICES)}
ADJ=tuple(sum(1<<j for j,w in enumerate(VERTICES)
              if all(a!=b for a,b in zip(v,w))) for v in VERTICES)

def action(p,q,t,k):
    return tuple(INDEX[(a^t,p[j] if k else p[i],q[i] if k else q[j])]
                 for a,i,j in VERTICES)

def graph_action_ok(g):
    return len(set(g))==N and all(
        bool(ADJ[i] & (1<<j))==bool(ADJ[g[i]] & (1<<g[j]))
        for i in range(N) for j in range(i+1,N))

def orbit_character(g):
    # A g-fixed oriented simplex is a union of g-orbits of vertices.
    seen=set();orbits=[]
    for i in range(N):
        if i in seen:continue
        orbit=[];j=i
        while j not in seen:
            seen.add(j);orbit.append(j);j=g[j]
        assert j==i
        orbits.append(orbit)
    good=[]
    for orbit in orbits:
        if all(not(ADJ[a] & (1<<b)) for z,a in enumerate(orbit)
               for b in orbit[z+1:]):
            good.append(orbit)
    d=len(good);neighborhood=[1<<i for i in range(d)]
    for i in range(d):
        for j in range(i+1,d):
            if any(ADJ[a] & (1<<b) for a in good[i] for b in good[j]):
                neighborhood[i]|=1<<j
                neighborhood[j]|=1<<i
    @lru_cache(None)
    def alternating(mask):
        if mask==0:return 1
        v=max((j for j in range(d) if mask>>j&1),
              key=lambda j:(neighborhood[j]&mask).bit_count())
        return alternating(mask^(1<<v))-alternating(mask&~neighborhood[v])
    # Since all reduced homology lies in degree 3, chi_H3=I_orbits(-1).
    return alternating((1<<d)-1)

def s3char(p,kind):
    fix=sum(p[i]==i for i in range(3))
    if kind=='1':return 1
    if kind=='W':return fix-1
    assert kind=='sgn'
    return (-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))

def mod2_boundary_ranks():
    # Independent simplices enumerated once, then column elimination over F2.
    faces=defaultdict(list)
    for mask in range(1,1<<N):
        if all(not(ADJ[i] & (mask^(1<<i))) for i in range(N) if mask>>i&1):
            faces[mask.bit_count()-1].append(mask)
    assert sum(map(len,faces.values()))==1649
    ranks={}
    for d in range(1,max(faces)+1):
        targets={face:i for i,face in enumerate(faces[d-1])}
        pivots={}
        for face in faces[d]:
            col=0;bits=face
            while bits:
                b=bits&-bits;bits-=b
                col^=1<<targets[face^b]
            while col:
                p=col.bit_length()-1
                if p in pivots:col^=pivots[p]
                else:
                    pivots[p]=col;break
        ranks[d]=len(pivots)
    betti={d:len(faces[d])-ranks.get(d,0)-ranks.get(d+1,0)
           for d in faces}
    assert betti=={0:1,1:0,2:0,3:14,4:0,5:0,6:0,7:0,8:0},betti
    return {d:len(faces[d]) for d in faces},ranks,betti

def main():
    perms={}
    for p in P:
        for q in P:
            for t in range(2):
                for k in range(2):
                    g=action(p,q,t,k)
                    assert graph_action_ok(g)
                    assert g not in perms
                    perms[g]=(p,q,t,k)
    assert len(perms)==144
    traces={(p,q,t,k):orbit_character(action(p,q,t,k))
            for p in P for q in P for t in range(2) for k in range(2)}
    id3=(0,1,2)
    assert traces[id3,id3,0,0]==14
    assert traces[id3,id3,1,0]==4
    assert traces[id3,id3,0,1]==-4
    assert traces[id3,id3,1,1]==-2
    assert sum(traces.values())==0
    assert sum(value for (p,q,t,k),value in traces.items() if k==0)==72
    # Multiplicities for C2 (layer) x S3 x S3, via character orthogonality.
    expected={(1,'1','1'):1,(1,'1','W'):1,(1,'W','1'):1,
              (1,'W','W'):1,(-1,'sgn','sgn'):1,
              (-1,'sgn','W'):1,(-1,'W','sgn'):1}
    found={}
    for ep in (1,-1):
        for U in ('1','sgn','W'):
            for V in ('1','sgn','W'):
                numer=sum(ep**t*s3char(p,U)*s3char(q,V)*traces[p,q,t,0]
                          for p in P for q in P for t in range(2))
                assert numer%72==0
                m=numer//72
                if m:found[ep,U,V]=m
    assert found==expected,(found,expected)
    # Exchange action on the three diagonal isotypic components.
    # Rank of central projector times exchange trace, using all group elements.
    for ep,U,trace_expected in ((1,'1',-1),(1,'W',-2),(-1,'sgn',-1)):
        dim=s3char(id3,U)
        numer=sum(ep**t*s3char(p,U)*s3char(q,U)*traces[p,q,t,1]
                  for p in P for q in P for t in range(2))
        assert dim*dim*numer%72==0
        assert dim*dim*numer//72==trace_expected
    counts,ranks,betti=mod2_boundary_ranks()
    print('TRIPLE_PRODUCT_144_EXACT_CHARACTER_AND_PROJECTORS_OK')
    print('graph automorphisms represented:',len(perms))
    print('simplices by degree:',counts)
    print('mod-two homology:',betti)
    print('rational homology constituents:',found)
    print('coordinate subgroup invariants:',1,'full-group invariants:',0)

if __name__=='__main__':main()
