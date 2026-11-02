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

The analytic proof proceeds through a gap-feasible lattice of integer lifts, a monotone interpolation lemma, cyclic-order preservation under token slides, and the exact median-flow metric of a cycle. The boundary configurations at \(n=6,k=3,U=2\) demonstrate failure without slack; the \(C_5\) example distinguishes isometry from the stronger geodesic-convexity property.

Executable check: `python verify_mv_isometry.py` using the standard Python library. For every \(n\) from 3 through 17, the checker independently constructs visible triples from the original geodesic-avoidance definition, reconstructs ambient and restricted token graphs, and compares **every** ordered-pair restricted distance, ambient distance, and median-flow expression. There are 162372 tested ordered pairs. The checker additionally verifies the saturated configuration obstruction. This check is finite; the theorem for arbitrary parameters rests on the proof, not extrapolation.

The verification does not assess historical priority, independently certify the proof, or extend the result to general graph hosts.
