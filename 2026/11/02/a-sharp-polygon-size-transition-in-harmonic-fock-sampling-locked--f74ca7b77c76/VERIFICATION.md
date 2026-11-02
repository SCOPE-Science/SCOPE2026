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

The mathematical proof is contained in RESULT.md and does not rely on numerical sampling. The embedded standalone checker (`checker.py`) computes the normalized harmonic reproducing-kernel Gram matrices and separate Poisson-residue series, compares spectra, positivity, trace and mode symmetry across multiple dimensions and radii, then verifies the exceptional transition formulas and selected alternating-mode witnesses. The exact roots-of-unity asymptotics prove the unbounded-radius conclusions; finite assertions alone cannot establish them. The checker executed successfully with 456 assertions. Independent audit has not been performed.

