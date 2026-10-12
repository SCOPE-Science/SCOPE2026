#!/usr/bin/env python3
"""Standalone exact checks of the two full-tree censuses and closed-pair witnesses."""
import json
from pathlib import Path
from math import gcd

HERE=Path(__file__).resolve().parent
A=json.loads((HERE/'tree_results.json').read_text())
B=json.loads((HERE/'expansion_results.json').read_text())
assert A['counts']==B['counts']
assert A['nine_word_exceptions']==B['nine_word_exceptions']
assert [x['total'] for x in A['counts']]==[1,2,5,14,42,132,429,1430]
assert A['counts'][-1]['nonsynchronizing_coprime']==4
assert set(B['certificates'])=={' '.join(x) for x in B['nine_word_exceptions']}
for words, data in B['certificates'].items():
    code=set(words.split())
    g=0
    for w in code:g=gcd(g,len(w))
    assert len(code)==9 and g==1
    assert all(not (u!=v and v.startswith(u)) for u in code for v in code)
    states={''}|{w[:i] for w in code for i in range(1,len(w))}
    assert all(s+'0' in code or s+'0' in states for s in states)
    assert all(s+'1' in code or s+'1' in states for s in states)
    pairs={frozenset(p) for p in data['closed_pairs']}
    assert frozenset(data['start']) in pairs
    for pair in pairs:
        assert len(pair)==2 and pair <= states
        for b in '01':
            successors=frozenset('' if x+b in code else x+b for x in pair)
            assert len(successors)==2 and successors in pairs
print('VERIFY_OK: two censuses agree; four closed nonmerging pair sets validated')
