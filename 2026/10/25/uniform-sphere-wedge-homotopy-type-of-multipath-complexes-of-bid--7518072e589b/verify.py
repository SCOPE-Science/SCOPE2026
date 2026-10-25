#!/usr/bin/env python3
"""Exact finite face-poset certificate for bidirected polygon multipath complexes.
For a cycle with L vertices, vertices +i,-i label the directed edges.
No directed cycles, branching or 2-cycles are permitted.
"""
import collections
import sys
import time

def generate(L):
    full = (1 << L)-1
    faces = []
    for minus in range(1 << L):
        blocked = minus | ((minus << 1) & full) | (minus >> 1)
        if minus & (1 << (L-1)): blocked |= 1
        if minus & 1: blocked |= 1 << (L-1)
        available = full ^ blocked
        plus = available
        while True:
            if (minus or plus) and not (minus == full and plus == 0) and not (plus == full and minus == 0):
                faces.append(plus | (minus << L))
            if plus == 0: break
            plus = (plus-1) & available
    return faces

def match(L,faces):
    active = set(faces)
    pairs = []
    for v in range(2*L):
        b = 1 << v
        for f in faces:
            if f not in active or f & b: continue
            h = f|b
            if h in active:
                active.remove(f);active.remove(h)
                pairs.append((f,h))
    return pairs,active

def check(L,detail=False):
    t=time.monotonic()
    faces=generate(L)
    full=(1<<L)-1
    top={f for f in faces if f.bit_count()==L-1}
    expected={(full^(1<<i)) for i in range(L)}|{(full^(1<<i))<<L for i in range(L)}
    assert top==expected,(L,'top_facets_wrong',len(top),len(expected))
    assert len(set(faces))==len(faces)
    pairs,critical=match(L,faces)
    pair_map={u:v for u,v in pairs}
    assert len(pairs)*2+len(critical)==len(faces)
    indices={f:i for i,f in enumerate(faces)}
    indeg=[0]*len(faces)
    adj=[[] for _ in faces]
    covering=0
    for top_id,f in enumerate(faces):
        b=f
        while b:
            bit=b&-b
            b-=bit
            low=f^bit
            if not low: continue
            low_id=indices[low]
            if pair_map.get(low)==f:
                adj[low_id].append(top_id);indeg[top_id]+=1
            else:
                adj[top_id].append(low_id);indeg[low_id]+=1
            covering+=1
    q=collections.deque(i for i,d in enumerate(indeg) if d==0)
    seen=0
    while q:
        i=q.popleft(); seen+=1
        for j in adj[i]:
            indeg[j]-=1
            if indeg[j]==0:q.append(j)
    assert seen==len(faces),(L,'directed_cycle',seen,len(faces))
    crit=collections.Counter(x.bit_count()-1 for x in critical)
    assert len(critical)==(4 if L%4 in (1,2,3) else 6)
    assert crit[0]==1 and crit[L-2]==2
    low={k:v for k,v in crit.items() if k not in (0,L-2)}
    expected={((L-2)//2 if L%4 in (0,2,3) else (L-1)//2):(3 if L%4==0 else 1)}
    # for L ≡ 1, lower is (L-1)/2; for L ≡ 2, lower is (L-2)/2.
    assert low==expected,(L,low,expected)
    got={'L':L,'faces':len(faces),'covering':covering,'matched_pairs':len(pairs),'critical':dict(sorted(crit.items())), 'acyclic':True}
    print(got,flush=True)
    if detail:
        print('critical_words',sorted((''.join('+' if s>>i&1 else '-' if s>>(L+i)&1 else '.' for i in range(L)) for s in critical)),flush=True)
    return got
if __name__=='__main__':
    for L in map(int,sys.argv[1:] or range(7,15)):
        check(L,True)
