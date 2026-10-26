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

`CHECKER.py` reports 223 passing deterministic assertions when executed with `python CHECKER.py` and the `mpmath` and `sympy` packages. It verifies the exact algebraic simplification of the fourth cumulant, the positive-coefficient identities, the zero-rate series coefficient, 62 successive coefficients of each positive-series criterion, and the derivative-based moment and pole formulas at eight rates. It separately matches the value and flux across the switching point of the backward ODE for twelve Laplace arguments.

The infinite proof is in `RESULT.md`: the Taylor coefficient formulas are valid for **all** integer indices and the induction establishes positivity beyond finite tested indices. The renewal pole is local in its transform parameter; finite numerical pole checks are not evidence for analytic existence and simplicity, which follow from exponentially integrable nonlattice regeneration times.

Scope limits: this verifies the fixed-rate long-time coefficient only. No finite-time sign theorem, irregular-spacing theorem, asymptotics uniform in rate and observation time, or external independent validation is claimed.
