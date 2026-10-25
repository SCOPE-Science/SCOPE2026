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
The geometric identity is \(W_n=\sum_{\{i,j\}\in E}|U_i-U_j|\), with \(U\) normalized in the intrinsic zero-sum hyperplane. The file `graphical_width_checker.py` is standalone apart from NumPy and was executed with `python graphical_width_checker.py`. Exhaustive sign choices for four small zonotopes gave 160 exact support/width comparisons, each within \(10^{-12}\). For 12,000 independent simulated directions per graph on 360 vertices, the sample centered-width variances were path \(0.417701\), cycle \(0.411029\), and four-regular circulant \(0.855115\), against theoretical limiting expressions at finite graph densities \(0.415349\), \(0.415644\), and \(0.860061\). The script checks every simulated absolute deviation is below \(0.11\), and every empirically centered mean is within \(0.07\) of zero. This is a diagnostic, not an exhaustive test of the limiting theorem.

The analytical verification checks the bivariate Gaussian absolute-moment coefficient, the exact \(\operatorname{Cov}(S_n,Q_n)=\mu m_n\), bounded-dependency cumulants of order \(r\ge3\), the effect of subtracting the Gaussian sample mean, the radial Taylor remainder, and positivity of the final variance. Every coefficient follows from the assumptions stated in `RESULT.md`. No external mathematical audit or certification was performed.
