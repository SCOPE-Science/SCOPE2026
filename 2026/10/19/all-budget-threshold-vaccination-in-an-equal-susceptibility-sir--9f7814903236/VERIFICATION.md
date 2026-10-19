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

# Reproducibility and limitations

The complete analytic proof is in `RESULT.md`. Run `python3 verify.py` using Python 3 standard libraries only. A completed execution returned:

`VERIFY_OK: 125 rational-grid vaccine allocations, 2 independent SIR trajectory checks; high-budget survivors 1.853622849292 > 1.574692330951`

The checker performs exact-rational comparisons of weighted unvaccinated exposure at all 125 allocations on a three-group quarter-dose grid, checks 13 exact budget levels, and uses bisection to compute the resulting survivor ordering. It also checks two distinct allocations within a tied-priority level, tests the scalar final-size identity on either side of and at the critical residual-exposure value, and solves the **original coupled SIR differential equations** independently by numerical Runge–Kutta evolution for the high-budget two-group example. The integration and bisection are floating-point numerical corroboration only.

The general theorem, including uniqueness of the physical positive root, strict positivity of the implicit denominator, exact bathtub threshold exchange, saturation of the budget, and rearrangement representation, is established analytically and does not depend on finite enumeration or numerical integration. The checker does not validate unknown prior literature, time-dependent control equivalence, arbitrarily fine grids, or any independent research certification.

## Executable artifact

`verify.py` is a complete standalone standard-library script supplied with this result. It requires no network access or auxiliary source files.
