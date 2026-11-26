---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS for the supplied repair, not for the weaker literal conditioning in the frozen assumptions. The original gives the action law conditional on the current belief vector, but uses it conditional on the whole history. These differ: set n=3, alpha=1, all initial beliefs 1/2, and use fresh draws except at time 2 when p_2=1/3. The joint masses with p_1=1/3 and 2/3 are 1/6 and 1/12. In the former group transfer delta=1/108 from action vector 000 to 111, and in the latter transfer 2delta back. All probabilities remain valid and the transfers cancel conditional on p_2, preserving its product-Bernoulli law. Both outcomes are immediately absorbing, so E[p_1 B] decreases by delta/18 with the marginals fixed; the claimed error at t=1 changes by delta/9. The repair explicitly states the fresh full-history conditional kernel of the intended model. Rechecking that final claim: subtracting the common update leaves deterministic deviations (1-alpha)^t d_i. The conditional variance is alpha^2/n^2 times n p_t(1-p_t)-s^t D_0, hence h_(t+1)=r h_t+alpha^2 D_0 s^t/n^2. Solving and using 0<=s<r<1 gives binary martingale convergence; E[B|history]=p_t identifies h_t with terminal squared error. Deterministic deviations then give both individual errors and rank-at-most-one covariance. Moving mass at fixed sum to an endpoint maximizes the square-sum with at most one fractional opinion; interpolation fills the feasible interval. The positive geometric convolution gives strict comparison at positive t and the r-rate for interior means. The s=0, t=0 convention and constant boundary means are accounted for. The packaged finite rational recurrence code was inspected, not executed; it does not test arbitrary history couplings or prove convergence. The repaired proof and the exact n=2 check in its notes establish the applicable reading and illustrate the strict penalty.

## originality

PASS

For the repaired, standard fresh-draw process, credit the model, general herding and the one-step moment machinery. The closed finite-horizon terminal-error law at arbitrary initial heterogeneity, with its best possible fixed-mean dispersion envelope, was not covered by the checked statements. The repair clarifies the hypothesis rather than claiming the previously known transition rule as the contribution.

## value

PASS

Complete self-inclusive mixing is a natural exactly solvable network baseline. The final result quantifies what general convergence does not: heterogeneous beliefs at the same mean make binary consensus harder to predict at every positive finite time, by a sharp amount and without changing its odds. The deterministic disagreement term and surviving leading penalty give an exact benchmark beyond the classical homogeneous resampling case or a numerical rate fit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
