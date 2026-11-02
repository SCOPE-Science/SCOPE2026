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

The supporting `verify.py` program uses SymPy for exact transfer, characteristic polynomial, nilpotency, power, and rational boundary calculations and NumPy for sampled singular values and spectral radii. Install `requirements.txt` and run `python verify.py`. The script passed during analysis with the final line:

`VERIFY_OK: 3600 Schur pairs, exact transfer matrix/characteristic, 12 critical orders, 108 exact powers, finite-horizon norms, 19990 optimization samples, 5/2 example`

The finite tests are corroboration only; proof of all positive parameters and all positive integer horizons is contained in `RESULT.md`. The critical spectral optimum at total sum one is an infimum only. Claims about noise, arbitrary variation or nonquadratic convergence are not made. The source-priority assessment is finite and independent validation has not been performed.
