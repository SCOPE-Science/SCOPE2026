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

Run `python3 verify.py` from the same directory, with Python 3. The program requires only the standard library and compares symbolic floor formulas over **entire intervals** using exact rational numbers in \(\mathbb Q(\sqrt2)\). Its division-free algebraic-number sign test and bisection integer-floor routine avoid floating-point tolerance; endpoint inequalities imply the interior floor is constant by affinity.

The seven exact interval certificates produce return vectors \((0,-1),(-1,0),(0,0),(1,-1),(-1,-1),(-1,-1),(-2,0)\). The adjacent equal outcomes combine to the six-phase theorem. A separate exact integer replay covers all \(19,999\) starting integers from \(2\) through \(20,000\) and validates the attainable breakpoint \(a=2\). This is an independently implemented replay of finite parts of the *same analytical argument*, not independent scientific review.

The entire continuum of fractional parts is covered by the seven symbolic interval checks and the one attainable breakpoint. Uniform distribution of \(a/\sqrt2\) and the infinitude/density of cycles are mathematical deductions from irrationality; finite tests do not establish either limiting statement. The check makes no claim about initial conditions off the positive horizontal axis.
