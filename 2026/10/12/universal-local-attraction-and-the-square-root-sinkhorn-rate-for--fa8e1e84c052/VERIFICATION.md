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

# Reproducibility and logical boundaries

Run `python3 verify.py` using Python 3.9 or later; the script imports only standard-library `fractions` and `math` and should finish in under one second. It prints `VERIFY_OK` if all assertions pass.

The exact-rational segment checks all arithmetic steps of the cumulative-column recurrence against direct multiplicative BDRS steps for six iterates, column-sum feasibility, weighted Jacobian symmetry and stochastic invariance for a positive three-column nonsquare coupling, and the analytic two-by-two characteristic-polynomial modulus identities for seven rational parameters. The floating-point segment uses three perturbation scales to check the derivative formula to first order. It is a diagnostic rather than a rigorous all-data interval certificate.

The universal local-attraction theorem is derived analytically in `RESULT.md` from positivity of the normalized coupling, Perron–Frobenius spectral separation, the exact two-step Jacobian, and the standard local spectral-radius contraction principle. No finite run proves the infinite-dimensional quantifier over all positive finite matrices. Initializations outside a local projective neighborhood are not covered. No independent audit has been performed.
