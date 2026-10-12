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

Run `python3 verify_unequal_coupon.py` in the extracted directory. The script solves finite first-step equations for three coordinates: remaining expected draws, expected final singleton count, and their raw mixed moment. It uses `fractions.Fraction`, capped occupation states and finite recursive elimination, without stochastic simulation or floating arithmetic. It reports 59 exact-rational cases and prints several benchmark moments; all passed when this package was constructed.

In the uniform case it checks the finite closed expression for covariance \(m(H_m^{(2)}-H_m)\); the complete uniform joint distribution already appears in Myers and Wilf (2003) and is not claimed as novel. For unequal vectors it checks strict negativity directly against independent finite-state equations. The universal theorem for arbitrary real vectors and all \(m\ge2\) is proved in RESULT.md by conditional moment identities and strict monotonicity, not by these tests.

No formal prover, third-party validation, or independent scientific audit has been performed. Full historical novelty cannot be conclusively established from finite literature searches.
