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

# Reproducibility and bounds

Run `python verify.py` in a Python environment with SymPy available. The check runs exact symbolic simplifications to verify both integrals from the triangle decomposition, the identity comparing the second moment with its published value, the fourth-moment rational formula, the fourth-to-second quotient, both exact deficit identities, and the nonnegative polynomial certificate. It verifies \(11^3=1331\) integer length triples by rational arithmetic and establishes exact regular-hexagon equality and elongated-path supremum. The expected terminal text is `MOMENT_PROOF_CHECK_OK`.

The mathematical proof uses the symbolic identities plus nonnegativity of every explicitly printed polynomial summand. The finite sample provides no independent universal proof. No external reviewer has audited these arguments. The orthogonal cycle-space metric is essential; changing the Euclidean realization invalidates the numerical formulas. Prior literature already contains the second moment, not claimed new.
