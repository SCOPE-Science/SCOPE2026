#!/usr/bin/env python3
"""Compare all-round counting colour histograms of square grids and the
single crossed-matching binary-relation variant; direct transitivity witness.
"""
from collections import Counter

def test(n):
    pts=[(i,j) for i in range(1,n+1) for j in range(1,n+1)]
    N=len(pts); idx={p:i for i,p in enumerate(pts)}
    ref=[[int(x!=y and x[0]<=y[0] and x[1]<=y[1]) for y in pts] for x in pts]
    bad=[row[:] for row in ref]
    for u,v in [((2,1),(4,1)),((1,2),(1,4))]:bad[idx[u]][idx[v]]=0
    for u,v in [((2,1),(1,4)),((1,2),(4,1))]:bad[idx[u]][idx[v]]=1
    assert ref[idx[(2,1)]][idx[(3,1)]] and ref[idx[(3,1)]][idx[(4,1)]]
    assert bad[idx[(2,1)]][idx[(3,1)]] and bad[idx[(3,1)]][idx[(4,1)]] and not bad[idx[(2,1)]][idx[(4,1)]]
    graphs=[ref,bad]
    colors=[[0]*N for _ in graphs]
    for round_no in range(N+1):
        keys=[]
        for g,G in enumerate(graphs):
            for i in range(N):
                c=Counter()
                for j in range(N):
                    relation=(int(i==j),G[i][j],G[j][i])
                    c[relation,colors[g][j]]+=1
                keys.append((colors[g][i],tuple(sorted(c.items()))))
        index={key:i for i,key in enumerate(sorted(set(keys)))}
        next_colors=[[index[keys[g*N+i]] for i in range(N)] for g in range(2)]
        assert Counter(next_colors[0])==Counter(next_colors[1]),('C2 separator',n,round_no)
        if next_colors==colors:break
        colors=next_colors
    else:raise AssertionError('refinement did not stabilize')
    return round_no,len(set(colors[0]))

if __name__=='__main__':
    for n in range(4,9):
        rounds,classes=test(n)
        print(f'square side={n}: counting-equivalent crossed-matching structure, nontransitive, stable classes={classes}, rounds={rounds}')
    print('PASS nontransitive C2 companions for square sides 4 through 8')
