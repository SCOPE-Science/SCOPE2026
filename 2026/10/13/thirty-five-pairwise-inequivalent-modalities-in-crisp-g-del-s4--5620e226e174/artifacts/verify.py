#!/usr/bin/env python3
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
D=json.loads((HERE/'witnesses.json').read_text('utf-8'))
mods=D['modalities']
assert len(mods)==35 and len(set(mods))==35

def rows(n,pairs):
    r=[0]*n
    for a,b in pairs:
        assert 0<=a<n and 0<=b<n
        r[a]|=1<<b
    return tuple(r)

def preorder(R,n):
    if any(not ((R[i]>>i)&1) for i in range(n)): return False
    for i in range(n):
        for j in range(n):
            if ((R[i]>>j)&1) and (R[j] & ~R[i]): return False
    return True

def locally_linear(le,n):
    for w in range(n):
        U=[u for u in range(n) if (le[w]>>u)&1]
        for u in U:
            for v in U:
                if not (((le[u]>>v)&1) or ((le[v]>>u)&1)): return False
    return True

def forward(le,R,n):
    # w<=w' and w R v => some v' with v<=v' and w' R v'
    for w in range(n):
      for wp in range(n):
       if (le[w]>>wp)&1:
        for v in range(n):
         if (R[w]>>v)&1:
          if not any(((le[v]>>vp)&1) and ((R[wp]>>vp)&1) for vp in range(n)): return False
    return True

def backward(le,R,n):
    # w R v and v<=v' => some w' with w<=w' and w' R v'
    for w in range(n):
      for v in range(n):
       if (R[w]>>v)&1:
        for vp in range(n):
         if (le[v]>>vp)&1:
          if not any(((le[w]>>wp)&1) and ((R[wp]>>vp)&1) for wp in range(n)): return False
    return True

def downward(le,R,n):
    # w<=v and v R v' => some w' with w R w' and w'<=v'
    for w in range(n):
      for v in range(n):
       if (le[w]>>v)&1:
        for vp in range(n):
         if (R[v]>>vp)&1:
          if not any(((R[w]>>wp)&1) and ((le[wp]>>vp)&1) for wp in range(n)): return False
    return True

def upset(S,le,n):
    return all(not ((S>>w)&1) or not ((le[w]>>v)&1) or ((S>>v)&1)
               for w in range(n) for v in range(n))

def neg(S,le,n):
    # Infallible intuitionistic negation: w |= ~phi iff no v>=w satisfies phi.
    out=0
    for w in range(n):
        if (S & le[w])==0: out|=1<<w
    return out

def box(S,le,R,n):
    # Birelational GS4 clause: all v reached by w<=u R v satisfy phi.
    out=0
    for w in range(n):
        reach=0
        for u in range(n):
            if (le[w]>>u)&1: reach |= R[u]
        if (reach & ~S)==0: out|=1<<w
    return out

def dia(S,R,n):
    out=0
    for w in range(n):
        if R[w] & S: out|=1<<w
    return out

def evaluate(word,S,le,R,n):
    x=S
    for c in reversed(word):
        if c=='N': x=neg(x,le,n)
        elif c=='B': x=box(x,le,R,n)
        elif c=='D': x=dia(x,R,n)
        else: raise AssertionError(c)
    return x

fingerprints=[[] for _ in mods]
for mi,M in enumerate(D['models']):
    n=M['n']; le=rows(n,M['leq']); R=rows(n,M['modal'])
    S=sum(1<<w for w in M['atom_true'])
    assert preorder(le,n), ('leq preorder',mi)
    assert preorder(R,n), ('modal preorder',mi)
    assert locally_linear(le,n), ('local linearity',mi)
    assert forward(le,R,n), ('forward confluence',mi)
    assert backward(le,R,n), ('backward confluence',mi)
    assert downward(le,R,n), ('downward confluence',mi)
    assert upset(S,le,n), ('atom upset',mi)
    for i,m in enumerate(mods):
        fingerprints[i].append(evaluate(m,S,le,R,n))

fp=[tuple(x) for x in fingerprints]
assert len(set(fp))==35, 'fingerprints are not pairwise distinct'
# Explicitly verify each pair has a witness component.
for i in range(35):
    for j in range(i):
        assert any(fp[i][k]!=fp[j][k] for k in range(len(D['models']))), (i,j)
print('VERIFY_OK modalities=35 models=8 pairs=595')
