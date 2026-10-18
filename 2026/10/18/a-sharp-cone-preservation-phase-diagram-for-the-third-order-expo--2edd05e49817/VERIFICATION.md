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

# Verification of the exact Riccati step classification

The stand-alone command is `python verify.py` (Python 3, no external packages). It performs exact rational matrix identities on explicit **noncommuting** positive-definite \(2\times2\) examples; exact-rational zero-input scalar threshold checks; deterministic dense scalar parameter-grid tests; seeded random noncommutative matrix inertia checks; and scalar \(\varphi\)-function threshold, monotonicity and endpoint diagnostics. The checker reports its executed assertion count. The reproducible tests compare the source step to the derived factorization and are deliberately independent of the claim's use of spectral tests where possible.

The proof, not finite testing, establishes the infinitely quantified step and dimension statements. This is exact-arithmetic mathematics; the checker uses floating-point values for some supplementary numerical checks and therefore is not an error-bounded interval certificate. Neither independence nor external audit has been performed.
