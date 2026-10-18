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

# Reproducibility and boundaries

Run `python verify.py` from the directory containing the script with Python 3, NumPy, and SciPy installed. The computation needs no network access and no auxiliary files. It checks \(d\in\{3,4,5\}\) and \(q-q_c\in\{0.03,0.01,0.003\}\), using Bessel quadrature to a radial cutoff of \(550\) and the explicit leading averaged Hankel tail for each finite-exponent integral. For all nine pairs, the computed ratio of the scaled sharp gap to the cutoff-derived predicted constant lies between \(0.96\) and \(1\), improving toward one as the exponent gap decreases. The script also returns positive finite-cutoff critical differences in the three dimensions. Its successful message is `VERIFY_OK 9 cutoff-assisted Bessel moment and scaling comparisons`.

Analytic verification: equation normalization is verified against the spherical Fourier--Bessel decomposition; the existence of \(\Delta_d\) uses a zero-mean periodic primitive with a uniformly integrable \(r^{-2}\) error. Strict positivity uses the *complete-cell* theorem in arXiv:2610.19648, Theorem 3.9, at its permitted exponent \(q_c>2\). The exact optimal global stability identity is from Theorems 1.2--1.3 of the same paper and is not recomputed numerically.

Limitations: finite oscillatory quadrature has cutoff, discretization, and approximate-tail errors, and cannot establish a positive infinite integral or an exact exponent. The checker does not replicate the long published proof of strict Bessel modal ordering. These are explicitly supplied as mathematical inputs to the analytic proof. No independent audit or certification was performed.
