"""Independent finite geometry checks for multi-plane unit-disk convex hulls.

Python 3, numpy, scipy. Discretizes actual disk boundary circles and obtains
Euclidean surface and volume from a three-dimensional convex hull; separately
integrates the analytic surface patches with Gauss--Legendre quadrature.
These tests do not replace the exact analytic proof.
"""
import math
import numpy as np
from scipy.spatial import ConvexHull
from numpy.polynomial.legendre import leggauss


def estimate(angles, radius=1.0, sample_count=300):
    theta = np.arange(sample_count) * (2*math.pi/sample_count)
    points = []
    for a in angles:
        # Three-dimensional actual boundary points on each disk, not on the derived hull.
        points.extend(np.column_stack((radius*np.cos(theta),
                                       radius*np.sin(theta)*np.cos(a),
                                       radius*np.sin(theta)*np.sin(a))))
    ch = ConvexHull(np.concatenate([np.asarray(points)]).reshape(-1,3))
    vertices = sorted([((a % math.pi)+math.pi) % math.pi for a in angles])
    arcs = []
    for i,a in enumerate(vertices):
        b = vertices[(i+1)%len(vertices)] + (math.pi if i==len(vertices)-1 else 0)
        arcs.append(b-a)
    # Q has doubled gaps, each arc repeated twice.
    q_area = sum(math.sin(g) for g in arcs)
    predicted_V = 4.0/3.0 * radius**3 * q_area
    predicted_S = radius**2 * (2*math.pi+2*q_area)
    xs, ws = leggauss(180)
    quadrature_S = radius**2*2*sum(sum(ws*(2*math.sin(g/2))*
        np.sqrt(1-xs*xs*(math.sin(g/2)**2))) for g in arcs)
    return ch.volume, ch.area, predicted_V, predicted_S, quadrature_S


def main():
    for angles in ([0.0,math.pi/2], [0.0,0.38], [0.0,0.6,1.5],
                   [0.0,0.05,0.7,2.1], [0.0,math.pi/5,2*math.pi/5,3*math.pi/5,4*math.pi/5]):
        cv, cs, av, aa, sq = estimate(angles)
        err_v = abs(av-cv)/av
        err_s = abs(aa-cs)/aa
        assert err_v < 0.0008, (angles,err_v)
        assert err_s < 0.0008, (angles,err_s)
        assert abs(aa-sq) < 1e-12, (angles,aa,sq)
        assert abs((aa-2*math.pi)-1.5*av) < 5e-14
        print('k=',len(angles),'V=',format(av,'.12f'),'S=',format(aa,'.12f'),
              'polyhedral relative errors=',format(err_v,'.4g'),format(err_s,'.4g'))
    for k in range(2,20):
        eqangles=[j*math.pi/k for j in range(k)]
        _,_,_,s,_=estimate(eqangles,sample_count=60)
        assert abs(s-(2*math.pi+2*k*math.sin(math.pi/k)))<3e-13
    rng=np.random.default_rng(20261009)
    for k in range(2,31):
        for repetition in range(70):
            gap_weights=rng.dirichlet(np.ones(k))
            gaps=math.pi*gap_weights
            v=4/3*sum(math.sin(g) for g in gaps)
            vmax=4/3*k*math.sin(math.pi/k)
            assert v <= vmax + 1e-12
            if k>2 or max(gaps)-min(gaps)>1e-8:
                assert v < vmax
    print('VERIFY_OK')

if __name__=='__main__':
    main()
