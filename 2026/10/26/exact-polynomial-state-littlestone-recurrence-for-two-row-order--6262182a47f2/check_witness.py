#!/usr/bin/env python3
"""Independently replay an existing two-row order-ideal mistake-tree JSON file."""
import json
from pathlib import Path

N=52
DEPTH=10
H=[(a,b) for a in range(N+1) for b in range(a+1)]
tree=json.loads(Path(__file__).with_name('depth10_n52_witness.json').read_text(encoding='utf-8'))
count=0

def visit(node, candidates, depth):
    global count
    if depth == 0:
        assert node is None and candidates
        count += 1
        return
    assert set(node)=={'row','column','zero','one'}
    row, col = node['row'], node['column']
    assert row in (1,2) and 1<=col<=N
    zero=[h for h in candidates if h[row-1]<col]
    one=[h for h in candidates if h[row-1]>=col]
    assert zero and one, ('dead branch',row,col,depth)
    visit(node['zero'], zero, depth-1)
    visit(node['one'], one, depth-1)

visit(tree,H,DEPTH)
assert count==2**DEPTH
print(f'STANDALONE_CERTIFICATE_OK n={N} depth={DEPTH} paths={count}')
