#!/usr/bin/env python3
"""Independent check by vertex-deletion recursion, without enumerating simplices."""
from functools import lru_cache

DIRECTIONS={(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}

def graph(kind):
    adj=[]
    for x in range(4):
        for y in range(4):
            ns=0
            for z in range(4):
                for w in range(4):
                    if ((z-x)%4,(w-y)%4) in DIRECTIONS if kind=='shri' else ((x==z or y==w) and (x,y)!=(z,w)):
                        ns|=1<<(4*z+w)
            adj.append(ns)
    return adj

def polynomial(adj):
    @lru_cache(None)
    def calc(remaining):
        if remaining==0:return (1,)
        v=(remaining&-remaining).bit_length()-1
        without_v=calc(remaining^(1<<v))
        with_v=calc((remaining^(1<<v))&~adj[v])
        out=[0]*(max(len(without_v),len(with_v)+1))
        for k,x in enumerate(without_v):out[k]+=x
        for k,x in enumerate(with_v):out[k+1]+=x
        return tuple(out)
    return calc((1<<len(adj))-1)

if __name__=='__main__':
    s=polynomial(graph('shri'));r=polynomial(graph('rook'))
    assert s==(1,16,72,96,16),s
    assert r==(1,16,72,96,24),r
    print('POLYNOMIAL_RECURSION_OK',s,r)
