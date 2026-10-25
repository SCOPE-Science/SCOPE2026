#!/usr/bin/env python3
"""Check the explicit dual-seam cocycle on finite triangulated annuli."""

def check(m):
    if m < 2:
        raise ValueError("m must be at least 2")
    eta = {}
    for j in range(m):
        eta[((j, 2), (j, 0))] = 1
    for j in range(m - 1):
        eta[((j, 2), (j + 1, 0))] = 1

    def value(a, b):
        if (a, b) in eta:
            return eta[(a, b)]
        if (b, a) in eta:
            return -eta[(b, a)]
        return 0

    triangles = []
    for j in range(m - 1):
        for i in range(3):
            triangles.append(((j, i), (j, (i + 1) % 3), (j + 1, (i + 1) % 3)))
            triangles.append(((j, i), (j + 1, i), (j + 1, (i + 1) % 3)))

    coboundary_values = [value(a, b) + value(b, c) + value(c, a) for a, b, c in triangles]
    ring_evaluations = []
    for j in range(m):
        ring = ((j, 0), (j, 1), (j, 2))
        ring_evaluations.append(sum(value(ring[i], ring[(i + 1) % 3]) for i in range(3)))

    assert all(v == 0 for v in coboundary_values)
    assert ring_evaluations == [1] * m
    assert len(eta) == 2 * m - 1
    scaled_l1 = len(eta) / m
    assert scaled_l1 < 2
    assert (1 / m) * sum(ring_evaluations) == 1
    return {"m": m, "triangles": len(triangles), "cocycle": True,
            "ring_pairings": ring_evaluations, "support_size": len(eta),
            "scaled_l1_bound": scaled_l1}

if __name__ == "__main__":
    for m in range(2, 11):
        print(check(m))

