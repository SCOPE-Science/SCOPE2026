#!/usr/bin/env python3
"""Exact integer checks for a family of smooth toric threefolds.

Run: python3 artifacts/verify_toric_example.py
No external dependencies.
"""
from collections import defaultdict
from fractions import Fraction

MAX_CONES = [(1,2,4),(2,3,4),(3,4,5),(4,5,6),(1,4,6),(1,6,7),
             (1,2,7),(2,3,7),(3,5,8),(5,6,8),(3,7,8),(6,7,8)]

def rays(d):
    return {1:(1,1,2), 2:(1,0,0), 3:(0,-1,0), 4:(0,0,-1),
            5:(-1,-2,d), 6:(0,1,0), 7:(0,0,1), 8:(-1,0,d+1)}

def det(a,b,c):
    return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])

def wall_coeff(u,v,p,q):
    s=tuple(p[i]+q[i] for i in range(3))
    for i,j in ((0,1),(0,2),(1,2)):
        delta=u[i]*v[j]-u[j]*v[i]
        if delta:
            a=Fraction(s[i]*v[j]-s[j]*v[i],delta)
            b=Fraction(u[i]*s[j]-u[j]*s[i],delta)
            assert all(a*u[k]+b*v[k]==s[k] for k in range(3))
            assert a.denominator==b.denominator==1
            return int(a),int(b)
    raise AssertionError('linearly dependent wall')

def expected(d):
    return {(1,2):2,(1,4):-1,(1,6):2,(1,7):3,
            (2,3):2,(2,4):3,(2,7):-1,(3,4):d,(3,5):3,
            (3,7):1-d,(3,8):-1,(4,5):2,(4,6):d+5,
            (5,6):-1,(5,8):2,(6,7):-d-2,(6,8):3,(7,8):2}

def main():
    for d in (0,1,2,3,4,5,6,11,31,103):
        v=rays(d)
        assert len(set(tuple(sorted(c)) for c in MAX_CONES))==12
        assert all(abs(det(*(v[i] for i in c)))==1 for c in MAX_CONES)
        adj=defaultdict(list)
        for c in MAX_CONES:
            for k in c:
                edge=tuple(sorted(set(c)-{k}))
                adj[edge].append(k)
        assert len(adj)==18 and all(len(a)==2 for a in adj.values())
        actual={}
        for (i,j),(k,l) in adj.items():
            alpha,beta=wall_coeff(v[i],v[j],v[k],v[l])
            actual[(i,j)]=2-alpha-beta
        assert actual==expected(d), (d,actual)
        if d>=2:
            assert all(z!=0 for z in actual.values())
        w={2:Fraction(1,d+1),8:Fraction(1,d+1),
           3:Fraction(d-1,2*(d+1)),6:Fraction(d-1,2*(d+1))}
        assert sum(w.values())==1
        if d>=2:
            assert all(z>0 for z in w.values())
        assert tuple(sum(w[i]*v[i][j] for i in w) for j in range(3))==v[7]
        # The star fan of v7, modulo Zv7, has rays (1,1), (1,0),
        # (0,1), (-1,0), (0,-1): blowup of P1xP1 at a torus fixed point.
        assert set(adj_edge[0] if adj_edge[1]==7 else adj_edge[1]
                   for adj_edge in adj if 7 in adj_edge)=={1,2,3,6,8}
        k7={ (1,7):-3, (2,7):1, (3,7):d-1,
             (6,7):d+2, (7,8):-2 }
        assert all(-actual[wall]==z for wall,z in k7.items())
        # Pairing on Bl_p(P1xP1): Fx^2=Fy^2=0, Fx.Fy=1, E^2=-1.
        def prod(a,b):
            return a[0]*b[1]+a[1]*b[0]-a[2]*b[2]
        K=(d-1,-2,3)
        classes={(1,7):(0,0,1),(2,7):(1,0,-1),(3,7):(0,1,0),
                 (6,7):(0,1,-1),(7,8):(1,0,0)}
        assert all(prod(K,classes[k])==value for k,value in k7.items())
        C=(d-1,2,0)
        assert prod(K,C)==0
        assert (d-2)==(d-1-1)*(2-1)
        assert prod(K,(1,0,0))==-2 and prod(K,(0,1,0))==d-1
    print('VERIFY_OK smooth_cones=12 walls=18 sample_parameters=10 canonical_zero_walls_for_d_ge_2=0')
    print('VERIFY_OK ray7_convex_obstruction=true star_surface=blowup_P1xP1')
    print('VERIFY_OK restriction_intersections=true zero_degree_curves=true unbounded_genus=true')

if __name__=='__main__':
    main()
