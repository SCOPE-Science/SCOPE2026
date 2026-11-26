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

Applying the two generators to 1, x_i and x_i x_j gives the same closed moment equations, including i=j, since 2 delta-kappa=zeta. The cubic difference is the third signed jump term -rho E[(1-A)^3] x_i^3. Finite initial second moments suffice for the closed finite-time equations. The past reset convolution is bounded coordinatewise by b_i/a_i; the past diffusion convolution converges almost surely by Brownian sublinearity and in L^2 since 2c_i>kappa. Synchronous differences decay almost surely in both systems (for the diffusion the difference factor is exp[-(c_i+kappa/2)t+sqrt(kappa)W_t]), so uniqueness holds even among invariant laws not assumed to have finite moments. Subtracting m_i m_j from the stationary raw second moment gives the stated covariance, the positive Gram matrix of distinct exponential functions after scaling by sqrt(kappa)m_i. The displayed Cauchy determinant has the correct squared Vandermonde and denominators. At full reset the invariant law is the image of one exponential age under a smooth curve, a countable union of compact Lipschitz images and hence Lebesgue null for d>=2. For the diffusion, truncation of the exponential-Brownian integral gives the derivative tail formula in D^{1,2}: after taking the expectation and integrating over 0<=s<=v<=u the squared derivative norm is 2 kappa b_i^2 times the integral of v exp[-c_i(u+v)+kappa v] over v<=u, namely 2 kappa b_i^2/[c_i(2c_i-kappa)^2]. This also gives derivative convergence by domination. A linear dependence among derivative tails differentiates to a dependence among the distinct exponentials after the common strictly positive Brownian factor is removed. The Malliavin covariance is therefore nonsingular pathwise and the standard absolute-continuity criterion applies. The curve then gives exactly unit TV, with the stated normalization.

## originality

PASS

The closely related weak-reset expansion supplies the second-order shared-noise construction, and catalogue records give other examples of matched stationary second moments with mismatched higher behavior. The distinct result is the finite-strength exact one-time degree-two matching in this driven system together with identical positive-definite stationary covariance and the singular-versus-density obstruction at full reset. This combination is not established by the closest inspected statements; the generators, renewal argument and density criterion are not themselves novelty claims.

## value

PASS

An exact, all-time quadratic surrogate can remain maximally wrong as a stationary probability model, and this persists with full-rank covariance rather than a trivially rank-one moment matrix. The coupled heterogeneous relaxation and shared shock give a natural example where the covariance cannot certify support dimension; the unit-TV witness quantifies a concrete limitation of moment checks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
