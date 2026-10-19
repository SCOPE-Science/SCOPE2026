#!/usr/bin/env python3
"""Optional reproducible exploratory check. Monte Carlo is not a proof of a tail law."""
import math
import numpy as np
rng = np.random.default_rng(7316)
n = 700_000
G = rng.normal(size=(n, 3))
p = (G * G) / np.sum(G * G, axis=1)[:, None]
M = np.eye(3)[None, :, :] - 2*np.einsum('ni,ij->nij', p, np.eye(3)) + p[:, :, None]*p[:, None, :]
e = np.linalg.eigvalsh(M)
c = 3/(math.pi*math.sqrt(2))
for t in (1e-3,1e-4,1e-5,1e-6):
    empirical = float(np.mean(e[:,0] < t))
    leading = c*math.sqrt(t)*math.log(1/t)
    print(f't={t:g} empirical={empirical:.7f} leading={leading:.7f} ratio={empirical/leading:.5f}')
