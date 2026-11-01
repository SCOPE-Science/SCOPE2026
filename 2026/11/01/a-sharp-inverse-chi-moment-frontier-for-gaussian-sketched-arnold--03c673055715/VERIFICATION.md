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

# Reproducibility and scientific limits

Run `python verify.py` with dependencies from `requirements.txt`. The script reconstructs the exact \((1,3)\) coefficient of \(RAR^{-1}\) symbolically, tests leading minors of the stated SPD matrix, and checks 900 independently seeded Gaussian sketch instances at six different sketch-row counts by QR similarity and an independently coded sketched modified Gram–Schmidt Arnoldi procedure. It also checks the small-argument chi CDF asymptotic at five degrees of freedom. Execution in the packaged environment passed all assertions.

The moment equivalence \(\mathbb E|h_{13}|^p<\infty\iff p<\ell-2\) for all real \(p>0\), the exact tail constant and the Gaussian weak limit are consequences of the analytic argument in RESULT.md; the script cannot certify infinite-dimensional quantifiers or prove noncoverage by previous publications. The coefficient is measured before the third step's terminal basis normalization. Numerical agreement is sensitive to exceptional ill-conditioned Gaussian sketches and does not assert finite arithmetic robustness.
