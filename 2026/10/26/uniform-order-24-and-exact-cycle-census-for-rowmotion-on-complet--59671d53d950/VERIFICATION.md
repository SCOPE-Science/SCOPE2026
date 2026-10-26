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
# Reproduction

Run `python3 verify_rowmotion.py` from the extracted package directory. Python's standard library is sufficient. The command reports `VERIFY_OK` when all checks pass.

The first check derives the \(48\)-state support dynamics directly from the three ideal-presence bits in every column. It verifies the \(13\) support cycles, their induced symbol permutations, the surjection-based cycle formulas, and cardinality identities. The separate finite check explicitly enumerates every ideal for \(2\le n\le6\) and compares minimal-complement rowmotion, rank-ordered toggles, and the full orbit histogram.

The mathematical all-parameter deduction relies on the proof that the symbolic support projection is exact for any number of leaves; verification at the finitely many named \(n\)-values is a consistency check only. No external independent audit or broader-group rowmotion verification was performed.
