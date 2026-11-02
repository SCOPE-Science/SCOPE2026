#!/usr/bin/env python3
"""Numerical convex-hull replication of a separately proved rational volume formula."""
import math
import numpy as np
from scipy.spatial import ConvexHull
for n in range(2,7):
    unit = np.vstack((np.eye(n), -np.ones((1,n))))
    alpha, beta = 0.5, 1.0/(2*n-1)
    pol = np.vstack((alpha*unit, -beta*unit))
    measured = math.factorial(n)*ConvexHull(pol).volume
    expected = n*(n+1)/(2**(n-1)*(2*n-1))
    assert abs(measured-expected) < 1e-9, (n, measured, expected)
print('VERIFY_OK')
