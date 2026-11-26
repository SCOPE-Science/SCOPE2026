---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

In a two-sided Poisson process the backward age and successive completed gaps from a fixed observation time are independent exponentials. Conditional Brownian independence gives the series, square-summable since ρ(A)<1, and synchronous coupling multiplies initial differences by A^{N_t}→0. The transform follows by conditioning; the displayed Frullani representation yields a symmetric Lévy measure with summed truncated second moments bounded by Σ_j tr(Σ_j)/λ. For v≠0, positive-definite noise makes the nonzero scale parameters exactly the nonvanishing iterates of A^T. Infinite survival gives arbitrarily many inverse-quadratic factors. With m finite, |t|^{2m−2} times the transform is integrable. Partial fractions give exponential-polynomial expressions on the two half-lines, including repeated poles, so one-sided limits exist. In the product Green equation only the top derivative can produce an atom, and its coefficient forces the claimed jump. Invertibility gives uniform radial bounds from the smallest eigenvalue of each finite covariance factor. In the singular case a joint density still exists, but if it were globally C², the distributional stationary equation would equate a locally absolutely continuous source to λ times a probability supported on ran A, impossible.

## originality

PASS

The scalar stationary product, scalar all-orders smoothness, full-reset Laplace cusp, and affine reset framework are prior. The supported distinct result is the sharp directional classification for arbitrary stable deterministic matrices, including the jump at each finite annihilation length and the non-C² joint consequence of rank loss. No inspected statement supplies that classification or a stronger one subsuming it.

## value

PASS

Loss of information under anisotropic resets motivates asking which projected observables retain a cusp despite nondegenerate diffusion. The zero-eigenvalue chain length gives an exact and useful distinction, and the coefficient quantifies it. The joint obstruction prevents inferring global elliptic smoothing merely from the noise covariance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
