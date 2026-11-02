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

The complete finite certificate consists of `orbits.json` (all 21 representative supports under the natural six-label permutation action), `tree.json` (a depth-four decision tree with 16 distinct center witnesses), and `verify.py` (an executable checker requiring only the Python 3 standard library).

The verifier independently enumerates all 4,845 four-query supports in addition to reconstructing every orbit. It checks the trace spectrum, all leaf paths of the decision tree, all Johnson parameters through six elements up to complement symmetry, and the open/closed contrast. All computations apply to explicitly finite sets; no conclusion about arbitrary Johnson parameters or historical priority is inferred from finite tests.
