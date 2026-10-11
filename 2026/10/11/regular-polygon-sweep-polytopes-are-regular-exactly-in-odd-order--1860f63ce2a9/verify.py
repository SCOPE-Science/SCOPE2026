#!/usr/bin/env python3
import math
import numpy as np

def sweep_data(n):
    pts = np.array([
        [math.cos(2*math.pi*j/n), math.sin(2*math.pi*j/n)]
        for j in range(n)
    ], dtype=float)

    generators = []
    classes = {k: [] for k in range(n)}
    for i in range(n):
        for j in range(i+1, n):
            g = (pts[i] - pts[j]) / 2.0
            generators.append(g)
            classes[(i+j) % n].append(g)

    y = math.pi / n

    # Raw support values in the n unoriented edge-normal classes.
    support = []
    for k in range(n):
        u = np.array([math.cos(k*y), math.sin(k*y)])
        support.append(sum(abs(float(np.dot(u, g))) for g in generators))

    # Edge length from each raw parallel-generator class.
    class_lengths = [
        sum(2.0*np.linalg.norm(g) for g in classes[k])
        for k in range(n)
    ]

    # Reconstruct all 2n vertices as intersections of consecutive support lines.
    verts = []
    for k in range(2*n):
        u = np.array([math.cos(k*y), math.sin(k*y)])
        v = np.array([math.cos((k+1)*y), math.sin((k+1)*y)])
        rhs = np.array([support[k % n], support[(k+1) % n]])
        verts.append(np.linalg.solve(np.vstack([u, v]), rhs))
    verts = np.array(verts)

    edge_lengths = np.linalg.norm(np.roll(verts, -1, axis=0) - verts, axis=1)
    perimeter = float(edge_lengths.sum())
    area = 0.5 * abs(float(np.sum(
        verts[:,0]*np.roll(verts[:,1], -1)
        - verts[:,1]*np.roll(verts[:,0], -1)
    )))
    radii = np.linalg.norm(verts, axis=1)

    return support, class_lengths, verts, edge_lengths, perimeter, area, radii

for n in range(3, 61):
    support, class_lengths, verts, edge_lengths, perimeter, area, radii = sweep_data(n)

    assert len(verts) == 2*n
    assert np.ptp(radii) < 2e-8

    if n % 2 == 1:
        x = math.pi / (2*n)
        L = 1.0 / math.tan(x)
        P = 2*n*L
        A = (n/2.0)*L**3

        assert max(abs(z-L) for z in class_lengths) < 2e-10
        assert max(abs(z-L) for z in edge_lengths) < 3e-8
        assert max(support)-min(support) < 2e-10
        assert abs(perimeter-P) < 2e-7
        assert abs(area-A) < 3e-6
    else:
        y = math.pi/n
        c = math.cos(y)
        s = math.sin(y)
        L_even = 2*c/s
        L_odd = 2/s
        p = (1+c*c)/(s*s)
        q = 2*c/(s*s)
        P = 2*n*(c/s + 1/s)
        A = n*c*(3+c*c)/(s**3)

        for k, z in enumerate(class_lengths):
            target = L_even if k % 2 == 0 else L_odd
            assert abs(z-target) < 3e-10

        for k, h in enumerate(support):
            target = p if k % 2 == 0 else q
            assert abs(h-target) < 3e-9

        # Reconstructed boundary edges are shifted by one normal index.
        for k, z in enumerate(edge_lengths):
            target = L_odd if k % 2 == 0 else L_even
            assert abs(z-target) < 4e-8

        assert abs(perimeter-P) < 3e-7
        assert abs(area-A) < 5e-6
        assert abs(L_even-L_odd) > 1e-8

print("VERIFY_OK regular-polygon-sweep-shape n=3..60 raw_generators=yes cyclicity=yes area_perimeter=yes")
