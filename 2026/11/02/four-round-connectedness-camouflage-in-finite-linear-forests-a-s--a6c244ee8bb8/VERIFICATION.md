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

The full finite classification uses a deterministic exact first-order type recurrence over ordered tuples, including repeated vertices. A disjoint union of paths is represented by a nondecreasing partition of its vertex order. `verify_exhaustive.cpp` checks all such partitions with parts at least two for vertex orders 4 through 29, compares their rank-four codes against all single-path rank-four classes (represented by path orders 2 through 35), and records partition counts in `exhaustive_diagnostics.txt`. The run found 3,690 negative cases below 29, then 845 negative cases and the single positive case `(14,15)` at total order 29.

Independent bottom-up type-refinement implementation `verify_boundary.py` compared the canonical path `P_16` with the positive two-component representatives `(14,15), (14,16), (15,15), (15,16), (16,16)` and negatives `(13,16), (14,14), (12,18)`, and checked `P_15 != P_16`. It returned `INDEPENDENT_BOTTOM_UP_BOUNDARY_OK`.

`census.csv`, `boundary_output.txt`, `exhaustive_output.txt`, and `exhaustive_diagnostics.txt` are the data/output artifacts. Reproduction is by `bash REPRODUCE.sh` with a C++17 compiler and Python 3; no other libraries are needed. The separate Brown–Hoshino connected-path theorem supports the infinite reduction, while disjoint-union congruence is proved in `RESULT.md`. The supplied programs are finite proof aids, not a formal proof-assistant or independent external mathematical audit.
