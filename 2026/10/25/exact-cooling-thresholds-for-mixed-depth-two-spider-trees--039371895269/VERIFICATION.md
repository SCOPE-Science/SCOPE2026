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

# Reproducibility

Execute `python3 verify_mixed_cooling.py` using Python 3 and no third-party dependencies. The companion text file `verify_mixed_cooling_output.txt` records the exact output.

The propagation enumeration implements the definition: first choose an arbitrary source, then at each later round propagate all cooled-neighbor edges and choose a new uncooled source unless all vertices are cooled. It searches every legal strategy using memoized cooled subsets for all 35 graphs having one to six short arms and one to six two-edge arms, subject to a total center degree of at least three.

A separate distance implementation builds breadth-first-search distances, independently searches feasible source tuples, and tests survival after the third or fourth round on 30 small graph/threshold pairs. It agrees with propagation enumeration and the closed formula in all tested cases.

These checks are finite. The infinite case split is proved in `RESULT.md`. No external mathematical audit or formal proof certificate is claimed.
