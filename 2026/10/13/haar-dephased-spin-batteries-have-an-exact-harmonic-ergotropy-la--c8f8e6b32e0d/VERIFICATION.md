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

# Reproducibility and verification

Run `python3 verify.py` with Python 3 standard library. Expected success marker: `VERIFY_OK exact=8 gaussian= 0.451598642784 samples=48000`.

The checker constructs the binomial-degenerate spectrum from exact combinations and separately from all bitstring Hamming weights at small sizes. Two formulas for the expected work are evaluated in exact rational arithmetic for \(n=1,\dots,8\): (a) harmonic coefficients for each sorted energy and (b) independent summation of expected decreasing simplex populations. It also computes the limiting normal integral numerically by deterministic Simpson quadrature and draws 48,000 normalized-exponential (Dirichlet) samples in dimensions up to 32. These procedures check algebra and normalization at finite sizes, not the all-dimensional order-statistic identity or the limit proof.

The mathematical proof supplies the missing infinite-dimensional justification: a sorted-simplex affine coordinate map gives the Dirichlet expectations, an \(L^2\) quantile argument establishes the sharp asymptotic, and Lévy's lemma gives the probability bound. The asserted concentration constant uses the real sphere \(\mathbb S^{2d-1}\), a conservative Lipschitz bound \(4n\omega\), and Lévy parameter \(1/(25\pi)\). This verification is not an independent audit.
