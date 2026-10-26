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

The mathematical theorem is proved analytically in `RESULT.md`. `checker.py` is a finite numerical cross-check. Run `python checker.py` after installing the two packages in `requirements.txt`; its archived standard output is `checker_output.txt`.

The checker performs six independent one-dimensional integrations of the normalized trapezoid indicator, 270 exact-parametrization reciprocal-lattice zero checks, and finite-radius distinct-zero censuses at \(R=45,90\) for \(\alpha=1/4\), \(\alpha=2/5\), and \(\alpha=\sqrt2/4\). Numerical root localization uses sign changes and may miss tangencies or detect approximate duplicates. Hence neither those counts nor the asymptotic visual agreement constitutes a certification of the infinite zero set. In particular, the \(O_\alpha(R)\) theorem rests on the monotonic tangent-branch lemma and lattice-counting proof, not on root sampling.

The original numerical output recorded a maximum quadrature discrepancy below \(10^{-15}\); all finite assertions passed. No external independent audit or scholarly publication-priority determination has been conducted.
