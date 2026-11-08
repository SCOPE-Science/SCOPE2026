---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For f(x)=xᵀHx/2, each orthonormal-frame forward-difference estimator is Hx+e(U), e=(h/2)Σ_j(u_jᵀHu_j)u_j. Haar column-sign symmetry gives mean zero, and standard sixth-sphere moments give eigenbasis variance c_i from the displayed trace polynomial. For any pair with Haar marginals, Cauchy–Schwarz shows Var(a_i e0i+e1i)≥c_i(1−|a_i|)². The spectral reflector S commuting with H and having eigenvalues −sgn(a_i) attains all mode bounds simultaneously. Independent block noise gives even-time geometric variance and exact stationary objective for |a_i|<1. Independent analytic angular integration for d=2 checked mode moments and mixed-sign alignment.

## originality

PASS

Best-of-knowledge comparison of explicit final claim with observed primary prior statements; unresolved historical sources listed explicitly.

## value

PASS

The theorem determines the exact optimum among all within-pair Haar-marginal couplings at all even horizons and gives an actionable sharp spectral sign threshold for antithetic sampling, a natural benchmark for structured zeroth-order quadratic optimization even when its Hessian-aware optimum is informationally expensive.

The dated certificate retains the supplied scientific assessment, sources and limitations.
