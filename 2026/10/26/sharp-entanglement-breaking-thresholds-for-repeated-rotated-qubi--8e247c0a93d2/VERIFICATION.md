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

# Verification of rotated-dephasing optimum

The analytical argument and boundary values are contained in `RESULT.md`. Execute the bundled reproducible numerical checks using `python verify.py` after installing `numpy>=1.24`. The program generated and tested exact-power witnesses for six representative values of \(q\) and every integer \(3\leq n\leq30\), verified the two-step singular values, checked the threshold sign changes at depths \(3\leq n\leq23\), and sampled 500 competitor rotations. It completed **1673 passing numerical assertions** in a reproducible execution.

These tests check finite instances subject to floating-point tolerance, not all \(q\), all rotations, or all depths. The determinant inequality, forced two-step singular value, rotation feasibility factorization, and characteristic polynomial prove the universal claim independently of numerical testing. The standard unital-qubit entanglement-breaking criterion is an explicitly acknowledged prior theorem. No independent scientific audit or external replication was performed.
