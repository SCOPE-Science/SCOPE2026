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

Run `python3 verify.py`. The script uses only the Python standard library. It reconstructs the Desargues graph, enumerates every independent set, checks the exact face vector, rebuilds the stated staged Morse matching, orients and checks every Hasse cover for acyclicity, computes the signed integral Morse boundary from the five critical 5-cells to the unique critical 4-cell, and independently computes all simplicial boundary ranks over \(\mathbb F_2\).

A successful run prints the face vector, critical cells, boundary ranks, Betti numbers, the zero Morse boundary vector, and ends with `DESARGUES_IND_VERIFY_OK`. The finite computation proves only the stated finite-graph claim; no family-wide extrapolation is made.
