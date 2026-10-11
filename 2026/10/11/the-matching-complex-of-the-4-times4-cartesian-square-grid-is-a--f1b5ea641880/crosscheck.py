#!/usr/bin/env python3
"""Independent direct mod-2 boundary ranks for the matching complex of P4 x P4."""

def grid_edges():
    return [(4*r+c,4*(r+1)+c) for r in range(3) for c in range(4)]+[(4*r+c,4*r+c+1) for r in range(4) for c in range(3)]

def all_matchings():
    edges=grid_edges()
    emasks=[(1<<a)|(1<<b) for a,b in edges]
    groups=[[] for _ in range(9)]
    def enumerate_from(start,occup,selection):
        groups[len(selection)].append(tuple(selection))
        for k in range(start,len(edges)):
            if not(occup&emasks[k]):
                selection.append(k)
                enumerate_from(k+1,occup|emasks[k],selection)
                selection.pop()
    enumerate_from(0,0,[])
    return groups

def rank2(columns):
    pivots={}
    for x in columns:
        while x:
            highest=x.bit_length()-1
            if highest in pivots:
                x^=pivots[highest]
            else:
                pivots[highest]=x
                break
    return len(pivots)

def verify():
    groups=all_matchings()
    assert [len(z) for z in groups]==[1,24,224,1044,2593,3388,2150,552,36]
    ranks=[0]
    for size in range(1,len(groups)):
        index={s:j for j,s in enumerate(groups[size-1])}
        cols=[sum(1<<index[s[:i]+s[i+1:]] for i in range(size)) for s in groups[size]]
        ranks.append(rank2(cols))
    ranks.append(0)
    assert ranks==[0,1,23,201,843,1750,1632,516,36,0]
    hom=[len(groups[k])-ranks[k]-ranks[k+1] for k in range(len(groups))]
    assert hom==[0,0,0,0,0,6,2,0,0]
    print('CROSSCHECK_OK','fvector',[len(g) for g in groups], 'ranks',ranks, 'reduced_betti4_5',(hom[5],hom[6]))
if __name__=='__main__':verify()
