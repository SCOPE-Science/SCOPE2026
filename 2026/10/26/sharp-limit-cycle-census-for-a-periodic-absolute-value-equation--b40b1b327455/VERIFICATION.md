---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the exact cycle count

The proof's exhaustive ingredient is analytic, not computational: global comparison partitions initial data into two fixed half-lines and a two-crossing interval. On that interval the exact equation \(P_\varepsilon'=1\) is \(\sin(kt)+\sin(kr_\varepsilon(t))=0\). The endpoint square-root factorization makes the phase matching map converge in \(C^1([0,\pi])\) to the identity, so the exact critical-point count \(k-1\) holds for each fixed integer harmonic order for small nonzero perturbation. Rolle and the Chebyshev Melnikov roots give matching bounds. These are the necessary infinite-quantifier steps.

Executed supplementary numerical checks: for each integer \(k\) from \(2\) through \(8\), at \(\varepsilon=0.07\), form the two positive primitives using cumulative trapezoidal quadrature at 15,001 equally spaced points on \([0,\pi]\), interpolate the inverse relation, and count interior sign changes of \(h_\varepsilon\). The counts were \(1,2,3,4,5,6,7\), respectively. The observed critical phases agreed with the expected nearby \(j\pi/k\) locations. Separately, for each \(k=2,3,4,5\) and \(y\in\{-0.6,-0.2,0.3\}\), quadrature of \(\int_0^{2\pi}\cos(kt)|y-\cos t|dt\) agreed with the analytic expression involving \(T_k''(y)\), at absolute discrepancy below \(10^{-14}\).

Reproduction pseudocode (Python with NumPy and SciPy):

```python
import numpy as np
from scipy.integrate import cumulative_trapezoid
for k in range(2, 9):
    t = np.linspace(0, np.pi, 15001)
    a = 0.07 / k
    A = cumulative_trapezoid(np.exp(-a*np.sin(k*t))*np.sin(t), t, initial=0)
    B = cumulative_trapezoid(np.exp(+a*np.sin(k*t))*np.sin(t), t, initial=0)
    r = np.interp(A, B, t)
    h = np.sin(k*t) + np.sin(k*r)
    changes = sum(h[i]*h[i+1] < 0 and t[i] > 0.001 and t[i+1] < np.pi-0.001
                  for i in range(len(t)-1))
    assert changes == k-1
```

This code is not an independent certificate: sign-change sampling is not exhaustive, and the analytic proof supplies the missing uniform-root and endpoint arguments. No external independent audit has been performed.
