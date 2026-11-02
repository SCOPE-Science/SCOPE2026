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

# Verification record

The complete proof is in `RESULT.md`. The independent-from-proof finite checker `verify.py` uses Python's standard library and runs with `python verify.py`. It passed 22,455 assertions, including exact rational five-vertex Markov products and endpoint algebra, numerical checks of all nonconstant Fourier modes for odd orders through 301, sampled competing feasible weights, and direct matrix reconstruction on smaller dimensions. A separate global numerical optimization using differential evolution on selected odd dimensions matched the formula to numerical precision.

These are finite or floating-point tests and do not prove the infinite family; the proof derives the lower bound and attainment analytically. Unrestricted spatially inhomogeneous factors, more than two rounds, and even cycles are outside the theorem. No independent mathematical audit has been performed.
