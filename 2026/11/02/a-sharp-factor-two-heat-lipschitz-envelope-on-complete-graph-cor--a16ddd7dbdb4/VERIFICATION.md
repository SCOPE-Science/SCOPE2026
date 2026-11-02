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

The derivation and proof are contained in `RESULT.md`. In `verify.py`, the full \(2n\)-vertex heat kernel is independently evaluated by stochastic uniformization of the exact finite graph generator. The resulting signed rows are converted to transportation costs via the pendant/complete-core flow formula and compared to each of the two analytic spectral expressions. For \(n=2,\ldots,12\) and five strictly positive time values, every one of the graph's 1,815 edge instances is included. A second calculation enumerates all integral one-Lipschitz potentials (with one core value fixed to zero) on \(n=2,3,4,5\), at two positive times, and verifies the dual transport values for 68 edge cases. The integrality follows from total unimodularity of directed incidence difference constraints.

Execution command: `python3 verify.py` (Python 3 standard library only).

Expected success lines:

```
CHECK_OK complete_corona_n=2..12 time_cases=55 edge_transport_checks=1815
CHECK_OK independent_integer_KR_dual_cases=68
CHECK_OK onset_derivative=n_minus_3 limiting_envelope=2
```

The finite floating-point evaluations are checks of implementation and formulas, not a substitute for the universal analytic proof. The strict signs, all-time maxima, complete extremizers, and sharp family envelope are established by exact algebraic inequalities in `RESULT.md`. No independently performed audit or external proof certification is asserted.
