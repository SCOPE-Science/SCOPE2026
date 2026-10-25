"""Reproducible checks for the near-maximal eight-point spherical polytope tail.
Scientific computation only: finite checks supplement the analytic proof.
"""
import math
from fractions import Fraction
from itertools import combinations
import numpy as np
from scipy.spatial import ConvexHull

# The exact coefficient in the probability law.
matchings = math.factorial(8) // (2**4 * math.factorial(4))
assert matchings == 105
# SO(4)/O(4) volume for the metric induced by eight spherical factors:
# each coordinate-plane generator has norm 2, so multiply its canonical
# Stiefel/Haar volume (32*pi**4) by 2**6.
orb_scale = 2**6
cross_orbit_coefficient = Fraction(matchings * 32 * orb_scale, 2**8)
normal_ellipsoid_factor = 6**6 * 3**3
coefficient_without_pi = cross_orbit_coefficient * normal_ellipsoid_factor / math.factorial(9)
assert coefficient_without_pi == 2916, coefficient_without_pi
print('Exact probability coefficient = 2916/pi^3')

rng = np.random.default_rng(20261024)
max_hull_error = 0.0
max_second_variation_error = 0.0
for repeat in range(90):
    # u_i,v_i are tangent at +/-e_i, respectively.
    u = rng.normal(size=(4, 4)); v = rng.normal(size=(4, 4))
    np.fill_diagonal(u, 0.); np.fill_diagonal(v, 0.)
    u /= 4.; v /= 4.
    x=(u-v)/2.; y=(u+v)/2.
    q2 = .5 * np.sum(y*y) + .5 * sum((x[i,j]+x[j,i])**2 for i,j in combinations(range(4),2))
    for t in (1e-3, 5e-4, 2.5e-4):
        points=[]
        for i in range(4):
            basis=np.eye(4)[i]
            p=(math.sqrt(1-t*t*np.dot(u[i],u[i]))*basis+t*u[i])
            m=(-math.sqrt(1-t*t*np.dot(v[i],v[i]))*basis+t*v[i])
            points.extend([p,m])
        points=np.array(points)
        hull_v=ConvexHull(points).volume
        halfdif=np.array([(points[2*i]-points[2*i+1])/2 for i in range(4)]).T
        det_v=(2./3.)*np.linalg.det(halfdif)
        max_hull_error=max(max_hull_error,abs(hull_v-det_v))
        # determinant tends to 1 - t**2 q2.
        remainder=abs((1-np.linalg.det(halfdif))/(t*t)-q2)
        max_second_variation_error=max(max_second_variation_error,remainder)
assert max_hull_error < 5e-13,max_hull_error
assert max_second_variation_error < 1e-4,max_second_variation_error
print('independent scipy convex hull equality: 270 cases; max discrepancy:',max_hull_error)
print('quadratic form finite-perturbation agreement: max discrepancy:',max_second_variation_error)
print('all checks passed')
