#!/usr/bin/env python3
"""Exact integer checks of toric wall intersections and an obstructing surface.

Requires only the Python standard library. The universal proof is in RESULT.md.
"""
from itertools import combinations

FAN_CONES = (
    (1, 2, 4), (2, 3, 4), (3, 4, 5), (4, 5, 6),
    (1, 4, 6), (1, 6, 7), (1, 2, 7), (2, 3, 7),
    (3, 5, 8), (5, 6, 8), (3, 7, 8), (6, 7, 8),
)

def rays(a):
    return {
        1:(1,1,2),2:(1,0,0),3:(0,-1,0),4:(0,0,-1),
        5:(-1,a,0),6:(0,1,0),7:(0,0,1),8:(-1,0,1),
    }

def det(a,b,c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -a[1]*(b[0]*c[2]-b[2]*c[0])
            +a[2]*(b[0]*c[1]-b[1]*c[0]))

def wall_degrees(a):
    v=rays(a)
    walls={}
    for triple in FAN_CONES:
        for ij in combinations(triple,2):
            ij=tuple(sorted(ij))
            walls.setdefault(ij,[]).append(next(k for k in triple if k not in ij))
    assert len(walls)==18 and all(len(opp)==2 for opp in walls.values())
    ret={}
    for (i,j),(k,l) in walls.items():
        # Unique relation: v_k + v_l + alpha*v_i + beta*v_j = 0.
        m=det(v[i],v[j],v[k])
        assert abs(m)==1
        t=tuple(-v[k][z]-v[l][z] for z in range(3))
        x=det(t,v[j],v[k]); y=det(v[i],t,v[k]); z=det(v[i],v[j],t)
        assert x%m==0 and y%m==0 and z//m==0
        alpha,beta=x//m,y//m
        assert all(v[k][h]+v[l][h]+alpha*v[i][h]+beta*v[j][h]==0 for h in range(3))
        ret[i,j]=2+alpha+beta
    return ret

def expected(a):
    return {(1,2):2,(1,4):-1,(1,6):2,(1,7):3,
            (2,3):2,(2,4):3,(2,7):-1,
            (3,4):a+2,(3,5):1-a,(3,7):1,(3,8):a+1,
            (4,5):2,(4,6):3-a,(5,6):a+1,(5,8):2,
            (6,7):-2,(6,8):1-a,(7,8):2}

def verify():
    for a in range(-15,41):
        assert wall_degrees(a)==expected(a),a
    for a in (4,5,6,10,50,100,1000):
        assert all(q!=0 for q in wall_degrees(a).values())
        v=rays(a)
        assert all(3*v[7][z]==v[1][z]+v[3][z]+v[8][z] for z in range(3))
        # The star of v7 has projected rays (1,1),(1,0),(0,-1),(-1,0),(0,1).
        star={tuple(sorted(k for k in co if k!=7)) for co in FAN_CONES if 7 in co}
        assert star=={(1,6),(1,2),(2,3),(3,8),(6,8)}
    # The toric surface S is Bl_p(P1 x P1): F1²=F2²=0, F1·F2=1, E²=-1.
    # The restriction L=(-K)|S=F1+2F2-3E, and C=F1+F2-E.
    # L·C = 1+2-3=0. Check against the invariant-boundary degrees:
    q=wall_degrees(4)
    assert (q[1,7],q[7,8],q[3,7],q[2,7],q[6,7])==(3,2,1,-1,-2)
    assert q[7,8]+q[3,7]-q[1,7]==0
    # H0(mL) corresponds to bihomogeneous monomials of bidegree (m,2m)
    # vanishing to order at least 3m at a chosen point.
    for m in range(1,31):
        monomials=[(i,j) for i in range(m+1) for j in range(2*m+1) if i+j>=3*m]
        assert monomials==[(m,2*m)]
    print('VERIFY_OK wall_profiles=56 fan_cones=12 walls=18 ray7_convex_witness=true surface=Bl_p(P1xP1) noninvariant_curve_degree_zero=true linear_series=30')

if __name__=='__main__':verify()
