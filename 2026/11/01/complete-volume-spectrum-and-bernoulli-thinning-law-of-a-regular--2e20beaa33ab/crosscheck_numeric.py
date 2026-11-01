"""Optional independent numerical convex-hull comparison for all vertex subsets.
Requires numpy and scipy. The exact census itself has no third-party dependency.
"""
from scipy.spatial import ConvexHull, QhullError
import numpy as np
from icosa_exact import V, volume_6, vf

points = np.array([[vf(z) for z in v] for v in V], dtype=float)
max_error = 0.0
for mask in range(1 << 12):
    chosen = [i for i in range(12) if mask & (1 << i)]
    try:
        reference = ConvexHull(points[chosen]).volume if len(chosen) >= 4 else 0.0
    except QhullError:
        reference = 0.0
    exact = vf(volume_6(mask)) / 6
    error = abs(reference - exact)
    max_error = max(max_error, error)
    assert error < 1e-10, (mask, reference, exact, error)
print('ALL_4096_INDEPENDENT_NUMERICAL_HULL_CHECKS_PASSED; max_absolute_error=',max_error)
