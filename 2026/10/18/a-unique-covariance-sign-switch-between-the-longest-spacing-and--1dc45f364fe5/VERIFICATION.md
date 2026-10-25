---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For m>=2 uniform order-statistic spacings have the Dirichlet(1,...,1) simplex law. The exact joint tail formula P(X_i>a_i for selected indices)=(1-sum a_i)_+^(m-1), together with inclusion-exclusion over the other m-1 gaps, gives the displayed piecewise polynomial C_m(t). The key nonstandard sign step is an analytic regression: conditional on X1=x, g_m(x)=E[max(x,(1-x)Q_{m-1})] is convex as an expectation of maxima of affine functions. Its value exceeds mu=H_m/m at x=0 and x=1 but is strictly below mu at x=1/m. The two sign crossings of g_m-mu, and C'_m(t)=-m(g_m(t)-mu)(m-1)(1-t)^(m-2), force C to decrease/increase/decrease with endpoints C(0)=C(1)=0, hence one interior zero. The exact inequality C_m(1/m)<0 for m>=3 and positive covariance with 1_{M>1/2} at t=1/2 establish 1/m<tau_m<1/2; m=2 yields tau=1/2. Independently reconstructed finite rational formulas and 24 Monte-Carlo correlations using 250,000 fresh normalized exponential vectors per m showed maximum absolute error 0.000416, plus exact boundary checks m=3,...,19. Sampling corroborates only tested cases; the convexity proof covers all real t and integers m>=2.

## originality

PASS

Best-of-knowledge novelty of the specified final mathematical claim, not of standard foundations; see four direct scientific comparisons and material primary-source reading with residual risks.

## value

PASS

The longest fragment and count of fragments above a variable threshold are natural competing summaries of one random partition. A unique sign-reversal threshold sharply describes nonmonotone dependence, not a routine moment identity or parameter substitution. The theorem supplies an exact reusable finite-m relation for occupancy/spacing statistics, with meaningful onset bounds valid for every sample size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
