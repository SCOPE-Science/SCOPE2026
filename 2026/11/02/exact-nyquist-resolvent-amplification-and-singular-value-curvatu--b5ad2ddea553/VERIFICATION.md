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

The source-only phase-fitted Helmholtz Green kernel was reconstructed directly from the three-point recurrence and both discrete radiation boundary conditions. The simple largest eigenvalue of the Hermitian square at the Nyquist limit was expanded to second order using exact finite sums.

Run `python verify.py` with NumPy installed. The checker evaluates integer-sum identities exactly for 127 orders, checks 80 independently assembled boundary-value solves against the analytic Green matrix, verifies 80 Frobenius norms, and performs 35 supplementary numerical singular-curvature probes. All these checks passed. These are not substitutes for the algebraic proof and do not certify uniformity in growing grid dimension.

Scientific limits: only uniform one-dimensional grids, zero impedance data, arbitrary complex interior sources, fixed grid dimension, and the stated phase-fitted construction. No independent audit or formal proof certificate is claimed.
