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

# Verification notes

The complete finite checker is `scripts/verify.py`. With Python 3, NumPy, SciPy and mpmath installed, run `python scripts/verify.py`. Its recorded execution completed **93 finite assertions**, including independent sine-weighted numerical quadrature of the oscillatory radial moments for several parameter and frequency choices, exact half-integer \(K\)-function comparisons, absolute-envelope error tests, and finite two-term signed-count checks.

The infinite spectrum, all Schatten memberships, sharp \(L^2\) and \(L\log L\) coefficients, nonattainment of a naive diagonal trace integral, and the boundary range \(0\le\beta<2\) are mathematical statements proved in `RESULT.md`, not consequences of finite computation. The trace expression that fails is the **symbol times Bergman diagonal kernel** integral, not the Berezin-transform trace formula for trace-class operators. No external or independent mathematical audit has been performed.
