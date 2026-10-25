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

# Verification record

Run `python3 verify.py` in the same folder. The verifier requires Python 3.9+ and no external packages. Its deterministic stdout is in `verification_output.txt` and ends in `VERIFY_OK`.

The verified assertions cover the six-permutation multiplication table, exhaustive one-cell-per-row legal face enumeration, distinctness and completeness of all 3,054 nonempty face masks, 12/324/216 maximal faces of sizes 3/4/5, exactly 1,402 disjoint matching pairs, a full 3,054-vertex topological sort on the directed graph of all 10,368 Hasse incidences, exactly 49 critical two-cells and 200 critical three-cells, construction of all 9,800 entries of the signed Morse matrix, 37 exact integer unit pivots and a zero 12-by-163 residual matrix.

A separate mod-two boundary computation on the original face complex yields the ranks `(35,325,863,216)` independently of the Morse-boundary recurrence. The homotopy conclusion additionally invokes the standard topological fact that, with one zero-cell and no one-cells, attaching maps of three-cells to wedges of two-spheres are determined by the corresponding integral degree columns, and unit columns permit elementary cell cancellation.

No independent audit, external proof assistant certification, or assertion about unenumerated infinite families is represented here. Exact finite verification does not itself establish bibliographic priority.
