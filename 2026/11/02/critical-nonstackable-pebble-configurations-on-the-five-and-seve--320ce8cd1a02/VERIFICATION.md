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
# Finite verification

Run `python verify_cycle_stacking.py` using Python 3's standard library. The algorithm enumerates all weak compositions through size \(8\) on \(C_5\) and size \(17\) on \(C_7\). It implements two independently oriented reachability algorithms: forward recursion on each state and reverse generation from stacked states. Their complete layer-by-layer successful sets must agree. It then checks exact identity of the critical bad sets with disjoint dihedral orbits and checks the empty bad sets at sizes \(8\) and \(17\).

This is a finite exhaustive verification of a well-founded recursion, not a heuristic search or an attempted proof for larger cycles. Only the named configurations, their labelled orbit counts, and the two finite thresholds are certified. The figures and algorithms already published for the numerical thresholds are not independent validation of this orbit refinement.
