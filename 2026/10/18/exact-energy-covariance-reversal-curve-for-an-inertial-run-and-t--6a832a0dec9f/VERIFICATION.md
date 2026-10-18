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

# Verification of the stationary energy-covariance sign boundary

Run `python verify.py` after installing SymPy. The code independently constructs the generator's polynomial-moment linear systems for degrees one, two, three and four, solves the systems using exact symbolic arithmetic, and checks their nonzero determinant factors and the displayed covariance rational expression. It separately performs 54 exact rational parameter solves, confirms the derivative-sign and limiting-root algebra, and checks sample parameters on opposite sides of the sign boundary. The executed program reports 135 passed exact assertions.

Analytic conclusions use positivity of the denominator, strict monotonicity of the threshold polynomial in the flip rate, its constant term's sign, and strict monotonicity in damping. The finite test cases are not an exhaustive proof; they supplement the exact generator and algebraic sign argument in RESULT.md.

All statements require strictly positive damping and switching rates. The zero-damping and zero-switching values are limiting boundary statements only. No independent audit or experimental validation has been performed.
