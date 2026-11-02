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

# Verification notes

The package contains a self-contained mathematical argument in `RESULT.md` and a separate numerical checker, `verify.py`. The checker depends on `requirements.txt` and was run against the embedded source files. It checks monotonicity of the exact integral eigenvalue formula, six normalized defect comparisons in dimensions one and two, 18 Gaussian-profile samples, six normalized traces, three quantile crossings in each dimension, six numerical curvature identities, and the normal-pair integral value \(1/\sqrt\pi\). These finite checks are supplementary only. The all-degree trace limit is justified analytically by the exponential-tilting tail inequalities in the proof, not by finite sampling. Independent proof review, independent computational validation and a definitive historical-priority audit have not been performed.
