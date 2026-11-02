#!/usr/bin/env python3
"""Independently verify supplied finite one-deletion cover witnesses (stdlib only)."""
import itertools
import json
from pathlib import Path

root=Path(__file__).resolve().parent
with (root/'data'/'base_witnesses.json').open(encoding='utf-8') as f:
    witnesses=json.load(f)
expected={2:2,4:6,6:12,8:22,10:34,12:48,14:66,16:86,20:134,22:162}
assert set(map(int,witnesses))==set(expected)

def deletion_ball(w):
    return {tuple(w[:i]+w[i+1:]) for i in range(3)}

for q in sorted(expected):
    data=witnesses[str(q)]
    arrows=[tuple(x) for x in data['arrows']]
    triples=[tuple(x) for x in data['triples']]
    assert len(arrows)==q
    assert len(triples)==(expected[q]-q)//2
    assert sorted(a for a,b in arrows)==list(range(q))
    assert all(0<=a<q and 0<=b<q and a!=b for a,b in arrows)
    assert len(triples)==len(set(triples))
    assert all(len(t)==3 and tuple(sorted(t))==t and len(set(t))==3 and all(0<=a<q for a in t) for t in triples)
    words=[(a,b,a) for a,b in arrows]
    for a,b,c in triples:
        words.extend([(a,b,c),(c,b,a)])
    assert len(words)==expected[q]==(q*q+2)//3
    assert len(set(words))==len(words)
    covered=set().union(*(deletion_ball(w) for w in words))
    target=set(itertools.product(range(q),repeat=2))
    assert covered==target, (q,len(covered),len(target-covered))
    print('q=%2d codewords=%3d coverage=%3d targets; all checked'%(q,len(words),len(covered)))

# Check the Colbourn--Hoffman--Rees existence inequalities in all three
# families through an arbitrary large finite test range; the actual
# all-t proof is the elementary symbolic verification in RESULT.md.
for t in range(3,101):
    for u in (0,8,10):
        g=6
        assert u<=g*(t-1)
        assert (g*(t-1)+u)%2==0
        assert (g*t)%2==0
        assert (g*g*t*(t-1)//2+g*t*u)%3==0
        assert (g*t+u)%2==0
        q=g*t+u
        local=(12*t + ({0:0,8:22,10:34}[u]))
        cross_pairs=(q*q-(g*g*t+u*u))//2
        assert cross_pairs%3==0
        assert local+2*(cross_pairs//3)==(q*q+2)//3
print('3-GDD admissibility and assembly counts: t=3..100, u=0,8,10 checked')
print('VERIFY_OK')
