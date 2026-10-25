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

# Reproducibility and limits

The standalone `verify.py` is compatible with Python 3 and uses only its standard library. Execute `python3 verify.py` in the directory containing the program; it exits nonzero if a mathematical comparison fails.

The executed verification gave:

`VERIFY_OK polynomial_4point_certificates=96 exact_formula_checks=2573 exhaustive_permutations=409112 exhaustive_mixed_moments=202 reversal_patterns=2143,3142,4231`

The exact four-point certificates are not mere finite experiments: both sides of the defining binomial boundary identities are polynomials in the integer-size variable of degree at most three, and four distinct exact evaluations prove equality for all sizes by algebra. The independent exhaustive permutation enumeration is supplementary; it does not assert anything beyond sizes two through nine. The general boundary theorem is proved directly by conditional enumeration and Vandermonde summation. No claim of a full joint distribution, statistical independence, stochastic dominance, or independent scientific validation is made.
