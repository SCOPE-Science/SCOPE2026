"""Construct and check complete depth-three neighborhood-shattering trees.
Run with: python3 witness_checker.py
"""
import json
from independent_threshold_check import rows_of

WORDS=('1101010','1010110','1010101','11011011')

def able(rows, centers, depth):
    if depth == 0:
        return bool(centers)
    n=len(rows)
    for query in range(n):
        neg=tuple(v for v in centers if not(rows[v]>>query&1))
        pos=tuple(v for v in centers if rows[v]>>query&1)
        if neg and pos and able(rows,neg,depth-1) and able(rows,pos,depth-1):
            return True
    return False

def build(rows, centers, depth):
    if depth==0:
        return {'witness_center':min(centers)}
    for q in range(len(rows)):
        neg=tuple(v for v in centers if not(rows[v]>>q&1))
        pos=tuple(v for v in centers if rows[v]>>q&1)
        if neg and pos and able(rows,neg,depth-1) and able(rows,pos,depth-1):
            return {'query':q, 'zero':build(rows,neg,depth-1), 'one':build(rows,pos,depth-1)}
    raise ValueError('No shattered tree of this depth')

def check(rows, node, history=()):
    if 'witness_center' in node:
        v=node['witness_center']
        assert all((rows[v]>>q&1)==b for q,b in history), (v,history)
        return [v]
    assert 'query' in node
    q=node['query']
    assert 0<=q<len(rows)
    return check(rows,node['zero'],history+((q,0),))+check(rows,node['one'],history+((q,1),))

def main():
    with open('witnesses.json',encoding='utf8') as f:
        stored=json.load(f)
    assert len(stored)==4
    for item,w in zip(stored,WORDS):
        assert item['creation_word']==w
        rows=rows_of(w)
        assert item['vertices']==len(rows) and item['depth']==3
        # Verify the ACTUAL stored certificate, and also regenerate it independently.
        centers=check(rows,item['tree'])
        assert centers==item['witness_centers_in_lexicographic_leaf_order']
        assert len(centers)==8 and len(set(centers))==8
        regenerated=build(rows,tuple(range(len(rows))),3)
        assert regenerated==item['tree']
    print('ALL_FOUR_COMPLETE_DEPTH3_WITNESSES_VERIFIED')

if __name__=='__main__':main()
