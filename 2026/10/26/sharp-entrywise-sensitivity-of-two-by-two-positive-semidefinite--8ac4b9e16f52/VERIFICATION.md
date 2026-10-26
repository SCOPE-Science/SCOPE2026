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

Run `python3 check.py` from the directory containing this document and `check.py`. The script uses only the Python standard library and executes exact-fraction coefficient checks, an integer-polynomial factorization, a rational spectral-Jacobian decomposition for 155 parameter pairs, four exact sharpness-direction identities, and three floating-point finite-perturbation checks. In the recorded replay it printed `PASS: 2711 exact/algebraic and sample numerical assertions`.

The checker supplies reproducible internal cross-checks, **not** exhaustive evaluation of real parameters. Universal correctness comes from the derivation in `RESULT.md`: (i) the spectral derivative formula, (ii) absolute row sums and the factored sharp inequality, (iii) strict integration across all nonsingular segment portions with a rank-one-line exception, and (iv) the limiting witness. Finite perturbation ratios are a diagnostic and are not claimed to attain the supremum. No separate independent audit or external validation has been performed.
