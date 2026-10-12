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

# Reproducibility and verification

Execute `python verify.py` with Python 3 and SymPy installed, from the directory containing the extracted artifacts. The expected exact output is `VERIFY_OK`.

The checker verifies that the strict derivative coefficient \(Q\) equals a sum of nonnegative terms, that the derivative quotient rule is algebraically exact, and that each channel's partial derivative has the claimed sign. It reconstructs and exactly substitutes the zero-feedback rational example, the first-channel-only strong limit, and the second-channel-only strong limit. Finally it solves one finite asymmetric feedback case numerically and checks each of the four stationary rates and mass normalization to a small residual.

The all-parameter uniqueness and the uniform joint-limit conclusions rely on the symbolic derivation and inequalities in `RESULT.md`, not on the finite numerical example or library testing. The script is an auxiliary consistency test and not an independent scientific audit. No external independent validation is asserted.
