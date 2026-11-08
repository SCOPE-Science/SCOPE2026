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

The exact ordered adaptive-pivot probability is Δ_ij/(S t_i), where S=tr K and t_i=S-(K²)_ii/K_ii. The last Schur complement trace det(K)/Δ_ij cancels Δ_ij, giving E=2det(K)/S sum_i 1/t_i. Inserting the spike identities yields the stated separable law. Each summand 1-L/[L+1+(L-1)w] has second derivative -2L(L-1)^2/[L+1+(L-1)w]^3<0; strict Jensen proves the unique balanced maximum and concavity/simplex vertices the axis minima. Direct exact rational Schur-complement enumeration of 16 independent matrices reproduced both stages, boundaries and 2-DPP benchmark. The one-step expectation K−K²/tr(K) is spectrally invariant, while dimension 2 has zero residual after two pivots. Limit L=1 has nonunique equality and is deliberately excluded.

## originality

PASS

Existing RPCholesky work derives the general one-step map and generic error bounds, whereas this claim computes the actual two-step expectation and all fixed-spectrum 3x3 orientation extremizers; a DPP comparison already known is properly acknowledged. Exact bounded instance search cannot by itself establish novelty.

## value

PASS

At fixed eigenvalues, this is a minimal sharp example showing eigenvector orientation can change expected sequential adaptive Cholesky performance; the exact 3/2 asymptotic gap and complete extremizers are useful counterpoints to spectral-only bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
