#!/usr/bin/env python3
"""Finite exhaustive verifier for unary Gödel-modal fragment signatures."""
import json
from pathlib import Path

DATA = json.loads(Path(__file__).with_name('certificate.json').read_text(encoding='utf-8'))
CASES = [tuple(pair) for pair in DATA['cases_r_p']]
assert DATA['scale'] == 4
assert len(CASES) == 11
assert len(set(CASES)) == 11
assert set(CASES) == {(0,0),(0,2),(0,4),(2,0),(2,1),(2,2),(2,3),(2,4),(4,0),(4,2),(4,4)}
R = tuple(a for a,b in CASES)
P = tuple(b for a,b in CASES)
Z=(0,)*len(CASES)
T=(4,)*len(CASES)

def value(op, args):
    if op == 'zero': return Z
    if op == 'one': return T
    if op == 'p': return P
    if op == 'box':
        return tuple(4 if r<=a else a for r,a in zip(R,args[0]))
    if op == 'diamond':
        return tuple(min(r,a) for r,a in zip(R,args[0]))
    if op == 'and':
        return tuple(min(a,b) for a,b in zip(args[0],args[1]))
    if op == 'or':
        return tuple(max(a,b) for a,b in zip(args[0],args[1]))
    if op == 'imp':
        return tuple(4 if a<=b else b for a,b in zip(args[0],args[1]))
    raise AssertionError(op)

for fragment, allowed_ops, expected in [('box',{'box','and','or','imp'},60),('diamond',{'diamond','and','or','imp'},342)]:
    nodes = DATA['fragments'][fragment]
    assert len(nodes)==expected
    functions=[]
    for i,node in enumerate(nodes):
        op, parents = node['op'], node['parents']
        assert op in allowed_ops | {'zero','one','p'}
        assert all(type(j) is int and 0 <= j < i for j in parents)
        assert len(parents)==({'zero':0,'one':0,'p':0,'box':1,'diamond':1}.get(op,2))
        output = value(op,[functions[j] for j in parents])
        assert tuple(node['v'])==output
        assert len(output)==11 and all(0<=v<=4 for v in output)
        functions.append(output)
    assert [node['op'] for node in nodes[:3]]==['zero','one','p']
    S=set(functions)
    assert len(S)==expected
    for a in functions:
        for op in ('box','diamond'):
            if op in allowed_ops: assert value(op,[a]) in S
        for b in functions:
            for op in ('and','or','imp'):
                assert value(op,[a,b]) in S
    print('EXACT_CLOSURE',fragment, len(S), 'all_derivations_and_operations_valid')
# On a singleton fuzzy frame, diamond top is exactly its access weight,
# so box phi = diamond(top) -> phi and diamond phi = diamond(top) AND phi.
assert value('diamond',[T])==R
for a in DATA['fragments']['diamond']:
    u=tuple(a['v'])
    assert value('box',[u])==value('imp',[R,u])
    assert value('diamond',[u])==value('and',[R,u])
print('GODEL_ONE_WORLD_FRAGMENTS_EXACT_OK 60 342')

# Independent depth filtration: nonmodal Gödel closure at depth zero,
# followed by a single application of the permitted modality and closure.
def propositional_closure(generators):
    functions=list(generators)
    seen=set(functions)
    i=0
    while i<len(functions):
        a=functions[i]
        for b in functions[:i+1]:
            for op in ('and','or','imp'):
                outputs=[value(op,[a,b])]
                if op=='imp':outputs.append(value(op,[b,a]))
                for u in outputs:
                    if u not in seen:
                        seen.add(u)
                        functions.append(u)
        i+=1
    return seen

D0=propositional_closure({Z,T,P})
assert len(D0)==6
for mode,expected in [('box',60),('diamond',342)]:
    D1=propositional_closure(D0|{value(mode,[a]) for a in D0})
    certified={tuple(row['v']) for row in DATA['fragments'][mode]}
    assert D1 == certified and len(D1)==expected
    assert len(D1)>len(D0)
    print('DEPTH_ONE_NORMAL_FORM',mode,len(D0),len(D1),'sharp')
