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

The general claim was checked algebraically by reconstructing both equilibrium equations rather than using the reduced quadratic alone. For a positive biomass coordinate, the water coordinate is positive exactly when the shared denominator \(a+mu-u^2\) is positive; its positive zero is \((m+\sqrt{m^2+4a})/2\).

`verifier.py` replays the exact witness with `fractions.Fraction`. It verifies the source case assumptions, the nonzero quadratic root, both equilibrium residuals at \((u,v)=(2,-1)\), the negative denominator, and the branch-sign numerator. It also enumerates the quadratic roots for the witness and confirms that no positive root yields positive \(v\).

The checker is finite only for the witness. The universal equivalence is supplied by the symbolic proof in `RESULT.md`; no finite experiment is used as an infinite proof. No stability, nonlinear bifurcation, or ecological-calibration claim is verified.
