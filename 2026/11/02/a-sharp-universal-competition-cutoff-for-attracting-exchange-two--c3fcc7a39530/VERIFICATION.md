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

Run `python3 verification/check_ricker_swap.py` from the directory containing `RESULT.md`; the script requires only the Python standard library.

The test verifies the exact exchange map at a transcendental parameter witness, compares the directly computed two-step Jacobian against the square of the one-step permutation-reduced Jacobian, finite-difference checks the derivatives, reproduces all three Schur expressions, tests 300 seeded parameter samples, and computes the roots of both stability threshold equations at seven coupling strengths. Observed computed critical values were \(z_*=0.75175950359911\) and \(\gamma_*=0.27783904026409\). The test completed successfully in the submitted working package.

These are diagnostics only. The proof of the complete parameter classification, the unique sharp competition cutoff and all strict boundary assertions appears in `RESULT.md` and does not depend on sampling. The test does not establish nonlinear stability at critical unit-circle boundaries, classify nonswapping cycles, or certify exhaustive historical priority.

Self-review was completed. Independent audit and independent validation have not been performed.
