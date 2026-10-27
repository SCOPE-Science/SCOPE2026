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
# Verification and limits

Run `python3 checker.py` with a standard Python 3 interpreter. It independently integrates the Fourier coefficients by composite Simpson quadrature for 120 combinations, compares them with the closed formula, checks positive coefficients at both boundaries through finite orders, and computes explicit negative Fourier eigenvalues of finite circulant Gram matrices outside the claimed parameter interval. Its completed checks had maximum integral discrepancy \(5\times10^{-15}\), with exterior circulant witnesses approximately \(-26.75888014\) and \(-0.06042365\).

The universal assertions require the analytic identities and inequalities in `RESULT.md`: (i) exact cosine-integral formula, (ii) strict parity-monotone ordering of all logarithmic derivatives, (iii) the positive hyperbolic-function inequality, and (iv) Fourier uniqueness for strict finite-site positivity. Finite frequency scans or finite matrices cannot establish the infinite-dimensional classification; the proof treats all nonnegative integer modes. Numerical testing of the two-sided boundaries is supplementary only.

The geodesic metric normalization and the range \(a>0\), \(b\in\mathbb R\) are essential. In particular, the Euclidean chordal-distance and periodicized Matérn constructions are different objects. Independent scientific audit and external validation are not performed.
