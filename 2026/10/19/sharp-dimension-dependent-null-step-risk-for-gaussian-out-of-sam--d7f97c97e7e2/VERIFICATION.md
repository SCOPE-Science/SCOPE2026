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

`check.py` is a standalone Python 3 program with standard-library dependencies only. Running `python check.py` at package construction printed `PASS: 70 families of analytical and replay checks`. Checks evaluate Student-ratio tails by an independent cosine-power recurrence, integrate the accepted and proposal risks by quadrature, check the exact one-dimensional cap constants and dimension-two logarithmic behavior, and replay Gaussian training/validation independently with a fixed seed and independent batch sizes.

The proof in `RESULT.md` supplies infinite-domain validity. Quadrature tolerances, seeds, and finite-replay error bars are explicit in the source program; these checks do not certify all parameter values. This is a self-review only; independent audit and independent validation have not been performed.
