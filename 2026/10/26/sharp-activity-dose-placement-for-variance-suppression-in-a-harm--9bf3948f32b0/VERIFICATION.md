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

Run `python verify.py` and `python verify_budget.py` in the same directory with Python 3, NumPy and SciPy. The first provides 461 independent ODE/invariant-envelope comparisons; the second provides 23 response-kernel, window-selection and exact ODE perturbation comparisons. The tests were executed on the supplied source files, and do not constitute an exhaustive search over measurable controls. The proof in `RESULT.md`, based on the generator, Volterra integral bounds, strict response unimodality and the allocation exchange principle, establishes the universal claim.

For the finite amplitude \(\varepsilon=0.1\), the displayed example compares three particular schedules and must not be interpreted as a proof of global finite-amplitude optimality. Only the first-order optimizer is globally classified.
