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

The result is proved symbolically, with no reliance on floating-point parameter scans. Run the embedded standalone file using:

`python verify.py`

It prints `VERIFY_OK` only after exact-rational checks of the conditional quadratic-drift identity and its representative drift signs.

The checker uses six independent quadratic-state tests and six distinct rational positive normalized stepsizes. Multiplying the drift identity by \(s\) gives a polynomial in \(s\) of degree at most five, whose coefficients are quadratic forms in the state. Since the six test states independently determine every coefficient of a quadratic form in three variables, and six distinct values determine a degree-five polynomial, these checks certify the identity for all real \(s\ne0\), not just the sampled values. Positive definiteness and the implication from the drift identity to mean-square convergence/nonconvergence are proved analytically in `RESULT.md`.

At the critical value \(s=2/\sqrt3\), the conditional energy drift is exactly zero and the energy is a nonnegative martingale. The checker does not infer almost-sure convergence or divergence from this equality.
