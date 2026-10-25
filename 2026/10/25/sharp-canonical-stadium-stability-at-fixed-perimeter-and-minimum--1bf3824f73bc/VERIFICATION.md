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

# Reproduction and scope
Run `python3 verification/check_stadium_stability.py` from the unpacked finding directory. The script uses only the Python 3 standard library. It examines cutoff degrees 4, 8, 16, 32, 64, and 128. For each, it numerically locates an even-mode root enforcing the exact minimum-width direction, verifies positive curvature density and approximate width preservation, and independently integrates area against the support function's mixed continuous/atomic curvature measure. It compares the numerical area difference with \(\frac\pi2\varepsilon^2\sum_{n=2}^N(n^2-1)^{-1}\) and the Hausdorff ratio with \(\frac2\pi\sum_{n=2}^N(n^2-1)^{-1}\).

The inequality for **all** convex bodies is proved by the support-function identity, Parseval, and weighted Cauchy–Schwarz. Numerical integration is neither an exhaustive search nor a substitute for those proofs. The sharpness limit follows from an elementary telescoping sum; positivity of the finite-truncation curvature measure and minimum-width preservation is proved in the accompanying analytic proof for sufficiently small positive amplitudes.

The old area–perimeter–minimum-width inequality is a prior theorem, not a new result. The sharp quantitative remainder and universal constant are the scientific claim. No independent validation has been performed.
