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

# Computational verification
The companion `verify_height2.py` performs complete direct face enumeration and exact mod-two boundary elimination for 119 eligible rooted-depth-two tree parameters \(1\le k\le4\), \(0\le b_i\le2\), total vertices at most 12. Seven additional parameter cases include \((2,2,2,2)\) and \((3,3)\). Every computed reduced Betti vector agrees with the exact sphere-wedge theorem. Eleven exact signed fixed-simplex Lefschetz computations agree with the asserted branch/leaf permutation action. `verification_output.txt` records a deterministic successful execution.

The computation supplies independent checks over characteristic two and of rational traces in finite cases, not a proof of integral torsion-freeness for all trees and not an independent scientific audit. The general statement follows from the complete center-link proof and integral Künneth argument in RESULT.md.
