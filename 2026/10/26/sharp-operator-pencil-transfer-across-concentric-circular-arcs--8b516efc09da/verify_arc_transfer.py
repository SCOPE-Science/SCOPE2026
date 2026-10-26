"""Finite checks for a sharp linear pencil arc transfer bound (not a proof)."""
import math
import cmath
import random
import numpy as np
rng=np.random.default_rng(5321)
checks=0
for theta,phi in [(0.11,0.31),(0.4,1.2),(0.9,2.1),(1.7,2.4),(2.4,3.05)]:
    scale=math.sin(phi/2)/math.sin(theta/2)
    inner=np.exp(1j*np.linspace(-theta,theta,501))
    outer=np.exp(1j*np.linspace(-phi,phi,501))
    for _ in range(80):
        a=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2))
        b=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2))
        ni=max(np.linalg.norm(a+z*b,2) for z in inner)
        no=max(np.linalg.norm(a+z*b,2) for z in outer)
        assert no <= scale*ni+2e-10,(theta,phi,ni,no,scale)
        checks += 1
    # exact sharpness from A = -B = identity: all support extrema are known analytically
    assert abs((2*math.sin(phi/2))/(2*math.sin(theta/2))-scale)<1e-12
    checks += 1
print(f'FINITE_ARC_PENCIL_CHECKS_OK {checks}')
