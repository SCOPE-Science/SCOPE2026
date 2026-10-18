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
The included `verify.py` recreates the canonical thirty-six-vertex graph from cyclically stable five-subsets, checks the independence polynomial via a separate recursive recurrence, enumerates all 1,519,600 augmented faces, constructs 759,796 matching pairs, and exhaustively verifies directed incidence-graph acyclicity by a complete topological sort. It also checks the exact critical masks, six of dimension six and two of dimension eight. The empty face is paired; Forman's theorem supplies a basepoint in the resulting CW model.

Run `python verify.py` with Python 3 and sufficient memory. No external dependencies are required. Exact integer arithmetic and set operations are used throughout, with no sampling or floating-point ranks. The verifier checks the finite combinatorial certificate, not any higher homotopy attaching maps. Independent external audit has not been performed.
