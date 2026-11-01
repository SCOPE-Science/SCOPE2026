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

# Reproducibility and limits
Run `python verify.py` with Python 3.11 and SymPy 1.14 or compatible versions. No network access or input files are required. The program checks the harmonic projection formula exactly, symbolic null-cone sextic examples, the area–product identity against direct harmonic extraction for specified bases, and 1,500 seeded normal directions. A distinct finite-difference support-area integration checks eight explicit situations. Its observed output was `PASS 1558 exact and deterministic finite geometric diagnostics`.

Critical mathematical evidence is the all-direction Fourier calculation in `RESULT.md` combined with the explicitly cited spherical harmonic separation and Sylvester multipole theorem. No finite sample establishes the assertion for all plane orientations. The inverse realization relies on strict positive curvature for sufficiently small nonzero perturbation and is not numerically certified for an arbitrary prescribed amplitude.

The review here is a self-review only; an independent mathematical audit has not been performed.
