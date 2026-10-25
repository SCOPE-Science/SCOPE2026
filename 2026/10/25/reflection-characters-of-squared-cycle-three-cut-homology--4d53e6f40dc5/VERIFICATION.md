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

# Verification details

Run `python3 verify_reflections.py` with Python 3.9 or later; no optional packages, network services or external source files are required. The program reconstructs simplices directly from graph connectivity and compares them against the four-orbit dual-face classification. It then calculates signed fixed-face Lefschetz sums for every reflection and compares with the closed formulas.

Verified output:

`VERIFY_OK dual_graph_sizes=14 dual_symmetry_checks=217 direct_cut_symmetry_checks=69 independent_face_template_checks=14`

The dual checks cover \(9\le n\le22\). Separate direct ordinary-cut-chain checks cover \(9\le n\le14\). These finite computations do not establish the universal quantifier; the proof in `RESULT.md` relies on an exhaustive neighbor-offset classification for \(n\ge9\), the fixed-orbit table and equivariant combinatorial Alexander duality. The known degree concentration comes from the published shellability theorem. No external independent audit has been conducted.
