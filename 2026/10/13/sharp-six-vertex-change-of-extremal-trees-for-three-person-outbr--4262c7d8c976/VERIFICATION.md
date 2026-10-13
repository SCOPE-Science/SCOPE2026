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

Run `python3 verify.py` in a directory containing the two files. The checker uses Python's standard library. It derives both edge-state and connected-induced-subtree coefficient vectors, confirms they coincide on all six unlabeled trees, exhaustively generates unlabeled trees via Prüfer sequences up through six vertices, tests the table and fourteen exact factorizations, and rechecks the bridge-loss formulas for a finite range of sizes. Its successful result begins with `VERIFY_OK`.

This is a deterministic finite cross-check. The proof's unrestricted quantification over all larger tree orders rests instead on the one-edge failure expansion and explicit graph families; the checker does not claim an exhaustive census at large sizes. A separate independent audit has not been performed. The claim does not extend to correlated SIR transmissions or heterogeneous edges.
