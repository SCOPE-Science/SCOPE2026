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

The analytic argument in `RESULT.md` establishes the theorem for every integer sample size and all real thresholds in the stated domain.

Run `python3 verification/check_voronoi.py` from the package root. This standalone standard-library checker independently integrates polynomial densities exactly with rational coefficients, compares both joint-survival formulas, verifies the low-dimensional factorizations and finite grid signs, and performs high-precision asymptotic comparisons.

The executed checker reported 1,829 exact integration identities, 1,209 finite strict-sign checks, 36 moment-sign sanity checks, and eight asymptotic comparisons. These finite checks do not certify universal strict-sign inequalities; those are proved in `RESULT.md`. No external independent audit has been performed.
