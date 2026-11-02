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
# Verification record

The proof in `RESULT.md` supplies all infinite-sample-size and all-polygon conclusions. To check finite identities, execute the standalone `checks/verify.py` with Python 3. The mandatory exact-rational tests use Python standard-library modules. Optional NumPy and SciPy allow additional direct convex-hull checks; if absent, these geometric tests are skipped explicitly.

The program was executed from the source included in this package. It printed `EXACT_MULTINOMIAL_GFs_AND_PAIR_BALANCING_PASSED`, `CENTRAL_BINOMIAL_INTERVAL_MONOTONICITY_PASSED`, `DIRECT_NONCONGRUENT_RHOMBUS_GEOMETRY_PASSED`, and `ALL_CHECKS_PASSED`.

The tests cover particular rational side-length vectors, sample sizes at most ten, binomial interval sizes at most thirty, and noncongruent rhombi. They are not exhaustive over continuous parameters and cannot establish the theorem without the analytic supporting-line, binomial-derivative, and rational-pole arguments. Full historical priority and independent mathematical validation remain unperformed.
