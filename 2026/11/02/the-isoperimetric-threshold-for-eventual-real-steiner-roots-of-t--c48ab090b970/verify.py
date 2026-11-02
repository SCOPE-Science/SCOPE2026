#!/usr/bin/env python3
"""Reproducible supplementary checks of tall-pyramid Steiner asymptotics.

Requires Python 3, NumPy, and SymPy. Numerical sampling is not a proof of a
continuum statement; the analytic surface-area and support-function arguments in
RESULT.md provide the proof.
"""
import math
import numpy as np
import sympy as sy


def polygon_coefficients(vertices, apex_xy, height):
    """Independent polyhedral edge/face computation of V, S and M.

    CCW polygon vertices, apex above apex_xy. M is half the sum of edge lengths
    times exterior dihedral angles (the 3D Steiner mean-curvature coefficient).
    """
    v = np.asarray(vertices, dtype=float)
    apex = np.array([*apex_xy, float(height)])
    n = len(v)
    assert n >= 3
    area = sum(np.linalg.det(np.stack([v[i], v[(i+1) % n]])) for i in range(n))/2
    assert area > 0
    perimeter = 0.0
    lateral_area = 0.0
    normals = []
    m = 0.0
    for i in range(n):
        v0 = np.r_[v[i],0.0]
        v1 = np.r_[v[(i+1)%n],0.0]
        edge = v1-v0
        edge_length = np.linalg.norm(edge)
        perimeter += edge_length
        vec = np.cross(edge, apex-v0)
        lateral_area += np.linalg.norm(vec)/2
        side_normal = vec/np.linalg.norm(vec)
        normals.append(side_normal)
        m += edge_length*math.acos(np.clip(np.dot(side_normal,[0.,0.,-1.]),-1,1))/2
    for i in range(n):
        edge_length = np.linalg.norm(apex-np.r_[v[i],0.0])
        m += edge_length*math.acos(np.clip(np.dot(normals[(i-1)%n],normals[i]),-1,1))/2
    return area*height/3, area+lateral_area, m, area, perimeter


def check_roots(v, apex_xy, h, expect_all_real):
    V,S,M,A,P = polygon_coefficients(v,apex_xy,h)
    roots = np.roots([4*math.pi/3,M,S,V])
    max_im = max(abs(z.imag) for z in roots)
    if expect_all_real:
        assert max_im < 1e-7, (h,roots)
        assert np.all(roots.real < 0), roots
    else:
        assert max_im > 1e-3, (h,roots)
    assert abs((S-P*h/2)-A) < 100/h, (S,A,P,h)
    assert abs(M-math.pi*h-math.pi*P/4) < 100/h, (M,P,h)
    return np.sort_complex(roots),A,P


def main():
    p=sy.symbols('p',positive=True)
    tt=-p/(4*sy.pi)
    area=3*p*p/(16*sy.pi)
    k=4*sy.pi*tt**3/3+sy.pi*p*tt**2/4+area*tt
    assert sy.simplify(k - p**3*(3*sy.pi-13)/(192*sy.pi**2))==0
    assert sy.simplify((-k/sy.pi)-p**3*(13-3*sy.pi)/(192*sy.pi**3))==0
    print('Critical double-root splitting coefficient: symbolic PASS')

    for n in [3,4,5,6,8,16]:
        v=np.array([(math.cos(2*math.pi*j/n),math.sin(2*math.pi*j/n)) for j in range(n)])
        roots,A,P=check_roots(v,(0.17,-0.09),3000.,expect_all_real=(n==3))
        Q=4*math.pi*A/P**2
        assert (Q<0.75)==(n==3)
        print(f'{n}-gon: Q={Q:.10f}, max imaginary root={max(abs(z.imag) for z in roots):.8f}; PASS')

    # A rectangle can attain the critical isoperimetric quotient Q=3/4.
    b=(4*math.pi/3-2)
    ratio=(b+math.sqrt(b*b-4))/2
    v=np.array([[-ratio/2,-.5],[ratio/2,-.5],[ratio/2,.5],[-ratio/2,.5]])
    Q=4*math.pi*ratio/(2*(1+ratio))**2
    assert abs(Q-.75)<1e-14
    for h in [300.,3000.,30000.]:
        roots,A,P=check_roots(v,(0.02,-0.03),h,expect_all_real=True)
        near=sorted(roots,key=lambda z:abs(z+P/(4*math.pi)))[:2]
        c=math.sqrt(P**3*(13-3*math.pi)/(192*math.pi**3))
        observed=abs(near[0].real-near[1].real)/2
        assert abs(observed*math.sqrt(h)/c-1)<.03,(h,observed,c)
        print(f'critical rectangle h={h:.0f}: bounded-root half-gap sqrt(h)={observed*math.sqrt(h):.8f}, predicted={c:.8f}; PASS')

    print('All independent geometric and algebraic checks passed.')

if __name__=='__main__':
    main()
