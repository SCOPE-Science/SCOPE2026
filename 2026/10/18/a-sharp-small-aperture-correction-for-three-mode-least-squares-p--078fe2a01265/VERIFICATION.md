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

# Reproducible verification and limitations

Execute `python verification/check_arc.py` in an environment with SymPy and mpmath. The checker derives the endpoint Legendre polynomial, its two zeros, the exact leading and quadratic constants, the factored monotonicity expression, and the second-order expansion of the genuine trigonometric Gram kernel. Five independently evaluated small-aperture integrals check the fourth-order remainder magnitude. During preparation all 25 assertions passed.

Analytical ingredients not delegated to finite numerics are explicit in `RESULT.md`: strict global maximizers from the central Cauchy--Schwarz bound and end-region derivative sign, uniform persistence by compactness and the implicit-function theorem, and the exact sign-region integration that produces the second-order coefficient. No finite set of successful samples certifies a statement quantified over all sufficiently small apertures. The value of the maximal admissible aperture is not determined. Historical originality is not independently certified.
