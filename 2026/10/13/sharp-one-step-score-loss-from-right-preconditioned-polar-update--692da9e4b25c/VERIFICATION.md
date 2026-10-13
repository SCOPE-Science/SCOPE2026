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

## Reproduction

With Python 3 and NumPy installed, run `python verify.py` in the directory containing the supplied script. The script uses a deterministic NumPy random generator and Python's standard `fractions.Fraction` for the exact-rational checks.

Observed output:

`VERIFY_OK rational_sharpness=70 random_full_rank_cases=2160 sharp_sequences=5 line_search_cases=2160`

The verifier reconstructs each thin polar factor from an independent SVD, recomputes both quadratic scores and optimal line-search decreases, and checks the predicted \(4\kappa/(\kappa+1)^2\) bound on real square and rectangular full-rank matrices. It also checks commuting equality, the nearly rank-one sharpness limit, and 70 rational specializations of the exact limiting identity.

## Logical limits

Sampling and floating-point calculations cannot certify the theorem for arbitrary matrices. Its universal proof relies on the positive-semidefinite spectral polynomial, the nuclear-norm triangle inequality, the polar variational characterization, and a full-rank limiting family. The independent audit has not been performed.
