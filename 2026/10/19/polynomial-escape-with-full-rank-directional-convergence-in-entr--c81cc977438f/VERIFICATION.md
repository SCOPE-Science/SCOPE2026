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

# Verification notes

Run `python3 verify.py` in the directory containing the standalone file. The program has no dependencies beyond Python's standard library. It checks the block-complex geometry in dimensions 2, 4, 6 and 8; compares the original pairwise entropy formula against its equal-singular-value limit at 16 parameter pairs; and integrates representative reparametrized planar systems with the fourth-order Runge–Kutta method for depths 2, 3 and 5. Assertions test the trapping interval, sign and monotonicity of the off-diagonal coordinate, asymptotic scaled diagonal defect, leading time scaling, and small completion loss.

These numerical checks do not prove convergence for arbitrary time or certify asymptotic error bars. Analytic proof uses the scalar comparison bounds, exact clock change, and variation-of-constants argument in `RESULT.md`. The source's entropy is defined up to an additive constant, which cancels from the flow and does not affect the logarithmic growth coefficient.

No independent audit or external scientific validation has been performed.
