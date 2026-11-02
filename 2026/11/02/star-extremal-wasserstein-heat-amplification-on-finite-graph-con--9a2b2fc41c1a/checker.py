"""Independent finite checks for a star-extremal transport bound on graph cones.

Requires Python 3, NumPy, and SciPy. This is supplementary evidence,
not a substitute for the all-graph proof.
"""
import itertools
import math
import numpy as np
from scipy.linalg import expm


def graph_cone(d, internal_edges):
    """Vertex 0 is the hub, peripheral vertices are 1,...,d."""
    Q = np.zeros((d + 1, d + 1), dtype=float)
    for v in range(1, d + 1):
        Q[0, v] = Q[v, 0] = 1
    for u, v in internal_edges:
        Q[u + 1, v + 1] = Q[v + 1, u + 1] = 1
    np.fill_diagonal(Q, -Q.sum(axis=1))
    return Q


def candidate_lipschitz_potentials(d, internal_edges):
    # The difference-constraint polytope (hub fixed at zero) is integral:
    # extreme potentials can be chosen in {-1,0,1}^d.
    pts = np.array(list(itertools.product((-1., 0., 1.), repeat=d)))
    for u, v in internal_edges:
        pts = pts[np.abs(pts[:, u] - pts[:, v]) <= 1]
    return np.column_stack((np.zeros(len(pts)), pts))


def coefficient(Q, potentials):
    d = Q.shape[0] - 1
    mask = Q > 0
    def evaluate(t):
        P = expm(t * Q)
        # Evaluate Kantorovich dual maximization independently on all edges.
        M = P @ potentials.T
        vals = np.abs(M[:, None, :] - M[None, :, :]).max(axis=2)
        return float(vals[mask].max()), vals
    return evaluate


def bound(d, t):
    return (2 * (d - 1) * math.exp(-t) - (d - 2) * math.exp(-(d + 1) * t)) / d


def main():
    checks = 0
    times = (0., 0.025, 0.08, 0.2, 0.5, 1.0, 2.5)
    graphs = 0
    for d in range(2, 6):
        edges = list(itertools.combinations(range(d), 2))
        for mask in range(1 << len(edges)):
            E = [edge for bit, edge in enumerate(edges) if mask & (1 << bit)]
            isolated = len(set(range(d)) - {z for e in E for z in e}) > 0
            Q = graph_cone(d, E)
            potentials = candidate_lipschitz_potentials(d, E)
            coeff = coefficient(Q, potentials)
            graphs += 1
            for t in times:
                value, _ = coeff(t)
                target = bound(d, t)
                assert value <= target + 5e-10, (d, E, t, value, target)
                checks += 1
                if isolated:
                    assert abs(value - target) < 5e-10, (d, E, t, value, target)
                elif t > 0:
                    assert value < target - 1e-12, (d, E, t, value, target)
                checks += 1
    for d in range(4, 300):
        tstar = math.log((d - 2) * (d + 1) / (2 * (d - 1))) / d
        assert tstar > 0
        v = bound(d, tstar)
        assert v > 1 and v < 2
        assert abs((2*(d-1)/(d+1))*math.exp(-tstar)-v) < 1e-12
        checks += 4
    print(f"CHECK_OK graphs={graphs} supplementary_assertions={checks}")


if __name__ == '__main__':
    main()
