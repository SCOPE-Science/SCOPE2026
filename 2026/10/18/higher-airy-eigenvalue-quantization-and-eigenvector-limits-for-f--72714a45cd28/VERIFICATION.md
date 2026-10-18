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

# Reproducibility and scope

Run `python VERIFY.py` with Python 3, NumPy and SciPy. The exact rational tests check the periodic ground-state equation, the quadratic-form identity, and the sharp four-edge resistance equality. The separate tridiagonal numerical tests compare the first three eigenlevels and the limiting Airy constants for two positive modulation pairs and three small geometric-damping parameters. They produce finite corroboration, not an exhaustive proof or a numerical certificate of an infinite asymptotic.

The analytic proof in `RESULT.md` establishes compactness for every bounded-energy sequence, simultaneous recovery on arbitrary fixed finite-dimensional subspaces, matching min–max bounds and eigenfunction convergence. No result for growing rank or a fixed finite-section cutoff is certified. Source priority remains subject to the access limitation disclosed in REVIEW.md.
