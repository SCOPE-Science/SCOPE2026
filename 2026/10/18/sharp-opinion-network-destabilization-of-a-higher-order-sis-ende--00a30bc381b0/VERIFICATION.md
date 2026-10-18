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

The analytic proof derives the exact homogeneous Jacobian, decomposes it using the orthogonal modes of an arbitrary real symmetric graph Laplacian, and applies the quadratic Hurwitz criterion. It also derives both nonsynchronous endemic equilibria for the two-community example and evaluates the full four-dimensional Jacobian determinant.

Run `python check.py` using the listed dependencies to replay the symbolic identities, an exact unequal equilibrium with \(w=1/12\), and supplementary finite-network eigenvalue comparisons. Symbolic identities corroborate the algebra, but the proof in `RESULT.md` is the justification for the claims with arbitrary network size. The finite-network tests do not constitute an exhaustive check of all graph sizes or weights.

The model is piecewise smooth; local claims are made only at equilibria with nonzero opinions. At the general spectral equality, no nonlinear stability claim is made. Global attraction, mixed-sign equilibria and stochastic epidemics are not verified. Independent validation has not been performed.
