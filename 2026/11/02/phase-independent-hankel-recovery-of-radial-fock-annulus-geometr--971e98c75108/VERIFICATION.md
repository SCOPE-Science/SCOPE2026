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

# Verification and limitations

The main theorem is verified analytically in `RESULT.md`: Fourier coefficients and gamma moments are computed in the stated normalization, the first nonconstant harmonic is nonzero, the exact Hankel identity is algebraically established, higher harmonic errors have a strict geometric bound, and inversion uses nonvanishing denominators.

Reproduce supplementary checks with Python 3 and the packages `mpmath` and `sympy`:

```shell
python checker.py
```

Expected output: `PASS 58 supplementary assertions`. The test covers three masks, including wrapped arcs, plus symbolic Hankel cancellation and auxiliary trace normalization. Numerical checks are finite and are not a proof of the infinite-index asymptotic, eventual sign, or novelty. General radial-symbol injectivity was known previously; only the specific sign-definite constructive geometric recovery is assessed as a new result. Unordered spectra and finite-noise stability are not covered.
