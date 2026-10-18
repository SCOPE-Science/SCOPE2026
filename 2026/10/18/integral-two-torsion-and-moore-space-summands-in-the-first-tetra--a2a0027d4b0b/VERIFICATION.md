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

# Reproducible finite verification

Run `python3 verify_johnson.py`; Python 3 standard library only. The program constructs the graph from lexicographic three-subsets, the ordinary open-neighborhood simplices and all consecutive-dimensional Hasse covers. In each of the two principal cases, it verifies the full acyclic matching by topological sorting of every oriented Hasse cover. It then recomputes the signed dimension-three cellular Morse boundary by integer unit-pivot elimination and verifies its greatest common divisor is two. The recorded critical-cell vectors leave no higher or lower attaching maps to inspect. Exact integer calculations are performed without floating-point arithmetic.

Expected data: \(n=6\), \(8620\) faces, \(4238\) pairs, \(41940\) Hasse covers, critical profile \((1,0,1,142)\), Morse differential \(31(+2),23(-2),88(0)\); \(n=7\), \(136220\) faces, \(67723\) pairs, \(839580\) Hasse covers, critical profile \((1,0,1,772)\), Morse differential \(125(+2),131(-2),1(-4),515(0)\). The preceding \(n=5\) case has critical profile \((1,0,0,11)\) and is also acyclic. These complete certificates support the finite-scope homotopy claims; no unbounded family or external independent validation is asserted.
