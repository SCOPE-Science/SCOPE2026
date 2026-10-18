---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For a completed n×p matrix X with unbiased sample covariance S=(1/(n−1))Σ(xi−xbar)(xi−xbar)^T, the exact scatter identity Σ_{i<j}(xi−xj)(xi−xj)^T=n(n−1)S proves Φ=n(n−1)p whenever every original row pair is active, equivalently at most one complete original row. Checked original paper Eqs. (3.1), (3.3), (3.8), active-pair definition, Eq. (3.11) ridge via full public text. Independent rational 6×2 example using SymPy gave det(S)=2552/25 and tr(S^-1 T)=60; the separately inspected package verifier constructs a six-missing-variable design with full rank six and two distinct positive-definite completions of value 60. Substituting (S+ηI)^-1 gives ridge formula n(n−1)Σλ/(λ+η), which is not flat in general. Independent Bernoulli cell omission probability q gives C~Bin(n,(1−q)^p), hence P(C≤1)=P(C=0)+P(C=1) and its Poisson transition at n(1−q)^p→λ. Statements conditional on positive definite completion and fixed original mask; no inference about singular or generally optimized ridge cases.

## originality

PASS

The source's Theorem 1 proves full-rank uniqueness of the FROZEN-covariance linear Hessian, not uniqueness of covariance-updated objective. Its Eq. (3.8) explicitly recomputes sample covariance from completions and states the nonlinear problem is generally nonconvex; it does not identify the all-active-pair exact constant objective in Section 3 or the MCAR dimension transition. The scatter identity is standard, but its implication for the exact source optimization program, the full-rank/flat contrast, and dimensional mask phase threshold are not the same as known generic Mahalanobis-depth imputation. Resultary search and relevant missingness source comparison found no covering same-object statement. Best of knowledge with classical folklore risk.

## value

PASS

Pinpoints an identifiability failure of a recently published nonlinear imputation refinement even when the predecessor linear design has full column rank; gives exact ridge caveat instead of pretending regularization fails similarly. The exact independent-cell MCAR mask threshold quantifies when all pairs are active, with a critical logarithmic dimension useful for experiment design, while not claiming all imputations fail on that event.

The dated certificate retains the supplied scientific assessment, sources and limitations.
