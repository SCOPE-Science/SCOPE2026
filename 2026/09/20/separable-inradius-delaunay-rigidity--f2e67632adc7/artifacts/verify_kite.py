"""Standalone numerical checks for the cyclic-kite formulas and power examples."""

from math import cos, hypot, pi, sin, sqrt


def area(a, b, c):
    return abs((b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])) / 2.0


def dist(a, b):
    return hypot(a[0]-b[0], a[1]-b[1])


def inradius(a, b, c):
    return 2.0 * area(a, b, c) / (dist(a,b)+dist(b,c)+dist(c,a))


def kite(alpha, lam=1.0, radial_D=1.0):
    A=(lam,0.0)
    C=(-lam,0.0)
    B=(lam*cos(2*alpha),lam*sin(2*alpha))
    D=(radial_D*lam*cos(2*alpha),-radial_D*lam*sin(2*alpha))
    return A,B,C,D


def sums(alpha, p=1.0, radial_D=1.0):
    A,B,C,D=kite(alpha,1.0,radial_D)
    ac=(inradius(A,B,C)**p + inradius(A,C,D)**p)
    bd=(inradius(A,B,D)**p + inradius(B,C,D)**p)
    return ac,bd


def main():
    alpha=pi/6
    A,B,C,D=kite(alpha)
    u1=inradius(A,B,C)
    u2=inradius(A,C,D)
    v=inradius(A,B,D)
    w=inradius(B,C,D)
    u=(sqrt(3)-1)/2
    v_exact=(2*sqrt(3)-3)/2
    w_exact=0.5
    assert abs(u1-u)<1e-12 and abs(u2-u)<1e-12
    assert abs(v-v_exact)<1e-12 and abs(w-w_exact)<1e-12
    assert abs((v+w)-2*u)<1e-12

    # p>1: moving D outward makes AC uniquely Delaunay; BD keeps larger p-sum.
    ac2,bd2=sums(alpha,p=2.0,radial_D=1.01)
    assert bd2>ac2

    # 0<p<1: moving D inward makes BD uniquely Delaunay; AC keeps larger p-sum.
    ach,bh=sums(alpha,p=0.5,radial_D=0.99)
    assert ach>bh

    print("cyclic formulas: OK")
    print("p=2 outward example: AC-BD =", ac2-bd2)
    print("p=1/2 inward example: AC-BD =", ach-bh)


if __name__ == "__main__":
    main()
