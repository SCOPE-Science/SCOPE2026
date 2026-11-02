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

# Verification and scientific limits

The exact monomial-basis matrix is diagonal with eigenvalues \(\lambda_n=n!^{-1}\int_{N-c\sqrt N}^{N+c\sqrt N}s^ne^{-s}ds\), for \(N=R^2/t\). Thus the infinite-dimensional normalization and the trace are established analytically. The proof in `RESULT.md` invokes the classical uniform Berry--Esseen bound for integer-shape Gamma sums on bounded rescaled index windows and Gamma Chernoff estimates for the tails. The latter are essential for applying continuous functions dominated near zero by \(u^p\), and finite numerical checks do not replace them.

Run the included source with `python verify.py`. It tests finite incomplete-Gamma eigenvalue sums at several parameter values, the exact trace \(2c\sqrt N\), the Schatten-defect Gaussian-profile integrals for exponents below, at and above one, the norm limit and the identity and derivative of the closed-form trace crossover. All tests are supplementary and do not establish novelty or the limit theorem. Source comparisons and residual publication-priority uncertainty appear in `REVIEW.md` and `AUDIT.json`.
