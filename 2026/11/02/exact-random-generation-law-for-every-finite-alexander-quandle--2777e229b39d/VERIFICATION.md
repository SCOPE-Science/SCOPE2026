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

# Verification and limits

The structural proof uses only finite abelian group Fitting decomposition, finite-module composition factors, and exact counting of finite-field spanning families. No computational hypothesis is used to extend the result from tested groups to all groups.

`check_alexander.py` was run against its package-local path using the system Python standard library. It constructs the full multiplication table from the automorphism matrices and applies actual iterative closure under the quandle binary operation for every ordered tuple at the stated lengths; it does not call the claimed probability formula for generation decisions. It compares the exact resulting fraction to independent predicted rational values for the nine listed test families, including a mixed-prime summand, two distinct nonsemisimple actions, a non-Latin nilpotent Fitting summand, and an irreducible quadratic residual field. It returned `VERIFY_OK`. Its full textual output is `verification_output.txt`.

Tests are exhaustive only for the finite groups and tuple lengths stated. They do not cover arbitrary finite abelian groups, prove novelty, or substitute for the mathematical proof. The source comparison could not inspect the complete Saki–Kiani specialized subquandle-lattice paper; priority remains subject to independent review.
