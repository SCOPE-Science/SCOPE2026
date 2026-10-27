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
The finite frames are constructed directly as reflexive accessibility matrices. The checker `artifacts/verify_star.py` tests all onto maps for three small domains using direct forth/back predicates, then separately checks all tagged-word counts and automorphism-orbit multiplicity profiles for twelve parameter pairs. Fourteen size sweeps check the sharp existence threshold against the closed formula. Running `python3 artifacts/verify_star.py` in an otherwise empty directory containing only this artifact reproduces `artifacts/verification_output.txt`.

The direct-function comparisons cover only small finite cases because exhaustive function enumeration grows exponentially; they do not certify infinite parameter ranges. The general theorem follows instead from the complete normal-form and inclusion–exclusion proof. No independent third-party audit, formal proof assistant or external certification is asserted.
