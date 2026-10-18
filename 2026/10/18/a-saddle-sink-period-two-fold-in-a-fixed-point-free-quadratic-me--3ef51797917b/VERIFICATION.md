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

Execute `python3 verify.py` in the directory containing this document. No third-party modules or network connectivity are required.

The program completed 2,526 deterministic finite assertions: it checks the reconstruction of each numerical two-cycle, both recurrence equations, the exact two-step trace/determinant and unit-multiplier identities, the sign of the two branches, sampled strict log-concavity, and the leading and next threshold coefficients for small positive gain increments. It also checks the exact fold multiplier relation numerically for several gains.

The mathematical proof is in `RESULT.md`: exact two-step reduction of every real period-two orbit; strict analytic second-derivative bound on the log-level curve; exact Jacobian factorization and Schur inequalities; asymptotic perturbation of a nondegenerate maximum. Finite calculations are checks, not a substitute for the all-parameter and infinite-time arguments. The literature comparison is limited to the actually accessed sources, and independent mathematical audit is not performed.
