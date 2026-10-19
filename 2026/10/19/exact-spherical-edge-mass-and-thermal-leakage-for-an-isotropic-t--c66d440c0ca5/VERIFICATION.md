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

# Verification and reproducibility

The theorem is a statement about a fixed, arbitrary integer dimension \(d\ge2\), a positive parameter \(\alpha=\gamma/\mu\), and fixed thermal offset \(u\in\mathbb R\) as \(D\downarrow0\). Exact stationary Dirichlet-mean and Gaussian-convolution premises are attributed to Guéneau–Majumdar–Schehr (arXiv:2602.08436).

The analytical verification reconstructs the coordinate Stieltjes transform, the summable coefficient sequence \(a_n\), the compound-Poisson convolution asymptotic, the \(d\)-dimensional radial-moment factor, the gamma/digamma normalization and the monotone Laplace Tauberian inversion. Gaussian tail truncation controls the thermal contribution beyond fixed scaled radial deficit, and the positive Gaussian-part moment gives the explicit \(u=0\) constant.

Reproduction: with Python 3, NumPy and SciPy installed, execute `python verify.py` next to this file. The script calculates 28 independent finite-order moment comparisons and verifies eight 2D exact beta-moment identities. It then uses a fixed random seed with 180,000 stationary stick-breaking samples for each of four physical parameter pairs; two small positive thermal standard deviations are checked for each pair. Printed finite-sample probabilities, simulation uncertainty and asymptotic predictions are corroborative, not deductive. The script does not claim rigorous error bounds or a computer proof for any infinite limit.

Limits: no joint large-dimension, vanishing-tumble or diverging-offset result; no exact finite-temperature probability; no independent external mathematical audit. The strongest prior article already supplies the exact model-level transform, so originality concerns the extracted sharp asymptotic limits, not the known transform or Gaussian convolution.
