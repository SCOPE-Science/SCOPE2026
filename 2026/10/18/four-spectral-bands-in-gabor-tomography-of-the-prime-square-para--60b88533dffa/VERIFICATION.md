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
The full analytic proof identifies every self-ambiguity magnitude by an exhaustive split on the \(p\)-adic valuation of the translation coordinate, and uses character orthogonality to obtain all projector-Gram eigenvalues.

Reproducible finite tests: run `python verify.py` with NumPy installed. It exhaustively enumerates all translations and all Fourier frequencies for \(p=3,5,7\), checks each magnitude against the exact permitted bands, validates their multiplicities, and checks the predicted ranks. `verify_output.txt` records one completed run. These numerical FFT comparisons are finite checks, not a proof of the all-prime theorem. Small absolute floating-point tolerance only tests the reported instances; the algebraic proof gives exact equality. No independent audit has been performed.
