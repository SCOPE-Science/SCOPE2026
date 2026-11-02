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

The exact scientific claim is proved in `RESULT.md`. The accompanying `verify.py` may be executed with `python verify.py` using NumPy and SciPy and checks independent matrix exponentials, four-state jump-chain correlations, the two repeated-root boundaries, and integrated-correlation normalizations. All 2,730 assertions passed in the execution represented by this package. The code does not constitute a formal proof of the infinite parameter assertions; the complete zero-count result follows from the ODE and the signs of its closed hyperbolic/trigonometric solutions.

The source's general stationary renewal correlation formulas are prior work. This package evaluates only the explicit two-state Markov-sign classification. Exact publication priority and independent scientific audit remain unperformed.
