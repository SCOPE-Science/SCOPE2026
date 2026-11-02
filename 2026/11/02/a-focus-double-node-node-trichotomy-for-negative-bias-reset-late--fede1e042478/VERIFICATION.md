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

# Verification and limits

The analytical proof is in `RESULT.md`. `verify.py` can be run using Python 3 and only the standard library. It constructs exact rational sample trajectories from the original piecewise map and checks their agreement with the scalar recurrence through first contact. It verifies that the map reaches \((-\varepsilon,-\varepsilon)\) exactly two steps after contact, and reconstructs exact forcing-response and eigenvalue identities for representative distinct and repeated positive-root cases.

The program checks 36 separate finite trajectories, using three rational seeds, three rational parameter sets representing the focus/double-node/node regimes, and four positive rational biases. It also checks first-contact inequalities for every visited index, the positivity of the relevant real-root response, and eventual decreasing order of sampled exact bias thresholds. It prints `PASS` and concrete sample times when successful.

These are finite reproducibility checks only. They do not certify a universal infinite claim, originality, or a human expert audit. Universality follows from the proof: decay of the linear positive-branch recurrence to a negative affine equilibrium, explicit impulse-response formulas, and fixed-index sign change of an oscillatory homogeneous solution. Numerical or exact finite enumeration never substitutes for these arguments.
