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

The exact order-five classification is reproducible using the standard-library program `verify.py` together with `profiles.csv`. Executing `python3 verify.py` reconstructs and compares an Eulerian DFS enumeration and all \(65536\) incoming/outgoing pairing assignments. It checks all \(2048\) distinct cycles and both independent maximal-run enumeration methods, verifies the length-profile table and all \(528\) symmetry orbits, and compares each row with the supplied CSV. Exact integer and rational calculations verify the six cells, the three total-run frequencies, the two period-two run-length distributions, and both reported moments.

Mathematical scope: cyclic factors have length at most the circumference, and maximal runs have least period at most four by the unique five-bit-window lemma. This is a finite classification only at order five. The general bound on least periods and the number of unary runs are proved directly in `RESULT.md`, not extrapolated from finite tests. External independent auditing has not occurred.
