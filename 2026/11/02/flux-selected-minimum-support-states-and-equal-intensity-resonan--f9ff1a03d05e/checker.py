#!/usr/bin/env python3
"""Independent checks for compact zero modes of a magnetic Lieb waveguide lattice.

All finite-patch counts are diagnostics; the accompanying graph proof is global.
"""
import cmath
import itertools
import math


def rectangle_state(t):
    # Edge tuples: (axis, x, y). For horizontal (h,x,y) left-to-right,
    # incidence B entries are +1 at left, -1 at right. For vertical (v,x,y)
    # bottom-to-top the entries are +1 at bottom, -t**x at top.
    return {
        ('h',0,0):-t,
        ('h',1,0):1+0j,
        ('h',0,1):t,
        ('h',1,1):-t*t,
        ('v',0,0):t,
        ('v',1,0):-(1+t),
        ('v',2,0):1+0j,
    }


def incidence_residual(z,t):
    rows={}
    for (axis,x,y),value in z.items():
        start=(x,y)
        end=(x+1,y) if axis=='h' else (x,y+1)
        rows[start]=rows.get(start,0j)+value
        rows[end]=rows.get(end,0j)-(1 if axis=='h' else t**x)*value
    return max((abs(v) for v in rows.values()),default=0.0)


def inverse_participation(z):
    a=[abs(c)**2 for c in z.values() if abs(c)>1e-12]
    return sum(x*x for x in a)/sum(a)**2


def edges(width,height):
    es=[]
    for x in range(width):
        for y in range(height+1):
            es.append(((x,y),(x+1,y)))
    for x in range(width+1):
        for y in range(height):
            es.append(((x,y),(x,y+1)))
    return es


def nontrivial_core(component):
    deg={}
    for a,b in component:
        deg[a]=deg.get(a,0)+1
        deg[b]=deg.get(b,0)+1
    return all(k>=2 for k in deg.values())


def components(support):
    remaining=list(support)
    comps=[]
    while remaining:
        component=[remaining.pop()]
        verts=set(component[0])
        old=-1
        while old!=len(component):
            old=len(component)
            j=0
            while j<len(remaining):
                a,b=remaining[j]
                if a in verts or b in verts:
                    component.append(remaining.pop(j)); verts.add(a); verts.add(b)
                else: j+=1
        comps.append(component)
    return comps


def closed_cycle_area(cyc):
    # For a degree-two simple cycle, traverse its boundary and calculate
    # doubled signed planar area, so |area| counts enclosed unit cells.
    adj={}
    for a,b in cyc:
        adj.setdefault(a,[]).append(b)
        adj.setdefault(b,[]).append(a)
    root=next(iter(adj))
    prev=None
    curr=root
    area2=0
    for step in range(len(cyc)):
        nxt=next(v for v in adj[curr] if v!=prev)
        area2+=curr[0]*nxt[1]-curr[1]*nxt[0]
        prev,curr=curr,nxt
    assert curr==root
    return abs(area2)//2


def small_patch_check(t, expected_min):
    es=edges(3,2)
    good=[]
    tested=0
    for k in range(1,8):
        for idx in itertools.combinations(range(len(es)),k):
            tested+=1
            subsets=[es[i] for i in idx]
            cs=components(subsets)
            if any(not nontrivial_core(c) for c in cs): continue
            for comp in cs:
                verts=set(sum((list(p) for p in comp),[]))
                # For <=7 edges and minimum degree two, either a single cycle
                # or a theta. For theta, 7 edges necessarily include two
                # adjacent unit squares and support a dependency at all flux.
                if len(comp)==len(verts):
                    assert all(sum(v in e for e in comp)==2 for v in verts)
                    a=closed_cycle_area(comp)
                    if abs(t**a-1)<1e-10:
                        good.append((k, 'cycle',a))
                elif len(comp)==len(verts)+1:
                    assert len(comp)>=7
                    good.append((k, 'theta',None))
    assert good and min(row[0] for row in good)==expected_min,(t,expected_min,good[:20])
    return tested, sum(k==expected_min for k,_,_ in good)


def run():
    assertions=0
    tests=[(1+0j,4),(-1+0j,6),
           (cmath.exp(2j*math.pi/3),7),
           (cmath.exp(1.139j),7),
           (cmath.exp(2.337j),7),
           (cmath.exp(3.899j),7)]
    for t,expected in tests:
        z=rectangle_state(t)
        assert incidence_residual(z,t)<1e-11
        assertions+=1
        nonzero=sum(abs(v)>1e-11 for v in z.values())
        assert nonzero==(6 if abs(t+1)<1e-11 else 7)
        assertions+=1
        q=abs(1+t)**2
        formula=(6+q*q)/(6+q)**2
        assert abs(inverse_participation(z)-formula)<1e-12
        assertions+=1
        cnt,m=small_patch_check(t,expected)
        assert m>0
        assertions+=1
        print('phase=',round(cmath.phase(t),7),'minimum=',expected,
              'patch-subsets=',cnt,'minimum-subsets=',m,
              'IPR=',round(formula,12))
    for k in range(1,400):
        phi=2*math.pi*k/400
        t=cmath.exp(1j*phi)
        z=rectangle_state(t)
        assert incidence_residual(z,t)<2e-12
        q=abs(1+t)**2
        ipr=inverse_participation(z)
        assert abs(ipr-(6+q*q)/(6+q)**2)<1e-12
        assert ipr>=1/7-1e-12
        assertions+=3
    for phi in [2*math.pi/3,4*math.pi/3]:
        z=rectangle_state(cmath.exp(1j*phi))
        assert max(abs(abs(v)-1) for v in z.values())<1e-12
        assert abs(inverse_participation(z)-1/7)<1e-12
        assertions+=2
    print('PASS; checks=',assertions)

if __name__=='__main__':run()
