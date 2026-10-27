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

# Reproducibility and verification

The standalone `verify.py` requires Python 3, NumPy and SciPy. Run `python verify.py` in the directory containing it. The program performs 36 direct independent position-space versus Fourier-space density-matrix comparisons, 16 Bessel integral and recurrence tests, and 192 normalization, symmetry and asymptotic crossover checks. All 244 assertions passed.

Finite tests do not prove the theorem. The uniform two-step expansion and telescoping estimate, Bloch rotation, and analytic Fourier–Bessel integration are the proof of the stated arbitrary-length limiting law. The program uses eight representative scaled times, even and odd lengths up to 801, and numerical tolerances appropriate to the finite-size approximation.

No independent audit, external formal verification, priority certification or human validation is claimed. The result is restricted to the single homogeneous delta coin, the specified equal-phase initial spinor and fixed finite scaled times.
