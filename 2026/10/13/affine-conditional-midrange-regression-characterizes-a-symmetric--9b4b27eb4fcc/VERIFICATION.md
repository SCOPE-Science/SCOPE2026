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

The proof is analytic. The accompanying checker verifies three independent pieces.

First, it substitutes the explicit quantile into the first-order differential equation and simplifies the residual to zero.

Second, it verifies the antiderivative
\[
H(p)=-2as[p(1-p)]^{1/(2a)}
\]
and checks that it reproduces the conditional-regression identity
\[
(1-2p)H(p)=2ap(1-p)Q(p).
\]

Third, for several admissible slopes it evaluates the lower and upper truncated quantile means numerically on a grid and compares their conditional midrange with \(aQ(p)\). It also tests the derivative sign at and on both sides of the sharp boundary \(a=\frac12\).

These computations are supplementary to the proof and do not certify untested regularity classes.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK ode_checks=28 identity_checks=56 conditional_regression_checks=56 monotonicity_checks=45`.
