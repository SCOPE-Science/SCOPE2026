---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

Factor Sigma=BB^T even in singular rank; if m>0 the nearest point p to the convex hull of the row vectors gives a unit Gaussian direction u with all common-factor loadings a_i>=sqrt(m). Condition on the orthogonal Gaussian residual: nondecreasing functions of shared Z have nonnegative cross-covariances. Hermite-Mehler contraction yields E Var(f_i(X_i)|H) >= a_i^2/Sigma_ii Var(f_i(X_i)), giving beta>=m/M. If m=0 a nonnegative linear Gaussian relation has zero numerator and positive denominator; strictly increasing slopes approximated. Independent rank-two mixed-sign example has m=1, M=10. We verified factorization and singular boundary, rather than inferring the theorem from finite checks.

## originality

PASS

The exact statement in Sei 2022 Section 7 is Conjecture 4, while Appendix E.2 establishes only positive-definite covariance. The factor separation plus Hermite conditional contraction resolves the missing strictly copositive singular case with explicit modulus. General matrix copositivity and Gaussian association/product inequalities are distinct and do not yield the nonlinear variance inequality without extra work. Resultary and primary term searches found no identical theorem, with residual search risk.

## value

PASS

Directly resolves a published named Gaussian-distribution conjecture and produces a dimension-free explicit positivity modulus m/M for singular Gaussian laws, a substantive characterization applicable beyond positive-definite covariance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
