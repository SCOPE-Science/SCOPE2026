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
# Verification

The analytic argument is given in RESULT.md. It uses convexity of the centered operator norm, a complete Fourier decomposition of the invariant transition matrices, exact minimax balancing of the two extreme rim eigenvalues, and elementary trigonometric bounds. No general statement rests on finite enumeration.

`verify.py` forms full stochastic matrices and separately solves the full invariant Fourier-mode linear program. Dependencies are in `requirements.txt`. On execution, `verification_output.txt` records:

`VERIFY_OK phase_pairs=209 invariant_LP_comparisons=98 direct_full_spectra=50`

All 209 examined integer pairs agree with the claimed sharp phase conditions; 98 linear programs and 50 full spectra also agree within explicit numerical tolerances. These tests are reproducible supplementary checks and do not constitute an independent mathematical audit.
