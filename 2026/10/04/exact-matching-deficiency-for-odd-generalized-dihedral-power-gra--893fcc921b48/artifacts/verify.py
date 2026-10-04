#!/usr/bin/env python3
from functools import lru_cache
from itertools import product

def add(a,b,mods):
    return tuple((x+y)%m for x,y,m in zip(a,b,mods))
def neg(a,mods):
    return tuple((-x)%m for x,m in zip(a,mods))
def mul(x,y,mods):
    a,e=x; b,f=y
    bb=b if e==0 else neg(b,mods)
    return (add(a,bb,mods),(e+f)%2)

def identity(mods): return (tuple(0 for _ in mods),0)

def elements(mods):
    A=list(product(*[range(m) for m in mods]))
    return [(a,e) for a in A for e in (0,1)]

def powers(x,mods):
    e=identity(mods); out={e}; y=e
    while True:
        y=mul(y,x,mods)
        if y in out: break
        out.add(y)
    return out

def graphs(mods):
    E=elements(mods); n=len(E)
    cyc={x:powers(x,mods) for x in E}
    P=[[False]*n for _ in range(n)]
    PE=[[False]*n for _ in range(n)]
    containing=[set() for _ in range(n)]
    idx={x:i for i,x in enumerate(E)}
    for z,S in cyc.items():
        inds=[idx[x] for x in S]
        for i in inds:
            containing[i].add(z)
    for i in range(n):
        for j in range(i+1,n):
            x,y=E[i],E[j]
            pp = y in cyc[x] or x in cyc[y]
            pe = bool(containing[i] & containing[j])
            P[i][j]=P[j][i]=pp
            PE[i][j]=PE[j][i]=pe
    return E,P,PE

def max_matching(adj):
    n=len(adj)
    @lru_cache(None)
    def f(mask):
        if not mask: return 0
        i=(mask & -mask).bit_length()-1
        best=f(mask & ~(1<<i))
        rest=mask & ~(1<<i)
        jmask=rest
        while jmask:
            j=(jmask & -jmask).bit_length()-1
            if adj[i][j]:
                best=max(best,1+f(rest & ~(1<<j)))
            jmask &= jmask-1
        return best
    return f((1<<n)-1)

def check(mods):
    E,P,PE=graphs(mods)
    m=1
    for q in mods: m*=q
    assert m%2==1 and m>1
    e=identity(mods); ei=E.index(e)
    leaves=[i for i,x in enumerate(E) if x[1]==1]
    assert len(leaves)==m
    for adj in (P,PE):
        for i in leaves:
            N=[j for j,v in enumerate(adj[i]) if v]
            assert N==[ei], (mods,E[i],N)
        mu=max_matching(adj)
        assert mu==(m+1)//2, (mods,mu,m)
    return m,(m+1)//2

def main():
    cases=[(3,),(5,),(9,),(3,3)]
    rows=[check(c) for c in cases]
    print("cases",rows)
    print("VERIFY_OK")
if __name__=="__main__":
    main()
