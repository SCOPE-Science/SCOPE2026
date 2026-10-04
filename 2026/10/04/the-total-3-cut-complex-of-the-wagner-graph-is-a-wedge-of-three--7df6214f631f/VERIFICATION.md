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

Run `python3 artifacts/verify.py` from a directory containing the embedded artifact. The verifier reconstructs the graph and total \(3\)-cut complex from definitions rather than loading a precomputed table.

It checks the eight independent triples, face vector \((8,28,48,32,8)\), the \(60\)-pair matching and four critical faces, and all \(368\) directed Hasse edges. A topological sort visits all \(124\) nonempty faces, proving the matching acyclic. It separately computes mod-\(2\) boundary ranks \((7,21,24,8)\), Betti vector \((1,0,3,0,0)\), and Euler characteristic \(4\).

Expected final line: `VERIFY_OK`.

The computation proves only the finite statement for \(M_8\) and \(k=3\). No family periodicity or claim for other coefficients is inferred from the mod-\(2\) cross-check; the homotopy conclusion instead comes from the acyclic matching.
