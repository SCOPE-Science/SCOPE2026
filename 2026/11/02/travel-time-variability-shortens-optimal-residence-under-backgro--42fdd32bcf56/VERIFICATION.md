---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Reconstructed Bellman A-contraction on bounded patch-entry values and stationary ratio V_t=G_mu(t)/(1-Ae^-mu t). Differentiation has sign of g(t)-A H_mu(t), and F=g/H decreases strictly from 1 to 0 because F′=mu G_mu g′/H_mu². Jensen strictness under convex-order martingale coupling gives larger A for distinct equal-mean ordered laws, forcing smaller threshold and larger A V*. Correct small-mu expansion of first-order condition yields variance difference coefficient g(t0)/(2g′(t0)(m+t0)), strictly negative; finite third moments and local C² handle remainder. Independent symbolic F′ verification and exact e^-t,mu=1 two-law thresholds and rewards passed.

## originality

PASS

Charnov/Calcagno standard marginal-value analyses maximize gain per travel+residence mean and do not include Laplace sensitivity of a mortality-clock objective. Wajnberg et al (2006) full text studies finite deterministic remaining horizon with uniform vs triangular transit laws whose means differ; this does not imply strict equal-mean convex-order shift under exponential mortality. Explicit full-text comparison supports a distinct model/result, though prior stochastic optimal-foraging literature may contain equivalent discounted renewal formulations.

## value

PASS

This exact global policy and convex-order comparative statics isolate a natural distributional effect absent from classical mean-based marginal-value models, with a useful small-hazard variance coefficient and counterintuitive welfare response. The finding is motivated independently of routine renewal-algebra details.

The dated certificate retains the supplied scientific assessment, sources and limitations.
