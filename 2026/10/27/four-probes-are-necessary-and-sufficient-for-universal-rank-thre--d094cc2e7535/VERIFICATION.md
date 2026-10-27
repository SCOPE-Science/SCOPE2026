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

Checks performed on this claim:

- Recomputed the fixed-rank dimension as the Stiefel-manifold dimension minus the free Kraus-gauge dimension: \(2d^2r-d^2-r^2\).
- Recomputed the rank-three qubit values: channel-manifold dimension \(11\); three probe outputs have at most \(9\) real coordinates.
- Checked that the four stated pure-state density matrices span \(I\) and all three Pauli directions, hence a basis of Hermitian \(M_2\).
- Checked that the no-injection argument is an invariance-of-domain contradiction and that the generic fiber statement is restricted to the maximal-rank locus of the real-analytic evaluation map.
- Checked the claim against the stated hypotheses and scope of the three cited primary sources. No numerical experiment is used as proof.

Limits: the general formula is a necessary lower bound, not a universal exact minimum for arbitrary d and r. The claim concerns exact noiseless output states and a fixed universal probe set, not target-specific exceptional sets or finite-sample stability.
