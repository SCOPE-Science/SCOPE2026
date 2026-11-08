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

The exact checker `verify.py` reconstructs the root coordinates and reads `collapse_pairs.json` from its own directory. It verifies all 752 ordered elementary free-face removals, the face count at every removal stage, the final induced eight-vertex four-cross-polytope boundary, and the pairwise Euclidean distance shells. The one-dimensional, two-dimensional, and higher-dimensional homotopy conclusions use the explicit cell-structure and join arguments in RESULT.md; the mod-two rank calculation is an independent finite check, not an integral-homology certificate by itself.

To reproduce: put `verify.py` and `collapse_pairs.json` in one directory and execute `python verify.py`. The provided `verification_output.txt` is the output of that exact command. Every integer and face comparison is exact. The verifier checks the finite 24-point complex only and does not certify any proposed infinite-dimensional or varying-parameter extension.
