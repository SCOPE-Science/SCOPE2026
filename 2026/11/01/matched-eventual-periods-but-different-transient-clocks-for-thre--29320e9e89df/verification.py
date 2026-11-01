#!/usr/bin/env python3
"""Exact independent checks for three-state excitable dynamics on labelled bicliques.
Run: python3 verification.py. Reads support_certificate.csv in this directory.
Uses only Python's standard library. Finite checks complement the all-size proof.
"""
from collections import Counter
from itertools import product
from pathlib import Path
import csv

COLORS = (0,1,2)


def local_next(c, other_colors, model):
    if model == 'CCA':
        return (c+1)%3 if (c+1)%3 in other_colors else c
    if c == 0:
        return 1 if 1 in other_colors else 0
    return (c+1)%3


def microscopic_step(state, a, model):
    left = state[:a]
    right = state[a:]
    return tuple(local_next(v, set(right), model) for v in left) + tuple(
        local_next(v, set(left), model) for v in right)


def palette_mask(colors):
    out = 0
    for c in colors:
        out |= 1 << c
    return out


def palette_step(pair, model):
    a,b = pair
    A = {i for i in COLORS if a & (1<<i)}
    B = {i for i in COLORS if b & (1<<i)}
    return (palette_mask(local_next(c,B,model) for c in A),
            palette_mask(local_next(c,A,model) for c in B))


def period_profile(x, f):
    seen = {}
    cur = x
    while cur not in seen:
        seen[cur] = len(seen)
        cur = f(cur)
    return seen[cur],len(seen)-seen[cur]


def terminal_type(pair):
    a,b = pair
    A = {i for i in COLORS if a & (1<<i)}
    B = {i for i in COLORS if b & (1<<i)}
    if len(A)==3 and len(B)==3:
        return 3
    if len(A)>=2 and len(B)>=2 and len(A|B)==3:
        return 4
    return 1


def onto(k,m):
    if k==1:return 1
    if k==2:return 2**m-2
    return 3**m-3*2**m+3


def expected_table(a,b,model):
    # Candidate closed formula for each exact (first periodic entry, least period) class.
    u,v = onto(2,a),onto(3,a)
    U,V = onto(2,b),onto(3,b)
    if model=='GHM':
        return {(0,1):1,(0,3):v*V,(0,4):2*u*U,
                (1,1):3+2*(u+U)+u*U,
                (1,4):2*u*U+u*V+v*U,
                (2,1):3+3*(u+U)+u*U+v+V,
                (2,4):2*u*U+u*V+v*U,
                (3,1):2+2*(u+U)+u*U+v+V,
                (3,4):u*V+v*U,
                (4,1):2*(u+U)+v+V}
    return {(0,1):3,(0,3):v*V,(0,4):6*u*U,
            (1,1):6+3*(u+U+u*U),
            (1,4):3*(u*V+v*U),
            (2,1):6*(u+U)+3*(v+V)}


def main():
    table_path=Path(__file__).with_name('support_certificate.csv')
    with table_path.open(newline='',encoding='utf-8') as f:
        rows=list(csv.DictReader(f))
    assert len(rows)==49
    seen=set()
    for row in rows:
        a,b=(int(row['left_mask']),int(row['right_mask']))
        assert 1<=a<=7 and 1<=b<=7 and (a,b) not in seen
        seen.add((a,b))
        assert int(row['eventual_period'])==terminal_type((a,b))
        for model in ('CCA','GHM'):
            nxt=palette_step((a,b),model)
            assert nxt == (int(row[f'{model.lower()}_next_left']),
                           int(row[f'{model.lower()}_next_right']))
            t,p=period_profile((a,b),lambda z:palette_step(z,model))
            assert t==int(row[f'{model.lower()}_palette_entry'])
            assert p==int(row[f'{model.lower()}_palette_cycle'])
            assert (3 if p==1 and palette_ends_full((a,b),model) else
                    4 if p==2 else 1)==terminal_type((a,b))
    assert len(seen)==49
    checked=0
    for a in range(1,6):
        for b in range(1,6):
            if a+b>9:continue
            for model in ('CCA','GHM'):
                hist=Counter()
                for z in product(COLORS,repeat=a+b):
                    t,p=period_profile(z,lambda w:microscopic_step(w,a,model))
                    hist[t,p]+=1
                    k=terminal_type((palette_mask(z[:a]),palette_mask(z[a:])))
                    assert p==k,(a,b,model,z,t,p,k)
                    t0,_=period_profile((palette_mask(z[:a]),palette_mask(z[a:])),
                                        lambda w:palette_step(w,model))
                    assert t==t0,(a,b,model,z,t,t0)
                    checked+=1
                assert sum(hist.values())==3**(a+b)
                assert {k:v for k,v in hist.items() if v} == \
                       {k:v for k,v in expected_table(a,b,model).items() if v}, \
                        (model,a,b,hist,expected_table(a,b,model))
    tested=0
    for a in range(1,21):
        for b in range(1,21):
            for model in ('CCA','GHM'):
                cnt=Counter()
                for x,y in product(range(1,8),repeat=2):
                    prof=period_profile((x,y),lambda z:palette_step(z,model))
                    period=(3 if prof[1]==1 and palette_ends_full((x,y),model)
                            else 4 if prof[1]==2 else 1)
                    cnt[prof[0],period]+=onto(x.bit_count(),a)*onto(y.bit_count(),b)
                assert cnt == Counter({k:v for k,v in expected_table(a,b,model).items() if v})
                tested+=1
    print('BICLIQUE_THREE_COLOR_VERIFY_OK')
    print('support pairs checked: 49; microscopic labelled configurations tested:',checked)
    print('formula support weighted cases:',tested)


def palette_ends_full(pair,model):
    seen=set()
    x=pair
    while x not in seen:
        seen.add(x)
        if x==(7,7):return True
        x=palette_step(x,model)
    return False


if __name__=='__main__':
    main()
