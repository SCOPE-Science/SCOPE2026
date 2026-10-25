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

# Reproduction and limitations

Run `python verify_spectrum.py` with SymPy (see `requirements.txt`). `CHECKS.txt` records the actual program output. The checker reconstructs the 24 root vectors, tests the exact adjacency product identities and idempotent projectors, checks their traces `(1,2,9,4,8)`, and checks the complete Chebyshev sampling Gram formula and nonnegative spectra in degrees 0 through 48. The general proof uses exact matrix identities and Chebyshev parity and does not extrapolate from the finite tests.

All normalization conventions and exceptional degrees are specified in `RESULT.md`. No independent mathematical audit has been performed.
