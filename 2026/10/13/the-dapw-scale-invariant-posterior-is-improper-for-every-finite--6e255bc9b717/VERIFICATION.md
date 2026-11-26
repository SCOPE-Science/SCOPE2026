---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The primary article specifies the asserted five-dimensional reciprocal prior for both displayed likelihoods. Work with A=log(alpha)>1 and ell=log A, and set theta_j=exp(-s_j)/A and beta_j=c_j/ell on the fixed rectangle s_j in [0,1], c_j in [1,2]. The exact CDF is [exp(-A theta_j^((x+1)^beta_j))-exp(-A)]/[1-exp(-A)]. Expanding exp(c_j log(x+1)/ell) for each fixed integer x gives log(A theta_j^((x+1)^beta_j))=-s_j-c_j log(x+1)+O(1/ell) uniformly. The limiting discrete Fréchet CDF is exp(-exp(-s_j)(x+1)^(-c_j)) for x>=0 and zero at -1. Every finite atom, including at zero, and every finite survivor is positive. The finitely many factors and denominators are uniformly controlled by continuity on the compact rectangle, so either data likelihood is uniformly bounded below for large A. In absolute log coordinates the Jacobian is triangular with determinant in absolute value 1/(c_1 c_2), giving exactly dA ds_1 ds_2 dc_1 dc_2/(c_1 c_2), of infinite mass on the tail. This proves divergence for every fixed finite valid dataset. The Type-II assertion is for the displayed likelihood and does not depend on a particular tie-correction formula: for an exact finite discrete observation event it suffices to choose one compatible finite raw sample realization, whose product probability is also bounded below. Under strict upper records, each denominator is the positive survivor at the preceding record. Mixed upper–lower records with fixed alpha are excluded, as are proper truncations. The frozen numerical script was not executed; the analytical lower bound, not a finite simulation, proves divergence.

## originality

PASS

The distinct result is impropriety for every finite valid Type-II or upper-record dataset under this actual common-alpha DAPW prior, via a nondegenerate discrete Fréchet escape with positive likelihood over infinite prior volume. Primary-source comparison confirms that this is not merely the observation that the prior is improper, and the closest indexed audit concerns a different likelihood and fixed-alpha regime. This is a best-of-knowledge assessment, not an absolute priority claim.

## value

PASS

This settles whether two specific published Bayesian procedures define posterior probability distributions, for all finite sample sizes rather than just a counterexample or a failed numerical fit. The positive-atom boundary explains why even data with many distinct observations cannot fix the normalization under the stated prior. It is a practical distinction for interpreting reported posterior summaries and for choosing a genuinely regularized model, without making claims about mixed records or unspecified numerical truncation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
