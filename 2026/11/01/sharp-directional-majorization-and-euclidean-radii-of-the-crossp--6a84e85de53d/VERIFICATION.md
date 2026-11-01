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

# Verification report

The accompanying `check.py` was executed in Python 3 with NumPy and SciPy. It returned `ALL_CHECKS_PASSED`, after checks of the exact dimension recurrence (79 dimensions), independent Fourier quadrature at both endpoints (11 dimensions), 192 balancing comparisons, six exact planar formulas, eight local-stability computations, 100 global-stability diagnostics, and four independent random-point tests. All runs used an explicitly fixed pseudorandom seed for reproducibility.

These computations are finite consistency tests only. The all-dimensional majorization, radii, equality cases, global lower bound, and local expansion are established by the written analytic argument. The first-moment formula uses an unnormalized volume-average definition; other centroid-body conventions multiply it by a fixed dimension-dependent scalar. No independent audit was performed.
