"""Direct finite-character test for mixed-alphabet axis-cross Fourier minors."""
from itertools import product
from math import sqrt
import numpy as np


def test(groups):
    d = len(groups)
    alphabets = [list(product(*(range(n) for n in factors))) for factors in groups]
    zeros = [tuple(0 for _ in factors) for factors in groups]
    ns = [len(a) for a in alphabets]
    cross = [tuple(zeros)]
    for i in range(d):
        for x in alphabets[i]:
            if x == zeros[i]:
                continue
            y = list(zeros)
            y[i] = x
            cross.append(tuple(y))

    def char(g, h):
        angle = sum(x*y/q for i in range(d)
                    for x, y, q in zip(g[i], h[i], groups[i]))
        return np.exp(2j*np.pi*angle)

    matrix = np.array([[char(f, x) for x in cross] for f in cross])
    values = np.linalg.svd(matrix, compute_uv=False)
    v = np.sqrt(np.array(ns, dtype=float)-1)
    s = np.empty((d+1, d+1), dtype=float)
    u = np.r_[1., v]
    s[:] = np.outer(u, u)
    s[1:, 1:] -= np.diag(ns)
    expected = sorted([abs(x) for x in np.linalg.eigvalsh(s)] +
                      [sqrt(ns[i]) for i in range(d) for _ in range(ns[i]-2)], reverse=True)
    err = max(abs(values - expected))
    det_pred = np.prod([n**(n/2) for n in ns])
    # Compare log magnitudes to avoid unstable determinant phases.
    determinant_error = abs(np.linalg.slogdet(matrix).logabsdet - np.log(det_pred))
    assert err < 1e-10, (groups, err)
    assert determinant_error < 1e-10, (groups, determinant_error)
    assert np.max(abs(s @ np.linalg.inv(s)-np.eye(d+1)))<1e-10
    # Exact algebraic inverse formula on the small symmetric block.
    diag = np.diag(1 / np.asarray(ns, dtype=float))
    sinv = np.block([
        [np.array([[1-v @ diag @ v]]), (v @ diag)[None, :]],
        [(diag @ v)[:, None], -diag],
    ])
    assert np.max(abs(s @ sinv - np.eye(d+1))) < 1e-10
    print('groups=', groups, 'points=', len(cross),
          'max_sigma_error=', f'{err:.2g}',
          'log_det_error=', f'{determinant_error:.2g}')


if __name__ == '__main__':
    for gs in [((2,), (3,)), ((2,), (3,), (4,)),
               ((2,), (2,), (3,), (5,)), ((2, 2), (3,), (2,)),
               ((3,), (4,), (5,)), ((2,), (2,), (2,), (2,)),
               ((2, 3), (3,), (2,)), ((3,), (3,), (3,)),
               ((2, 2, 2), (2,), (3,))]:
        test(gs)
