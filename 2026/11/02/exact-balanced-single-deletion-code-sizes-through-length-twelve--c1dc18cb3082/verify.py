#!/usr/bin/env python3
"""Exact standalone verifier for balanced single-deletion packing certificates."""
import itertools, json, math, pathlib
DATA = pathlib.Path(__file__).with_name('dual_certificates.json')
certs=json.loads(DATA.read_text(encoding='utf-8'))
expected={1:1,2:2,3:5,4:14,5:42,6:132}

def deletion_shadow(word):
    return {word[:i]+word[i+1:] for i in range(len(word))}

for m, optimum in expected.items():
    n=2*m
    words=[''.join(bits) for bits in itertools.product('01',repeat=n) if bits.count('1')==m]
    assert len(words)==math.comb(n,m)
    residue_classes={r:[] for r in range(m+1)}
    for w in words:
        residue=sum((i+1)*int(bit) for i,bit in enumerate(w))%(m+1)
        residue_classes[residue].append(w)
    assert all(len(C)==optimum for C in residue_classes.values())
    for C in residue_classes.values():
        used=set()
        for x in C:
            out=deletion_shadow(x)
            assert used.isdisjoint(out), ('lower-bound code collision',m,x)
            used.update(out)
    D=certs[str(m)]
    scale=D['scale']; weights=D['weights']
    assert isinstance(scale,int) and scale>0
    assert all(len(y)==n-1 and y.count('1') in (m-1,m) and isinstance(v,int) and v>=0 for y,v in weights.items())
    total=sum(weights.values())
    assert total<(optimum+1)*scale,(m,total,scale)
    cover=[sum(weights.get(y,0) for y in deletion_shadow(x)) for x in words]
    assert min(cover)>=scale,(m,min(cover))
    print(f'm={m} n={n} N={len(words)} C={optimum} dual_sum={total}/{scale} min_cover={min(cover)}/{scale} nonzero={len(weights)}')
# Strict fractional-versus-integral gap for the first nontrivial even balanced layer.
P=json.loads(pathlib.Path(__file__).with_name('primal_gap_m4.json').read_text(encoding='utf-8'))
assert P['m']==4 and P['scale']>0
assert all(len(x)==8 and x.count('1')==4 and isinstance(v,int) and v>=0 for x,v in P['weights'].items())
assert sum(P['weights'].values())>14*P['scale']
for y in [''.join(bits) for bits in itertools.product('01',repeat=7) if bits.count('1') in (3,4)]:
    load=sum(v for x,v in P['weights'].items() if y in deletion_shadow(x))
    assert load<=P['scale'], ('fractional packing infeasible',y,load)
# At m=1,2,3 the rounded dual supports are 0-1 weights with one unit
# per positive output. Their totals equal the integral Catalan lower bounds.
for m in (1,2,3):
    D=certs[str(m)]; nonzero={y:1 for y in D['weights']}
    for x in [''.join(bits) for bits in itertools.product('01',repeat=2*m) if bits.count('1')==m]:
        assert sum(nonzero.get(y,0) for y in deletion_shadow(x))>=1
    assert sum(nonzero.values())==expected[m]
print('FRACTIONAL_GAP',sum(P['weights'].values()),'/',P['scale'],'> 14')
print('VERIFY_OK')
