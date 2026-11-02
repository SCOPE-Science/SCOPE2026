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

# Verification and reproducibility

The exact theorem and its integral proof are in `RESULT.md`; code is a finite diagnostic and does not certify universal claims or historical priority.

With NumPy and SciPy available, run `python3 check_dephasing_star.py` from the folder containing this file. The program independently constructs generators for original weighted stars of 2 through 9 leaves, tests 96 randomized full-space integrated-density certificates, checks three finite-time matrix-exponential integrals, and verifies two-dimensional rate minimization identities/inequalities in 345 further randomly generated parameter groups. Expected output is three `PASS` lines, plus observed normalized residuals; analytic proof establishes the exact all-parameter conclusions.

The physically relevant initial state is a source leaf. For more than two leaves, a full-space inverse Liouvillian need not exist because additional dark leaf combinations are not excited. The code solves the reachable three-dimensional subspace, verifies the embedding in the original Hilbert space, and avoids falsely asserting full-space decay. Source coherence decay rate is exactly \(\gamma\), hub population decay rate exactly \(\kappa\). A source-only, not all-site, dephasing channel is essential.

No third-party experimental replication, publication-priority certification or independent scientific audit is claimed.
