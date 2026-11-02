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

Execute the accompanying `verify.py` under Python 3. It implements Roman feasibility directly from adjacency and independently checks pointwise minimality by one-coordinate decreases; feasibility is upward closed, so this checks the full definition. The program exhaustively checks all \(75\) simple base graphs with \(1\le n\le4\), then every Roman function on the sunlets of cycle orders \(3\) through \(6\), comparing raw enumerations against both subset and weighted-transfer formulas. A separate recurrence calculation tests the exact unweighted Pell–Lucas formula for cycle orders \(3\) through \(18\).

The expected completion marker is `VERIFY_OK`. The computational scope is finite and does not establish the theorem for arbitrary graph orders; the proof in `RESULT.md` supplies that argument. The matrix characteristic polynomial is also displayed explicitly there and can be checked by a direct four-by-four determinant expansion. No independent audit has been performed.
