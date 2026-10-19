"""Independent finite-volume checks for stationary telegraph-driven velocity resetting.

Requires NumPy and SciPy. Run: python verify.py
The finite-volume tests corroborate, but do not prove, the analytical results.
"""
import math
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve


def stationary_density(n, r, lam, sigma, drag, edge):
    """Stationary finite-volume CTMC on velocities and two propulsion states.

    Cell-center upwind transport, orientation flips at lam, resets of velocity
    to the central cell at r with the propulsion sign kept unchanged.
    """
    assert n > 5 and n % 2 == 1 and r > 0 and lam > 0
    h = 2 * edge / n
    grid = -edge + (np.arange(n) + 0.5) * h
    mid = n // 2
    rows, cols, entries = [], [], []

    def add(i, j, x):
        rows.append(i)
        cols.append(j)
        entries.append(x)

    for sign_index, sign in enumerate((1, -1)):
        for i, v in enumerate(grid):
            src = 2 * i + sign_index
            loss = 0.0
            speed = sign * sigma - drag(v)
            if speed > 0 and i < n - 1:
                rate = speed / h
                add(src, 2 * (i + 1) + sign_index, rate)
                loss += rate
            if speed < 0 and i > 0:
                rate = -speed / h
                add(src, 2 * (i - 1) + sign_index, rate)
                loss += rate
            add(src, 2 * i + 1 - sign_index, lam)
            loss += lam
            if i != mid:
                add(src, 2 * mid + sign_index, r)
                loss += r
            add(src, src, -loss)

    mat = coo_matrix((entries, (rows, cols)), shape=(2 * n, 2 * n)).transpose().tolil()
    mat[-1, :] = 1.0
    target = np.zeros(2 * n)
    target[-1] = 1.0
    prob = spsolve(mat.tocsc(), target)
    density = prob.reshape(n, 2).sum(axis=1) / h
    assert density.min() > -1e-8
    assert abs(density.sum() * h - 1.0) < 1e-8
    return grid, density


def one_sided_slope(grid, density):
    """Use cells 1 and 2 to the right of zero; center contains reset source."""
    mid = len(grid) // 2
    h = grid[1] - grid[0]
    return (density[mid + 2] - density[mid + 1]) / h


def local_curvature(grid, density):
    mid = len(grid) // 2
    h = grid[1] - grid[0]
    return (density[mid + 3] - 2 * density[mid + 2] + density[mid + 1]) / (h * h)


def run():
    sigma = 2.0
    examples = [
        ('shear-thickening / origin minimum', np.tan, math.atan(sigma), 0.4, 0.2),
        ('shear-thickening / cusp and edge peaks', np.tan, math.atan(sigma), 0.7, 0.2),
        ('linear-drag control', lambda v: v, sigma, 0.7, 0.2),
    ]
    count = 0
    for title, drag, edge, r, lam in examples:
        expected = r * (1 - r - 2 * lam) / (2 * sigma * sigma)
        coarse = stationary_density(2001, r, lam, sigma, drag, edge)
        fine = stationary_density(4001, r, lam, sigma, drag, edge)
        xcoarse = one_sided_slope(*coarse)
        xfine = one_sided_slope(*fine)
        assert abs(xfine - expected) < 1.2e-4, (title, xfine, expected)
        assert abs(xfine - expected) < abs(xcoarse - expected) + 1e-7
        print(f'{title}: predicted slope={expected:.9f}; '
              f'2001 cells={xcoarse:.9f}; 4001 cells={xfine:.9f}')
        count += 1
    # Critical origin: r+2lambda=g'(0), derivative zero, quadratic curvature positive.
    r, lam = 0.6, 0.2
    grid, d = stationary_density(8001, r, lam, sigma, np.tan, math.atan(sigma))
    curv = local_curvature(grid, d)
    p0 = d[4001]  # first cell immediately to right of the source cell
    predicted = 2 * lam * p0 / (sigma * sigma)
    assert abs(curv - predicted) < 3e-4, (curv, predicted)
    print(f'critical curvature: predicted={predicted:.9f}; discrete={curv:.9f}')
    count += 1
    # For shear thickening g(v)=tan(v), terminal drag slope is 1+sigma^2.
    r, lam = 0.7, 0.2
    edge_exponent = (r + lam) / (1 + sigma * sigma) - 1
    assert edge_exponent < 0
    v1, q1 = stationary_density(2001, r, lam, sigma, np.tan, math.atan(sigma))
    v2, q2 = stationary_density(4001, r, lam, sigma, np.tan, math.atan(sigma))
    assert q2[-1] > q1[-1] > 0
    print(f'edge lower-bound power={edge_exponent:.9f}; '
          f'edge cells={q1[-1]:.6f}, {q2[-1]:.6f}')
    count += 1
    print(f'PASS: {count} independent discretization/edge checks')


if __name__ == '__main__':
    run()
