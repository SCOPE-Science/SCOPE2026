"""Exact rational checks of the four-point metric free-space ellipsoid formulas.

The all-parameter result is proved analytically; this file tests independently
reconstructed unit-ball vertices and both ellipsoid containment inequalities.
Python 3 standard library only. Execute: python k4_one_edge_verify.py
"""
from fractions import Fraction as F
from itertools import combinations
from random import Random


def det(m):
    return (m[0][0] * (m[1][1]*m[2][2] - m[1][2]*m[2][1])
          - m[0][1] * (m[1][0]*m[2][2] - m[1][2]*m[2][0])
          + m[0][2] * (m[1][0]*m[2][1] - m[1][1]*m[2][0]))


def vertices(t):
    # Constraints in first octant, written as v dot (X,Y,Z) <= rhs.
    hs = [((-1,0,0),F(0)), ((0,-1,0),F(0)), ((0,0,-1),F(0)),
          ((1,0,0),t), ((0,1,0),F(1)), ((1,1,2),F(2))]
    out = set()
    for comb in combinations(hs,3):
        mat=[list(h[0]) for h in comb]
        d=det(mat)
        if d==0:
            continue
        rhs=[h[1] for h in comb]
        x=[]
        for j in range(3):
            h=[r.copy() for r in mat]
            for k in range(3):h[k][j]=rhs[k]
            x.append(det(h)/d)
        if all(sum(F(a)*v for a,v in zip(coeff,x)) <= b for coeff,b in hs):
            out.add(tuple(x))
    return out


def p_max(t,a,b,c):
    return max(a*x*x + b*y*y + c*z*z for x,y,z in vertices(t))


def q_max(t,a,b,c):
    return max(1/(t*t*a),1/b,1/(4*a)+1/(4*b)+1/c)


def expected(t):
    if t<=1:
        a,b,c=1/(t*t),F(1),4/(3-t*t)
        val=(7-2*t-t*t)/(3-t*t)
        assert q_max(t,a,b,c)==1
        assert p_max(t,a,b,c)==val
    else:
        a,b,c=(3-t)/4,(t+1)/4,F(1)
        val=1+4/((t+1)*(3-t))
        assert p_max(t,a,b,c)==1
        assert q_max(t,a,b,c)==val
    return val


def main():
    rng=Random(1729)
    count=0
    for k in range(1,49):
        t=F(k,24)
        v=vertices(t)
        assert len(v)>=5
        value=expected(t)
        # Nonoptimal diagonal ellipsoids cannot improve the claimed distortion.
        for _ in range(48):
            a=F(rng.randrange(1,61),rng.randrange(1,61))
            b=F(rng.randrange(1,61),rng.randrange(1,61))
            c=F(rng.randrange(1,61),rng.randrange(1,61))
            assert p_max(t,a,b,c)*q_max(t,a,b,c)>=value
            count+=1
    assert expected(F(1))==2
    assert expected(F(2))==F(7,3)
    print('K4_ONE_EDGE_EXACT_OK',count,'ellipsoid tests; 48 rational parameters')


if __name__=='__main__':main()
