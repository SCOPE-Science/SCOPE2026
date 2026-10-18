"""Deterministic finite regression checks for the sharp tetrahedral envelope.

This is not a proof for arbitrary polygon order or twist; see RESULT.md.
Requires only the Python standard library.
"""
from math import sin, cos, pi, isclose
from itertools import combinations


def det3(a,b,c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -a[1]*(b[0]*c[2]-b[2]*c[0])
            +a[2]*(b[0]*c[1]-b[1]*c[0]))


def predicted(n, theta, R=1., h=1.):
    step=2*pi/n if n%2 == 0 else pi/n
    longest=2*R if n%2 == 0 else 2*R*cos(pi/(2*n))
    delta=abs((theta-pi/2+step/2) % step - step/2)
    return h*longest**2*cos(delta)/6


def enumerate_tetrahedra(n, theta, R=1., h=1.):
    pts=[(R*cos(2*pi*j/n),R*sin(2*pi*j/n),0.) for j in range(n)]
    pts += [(R*cos(theta+2*pi*j/n),R*sin(theta+2*pi*j/n),h) for j in range(n)]
    best=0.
    maximizing_layer_splits=set()
    for inds in combinations(range(2*n),4):
        v=[pts[j] for j in inds]
        u=tuple(v[1][i]-v[0][i] for i in range(3))
        w=tuple(v[2][i]-v[0][i] for i in range(3))
        z=tuple(v[3][i]-v[0][i] for i in range(3))
        volume=abs(det3(u,w,z))/6
        if volume>best+1e-9:
            best=volume
            maximizing_layer_splits={sum(j<n for j in inds)}
        elif abs(volume-best)<1e-9:
            maximizing_layer_splits.add(sum(j<n for j in inds))
    return best,maximizing_layer_splits


def run():
    ncases=0
    for n in range(3,14):
        step=2*pi/n if n%2==0 else pi/n
        for fraction in [0,0.17,0.5,0.79,1]:
            for R,h in [(1.,1.),(1.2,0.7)]:
                theta=step*fraction
                brute,types=enumerate_tetrahedra(n,theta,R,h)
                exact=predicted(n,theta,R,h)
                assert isclose(brute,exact,rel_tol=2e-12,abs_tol=1e-10), (n,theta,brute,exact)
                if n>=4:
                    assert types=={2}, (n,theta,types)
                ncases+=1
    # Direct exact-formula specializations, tested by floating evaluation.
    assert isclose(predicted(3,0),3**0.5/4,abs_tol=1e-12)
    assert isclose(predicted(3,pi/6),1/2,abs_tol=1e-12)
    assert isclose(predicted(4,0),2/3,abs_tol=1e-12)
    assert isclose(predicted(4,pi/4),2**0.5/3,abs_tol=1e-12)
    assert isclose(predicted(6,0),3**0.5/3,abs_tol=1e-12)
    assert isclose(predicted(6,pi/6),2/3,abs_tol=1e-12)
    print(f'PASS: {ncases} vertex-quadruple enumerations; order 3..13, 5 twists, 2 scales; 6 specializations')

if __name__=='__main__':run()
