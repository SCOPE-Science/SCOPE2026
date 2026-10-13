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
The standalone `verify.py` tests the exact rank-one Rademacher sketch law on multiple strictly positive diagonal spectra, using Python's rational arithmetic, not floating-point tolerances. It checks every first-stage sign sketch and every residual sign probe in dimensions two through five, plus all two-probe combinations for small dimensions.

For each selected spectrum it compares all conditional output probability multisets, checks the weighted sign-sum formula, calculates the exact rational mean and variance and compares against the proved expression. It separately checks the complete flat-spectrum two-point law for a \(2\times2\) identity multiple and the isotropic variance in larger dimensions.

These finite checks are transcription evidence only. The proof in `RESULT.md` uses exact sign conjugation, quadratic-form moments, and a general positivity argument, and does not rely on extrapolating numerical experiments to all dimensions.
