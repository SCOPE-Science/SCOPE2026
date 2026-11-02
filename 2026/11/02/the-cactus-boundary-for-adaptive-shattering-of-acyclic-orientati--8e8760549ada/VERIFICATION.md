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

# Reproducibility and limits

Run `python verify.py` with Python 3.9 or later and no third-party dependencies. The program reads `certificates/diamond_tree.json` from the adjacent directory and validates every internal query and all 16 leaf witnesses in the complete depth-four tree for the diamond graph. It independently enumerates all 18 acyclic orientations of the diamond, checks exact adaptive and static dimensions there, then tests the predicted one-level excess for six theta-subdivision examples. Finally, it exhaustively evaluates all labeled simple graphs on four and five vertices, using independent cycle detection, graphic rank computation, orientation enumeration, and the exact Littlestone recursion. All results are deterministic.

The observed standard output is in `verification_output.txt`. Its final line is `ACYCLIC_ORIENTATION_CACTUS_ALL_CHECKS_PASS`. The 1,088-graph small-order census tests rather than proves the unrestricted classification. The all-graph argument appears in the mathematical proof, particularly the two product/extension lemmas and the theta-subdivision construction. No Lean proof, external peer-review evidence, or independent audit is claimed.
