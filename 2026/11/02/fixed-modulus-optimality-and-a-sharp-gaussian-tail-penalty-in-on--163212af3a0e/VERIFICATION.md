---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For A=U diag(sqrt(a_i)) with right singular vectors coordinate-aligned, a_i>0, d≥3, q≥0, one iid nonzero centered unit-variance real probe, the one-column projection residual is ∑a_i−∑a_i b_iW_i/∑b_iW_i, b_i=a_i^(2q+1). Swap-symmetrization of exchangeable positive W_i shows α_j−α_i=(b_i−b_j)E[(W_i−W_j)^2/(2SS_swap)], giving the claimed sum of nonnegative pair terms and strict equality cases. Finiteness requires only E W_i=1 and S>0, not 4th moments. In spike family H=L^(2q+1), sign excess=(L−1)(d−1)/(H+d−1), Gaussian excess=(L−1)E[(1−T)/(1+(H−1)T)] with T~Beta(1/2,(d−1)/2). Dominated convergence under u=Ht yields sharp H^(−1/2) constant. Independently enumerated 18 positive finite-law products with exact fractions and checked pairwise identity.

## originality

PASS

Exact distribution-free one-column aligned iid sign-optimality and Gaussian one-spike excess exponent are not the same as high-probability error bounds for general sketches or rotation-invariant adversarial minimax bounds. The inspected full Saibaba–Międlar analysis covers bounded/subGaussian probes and oversampled methods, not this complete fixed-matrix optimality identity; priority of an earlier exchangeability inequality remains qualified.

## value

PASS

A genuine design rule for the simplest randomized subspace-iteration building block: constant-magnitude sign probes minimize expected squared error for fixed aligned spectra, with quantified excess of all competing iid magnitudes and a sharp Gaussian power-iteration decay penalty. The alignment and one-column restrictions are explicit mathematical boundaries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
