"""Standalone discovery code for comparison trees of two chain interleavings."""
from itertools import combinations
from functools import lru_cache
import json
from pathlib import Path

OUT=Path(__file__).parent

def words(a,b):
    return [''.join('A' if x in apos else 'B' for x in range(a+b))
            for apos in combinations(range(a+b),a)]

def qmasks(a,b,words_):
    masks={}
    for i in range(1,a+1):
        for j in range(1,b+1):
            masks[f'{i},{j}']=sum(1<<k for k,w in enumerate(words_) if [t for t,c in enumerate(w) if c=='A'][i-1] < [t for t,c in enumerate(w) if c=='B'][j-1])
    return masks

def witness(a,b):
    ww=words(a,b); masks=qmasks(a,b,ww)
    @lru_cache(None)
    def ld(S):
        if S.bit_count()<2:return 0
        best=0
        for _,m in masks.items():
            T=S&m; U=S&~m
            if T and U:
                best=max(best,1+min(ld(T),ld(U)))
        return best
    S=(1<<len(ww))-1
    def build(S,d):
        if d==0:
            ix=(S&-S).bit_length()-1
            return {'word':ww[ix]}
        for q,m in masks.items():
            T=S&m;U=S&~m
            if T and U and ld(T)>=d-1 and ld(U)>=d-1:
                return {'query':q,'0':build(U,d-1),'1':build(T,d-1)}
        raise AssertionError((a,b,S,d))
    depth=ld(S)
    return {'a':a,'b':b,'depth':depth,'tree':build(S,depth),'n_words':len(ww)}

out={'definition':'Each word is an interleaving of A and B with fixed internal orders. Query i,j is 1 precisely when A_i precedes B_j. Child keys are queried answers.'}
out['certificates']=[witness(*ab) for ab in [(2,2),(2,3),(2,5),(3,3)]]
(OUT/'witnesses.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
for w in out['certificates']:
    print('CERT',w['a'],w['b'],w['depth'],w['n_words'])
