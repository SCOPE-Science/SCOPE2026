---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For x nonzero and H SPD, set s=rho||x||/||Hx||. Exactly f(x-sHx)-f(x)=-rho sqrt(AC)+rho^2 BC/(2A), with A=x^TH^2x, B=x^TH^3x, C=||x||^2. Thus per-state boundary 2 A^(3/2)/(B sqrt C). Normalize spectrum X in [1/kappa,1], and let Y=X^2; convexity of y^(3/2) implies maximal E[X^3] at a two-endpoint mixture for each E[X^2]. Differentiating B/A^(3/2) gives p=a^2(a+2)/((a+1)(a^2+a+1)) and rho*=3sqrt(3) a(a+1)/(a^2+a+1)^(3/2). Independently numerically verified rational p and closed forms for k=1,2,9,100. Endpoint mixture provides exact equality at threshold and objective increase above it. Distinction from uniform strict inequality at zero and boundary is correct.

## originality

PASS

Gitman et al. 2018 actually formulates the norm-proportional update and gives qualitative 1D/general convex convergence bounds, not a sharp multidimensional spectral condition-number dependent one-step objective monotonicity frontier. The Resultary Polyak, BB and Cauchy scaling frontiers use different norms/steps, so no formula-substitution implication was found.

## value

PASS

A sharp safe trust-coefficient boundary is directly motivated by maintaining deterministic objective descent in a standard layer-scaled optimizer. The explicit extremal Hessian eigenmass and asymptotic gain over a crude 2/kappa bound quantify a nontrivial useful property rather than a tiny numerical optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
