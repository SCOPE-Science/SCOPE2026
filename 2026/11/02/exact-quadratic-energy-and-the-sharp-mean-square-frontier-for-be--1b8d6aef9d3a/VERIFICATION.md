---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

From the actual frozen RESULT.md, P=[[1,-qz/(1+qz)],[-qz/(1+qz),qz^2]] is positive definite because det P=qz^2[1-q/(1+qz)^2]>0 for 0<q<1,z>0. Direct independent symbolic multiplication of both companion matrices gives exact E[A_D^T P A_D]-P=delta*diag(1,0), delta=z(qz^2+z-2)/(1+qz). The two-step expected squared-state form x^2+E X_1^2 is positive definite, implying geometric contraction at delta<0 and growth at delta>0; zero drift conserves positive expected energy. Independent centered noise adds sigma^2 to energy, giving the exact stationary variance in the stable region and critical linear energy growth. The separate mean-recursion Jury criteria yield the strict blind-spot interval; at q=1/2,z=3/2 roots have modulus sqrt(3)/2 although delta>0. Independent sympy calculation verified the drift, lifted-moment determinant, stationary MSE exactly. Scope is iid Bernoulli zero/one lag and real scalar convex quadratic, not general async SGD.

## originality

PASS

The novelty assessed is the explicit all-q sharp Lyapunov frontier, additive-noise pole and strict first-vs-second-moment separation as a package, not the existence of mean-square spectral-radius criteria for switched linear systems. Searches identified asynchronous SGD, deterministic delayed quadratics, random-delay Lyapunov exponents, published covariance results on other algorithms, but no proved coverage of this exact iid Bernoulli scalar model and all formulas. Historical specializations remain a genuine risk.

## value

PASS

A stochastic stale-gradient stability frontier is a natural optimization-design invariant: the exact admissible stepsize and noise amplification distinguish safe mean-square operation from deceptively contracting expected iterates. The explicit positive energy is structural rather than a renamed textbook convergence assertion; the sharp boundary and pole can be used directly by researchers working with bounded random staleness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
