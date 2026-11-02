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

Run `python3 verify.py` using Python 3.9 or later. No external dependency is required.

The exact-rational procedure constructs the diagonal-majorant slack for each test size and antagonism weight; verifies an explicit nonnegative quadratic-form factorization, dual feasibility through a two-rank-one Gram representation, equality of primal and dual objectives, complementary slackness, strict positivity of optimal probabilities, and predicted exact nullity. The implemented rational matrix rank uses Gaussian elimination, not a floating-point tolerance. It ran 124 parameter cases in dimensions 5 through 18, including equality at the threshold.

A second, independent numerical construction solves for inverse-Gram diagonal entries giving row Gram diagonal one, forms an actual unit-row matrix, constructs the expected error-decrement matrix directly, and checks its smallest eigenvalue against the formula for 28 small cases. These floating-point tests are diagnostic only; the analytic proof supplies the universal certificate.

Observed replay: `PASS: 124 exact-rational certificate cases, 28 normalized-system eigenvalue cases, 47263 assertion checks`.

The tests do not establish novelty, global historical completeness, the existence of normalized systems at all prescribed large off-diagonal weights, or optimality for multistep/adaptive algorithms. Independent mathematical validation has not been performed.
