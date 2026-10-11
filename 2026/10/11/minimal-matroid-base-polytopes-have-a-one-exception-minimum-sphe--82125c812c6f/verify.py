#!/usr/bin/env python3
import numpy as np
from scipy.optimize import minimize_scalar

for n in range(2, 31):
    for r in range(1, n):
        t = n-r
        a = n/(r*t)

        if r*t <= n:
            q = r*t/n
            R2 = r*t/n
        else:
            q = 1.0
            R2 = 2.0 - n/(r*t)

        v0 = np.r_[np.ones(r), np.zeros(t)]
        vertices = [v0]
        for i in range(r):
            for j in range(t):
                v = v0.copy()
                v[i] = 0.0
                v[r+j] = 1.0
                vertices.append(v)
        vertices = np.array(vertices)

        center = np.r_[
            np.full(r, 1.0-q/r),
            np.full(t, q/t)
        ]
        d2 = np.sum((vertices-center)**2, axis=1)
        assert abs(float(np.max(d2))-R2) < 1e-10

        if r*t <= n:
            assert np.max(np.abs(d2-R2)) < 1e-10
        else:
            assert abs(float(d2[0])-n/(r*t)) < 1e-10
            assert np.max(np.abs(d2[1:]-R2)) < 1e-10
            assert d2[0] < R2

        def objective(qq):
            return max(
                a*qq*qq,
                2.0+a*qq*qq-2.0*a*qq
            )

        numeric = minimize_scalar(
            objective,
            bounds=(0.0, 2.0),
            method="bounded",
            options={"xatol": 1e-13}
        )
        assert abs(float(numeric.fun)-R2) < 1e-8

print("VERIFY_OK minimal-matroid-MEB n=2..30 all-ranks=yes orbit-minimax=yes contacts=yes")
