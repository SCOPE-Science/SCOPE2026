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

# Verification and limitations

The analytic proof is contained in `RESULT.md`, especially its rank-one determinant reduction and the analytic implicit-function expansion at the two band edges. The independently implemented `check.py` builds the full restricted resolvent from the free Green kernel, checks two exact definitions of the positive invariant, solves the resulting determinant at high precision, and compares finite Jacobi matrix eigenvalues against the infinite-volume roots. `check_output.txt` is the actual captured output. This computation does not prove the full theorem, verify all defect patterns, or exclude a historical equivalent from unread sources.

Reproduce with `python check.py`. The checker requires NumPy, SciPy and mpmath, and prints `ALL CHECKS PASSED` only if its assertions succeed. The proof establishes all sufficiently small nonzero real couplings for uniqueness and the asymptotics; arbitrary nonzero coupling is covered only for existence of at least one eigenvalue on each side.
