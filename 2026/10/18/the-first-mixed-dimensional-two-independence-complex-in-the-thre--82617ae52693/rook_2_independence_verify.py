#!/usr/bin/env python3
"""Exact finite simplicial/Morse proof for 2-independence complexes of 3 x n rook graphs.
Run: python3 rook_2_independence_verify.py
Pure Python 3 standard library, deterministic and self-contained.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache

ORDERS = {
 1: [0,1,2],
 2: [0,1,2,3,4,5],
 3: [0,7,3,2,6,4,1,5,8],
 4: [0,6,8,5,3,1,9,2,4,7,10,11],
 5: [3,6,9,13,12,5,2,10,11,4,0,8,7,1,14],
 6: [10,5,14,16,2,11,6,0,13,3,8,12,4,17,1,7,15,9],
}
EXPECTED = {
 1: {0:1,1:1},
 2: {0:1,1:4},
 3: {0:1,2:5},
 4: {0:1,3:13},
 5: {0:1,3:61},
 6: {0:1,3:113,4:7},
}

def facets(z):
    bit=z; place=0
    while bit:
        t=bit & -bit; bit -= t
        yield z ^ t, 1 if place % 2==0 else -1
        place+=1

def admissible_faces(n):
    # Bit i*n+j corresponds to board square (i,j), i=0,1,2.
    N=3*n
    adj=[0]*N
    for u in range(N):
        i,j=divmod(u,n)
        for v in range(N):
            a,b=divmod(v,n)
            if u != v and (i==a or j==b):
                adj[u] |= 1<<v
    F=set()
    for mask in range(1,1<<N):
        selected=[u for u in range(N) if (mask>>u)&1]
        # Each induced connected component has <=2 vertices iff induced degrees <=1.
        if all((mask&adj[u]).bit_count()<=1 for u in selected):
            F.add(mask)
    return F

def run(n):
    F=admissible_faces(n)
    remaining=set(F)
    matching=[]
    for v in ORDERS[n]:
        bit=1<<v
        pairs=[(s,s|bit) for s in sorted(remaining)
               if not(s&bit) and (s|bit) in remaining]
        for a,b in pairs:
            assert a in remaining and b in remaining
            remaining.remove(a);remaining.remove(b)
        matching.extend(pairs)
    lower_to_upper={a:b for a,b in matching}
    upper_to_lower={b:a for a,b in matching}
    assert len(lower_to_upper)==len(upper_to_lower)==len(matching)
    assert len(matching)*2+len(remaining)==len(F)
    critical_counts=dict(sorted(Counter(s.bit_count()-1 for s in remaining).items()))
    assert critical_counts == EXPECTED[n],(n,critical_counts)
    # Directed Hasse graph: reverse paired arcs to test Forman acyclicity.
    incoming={s:0 for s in F};out={s:[] for s in F};cover_count=0
    for upper in F:
        for low,_ in facets(upper):
            if not low:continue
            assert low in F
            cover_count += 1
            if lower_to_upper.get(low)==upper:
                a,b=low,upper
            else:
                a,b=upper,low
            out[a].append(b);incoming[b]+=1
    q=deque(s for s in F if incoming[s]==0)
    nvisited=0
    while q:
        s=q.popleft();nvisited+=1
        for t in out[s]:
            incoming[t]-=1
            if incoming[t]==0:q.append(t)
    assert nvisited==len(F),('cycle in matching',n,nvisited,len(F))
    # Exact signed integral gradient-path computation for every Morse differential.
    @lru_cache(None)
    def project(face):
        if face in remaining: return {face:1}
        if face in upper_to_lower: return {}
        assert face in lower_to_upper
        b=lower_to_upper[face]
        incidence=next(sgn for f,sgn in facets(b) if f==face)
        answer=defaultdict(int)
        for f,sgn in facets(b):
            if f==face:continue
            for critical,coeff in project(f).items():
                answer[critical]-=incidence*sgn*coeff
        return {k:v for k,v in answer.items() if v}
    nonzero=[]
    for face in remaining:
        if face.bit_count()==1:continue
        answer=defaultdict(int)
        for f,sgn in facets(face):
            for critical,coeff in project(f).items():
                answer[critical]+=sgn*coeff
        answer={k:v for k,v in answer.items() if v}
        if answer:nonzero.append((face,answer))
    assert not nonzero,(n,nonzero[:3])
    fvector=dict(sorted(Counter(s.bit_count()-1 for s in F).items()))
    print('n=%d vertices=%d faces=%d f_vector=%s covers=%d pairs=%d critical=%s morse_boundary_nonzero=0 DAG=PASS' %
          (n,3*n,len(F),fvector,cover_count,len(matching),critical_counts))
    return critical_counts

if __name__=='__main__':
    for n in range(1,7):run(n)
    print('ALL EXACT INTEGRAL MORSE CHECKS PASSED')
