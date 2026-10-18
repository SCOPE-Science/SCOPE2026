#!/usr/bin/env python3
"""Independent face-boundary mod-two check for bidirected wheels, rim 3..7.
Mod-two checks corroborate ranks only, not absence of integral torsion.
"""
from itertools import product
from collections import Counter, defaultdict


def wheel_arcs(n):
    edges={(0,i) for i in range(1,n+1)}
    edges.update(tuple(sorted((i,1+i%n))) for i in range(1,n+1))
    arcs=sorted([(a,b) for a,b in edges]+[(b,a) for a,b in edges])
    neigh={v:[(x,j) for j,(u,x) in enumerate(arcs) if u==v]
           for v in range(n+1)}
    return neigh

def direct_faces(n):
    neigh=wheel_arcs(n)
    faces=[]
    for options in product(*[[(None,None)]+neigh[v] for v in range(n+1)]):
        tgts=[e[0] for e in options if e[0] is not None]
        if len(tgts)!=len(set(tgts)):continue
        if any(has_cycle(v,options) for v in range(n+1)):continue
        faces.append(sum(1<<e[1] for e in options if e[1] is not None))
    return faces

def has_cycle(v, opts):
    seen=set()
    while v is not None and v not in seen:
        seen.add(v);v=opts[v][0]
    return v is not None

def gf2_rank(columns):
    basis={}
    for word in columns:
        while word:
            k=word.bit_length()-1
            if k in basis:word^=basis[k]
            else:basis[k]=word;break
    return len(basis)

def checks():
    results={}
    for n in range(3,8):
        ff=direct_faces(n)
        by=defaultdict(list)
        for f in ff:by[f.bit_count()-1].append(f)
        ranks={}
        for k in range(0,n):
            hi=by.get(k,[]);lo=by.get(k-1,[])
            if not hi or not lo:continue
            ix={f:i for i,f in enumerate(lo)}
            columns=[]
            for face in hi:
                x=0
                bits=face
                while bits:
                    bit=bits&-bits
                    bits^=bit
                    x^=1<<ix[face^bit]
                columns.append(x)
            ranks[k]=gf2_rank(columns)
        betti={k:len(by.get(k,[]))-ranks.get(k,0)-ranks.get(k+1,0)
               for k in range(n)}
        results[n]={k:v for k,v in betti.items() if v}
    return results

if __name__=='__main__':
    results=checks()
    expected={3:{1:7,2:6},4:{2:19,3:8},5:{2:2,3:23,4:10},
              6:{3:29,4:26,5:12},7:{4:43,5:30,6:14}}
    assert results==expected,(results,expected)
    print(results)
    print('INDEPENDENT_DIRECT_GF2_BOUNDARIES_AGREE')
