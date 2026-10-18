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

# Verification

Execute `python3 check_coloring.py`. No third-party dependencies are used. The program checks two point-line realizations, all possible labeled two-colorings, a separate vertexless-triangle construction, two independent adjacency descriptions, and full all-source shortest paths. It checks exact output counters, including 52,416 ordered detours and 112 detours per source; no random sampling or timeout-as-proof inference is used. `check_output.txt` records one successful execution. The precise claim is finite; no infinite-family inference is made.

The two models use homogeneous dot-product incidence and an affine-plus-infinity incidence construction. Both share the final indexed point representation but derive their line incidence differently. Breadth-first search is the exact shortest-path algorithm for finite unweighted graphs. The full transcript output is an ordinary computational reproducibility check, not an independent scientific audit.
