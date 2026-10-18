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

# Reproducible checks and scope

Run `python3 verify_peak.py` with Python 3 and its standard library. The program computes the exact fractional-linear logistic flight and finite-dimensional periodic map over positive rational exponential flight factors. It establishes the stated two-pulse example exactly and compares 144 algebraic and numerical assertions for two- and three-pulse timing choices. All checks passed on the packaged version.

The mathematical proof, not sampling, covers arbitrary real \(A,T>0\), any finite number of pulses, and all prescribed multipliers in \((0,1)\) satisfying \(e^{AT}Q>1\). Floating-point bisection is used only for a three-pulse illustrative bound; the two-pulse example and repeated test trajectories use `fractions.Fraction`. The upper bound is a supremum when multiple pulses are required to have strictly positive separation, not an attained maximum. Invasion claims are linearized around the disease-free orbit and are not nonlinear eradication guarantees.
