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

# Reproducible checks and bounds

Run `python verify.py` with Python 3, SymPy and SciPy installed. The program checks exact symbolic identities linking the transient generator, survival Laplace transform, derivative/convolution transform, mean, variance, squared coefficient of variation, and its derivative. It also checks a sharp interior maximum for \(m=1\), \(\lambda=1/10\), \(c=59/180\), then independently computes first two moments by fundamental matrices over 128 parameter triples. The finite parameter checks, floating-point resolvents and time comparisons are corroboration only. Universal validity derives from the analytic proof in `RESULT.md`.

No external or independent audit is asserted. The model contains no claims about stochastic dominance outside the fixed-marginal-hazard two-patch Poisson disaster mechanism. Published related sources are not exhaustive; Johst–Drechsler (2003) could not be inspected in full.
