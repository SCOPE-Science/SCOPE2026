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

# Reproducibility and verification

The analytic proof in `RESULT.md` is primary evidence. It checks existence and uniqueness of nonzero scalar equilibria, the monotone hyperbolic crossing, exact block averaging for any square-integrable initial state, the two planar eigenvalues, and exponential decay of the transverse component. Its claims do not rely on a finite truncation.

Run `python verify.py` using only Python's standard library. The checker independently evaluates the explicitly identified root and its gain, confirms the equilibrium identity for both block signs, verifies the polarized mode signs below and above the crossing, and checks that the critical common-mode eigenvalue vanishes while the difference-mode eigenvalue is negative. The test completed successfully for the stated numerical example.

The numerical checks use ordinary floating-point bisection and do not independently prove uniqueness or quantify all possible rounding errors. Those conclusions instead follow from the monotonicity and exact reduction established in the proof. Stability at the nonhyperbolic equality case, finite-network approximations, and global attraction of polarized states are not asserted or checked.
