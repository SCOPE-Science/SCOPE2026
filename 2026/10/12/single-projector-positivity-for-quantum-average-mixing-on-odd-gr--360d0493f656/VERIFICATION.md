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

The standalone `verify.py` checks integer-valued signed transversal vectors for graph orders corresponding to \(1\le k\le6\). It verifies the adjacency eigen-equation at every vertex, all asserted moments of explicit degree-\(j\) witnesses, and lower-degree incidence orthogonality for \(k\le4\). Execute from a directory containing this file and `verify.py` with `python3 verify.py`. Python's standard library suffices.

The actual unrestricted mathematical proof is in `RESULT.md`: its orbit-spanning argument and projector factorization establish the result for every integer \(k\ge1\). Finite verification does not certify all parameters or replace independent review.
