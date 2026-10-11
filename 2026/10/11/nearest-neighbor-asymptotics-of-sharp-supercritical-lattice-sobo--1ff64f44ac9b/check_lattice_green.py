"""Finite-box illustrations of the Green-kernel coefficients.

This is a numerical sanity check, not an infinite-lattice proof.
Requires numpy and scipy.  Run: python check_lattice_green.py
"""
from itertools import product
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve


def check_box(radius=5, dimension=3):
    points = list(product(range(-radius, radius + 1), repeat=dimension))
    index = {point: i for i, point in enumerate(points)}
    matrix = lil_matrix((len(points), len(points)), dtype=float)
    for point, i in index.items():
        matrix[i, i] = 2 * dimension
        for axis in range(dimension):
            for step in (-1, 1):
                neighbor = list(point)
                neighbor[axis] += step
                neighbor = tuple(neighbor)
                if neighbor in index:
                    matrix[i, index[neighbor]] = -1
    matrix = matrix.tocsr()
    source = np.zeros(len(points))
    source[index[(0,) * dimension]] = 1
    green = spsolve(matrix, source)
    residual = max(abs(matrix @ green - source))
    origin = green[index[(0,) * dimension]]
    neighbor = green[index[(1,) + (0,) * (dimension - 1)]]
    h = green / origin
    rho = neighbor / origin
    other = np.array([
        h[i] for point, i in index.items()
        if sum(abs(coordinate) for coordinate in point) > 1
    ])
    assert residual < 1e-12
    assert abs(origin - neighbor - 1 / (2 * dimension)) < 1e-12
    assert max(other) < rho < 1
    assert min(h) > 0
    tails = []
    for exponent in (8, 12, 18, 24, 36):
        tail = sum(
            h[i] ** exponent for point, i in index.items()
            if point != (0,) * dimension
        )
        quotient = tail / (2 * dimension * rho**exponent)
        tails.append(quotient)
    assert abs(tails[-1] - 1) < 1e-6
    print(f"finite box radius={radius}, dimension={dimension}, nodes={len(points)}")
    print(f"Green(0)={origin:.12f}; nearest ratio={rho:.12f}; next shell <= {max(other):.12f}")
    print(f"residual={residual:.2e}; exponents=8,12,18,24,36")
    print("tail / (2d rho**q):", [round(x, 10) for x in tails])
    print("All finite-box checks passed; no infinite-volume assertion certified.")


if __name__ == "__main__":
    check_box()
