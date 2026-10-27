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

# Verification

The standalone `verify_cartier.py` constructs the 6-by-6 Cartier matrix from the six differential basis elements and the monomial exponent congruence in characteristic three. For each tuple of coefficients over both the field of three and the quadratic extension with nine elements, the program computes the ranks of the matrix and its semilinear square and cube using exact finite-field arithmetic. It also checks the exact occurrence counts for the two a-number strata.

Observed result: `VERIFY_OK: characteristic 3 genus 6 Cartier ranks {3: 54, 4: 27} F9 {3: 5832, 4: 729}`.

Universal coverage comes from the proof of the Cartier identities, not finite enumeration. A formal independent audit was not performed. The results do not determine the Newton polygon or complete Ekedahl–Oort type.
