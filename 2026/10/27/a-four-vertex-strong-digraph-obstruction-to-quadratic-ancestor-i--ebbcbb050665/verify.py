#!/usr/bin/env python3
"""Exact reproducibility checks for a directed-arborescence ancestor counterexample."""
from fractions import Fraction
from itertools import product

VERTICES=(0,1,2,3)
ROOT=0
B=1
ARCS={(0,1): 1, (1,0): 'z', (1,2): 1,
      (2,1): 'z', (2,3): 1, (3,1): 'z', (3,0): 1}

def paths_to_root(p):
    paths={}
    for start in (1,2,3):
        visited={start}
        path=[start]
        v=start
        while v != ROOT:
            v=p[v]
            if v in visited: return None
            visited.add(v)
            path.append(v)
        paths[start]=tuple(path)
    return paths

def enumerate_trees(z):
    opts={v:[(w,z if raw=='z' else Fraction(raw)) for (u,w),raw in ARCS.items() if u==v] for v in (1,2,3)}
    out=[]
    for selected in product(*(opts[v] for v in (1,2,3))):
        p={i:chosen[0] for i,chosen in zip((1,2,3),selected)}
        ps=paths_to_root(p)
        if ps is None: continue
        wt=selected[0][1]*selected[1][1]*selected[2][1]
        px,py=ps[2],ps[3]
        lca=next(v for v in px if v in py)
        out.append((tuple(p[v] for v in (1,2,3)),wt, B in px, B in py, lca==B))
    return out

def strongly_connected():
    for start in VERTICES:
        seen={start}; queue=[start]
        for v in queue:
            for (u,w) in ARCS:
                if u==v and w not in seen:
                    seen.add(w);queue.append(w)
        assert seen == set(VERTICES)

def check():
    strongly_connected()
    for k in range(0,17):
        z=Fraction(1,2**k)
        rows=enumerate_trees(z)
        assert len(rows)==5
        Z=sum((t[1] for t in rows),Fraction(0))
        hx=sum((t[1] for t in rows if t[2]),Fraction(0))/Z
        hy=sum((t[1] for t in rows if t[3]),Fraction(0))/Z
        a=sum((t[1] for t in rows if t[4]),Fraction(0))/Z
        assert Z==1+z+2*z*z+z*z*z
        assert hx==z*z*(z+2)/Z
        assert hy==z*z*(z+1)/Z
        assert a==z*z*z/Z
        fx=hy/(hx+hy)
        fy=hx/(hx+hy)
        assert fx+fy==1
        ratio=2*fx*fy*a/(fx*hx+fy*hy)**2
        assert ratio==Z/(2*z*(z+1)*(z+2))
        if k==3:
            assert Z==Fraction(593,512)
            assert (hx,hy,a)==(Fraction(17,593),Fraction(9,593),Fraction(1,593))
            assert (fx,fy)==(Fraction(9,26),Fraction(17,26))
            assert ratio==Fraction(593,306)
    assert sorted(r[0] for r in enumerate_trees(Fraction(1,8))) == [
        (0,1,0),(0,1,1),(0,3,0),(0,3,1),(2,3,0)]
    print('PASS: directed strong connectivity, five-tree classification, 17 rational parameter checks, exact limit formula, and rational witness ratio 593/306.')
if __name__=='__main__': check()
