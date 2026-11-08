"""Independent exact invariance and finite-polygon area checks.

Pure standard-library Python; numerical checks only corroborate the full analytic proof.
"""
from fractions import Fraction
from math import cos, pi, sin, sqrt, tan, gcd


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def transpose(A):
    return [[A[j][i] for j in range(2)] for i in range(2)]


def exact_invariant(c):
    c = Fraction(c)
    J = [[2-c, -1], [1, 0]]
    Q = [[Fraction(1), (c-2)/2], [(c-2)/2, Fraction(1)]]
    assert matmul(transpose(J), matmul(Q, J)) == Q
    det = Q[0][0]*Q[1][1]-Q[0][1]*Q[1][0]
    assert det == c*(4-c)/4
    return Q


def shoelace(pts):
    return abs(sum(x*y2-x2*y for (x,y),(x2,y2) in zip(pts,pts[1:]+pts[:1])))/2


def numeric_polygon(n, a=1, h=1):
    assert gcd(a,n)==1 and 0<2*a<n
    c=2*(1-cos(2*pi*a/n))
    r=h*sqrt(4-c)/2
    L=n if n%2==0 else 2*n
    # For an L-gon whose supporting normals are equally spaced,
    # vertices are at the intersections of successive support lines.
    # An arbitrary fixed rotation of all normals preserves the area.
    R=r/cos(pi/L)
    verts=[(R*cos(2*pi*(j+.5)/L),R*sin(2*pi*(j+.5)/L)) for j in range(L)]
    measured=shoelace(verts)/sqrt(c*(4-c)/4)
    theory=(h*h/2)*sqrt((4-c)/c)*L*tan(pi/L)
    assert abs(measured/theory-1)<1e-12, (n,a,measured,theory)
    disk_area=pi*h*h*sqrt((4-c)/c)/2
    assert theory>disk_area
    return n,a,L,measured,theory,disk_area


if __name__=='__main__':
    for c in [Fraction(1,4),Fraction(1),Fraction(2),Fraction(3),Fraction(7,2)]:
        exact_invariant(c)
    results=[]
    for n in range(3,30):
        for a in range(1,(n+1)//2):
            if gcd(a,n)==1:
                results.append(numeric_polygon(n,a))
    assert abs(numeric_polygon(4,1)[4]-2)<1e-12
    assert abs(numeric_polygon(3,1)[4]-1)<1e-12
    assert abs(numeric_polygon(6,1)[4]-3)<1e-12
    print('STOCK_CENTER_AREA_EXACT_Q_AND_POLYGON_OK', 'angles='+str(len(results)))
