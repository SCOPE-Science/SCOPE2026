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

# Verification of conditional bridge return-time ordering

Run `python3 verification.py` in a directory containing the embedded standalone program. It uses only the Python standard library. The program (i) enumerates all balanced bridges through semilength ten, (ii) compares empirical integer counts against independent Catalan-convolution and closed coefficient formulas, and (iii) verifies conditional likelihood-ratio comparisons, strict finite-sample stochastic order, the boundary truncation identity and its total-variation value. Further exact integer checks run across larger sizes.

The verification is not an infinite proof, is not independent expert validation and does not certify historical novelty. The all-size proof is the Lagrange inversion and factorial-ratio argument in `RESULT.md`; independent auditing has not been performed.
