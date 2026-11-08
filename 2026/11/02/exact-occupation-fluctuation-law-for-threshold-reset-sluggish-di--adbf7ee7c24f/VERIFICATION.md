---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For alpha>=0 and rho in [0,1), the natural-scale nonsticky time-change unambiguously fixes the singular diffusion; a single reset cycle has m(rho)=(1-rho^(alpha+2))/((alpha+1)(alpha+2)). The center-reward Poisson problem and 2G kernel give E[(R-theta*tau)^2]=3(1-rho^2)/[4(alpha+2)^2(alpha+3)(2alpha+3)]. The regenerative CLT then gives (L^(alpha+2)/kappa)Q_alpha(rho), almost sure mean theta, and the variance limit via exponential cycle moments. Independent exact Green integrations passed for 35 integer alpha and rational reset pairs; monotonicity follows by the derivative sign of (1-rho^2)/(1-rho^(alpha+2)), with alpha=0 constant 1/24. No lattice or rho=1 claim.

## originality

PASS

Best-of-knowledge new stated claim after primary statement/implication comparisons and a Resultary search: Prior qualitative T^-1/2 concentration does not determine a variance constant; Frimpong et al. same mean cannot imply Q without an extra second moment. Poisson resetting papers involve independent reset clocks and cannot be substituted by parameter changes.

## value

PASS

The exact second-order occupation coefficient and its nontrivial reset-location dependence quantify a natural observable of a previously studied threshold-reset diffusion, including an unexpected Brownian rigidity and strict sluggishness breakdown. General renewal tools do not remove the need for the nonstandard Green-kernel evaluation; this is a motivated, potentially useful exact fluctuation law, not a normalization check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
