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

# Reproducibility and limits

Run `python verify.py` from the directory containing that file. The standard-library script enumerates all \(n^{n-2}\) labeled Cayley trees for \(2\le n\le8\) through Prüfer codes, determines the marked root's parity class and degree directly, and checks the exact joint-count formula. Exact rational checks also cover class-size normalization, symmetric tilting, two variance/covariance identities, and reverse total positivity for \(2\le n\le22\). Additional numerical checks at larger sizes illustrate, but do not establish, the asymptotic values. The recorded execution passed 203981 assertions in under four seconds.

The infinite-law verification is analytical: the weighted matrix-tree cofactor gives an exact generating polynomial, the binomial ratio argument covers all integers, and the asymptotic covariance uses a cited established near-symmetry limit. The Gaussian–Poisson joint limit uses the cited marginal Gaussian limit and convergence of conditional probability generating functions. No independent proof assessment or external certification is asserted.
