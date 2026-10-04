#!/usr/bin/env python3
import json
from itertools import product
from pathlib import Path

ROOT=Path(__file__).resolve().parent
cert=json.loads((ROOT/'certificate.json').read_text(encoding='utf-8'))
assert cert['schema_version']==1
assert cert['n']==7 and cert['read_count']==2 and cert['deletion_count']==1
assert cert['maximum_code_size']==70

words=[''.join(p) for p in product('01', repeat=7)]
wordset=set(words)

def deletion_ball(w):
    return {w[:i]+w[i+1:] for i in range(7)}

balls={w:deletion_ball(w) for w in words}
# Directly recompute the compatibility relation from the channel definition.
def compatible(x,y):
    return len(balls[x] & balls[y]) < 2

code=cert['codewords']
assert len(code)==70 and len(set(code))==70 and set(code)<=wordset
for i,x in enumerate(code):
    for y in code[i+1:]:
        assert compatible(x,y), (x,y,balls[x]&balls[y])

coloring=cert['coloring']
assert set(coloring)==wordset
colors=set(coloring.values())
assert colors==set(range(70)), (min(colors),max(colors),len(colors))
# A proper 70-coloring of the compatibility graph proves every compatible
# clique, hence every two-read reconstruction code, has at most 70 words.
for i,x in enumerate(words):
    for y in words[i+1:]:
        if compatible(x,y):
            assert coloring[x] != coloring[y], (x,y,coloring[x])

# Check the equivalent confusability-graph cover formulation: each color
# class is a clique under intersection size exactly two or a singleton.
classes={c:[] for c in range(70)}
for w,c in coloring.items(): classes[c].append(w)
assert sum(map(len,classes.values()))==128
for members in classes.values():
    for i,x in enumerate(members):
        for y in members[i+1:]:
            assert len(balls[x]&balls[y])==2, (x,y,balls[x]&balls[y])

print('vertices=128')
print('witness_code_size=70')
print('color_count=70')
print('VERIFY_OK')
