---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For independent endpoint norms U and V the Gaussian density at zero times the d-ball volume is c=exp(-||r_(k-w)||^2/(2 sigma^2))/(2^(d/2) sigma^d Gamma(d/2+1)), so P(V<s)~c s^d. Integrating near zero gives a finite negative moment of order p exactly for p<d, and conditioning on U gives t^(dw) P(Q>t)->c E U^d by the uniform density bound and finite E U^d. As the deterministic centers vanish, the endpoint norm pair converges jointly; the central independent chi-square ratio and Beta(a,a) transformation give the displayed CDF, gamma moments and central tail constant. The moment domain is sharp at equality; uniform shifted Gaussian small-ball bounds and bounded means give uniform integrability for q<dw via any q' strictly between q and dw. Reciprocal symmetry and absence of an atom at one give P(Q>1)=1/2; strict Q^2+Q^(-2)>2 except at one gives the strict second-moment inequality, allowing infinity. For the growing full-history window, upper Gaussian tails at exp(epsilon k) and lower small-ball tails at exp(-epsilon k) are summable; Borel–Cantelli over rational epsilon and the finite nonzero initial norm give log Q->0 a.s. The exact-gradient update on the unit curvature component multiplies by -Q. The mean-square statement refers to E Q^2 (for a fixed nonzero test component, the one-step squared gain); it does not interchange expectations for an error component dependent on the history or establish a closed-loop stability theorem.

## originality

PASS

The scoped distinct contribution is the joint fixed-window versus full-history diagnosis of this specific 1+rho step under fresh Gaussian observation errors and prescribed vanishing residuals, not any of the Gaussian ratio distribution identities viewed alone. The endpoint ratio is a power of a known doubly noncentral F random variable at finite k and of a central F variable at the floor. This is substantial prior coverage of the distributional ingredients. The exact-residual parameter rule already exists. In the matched rule-specific statements inspected, neither those distribution references nor the studies of deterministic feedback supply the fixed-window mean-square obstruction together with the almost-sure full-history boundary under this observation model. The latter assertion uses growth of the window along the sequence, not an identity for a single F random variable.

## value

PASS

The fixed-window gain may lack even a second moment despite Gaussian measurements; raising dw beyond two restores finiteness but never makes the limiting one-step diagnostic mean-square contractive. This distinguishes two different practical obstructions for a concrete proposed parameter rule. An increasing full-history window instead drives the step to the deterministic stability boundary, so fixed-memory conclusions cannot simply be transferred to it. The contribution is a motivated boundary for measurement-based use of the rule, not a new textbook ratio identity or evidence about whole trajectories.

The dated certificate retains the supplied scientific assessment, sources and limitations.
