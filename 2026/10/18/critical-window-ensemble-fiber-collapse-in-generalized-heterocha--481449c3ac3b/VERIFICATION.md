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

# Mathematical verification

The proof in `RESULT.md` checks the geometric hypotheses at the full-fiber boundary, the reflection probability tilt and parity conventions, the local Gaussian coefficient, dominated summation, and the two extreme fixed-bias regimes. Reproduction uses only the Python standard library: run `python CHECK.py` next to the scientific files.

The checker verifies rational reflected-recursion probabilities and reflection formulas for five distinct biases through length fourteen. It separately reproduces \(M\)-adic interval depths for three choices of \(M\), and checks near-critical and exact-critical asymptotic constants numerically at finite horizon. Successful markers are `EXACT_RATIONAL_REFLECTION_AND_BINOMIAL_IDENTITIES_PASS`, `GEOMETRIC_M_ADIC_FIBER_REDUCTION_PASS`, `CRITICAL_WINDOW_BOUNDARY_LOCAL_LIMIT_NUMERIC_PASS`, and `CRITICAL_MEAN_WIDTH_CONSTANT_NUMERIC_PASS`.

No finite experiment proves the local limit, invariance principle, recurrence theorem, or exact asymptotic. Those assertions are supported by the analytical steps described in `RESULT.md`. The Gaussian formulas apply for fixed real drift, not for drifting ranges that increase with the horizon. There has been no independent mathematical audit.
