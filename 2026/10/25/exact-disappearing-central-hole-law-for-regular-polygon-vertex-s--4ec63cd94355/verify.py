#!/usr/bin/env python3
"""Check planar polygon union against a derived regular-polygon gap model."""
import math
from shapely.geometry import Polygon
from shapely.affinity import translate
from shapely.ops import unary_union


def vertices(n,rad=1.0,phase=0):
    return [(rad*math.cos(2*math.pi*j/n+phase),rad*math.sin(2*math.pi*j/n+phase)) for j in range(n)]

def verify():
    cases=0
    worst=0.0
    for n in [3,5,7,9,11,15,19]:
        theta=math.pi/n
        h=math.cos(theta)
        cutoff=1/h
        verts=vertices(n)
        for fraction in [0,0.03,0.2,0.5,0.82,0.97,1.0]:
            lam=1+fraction*(cutoff-1)
            eps=1-lam*h
            outer=Polygon(vertices(n,1+lam))
            pieces=[translate(Polygon(vertices(n,lam)),xoff=x,yoff=y) for x,y in verts]
            union=unary_union(pieces)
            if eps>1e-12:
                # the hole is the polar polygon of the vertex-normal fan
                hole=Polygon(vertices(n,eps/h,theta))
                expected=outer.difference(hole)
            else:
                hole=Polygon()
                expected=outer
            sym=expected.symmetric_difference(union).area
            exact=n*math.tan(theta)*eps*eps
            discrepancy=abs(outer.area-union.area-exact)
            assert sym < 2e-7 and discrepancy<2e-7, (n,lam,eps,sym,discrepancy)
            worst=max(worst,sym,discrepancy)
            cases+=1
    print(f'OK {cases} independent union/area checks, worst area error {worst:.3g}')
    for n in [3,5,7,13,37,103]:
        if n%2==0:continue
        th=math.pi/n
        m=n*math.tan(th)*(1-math.cos(th))**2
        a=math.pi**5/(4*n**4)
        print(f'n={n} lambda1 area={m:.14g} / leading_asymptotic={m/a:.8f}')

if __name__=='__main__':verify()
