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

# Reproducibility and proved limits

Extract the accompanying Python source `verify.py` next to this file, then run `python verify.py` using Python 3 standard library only. Its tested run printed:

```
VERIFY_OK exact_assertions=18167
```

The code uses exact rational Fourier coefficient maps; it checks rank-one cosine updates, Duhamel expansion, companion-block characteristic polynomials for several degrees and feedback parameters, and the nonreturn of off-resonance harmonics. The code does not simulate the full infinite-dimensional function space and cannot alone establish the theorem.

Separately, a periodic-grid centered directional-difference test of the original pushforward formula compared 25 observable/parameter combinations (five degree/harmonic/strength cases and five output frequencies), at 32768 grid points and difference step \(10^{-5}\); the comparison tolerance was \(2\cdot10^{-7}\). This numerical check is a derivative-normalization diagnostic only.

The infinite-dimensional theorem is established by Steps 1–4 of RESULT.md: test-function linear response, sharp transfer contraction scale, exact harmonic-return recurrence, and finite-dimensional eigenblock. The spectral classification does not assert nonlinear local stability or independent validation.
