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
The exact identity uses \(s=\sqrt{a_1}\), \(b=a_4/2\), \(\beta=a_3-a_4^2/4+2s\), and the optimized \(\alpha=-2a_2-2a_4s\). The cancellation of all cubic and linear terms reduces nonnegativity to one squared quadratic plus \(\beta x^2\). At \(\beta<0\) the quadratic has one positive and one negative real root, so no affine adjustment can make both evaluations nonnegative.

For the dynamics, differentiate \((2-2\alpha y-\alpha^2x^2)e^{\alpha y}\) directly; its exact time derivative is \(\alpha^2x^2e^{\alpha y}(\alpha x+2H)\). The \(\alpha=0\) case uses the quadratic energy directly, not a limiting version of the certificate derivative.

For boundedness, \(\phi'(x)=(1+x^2)^{-3}\) and \(\phi\) is bounded. The upper bound on \(\dot W\) is of order \(-x^6+O(x^5)+O(x^4)-\tfrac12\phi'(x)y^2\), which is negative outside some compact set. A hyperbolic local sink and the exclusion of periodic or connecting invariant graphs force omega-limit convergence.

Run `python3 check.py` to reproduce exact rational evaluations for a sample, a boundary configuration, and a below-threshold obstruction. The checker is not a universal finite certificate, and no independent audit has been performed.
