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

# Reproducibility

Execute `python3 verify.py` using Python's standard library. It verifies the source first-integral identity exactly at specified rational points; enumerates prime-period energies for multiple step values and cutoff sizes; verifies the unique minimizing denominator pair and formula; checks quadratic counting estimates and the exact endpoint-mass expression numerically. The finite tests are not a substitute for the general proof in `RESULT.md`.

The general result rests on the source's Möbius conjugacy and rotation formula, monotonicity and strict convexity, the universal reduced-fraction denominator bound, Möbius inversion, and an elementary change of variables. Every source premise and quantitative conclusion is stated with its domain in `RESULT.md`. Verification is not an independent audit.
