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

# Reproducible mathematical checks

The complete derivation is in RESULT.md. `check_asymmetric_gabor.py` uses only the Python standard library and separately calculates the exact geometric Zak function and the closed-form extrema on nine sample parameter pairs. It checks critical spatial phases, the analytic lower and upper values, 61-by-61 two-dimensional fibers, strict positivity, and the reflection relation. The run printed `CHECK_OK: exact geometric Zak fibers, global bounds, internal minimizers and reflection symmetry`. These finite tests do not prove the universal continuum theorem. The proof uses strict numerator/denominator cosine monotonicity, convexity of the positive phase-zero Zak function, uniqueness of the positive derivative root and absence of simultaneous real-phase Zak zeros.
