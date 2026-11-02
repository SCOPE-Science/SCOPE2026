#!/usr/bin/env python3
"""Exact unfolding and moment checks for a marked unit-cube surface.

Run: python3 verify_cube_geodesic_law.py
Only Python's standard library is required.
"""
from fractions import Fraction as F
from itertools import product
from math import acos, asin, comb, pi, sqrt
from random import Random

VERTICES = list(product((0, 1), repeat=3))
FACES = {f'{"xyz"[j]}{h}': [v for v in VERTICES if v[j] == h]
         for j in range(3) for h in (0, 1)}
ADJ = {k: [l for l in FACES if l != k and
           len(set(FACES[k]) & set(FACES[l])) == 2]
       for k in FACES}

def plus(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def half(a): return tuple(x/F(2) for x in a)

def paths_to(target):
    out = []
    def rec(path):
        if path[-1] == target:
            out.append(path)
        else:
            for q in ADJ[path[-1]]:
                if q not in path: rec(path+[q])
    rec(['z1'])
    return out

def unfold(path):
    maps = [{v: (F(v[0]), F(v[1])) for v in FACES['z1']}]
    for u,v in zip(path[:-1],path[1:]):
        old = maps[-1]
        a,b = sorted(set(FACES[u]) & set(FACES[v]))
        A,B = old[a],old[b]
        edge = sub(B,A)
        n = (-edge[1],edge[0])
        midpoint = half(plus(A,B))
        center = tuple(sum(old[w][j] for w in FACES[u])/4 for j in (0,1))
        if dot(n,sub(center,midpoint))>0:
            n = (-n[0],-n[1])
        new = {a:A,b:B}
        for shared in (a,b):
            others = [w for w in FACES[v] if w not in new and
                      sum(x!=y for x,y in zip(shared,w)) == 1]
            assert len(others)==1
            new[others[0]] = plus(new[shared],n)
        assert len(new)==4
        maps.append(new)
    return maps[-1]

def source_image(path, target):
    mapping = unfold(path)
    if target == 'z0':
        v0, v1, v2 = (0,0,0),(1,0,0),(0,1,0)
    elif target == 'x0':
        v0, v1, v2 = (0,0,0),(0,1,0),(0,0,1)
    else: raise ValueError(target)
    origin = mapping[v0]
    e1,e2 = sub(mapping[v1],origin),sub(mapping[v2],origin)
    assert dot(e1,e1)==dot(e2,e2)==1 and dot(e1,e2)==0
    p = (F(1,2),F(1,2))
    return (dot(sub(p,origin),e1),dot(sub(p,origin),e2))

def gap_at_corner(s,c,q):
    return sum((q[i]-s[i])**2 - (q[i]-c[i])**2 for i in range(2))

def dominated(s,c):
    return all(gap_at_corner(s,c,q)>=0 for q in product((F(0),F(1)),repeat=2))

def check_unfoldings():
    bottom_candidates = ((F(-3,2),F(1,2)),(F(5,2),F(1,2)),
                         (F(1,2),F(-3,2)),(F(1,2),F(5,2)))
    side_candidates = ((F(1,2),F(3,2)),)
    for target, expected, candidates in (('z0',28,bottom_candidates),
                                          ('x0',26,side_candidates)):
        paths = paths_to(target)
        assert len(paths)==expected, (target,len(paths))
        centers = [source_image(path,target) for path in paths]
        assert all(any(dominated(c,s) for s in candidates) for c in centers)
        assert all(s in centers for s in candidates)
        print('Exact unfolding dominance:',target,len(paths),'simple face sequences')

def moment(k):
    # Integrate the polynomials on the top square, four sides and opposite square.
    T=S=B=F(0)
    for j in range(k+1):
        Uj = F(1,4**j*(2*j+1))
        T += comb(k,j)*Uj*F(1,4**(k-j)*(2*(k-j)+1))
        m=k-j
        V = ((F(3,2)**(2*m+1))-(F(1,2)**(2*m+1)))/(2*m+1)
        S += comb(k,j)*Uj*V
        for a in range(2*j+1):
            for b in range(2*m+1):
                B += 8*comb(k,j)*comb(2*j,a)*comb(2*m,b)*F(3,2)**(2*j-a)*F(-1,2)**(2*m-b)*F(1,(a+1)*(a+b+2)*2**(a+b+2))
    return (T+4*S+B)/6, (T,S,B)

def H(r,t):
    t = min(max(t,0.),r)
    return .5*(t*sqrt(max(0.,r*r-t*t))+r*r*asin(t/r))

def top_area(r):
    if r<=0: return 0.
    if r<=.5:return pi*r*r
    if r<sqrt(.5): return pi*r*r-4*r*r*acos(.5/r)+2*sqrt(r*r-.25)
    return 1.

def side_area(r):
    if r<=.5:return 0.
    if r<=sqrt(.5): return 2*(H(r,r)-H(r,.5))
    if r<sqrt(2.5):
        v0=sqrt(r*r-.25)
        return v0-.5+2*(H(r,min(r,1.5))-H(r,v0))
    return 1.

def opposite_area(r):
    if r<=1.5: return 0.
    if r>=2: return 1.
    if r<=sqrt(2.5): return 8*(H(r,r)-H(r,1.5))
    s0=(sqrt(2*r*r-4)-1)/2
    return 8*(.5*s0-.5*s0*s0+H(r,r)-H(r,1.5+s0))

def cdf(r):
    return (top_area(r)+4*side_area(r)+opposite_area(r))/6

def sample_distance_squared(face,rng):
    a,b=rng.random(),rng.random()
    if face==0: return (a-.5)**2+(b-.5)**2
    if face<=4: return (a-.5)**2+(b+.5)**2
    return min((a+1.5)**2+(b-.5)**2,
               (a-2.5)**2+(b-.5)**2,
               (a-.5)**2+(b+1.5)**2,
               (a-.5)**2+(b-2.5)**2)

def check_cdf():
    thresholds=(0.,.5,sqrt(.5),1.5,sqrt(2.5),2.)
    for r in thresholds:
        assert -.00000001<=cdf(r)<=1.00000001
        if r>0: assert abs(cdf(r-1e-7)-cdf(r+1e-7))<.00002
    grid=[2*i/3000 for i in range(3001)]
    assert all(-1e-9<=cdf(r)<=1+1e-9 for r in grid)
    assert all(cdf(b)>=cdf(a)-1e-9 for a,b in zip(grid,grid[1:]))
    assert abs(cdf(2.)-1.)<1e-13
    N=180000
    rng=Random(4273)
    ds=sorted(sqrt(sample_distance_squared(i%6,rng)) for i in range(N))
    import bisect
    error=max(abs(bisect.bisect_right(ds,r)/N-cdf(r)) for r in grid)
    assert error<.006, error
    print('CDF: 3001 monotonicity/boundary probes, 180000 sampled distances, maximum empirical discrepancy',error)

if __name__=='__main__':
    check_unfoldings()
    expected = [F(1),F(23,18),F(451,180),F(331,56),F(389423,25200)]
    for i,val in enumerate(expected):
        got,components=moment(i)
        assert got==val,(i,got,val)
        print('Exact even moment',i, str(got),'face terms',*[str(a) for a in components])
    check_cdf()
    print('All checks passed.')
