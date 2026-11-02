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
# Reproducibility and limits

Run `python3 check_sunlet.py` from the directory containing this file. The standard-library-only checker evaluates root and leaf Fourier blocks against direct distance matrices for specified odd and even graph orders, evaluates closed exponent-one spectra, and numerically brackets some thresholds. It prints 4,377 assertion groups passing and a numerical cosine-integral constant near 8.097627357.

The numerical experiments are finite and subject to floating-point tolerances, and do not establish the infinite asymptotic theorem or historical originality. The analytic Fourier, Taylor, and bounded-variation arguments in RESULT.md are the proof. No external independent validation is represented by this document.
