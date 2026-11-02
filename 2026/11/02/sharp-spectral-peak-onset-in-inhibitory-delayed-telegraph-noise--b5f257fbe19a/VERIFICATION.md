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

The included standalone `checker.py` uses the exact formula for the spectral denominator and an independent numerical optimizer to compare its global minimum against the zero-frequency value. It checks three parameter pairs at six relative delays, evaluates finite-interval spectral quadrature with a leading-order high-frequency tail approximation, and compares the predicted square-root peak-onset coefficient at three short positive offsets for each parameter pair. It reports `PASS: 48 independent parameter and spectral checks` with NumPy and SciPy.

The strict global inequality and critical local bifurcation follow from analytical arguments in `RESULT.md`, not finite numerical tests. The model is only asserted for \(0<h<c\) and \(T>0\); published formulas for the underlying process and Fourier transform are credited. Independent audit has not been performed.
