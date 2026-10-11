#!/usr/bin/env python3
"""Independent finite diagnostics for an exact random-projection perimeter theorem."""
import math
from itertools import product
import mpmath as mp
import numpy as np
from scipy.spatial import ConvexHull

mp.mp.dps = 45


def H(d):
    return mp.hyper([mp.mpf('-0.5'), mp.mpf('0.5'), mp.mpf('1.5')],
                    [mp.mpf(1), mp.mpf(d + 1)/2], 1)


def expected_pair(d):
    return mp.pi * H(d) / (2*(d-1))


def independent_beta_integral(d):
    # Angular average equals (2/pi)*EllipticE(t), using the parameter t.
    c = mp.gamma(mp.mpf('1.5'))*mp.gamma(mp.mpf(d-1)/2)/mp.gamma(mp.mpf(d)/2)
    z = mp.mpf(d-2)/2
    # The substitution t=sin(phi)^2 removes the singular Beta endpoint.
    f = lambda phi: (2*mp.sin(phi)**2*mp.cos(phi)**(d-3)
                     * (2/mp.pi)*mp.ellipe(mp.sin(phi)**2))
    return c*z*mp.quad(f,[0,mp.pi/4,mp.pi/2])


def first(d, lengths):
    return (mp.sqrt(mp.pi)*mp.gamma(mp.mpf(d)/2)
            /mp.gamma(mp.mpf(d+1)/2)*sum(lengths))


def second(d, lengths):
    diag = (mp.mpf(8)/d)*sum(x*x for x in lengths)
    off = 8*expected_pair(d)*sum(lengths[i]*lengths[j]
                      for i in range(d) for j in range(i+1,d))
    return diag+off


max_integral_error = mp.mpf(0)
for d in [3,4,5,7,10]:
    a = expected_pair(d)
    b = independent_beta_integral(d)
    max_integral_error = max(max_integral_error,abs(a-b))
    assert abs(a-b)<mp.mpf('1e-29'),(d,a,b)

assert abs(second(3,[1,1,1])-mp.mpf('22.237117433439470'))<mp.mpf('1e-15')
assert abs(second(4,[1,1,1,1])-mp.mpf('28.495793565063314'))<mp.mpf('1e-15')
assert abs(second(4,[1,1,1,1])-first(4,[1,1,1,1])**2
            -mp.mpf('0.051349120618869646'))<mp.mpf('1e-15')

# Diagnostics are independent of hypergeometric evaluation: project vertices
# of each small cube and independently take a two-dimensional convex hull.
rng = np.random.default_rng(20261008)
max_hull_error=0.0
for d in [3,4,5]:
    vertices=np.array(list(product([-0.5,0.5],repeat=d)),dtype=float)
    for _ in range(35):
        q,_ = np.linalg.qr(rng.standard_normal((d,2)))
        xy=vertices@q
        hull=ConvexHull(xy)
        perimeter=float(sum(np.linalg.norm(xy[hull.vertices[i]]-
                                           xy[hull.vertices[(i+1)%len(hull.vertices)]])
                            for i in range(len(hull.vertices))))
        zonotope=2*sum(np.linalg.norm(q[i,:]) for i in range(d))
        max_hull_error=max(max_hull_error,abs(perimeter-zonotope))
        assert abs(perimeter-zonotope)<4e-13

# Haar-QR Monte Carlo checks genuine mixed edge moments, with tolerances
# appropriate to sampling noise (not a proof of exactness).
mc_summary=[]
for d in [3,4,5,7]:
    n=25000
    lengths=np.arange(1,d+1,dtype=float)/d
    values=np.empty(n)
    cross=np.empty(n)
    for j in range(n):
        q,_=np.linalg.qr(rng.standard_normal((d,2)))
        edge_lengths=np.linalg.norm(q,axis=1)
        values[j]=2*np.dot(lengths,edge_lengths)
        cross[j]=edge_lengths[0]*edge_lengths[1]
    exact_first=float(first(d,lengths))
    exact_second=float(second(d,lengths))
    exact_cross=float(expected_pair(d))
    assert abs(values.mean()-exact_first)<0.035
    assert abs(np.mean(values**2)-exact_second)<0.27
    assert abs(cross.mean()-exact_cross)<0.012
    mc_summary.append((d,values.mean(),np.mean(values**2),cross.mean()))

for d in [10,25,50]:
    var=second(d,[mp.mpf(1)]*d)-first(d,[mp.mpf(1)]*d)**2
    assert 0<var<mp.mpf('0.147')

print('VERIFY_OK')
print('max_integral_comparison_error =',mp.nstr(max_integral_error,8))
print('max_convex_hull_perimeter_error =',f'{max_hull_error:.3e}')
print('E_four_cube_squared_perimeter =',mp.nstr(second(4,[1]*4),24))
print('Var_four_cube_perimeter =',mp.nstr(second(4,[1]*4)-first(4,[1]*4)**2,24))
print('variance_limit =',mp.nstr(8-mp.mpf(5)*mp.pi/2,24))
print('haar_orthotope_diagnostics =',mc_summary)
