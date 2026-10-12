#!/usr/bin/env python3
"""Exact rational-state verifier for uniform-legal-choice general-position growth."""
from collections import Counter
from functools import lru_cache
from fractions import Fraction as F
from itertools import combinations

CATEGORIES = ('row','column','matching','rectangle')


def prediction(m, n):
    p_row = F(n-1, m*n-1) * F(n-2, n-2+2*(m-1))
    p_col = F(m-1, m*n-1) * F(m-2, m-2+2*(n-1))
    p_mat = F((m-1)*(n-1), m*n-1) * F((m-2)*(n-2), (m-2)*(n-2)+2)
    return {'row': p_row, 'column': p_col, 'matching': p_mat,
            'rectangle': F(1)-p_row-p_col-p_mat}


def brute(m,n):
    cells=[(i,j) for i in range(m) for j in range(n)]
    N=len(cells)
    neighbors=[{v for v,(ii,jj) in enumerate(cells) if i!=ii and j!=jj}
               for i,j in cells]
    ds=[]
    for u in range(N):
        row={u:0}; frontier=[u]
        while frontier:
            nxt=[]
            for v in frontier:
                for w in neighbors[v]:
                    if w not in row:
                        row[w]=row[v]+1; nxt.append(w)
            frontier=nxt
        ds.append([row[v] for v in range(N)])
    assert max(max(x) for x in ds)==2
    bad=[]
    for u,v,w in combinations(range(N),3):
        if (ds[u][v]+ds[v][w]==ds[u][w]
            or ds[v][w]+ds[w][u]==ds[v][u]
            or ds[w][u]+ds[u][v]==ds[w][v]):
            bad.append((1<<u)|(1<<v)|(1<<w))
    @lru_cache(None)
    def legal(mask):
        return all(mask&t != t for t in bad)
    @lru_cache(None)
    def recurse(mask):
        assert legal(mask)
        ext=[mask|(1<<u) for u in range(N) if not mask>>u&1 and legal(mask|(1<<u))]
        if not ext:
            selected=[cells[u] for u in range(N) if mask>>u&1]
            rows={i for i,j in selected}; cols={j for i,j in selected}
            if len(rows)==1: c='row'
            elif len(cols)==1: c='column'
            elif len(rows)==len(selected) and len(cols)==len(selected): c='matching'
            elif len(selected)==4 and len(rows)==len(cols)==2: c='rectangle'
            else: raise AssertionError((m,n,selected))
            return {c:F(1)}
        ans=Counter()
        for x in ext:
            for c,p in recurse(x).items(): ans[c]+=p/F(len(ext))
        return dict(ans)
    ans=recurse(0); expect=prediction(m,n)
    assert all(ans.get(c,F())==expect[c] for c in CATEGORIES),(m,n,ans,expect)
    assert sum(ans.values())==1
    print(f'board={m}x{n}: explored_states={recurse.cache_info().currsize}, forbidden_geodesic_triples={len(bad)}, terminal_law='+','.join(f'{c}:{ans.get(c,F(0))}' for c in CATEGORIES))
    return ans


def main():
    for m,n in ((3,3),(3,4),(3,5),(4,4),(4,5),(5,5)):
        brute(m,n)
    for q in (4,5,20,100,1000):
        a=prediction(q,q)
        p_rect=a['rectangle']
        expected_gap=F(q-4)*p_rect
        assert F(0)<=p_rect<=F(1)
        print(f'square_order={q}: P_rectangle={p_rect}; expected_shortfall={expected_gap}')
    for m,n in ((3,100),(4,100),(7,1000)):
        p=prediction(m,n)
        print(f'asymmetric={m}x{n}: P_row={p["row"]}; P_matching={p["matching"]}')
    print('PASS')

if __name__=='__main__':main()
