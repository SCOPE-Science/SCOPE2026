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

# Verification of algebraic identities and finite numerical illustrations

The accompanying `verify.py` is a standalone Python 3 script requiring SymPy, NumPy, and SciPy. Execute it with `python verify.py` in any directory containing the script; no other files are required. It checks by exact symbolic polynomial operations that:

* For \(q=b/(c-b)\), the derivative of \(V_q=[x^2+(1+q)y^2+q(z-c)^2]/2\) is \(-ax^2-q(z-c)^2\).
* At \(c=b\), the derivative of \((y^2+(z-b)^2)/2\) is exactly \(-(z-b)^2\).
* The claimed center-manifold four-jet satisfies both invariance equations through the required orders, and the reduced cubic and quintic coefficients imply the stated logarithmic coefficient.
* Both noncentral equilibria are solutions at one exact positive parameter choice where \(c<b\).

The code then integrates three critical parameter choices to finite time \(4000\), compares the subtracted inverse-square clock at times \(1500\), \(3000\), and \(4000\), and checks convergence at an off-critical parameter choice. These finite tests are numerical corroboration only. Global completeness, exact global convergence, uniqueness of the exceptional stable manifold, its measure zero, and infinite-time asymptotics depend on the mathematical proof in `RESULT.md`, not on the executable.

The independent audit state in the front matter is intentionally `not_performed`. This file does not claim any outside certification.
