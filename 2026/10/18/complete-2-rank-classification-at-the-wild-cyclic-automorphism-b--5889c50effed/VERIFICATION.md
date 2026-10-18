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

# Reproducibility

Run the accompanying standalone `verify.py` with Python 3 (standard library only). A successful run prints:

`VERIFY_OK genus4_counts=3,5,9,9 Cartier_nilpotence=3 wild_C4_zero=true`

The program encodes the semilinear Cartier matrices derived symbolically in the proof for the intermediate genus-four quotient, multiplies them exactly to test nilpotence indices, and counts points of the characteristic-two genus-four curve over four explicitly constructed finite fields. The calculated point totals \((3,5,9,9)\) yield first zeta coefficients \((1,0,0,0,-2)\) by Newton identities; in characteristic two these coefficients are divisible by two after the constant term, consistent with vanishing \(2\)-rank. It separately checks the numerical Deuring–Shafarevich identity for the cyclic-four case.

The general characteristic-two \(2\)-rank classification is proved by Deuring–Shafarevich plus the two symbolic Cartier calculations, conditional on the published classification of wild-boundary cyclic actions. No claim of exhaustive historical priority, supersingularity of all zero-rank Jacobians, or external verification is made.
