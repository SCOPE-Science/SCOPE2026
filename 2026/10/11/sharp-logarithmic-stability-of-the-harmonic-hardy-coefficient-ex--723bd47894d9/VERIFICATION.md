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

The coefficient-duality identity and the ensuing weighted quadratic defect estimate are derived analytically in `RESULT.md`. The weighted cosine distribution is integrated exactly, and the sharpness family is handled for every integer coefficient index by a measure-preserving circle map. The decisive lower bound optimizes over both phase parameters; it is not inferred from observing one particular sign function.

To replay representative numerical consistency checks, use `python3 check_stability.py` in this directory. Nine cases passed using the Python standard library, comparing directly computed Fourier coefficients with the weighted defect expression. No finite quadrature establishes an infinite or uniform theorem. An independent audit has not been performed.
