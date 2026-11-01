#!/usr/bin/env python3
"""Exact finite homotopy certificates for neighborhood complexes of stable-set graphs.

Usage: python verify.py
Dependency: sympy >= 1.12. All enumeration, incidence and integer checks are repeated.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations
from random import Random
from sympy import zeros
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def models(k):
    n = 3*k + 2
    # Enumerate all k-element independent sets by testing the actual graph edges.
    states = []
    for a in combinations(range(n), k):
        if any(min((j-i) % n, (i-j) % n) <= 2
               for i,j in combinations(a, 2)):
            continue
        states.append(sum(1 << i for i in a))
    # Independently check cyclic-gap characterization and its exact count.
    by_gaps = []
    for a in combinations(range(n), k):
        if all((a[(j+1)%k]-a[j]) % n >= 3 for j in range(k)):
            by_gaps.append(sum(1 << i for i in a))
    assert states == by_gaps
    assert len(states) == n*(k+1)//2
    # Vertices of H are these states; two are adjacent iff disjoint.
    adj = [sum(1 << j for j,b in enumerate(states) if i != j and a&b == 0)
           for i,a in enumerate(states)]
    for i,row in enumerate(adj):
        for j in range(len(states)):
            assert bool(row >> j & 1) == bool(adj[j] >> i & 1)
    return states, adj


def complex_faces(adj):
    # A face has a common neighbor iff contained in the open neighborhood of
    # at least one vertex. Enumerate every subset of every neighborhood.
    F = {0}
    for nbhd in adj:
        s = nbhd
        while s:
            F.add(s)
            s = (s-1) & nbhd
    assert len(F) == sum(1 for _ in F)
    # Verify the defining common-neighbor condition directly for every face.
    for f in F:
        if f:
            assert any((f & nbhd) == f for nbhd in adj)
    # And all codimension-one faces must be present.
    for f in F:
        s=f
        while s:
            x=s&-s;s-=x
            assert f^x in F
    return F


def bdry(q):
    s=q; sign=1
    while s:
        bit=s & -s;s-=bit
        yield q^bit, sign
        sign=-sign


def matching(F, n):
    # Deterministic maximal-pair vertex toggling, with a fixed tie breaker.
    # The result is independently certified by a complete directed-Hasse DAG.
    remaining = set(F)
    pairs=[];order=[]
    rng=Random(0)
    for _ in range(n):
        choices=[]
        for v in range(n):
            if v in order:continue
            bit=1<<v
            count=sum(1 for q in remaining if not (q&bit) and q|bit in remaining)
            choices.append((count,rng.random(),v))
        if not choices:break
        _,_,v=max(choices)
        order.append(v)
        bit=1<<v
        newpairs=[(q,q|bit) for q in remaining
                  if not (q&bit) and q|bit in remaining]
        for lo,hi in newpairs:
            assert lo in remaining and hi in remaining
            remaining.remove(lo);remaining.remove(hi)
        pairs.extend(newpairs)
        if len(remaining)<30:break
    assert len(F)==2*len(pairs)+len(remaining)
    return remaining,pairs,order


def dag_check(F,pairs):
    up={a:b for a,b in pairs}
    assert len(up)==len(pairs)
    indeg=dict.fromkeys(F,0)
    incidences=0
    for b in F:
        for a,_ in bdry(b):
            assert a in F
            incidences+=1
            if up.get(a)==b:indeg[b]+=1  # Reverse the matched edge.
            else:indeg[a]+=1
    q=deque(x for x,v in indeg.items() if v==0)
    processed=0
    while q:
        b=q.popleft();processed+=1
        if b in up:
            a=up[b];indeg[a]-=1
            if indeg[a]==0:q.append(a)
        for a,_ in bdry(b):
            if up.get(a)==b:continue
            indeg[a]-=1
            if indeg[a]==0:q.append(a)
    assert processed==len(F),(processed,len(F))
    return incidences


def morse_boundary(critical,pairs):
    # Exact algebraic Morse projection, using signed gradient paths.
    critical=set(critical)
    lowers={a:(b,next(c for f,c in bdry(b) if f==a)) for a,b in pairs}
    uppers={b for _,b in pairs}
    dimensions=defaultdict(list)
    for s in critical:dimensions[s.bit_count()-1].append(s)
    for d in dimensions:dimensions[d].sort()
    @lru_cache(None)
    def project(q):
        if q in critical:return {q:1}
        if q in uppers:return {}
        b,sgn=lowers[q]
        out=defaultdict(int)
        for f,c in bdry(b):
            if f==q:continue
            for z,v in project(f).items():out[z]-=sgn*c*v
        return {z:v for z,v in out.items() if v}
    matrices={};diagonals={}
    for d in sorted(dimensions):
        if d-1 not in dimensions:continue
        rowindex={s:i for i,s in enumerate(dimensions[d-1])}
        M=zeros(len(rowindex),len(dimensions[d]))
        for j,s in enumerate(dimensions[d]):
            for f,c in bdry(s):
                for z,v in project(f).items():
                    assert z in rowindex
                    M[rowindex[z],j]+=c*v
        diag=smith_normal_form(M,domain=ZZ)
        entries=[abs(int(diag[i,i])) for i in range(min(diag.shape)) if diag[i,i]]
        matrices[d]=M;diagonals[d]=entries
    for d,M in matrices.items():
        if d-1 in matrices:
            assert matrices[d-1]*M == zeros(matrices[d-1].rows,M.cols)
    return {d:len(v) for d,v in dimensions.items()},diagonals


def run():
    target={
       2:({'vertices':12,'faces':911,'critical':{2:9,3:8},'smith':{3:[1]*7}},
          'S2veeS2veeS3'),
       3:({'vertices':22,'faces':16391,'critical':{2:8,3:13,4:5,5:1},
           'smith':{3:[1]*8,4:[1]*4,5:[1]}},'S3'),
       4:({'vertices':35,'faces':272861,'critical':{1:1,2:11,3:11},
           'smith':{2:[1],3:[1]*10}},'S3')
    }
    for k in (2,3,4):
        expected,homotopy=target[k]
        states,adj=models(k)
        F=complex_faces(adj)
        fvector=[sum(1 for x in F if x.bit_count()==q) for q in range(1,max(x.bit_count() for x in F)+1)]
        expected_fvectors={
            2:[12,66,204,304,228,84,12],
            3:[22,231,1133,2871,4301,4092,2519,979,220,22],
            4:[35,567,3920,14427,33502,53585,61684,52136,32459,14707,4704,1001,126,7]
        }
        assert fvector==expected_fvectors[k],(k,fvector)
        remaining,pairs,order=matching(F,len(states))
        inc=dag_check(F,pairs)
        critical,smith=morse_boundary(remaining,pairs)
        assert len(states)==expected['vertices']
        assert len(F)==expected['faces']
        assert critical==expected['critical'],(k,critical)
        assert smith==expected['smith'],(k,smith)
        homology={d:c-len(smith.get(d,[]))-len(smith.get(d+1,[])) for d,c in critical.items()}
        homology={d:r for d,r in homology.items() if r}
        assert homology==({2:2,3:1} if k==2 else {3:1})
        print('VERIFY_OK k=%d n=%d vertices=%d faces=%d pairs=%d incidences=%d'%
              (k,3*k+2,len(states),len(F),len(pairs),inc))
        print('VERIFY_OK critical=%s smith=%s homology=%s homotopy=%s'%
              (dict(sorted(critical.items())),dict(sorted(smith.items())),homology,homotopy))
    print('ALL_VERIFY_OK exact complete enumeration, Hasse acyclicity and integer Smith invariants')


if __name__=='__main__':run()
