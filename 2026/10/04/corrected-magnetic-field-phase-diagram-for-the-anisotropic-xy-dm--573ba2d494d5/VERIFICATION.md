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

The source Gibbs state was independently reduced to its two \(X\)-state concurrence candidates. Squaring only nonnegative quantities gives the exact equivalences
\[
f_1>0\iff q_B>2,
\qquad
f_2>0\iff q_B<0.
\]

`verify_xy_dm_field_phase.py` checks those equivalences on deterministic grids, verifies the single-maximum shape for \(B>B_0\), solves the tangency equations for the source parameters, and checks the predicted root counts below and above \(B_*\).

For
\[
J=1,\qquad
\gamma=0.6,\qquad
D=0.5,
\]
the replay returns
\[
B_*=1.7495575301980955\ldots.
\]

Finite numerical checks are supplementary. The global root-count classification and high-field asymptotic are proved analytically in `RESULT.md`.

No independent audit has been performed.
