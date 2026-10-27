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

# Reproduction and mathematical limits

`check_cycles.py` is a standalone Python 3 checker requiring `sympy` and `scipy`. Execute `python check_cycles.py` in the directory containing this document and the script. The script symbolically differentiates the exact inverse-definition function three times and compares those expressions with the ones used in the proof. It then numerically reconstructs the epidemic final size by solving a monotone scalar equation, checks 42 parameter cases and local multipliers, tests 199 decreasing-threshold comparisons, and evaluates examples on either side of the cost frontier.

Numerical roots are rounded finite-precision computations; they do not establish the theorem for every real parameter. The analytic proof in `RESULT.md` supplies that quantification via monotonicity and elementary calculus. At the exact touching threshold the annual map is nonsmooth; this work does not report local asymptotic stability there. The check also does not establish global basins, uniqueness of non-crossing cycles, or applicability to imperfect vaccine efficacy.

Independent audit and independent validation have not been performed.
