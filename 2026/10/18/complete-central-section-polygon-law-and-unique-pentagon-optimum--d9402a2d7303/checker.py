"""Independent numerical and combinatorial tests for central-section laws of triangular prisms.

The executable deliberately uses direct edge-sign crossings for its Monte Carlo route,
not the combinatorial classification used in the mathematical proof.
"""
import math
import numpy as np
from scipy.optimize import brentq


def probabilities(t):
    if t <= 0:
        raise ValueError('height/radius must be positive')
    phi = math.acos((t*t+0.5)/(1+t*t))
    beta = math.acos((t*t-0.5)/(1+t*t))
    p3 = 1-3*phi/math.pi
    mean = (6*math.atan(t)+6*beta)/math.pi
    p5 = mean-4+p3
    p4 = 1-p3-p5
    return np.array([p3,p4,p5]),mean


def objective(t):
    return 1 + t/math.sqrt(4*t*t+3) - 2*math.sqrt(3)*t/math.sqrt(4*t*t+1)


def simulate(t,count=220_000,seed=29):
    rng = np.random.default_rng(seed)
    phi = 2*np.pi*np.arange(3)/3
    basal = np.column_stack([np.cos(phi),np.sin(phi)])
    vertices = np.concatenate([np.column_stack([basal,np.full(3,t)]),
                               np.column_stack([basal,np.full(3,-t)])])
    edges = [(0,1),(1,2),(2,0),(3,4),(4,5),(5,3),
             (0,3),(1,4),(2,5)]
    counts=np.zeros(3,dtype=np.int64)
    for low in range(0,count,50000):
        n=min(50000,count-low)
        normals = rng.standard_normal((n,3))
        values=normals @ vertices.T
        cross=np.zeros(n,dtype=np.int64)
        for a,b in edges:
            cross += (values[:,a]*values[:,b]<0)
        if not np.all(np.isin(cross,[3,4,5])):
            raise AssertionError(f'unexpected section counts {np.unique(cross)}')
        counts += np.bincount(cross-3,minlength=3)
    return counts/count


def main():
    root=brentq(objective,0.1,2,xtol=1e-15)
    assert abs(root-0.5314695510636087)<1e-12
    for t in [0.1,0.3,0.5314695510636087,1.,3.]:
        formula, expected = probabilities(t)
        observed=simulate(t)
        bound=0.008
        assert np.max(np.abs(formula-observed))<bound,(t,formula,observed)
        assert abs(sum(formula)-1)<1e-12
        assert abs(expected-(3*formula[0]+4*formula[1]+5*formula[2]))<1e-12
        print(f't={t:.12f} exact={np.round(formula,7)} simulated={np.round(observed,7)}')
    for t in np.geomspace(1e-5,1e5,2001):
        assert 0 <= probabilities(t)[0].min()+1e-13
        assert abs(sum(probabilities(t)[0])-1)<1e-12
        # Strictly negative derivative of the first-order condition.
        fd=3/(4*t*t+3)**1.5 - 2*math.sqrt(3)/(4*t*t+1)**1.5
        assert fd < 0
    for t in np.geomspace(1e-4,1e4,401):
        if abs(t-root)>0.00001:
            assert probabilities(t)[0][2]<probabilities(root)[0][2]
    print('unique maximum',root,'pentagon probability',probabilities(root)[0][2])
    print('ALL NUMERICAL AND DIRECT EDGE-CROSSING CHECKS PASS')

if __name__ == '__main__':
    main()
