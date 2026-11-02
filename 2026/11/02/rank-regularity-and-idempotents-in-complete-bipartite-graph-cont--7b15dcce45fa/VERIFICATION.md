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

Run `python3 verify.py` from the directory containing this document. The program tests continuity directly by checking inverse images of every vertex and edge; computes regularity through an independently generated continuous section for each map; computes idempotence from the original partial-function identity; and compares three coefficient arrays for every rank against the theorem's closed formulas.

Observed output ended with `VERIFY_OK` after four graph-size tests, including \(K_{2,2}\), \(K_{2,3}\), and \(K_{3,3}\). The full source code is included in this package. The enumeration is exhaustive for the listed finite graphs only; unlimited parameters rest on the argument in `RESULT.md`. The 2026 target preprint was not inspected in full; this limits historical originality assessment, not the proof's finite combinatorial derivation. No independent audit has been performed.
