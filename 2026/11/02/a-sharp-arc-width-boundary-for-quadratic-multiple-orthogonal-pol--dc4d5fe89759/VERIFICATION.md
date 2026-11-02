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

# Reproducibility and mathematical limits

The proof of the infinite-parameter theorem is in `RESULT.md`: the original type-II moment system, its real quadratic reduction, the exact Schur test, the sharp cosine-moment bound, the smooth full-support limiting construction, the endpoint-pair phase angle, and the uniform-density comparison.

Run `python checker.py` from this directory using Python 3.9 or later; the checker uses only Python's standard library and a fixed pseudorandom seed. The completed execution passed **14,215 deterministic supplementary assertions**, including direct moment-orthogonality checks, root identities, mixed finite even measures, supercritical endpoint-pair families, one positive full-support smooth approximation, and subcritical and uniform-weight comparisons.

Numerical roots and sampled quadrature cannot certify a theorem for all probability measures or all angles. The analytic strict-inequality argument and the moment weak-limit construction establish the universal and existential statements respectively. There has been no independent audit or external certificate.
