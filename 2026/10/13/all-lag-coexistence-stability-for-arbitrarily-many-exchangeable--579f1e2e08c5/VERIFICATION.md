---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

At strictly positive equilibria P_i=I_i, R_i=aI_i/b and S_i=1-(1+a/b)I_i. Dividing equilibrium equations by full positive product Q yields common strictly decreasing f(z)/Q(z), forcing equal I_i. Scalar equilibrium F(x) decreases from R0 to zero, so unique iff R0>1. Physical 3n Jacobian diagonalizes via symmetric and zero-sum eigenvalues θ+=1+(n-1)w, θ-=1-w>=0. Verified algebraically independently using SymPy the block M(v), char cubic A1=b+c+u, A2=u(a+b)+c(b+u+v), A3=c(u(a+b)+bv), and A1A2-A3=(b+u)[u(a+b)+c(b+u+c)]+cv(u+c)>0. All finite n modes strictly Hurwitz; no assertion of global stability or uniform rate.

## originality

PASS

The 2026 original LeJeune et al. 37-page arXiv full text, §3.2, tables and Appendix were inspected. Its s>0 coexistence stability conditions are explicitly conjectures, while only no spillover is proved. New equal-parameter n-parameter extension and strict all-lag positivity not implied by the published conjecture or generalized symmetry method. Other models differ substantively. Residual risk of equivalent unindexed epidemiology theorem acknowledged.

## value

PASS

Completing an explicitly stated dynamical stability conjecture under motivated equal-parameter conditions, excluding Hopf for all positive perception lags, and proving extension to arbitrary finite exchangeable n pathogens is a meaningful structural theorem with a nontrivial cubic certificate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
