"""Supplementary finite-matrix checks of positive spectral-coupling root rates."""
import math
import numpy as np


def s_norm(matrix, p):
    values = np.linalg.svd(matrix, compute_uv=False)
    if p == math.inf:
        return float(np.max(values))
    return float(np.sum(values ** p) ** (1.0 / p))


def rates(a, b, t):
    support = [(float(ai), float(bj)) for i, ai in enumerate(a) for j, bj in enumerate(b) if t[i, j] != 0]
    if not support:
        raise ValueError("nonzero coupling required")
    return max(bj/ai for ai,bj in support), max(ai/bj for ai,bj in support)


def scaled_root(a, b, t, p, n, mode):
    result = rates(a,b,t)[0 if mode == 1 else 1]
    terms = (b[None, :] / a[:, None]) if mode == 1 else (a[:, None] / b[None, :])
    scaled = t * (terms / result) ** n
    return result * s_norm(scaled, p) ** (1/n)


def main():
    a = np.array([1.0, 2.0, 5.0])
    b = np.array([3.0, 4.0])
    t = np.array([[1.0, 0.0], [0.0, 2.0], [3.0, 0.0]])
    assert rates(a, b, t) == (3.0, 5.0/3.0)
    counter = 0
    for p in (0.5, 0.8, 1.0, 2.0, 4.0, math.inf):
        for mode in (1, -1):
            target = rates(a,b,t)[0 if mode == 1 else 1]
            for n in (20, 48, 80, 120):
                value = scaled_root(a, b, t, p, n, mode)
                assert 0.99999999*target <= value <= target*1.2, (p,mode,n,value,target)
                counter += 1
    # A nontrivial exact intertwiner: common eigenvalue 2 and an entry linking only it.
    a2 = np.array([1., 2., 5.])
    b2 = np.array([2., 4.])
    t2 = np.array([[0., 0.], [7., 0.], [0., 0.]])
    assert rates(a2,b2,t2) == (1.,1.)
    for n in (1,10,100):
        for p in (0.5,1.,2.,math.inf):
            assert abs(scaled_root(a2,b2,t2,p,n,1)-7**(1/n)) < 1e-10
            assert abs(scaled_root(a2,b2,t2,p,n,-1)-7**(1/n)) < 1e-10
            counter += 2
    print("VERIFIED:",counter,"supplementary finite spectral-coupling comparisons")

if __name__ == "__main__":
    main()
