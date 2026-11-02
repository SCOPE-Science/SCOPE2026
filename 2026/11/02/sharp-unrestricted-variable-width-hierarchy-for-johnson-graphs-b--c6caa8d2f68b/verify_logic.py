"""Noncounting two-dimensional color refinement on Johnson graphs.

A pair's new color records its previous color and the SET (not multiset)
of two-step color pairs. This is the noncounting three-variable refinement.
"""
from itertools import combinations


def graph(n,r):
    v=[sum(1<<i for i in x) for x in combinations(range(n),r)]
    m=len(v)
    col=[[0 if i==j else (1 if (v[i]^v[j]).bit_count()==2 else 2)
          for j in range(m)] for i in range(m)]
    return col


def refine(graphs, maxround=30):
    colors=graphs
    sizes=[len(g) for g in colors]
    for stage in range(maxround+1):
        diag=[colors[i][0][0] for i in range(len(colors))]
        if stage in (0,1,2,3,4,5):
            print('round',stage,'diagonal colors',diag)
        keys=[]
        for g in colors:
            m=len(g)
            keys.append([[(g[i][j],frozenset((g[i][z],g[z][j]) for z in range(m)))
                 for j in range(m)] for i in range(m)])
        mapping={}
        for k in keys:
            for row in k:
                for a in row:
                    if a not in mapping: mapping[a]=len(mapping)
        nxt=[[[mapping[a] for a in row] for row in k] for k in keys]
        old_unique=set()
        for g in colors:
            for row in g:
                old_unique.update(row)
        # Refinement never merges old colors because the old color is in its key.
        if len(mapping)==len(old_unique):
            colors=nxt
            print('stable at round',stage+1,'colors',len(mapping))
            return [g[0][0] for g in colors]
        colors=nxt
    raise AssertionError('no stable partition')


if __name__=='__main__':
    for r,orders in [(2,[4,5,6,7,8]),(3,[6,7,8,9,10])]:
        print('r',r,'orders',orders)
        diag=refine([graph(n,r) for n in orders])
        groups={}
        for n,k in zip(orders,diag): groups.setdefault(k,[]).append(n)
        profile=sorted(groups.values(),key=lambda a:a[0])
        assert profile==[[n] for n in orders if n<3*r]+[[n for n in orders if n>=3*r]],profile
        print('final equivalence classes',profile)
    print('LOGIC_REFINEMENT_OK')
