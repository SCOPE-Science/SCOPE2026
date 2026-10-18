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

The analytic proof in RESULT.md covers every \(N\ge3\) and matching size \(1\le m\le\lfloor N/2\rfloor\). No unspecified numerical oracle, optimizer, database table or external program is required for its mathematics.

Run `python check_matching_cov.py` in any Python 3 environment with the standard library. It enumerates integer lattice points of dilates of the actual anchored Lipschitz polytope, evaluates exact sums of independent squared contrast functionals, and interpolates their leading rational coefficients. Graph metric constraints are applied directly at each lattice point; the analytic dissection into ordinary and exceptional range strata is not used by the checker.

The exact-arithmetic verification passed all eight parameter pairs \((N,m)\) with \(N=3,4,5,6\) and \(1\le m\le\lfloor N/2\rfloor\). For example, \((N,m)=(4,2)\) has volume \(16/3\), matched-pair difference eigenvalue \(1/5\), and matched-class contrast eigenvalue \(1/10\). For \((N,m)=(6,3)\), the analogous eigenvalues are \(26/189\) and \(25/252\); all were reconstructed from weighted Ehrhart leading terms. Each of the eight cases checked the volume and every present invariant-component eigenvalue.

The proof additionally checks the beta density, centered covariance mixture and nondegenerate top eigenvalue directly. Extrapolation from a finite integer lattice table would not justify an infinite all-dimensional theorem; the symbolic dissection and eigenspace argument do. No independent scientific audit has been performed.
