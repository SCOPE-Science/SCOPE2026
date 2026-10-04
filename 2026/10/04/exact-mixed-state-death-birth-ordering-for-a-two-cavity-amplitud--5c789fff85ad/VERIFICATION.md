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

`verify_mixed_death_birth.py` reconstructs the full two-cavity/two-reservoir Stinespring evolution from the local amplitude-damping isometry.

The verifier compares direct partial traces with the analytic cavity matrix and with the complementary reservoir matrix, then recomputes both concurrences from the X-state formula. It checks the threshold signs on both sides of the predicted death and birth events, the simultaneous curve, the pure-state \(\tan\theta=2\) limit, the no-finite-threshold boundary, and the positive separation from the simultaneous curve obtained by treating the printed mixed matrices literally.

It separately confirms non-unitality by applying the one-qubit channel to \(I/2\).

These numerical checks are finite and supplementary. The all-parameter classification is proved by the affine factor
\[
rc-A(2-\eta)-rb(1-\eta)
=
(A+rb)(\eta-\alpha).
\]

No independent audit has been performed.
