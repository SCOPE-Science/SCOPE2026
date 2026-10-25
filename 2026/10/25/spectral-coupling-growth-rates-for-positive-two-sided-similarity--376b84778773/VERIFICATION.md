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

The result is established analytically in `RESULT.md`, including the support-localization lemma, finite spectral-grid upper bound, localized-compression lower bound, two-sided growth formula, and intertwining characterization. In the quasi-Banach range \(0<p<1\), the proof specifically uses the \(p\)-triangle inequality and the two-sided ideal property; no convexity of the quasi-norm is assumed.

The standalone `verify.py` uses NumPy to compare finite spectral-coupling ratios against norm-root values for \(p\in\{0.5,0.8,1,2,4,\infty\}\), both conjugation directions, and multiple positive powers. It also tests an exact nonzero intertwiner with two different spectra. Its output reports the number of finite supplementary checks actually performed.

This numerical experiment is not an exhaustive computation over operators and is not a proof of an infinite-dimensional statement. Nonpoint spectral support is addressed by the analytic proof and the explicitly calculated rank-one multiplication example in `RESULT.md`. No independent external scientific validation is represented.
