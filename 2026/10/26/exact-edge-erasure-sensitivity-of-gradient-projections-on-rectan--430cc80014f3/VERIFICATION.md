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

The identity follows from the explicit full-biclique additive-centering matrix and its exact rank-one row/column erasure update. The original sign analysis divides retained edges into three automorphism orbits; every coefficient sign and each row sum has a stated algebraic proof. For exact computational cross-checks, run `python edge_erasure_checker.py` with SymPy. The script grounds one vertex, independently inverts the incidence Gram matrix, and checks every row-norm expression on 49 graphs (1,176 edge rows). It executed successfully. These are finite tests, while the rational identities in RESULT.md establish the unbounded integer range.

The literature comparison inspects the Hodge projection description and transfer-current formula in the two cited papers, with prior balanced-parameter coverage expressly distinguished. Unindexed or differently named prior treatments remain a possibility. This verification contains no external independent audit.
