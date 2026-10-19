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

# Verification of the cusp-order return-time theorem

The standalone program `verify.py` was run against the accompanying files with Python 3 and produced `VERIFY_OK`. Five exact-rational trajectories for \(p=2\), \(\lambda=1/5\), including initial heights exactly equal to powers of \(\lambda\), match the claimed eventual integer recurrence. Six other combinations of cusp order and contraction strength were simulated in logarithmic coordinates to check the predicted late return-time ratios without numerical underflow. These finite checks are falsification tests, not a verification of all real parameter values or all forward times.

The general proof is deductive: positive height persists; the upper branch immediately returns to the lower branch; repeated lower contractions eventually cross the power cusp; the exact integer first-return threshold follows from a strict inequality. Uniform boundedness of reset positions gives a bounded-error affine recurrence, whose normalized sequence converges to a strictly positive limit. For the parabolic cusp, the reset coordinate approaches one from below, fixing the integer floor even at resonant heights. No computer-assisted exhaustive infinite statement or independent review is claimed.
