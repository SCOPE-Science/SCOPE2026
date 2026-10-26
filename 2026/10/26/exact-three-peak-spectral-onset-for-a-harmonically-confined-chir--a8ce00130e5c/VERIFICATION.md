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

## Reproducibility
The standalone `spectral_verify.py` computes the reduced rational-spectrum derivative by exact symbolic differentiation and checks its expanded polynomial. It reconstructs the cubic discriminant and critical factorization with rational arithmetic. It checks the fold slopes, the central-curvature polynomial and 10 independently isolated sample-root configurations. The run completed 21 assertions without exception.

## Boundaries
The symbolic checks verify algebra and finite parameter samples; they do not replace the proof of the root-count trichotomy over all continuous parameter values. The proof's root-sign and strict-concavity arguments are necessary for that infinite statement. Independence and external certification have not been undertaken.
