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

# Reproducibility checks

The analytical argument consists of the published Laguerre Fourier--Weyl multiplier, a smooth localization on its finitely many spectral circles, the angular Bessel obstruction to planar \(L^p\) Helmholtz waves for \(1\le p\le4\), and the angular plane-wave construction of a bounded \(J_0\) null symbol for \(p>4\). The exact endpoint coefficient is obtained by averaging \(\cos^4\) over its oscillation period. These steps are not replaced by finite numerical experiments.

The accompanying `check_threshold.py` passed 153 deterministic checks with NumPy and SciPy: Laguerre positive roots and their numerical simplicity through degree 11, six angular integral identities, the fourth-power logarithmic slope on three annuli, and radial Bessel envelope values. Execute `python check_threshold.py` in a Python environment with these two packages installed.

No independent mathematical audit has been conducted. Historical-priority uncertainty and the bounded-symbol/one-complex-dimension scope remain.
