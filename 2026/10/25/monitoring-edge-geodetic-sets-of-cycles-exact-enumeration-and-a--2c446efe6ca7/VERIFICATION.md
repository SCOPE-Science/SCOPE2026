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

# Reproducible verification

Run `python3 verify.py` with Python 3 and only its standard library. The expected final output is `VERIFY_OK`.

The program independently constructs the path-distance change condition for each edge failure and each probe pair using breadth-first search, without relying on the cyclic-gap theorem. It exhaustively tests every subset for each \(3\le n\le16\), compares the all-set coefficient distributions with the cyclic-gap classification, and tests the exact polynomial for the inclusion-minimal sets. The program also checks the boundary cases \(n=3,4\), where the only MEG-set is the entire cycle, and even cycles where four-vertex minimal sets occur.

The finite checks do not establish infinitely many cases. The complete proof is contained in `RESULT.md`, Lemmas 1--5, with no external software, tables or unprovided files required. Literature priority is not mechanically certified.
