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

# Verification instructions

Run `python verify.py` from the extracted files, with NumPy installed. The script constructs full grounded Laplacians and compares exact tree formulas with direct linear algebra, checks the directional derivative and critical price under a budget reallocation, tests strict interval inclusion, compares finite kernels with the continuum arcsine formula, and evaluates the predicted endpoint square-root correction against exact discrete sums.

This code supplies finite numerical stress tests and cannot replace the analytic proof for all sizes or real price values. The proof uses a positive-definite Hessian, finite resistor-network identities, uniform singular Riemann sums, and a square-root power-sum remainder. Independent mathematical validation has not been performed.
