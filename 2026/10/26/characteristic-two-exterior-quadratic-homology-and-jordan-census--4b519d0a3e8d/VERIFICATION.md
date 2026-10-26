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

The standalone checker `verify_exterior_quadratic.py` was run directly from the package input. It exhaustively enumerated all homogeneous quadratic forms in dimensions 2..5 over \(\mathbb F_2\) and dimensions 2..4 over \(\mathbb F_4\). The checker also used explicit rank representatives in dimensions 6 and 7 over \(\mathbb F_2\). It constructed both coefficient matrices and full wedge-multiplication matrices, compared their ranks with the theorem, and independently tested all fiber sizes against Gaussian-symplectic factors. The run ended with `ALL_EXTERIOR_QUADRATIC_CHECKS_PASSED 5270`.

This finite validation does not prove the infinite result; the normal-form and tensor-complex proof supplies the general argument. No independent audit has been performed.
