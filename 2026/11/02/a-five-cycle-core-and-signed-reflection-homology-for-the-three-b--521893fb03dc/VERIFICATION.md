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

# Exact certificate checks

Run `python CHECK.py` with `COLLAPSE.json` beside it. The checker derives eleven perfect matchings from the 3-by-4 Cartesian grid, enumerates 495 simplices, verifies 242 elementary free-face pairs from the certificate in exact succession, identifies the final five-vertex, five-edge cycle, and computes exact oriented simplicial Lefschetz numbers for row, column, and combined reflections. The terminal success marker is `GRID34_COMPLETE_COLLAPSE_AND_SYMMETRY_OK`. The computational proof is exhaustive only for this finite graph, not for other grid sizes. The scientific documents and checker must be assessed independently before treating the result as externally validated.
