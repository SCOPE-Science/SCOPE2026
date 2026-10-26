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

# Verification of the co-rank-one involution

Run `python check_corank_one_involution.py` using standard Python 3. The script exhaustively checks the algebraic inverse identities for each map in the rank-\(n-1\) class for \(2\le n\le9\) by direct composition; it also tests involutivity, fixed-point classification and cycle counts independently of the semigroup-structure argument. The expected final output is `VERIFY_OK`. The finite checks are not a proof for unbounded \(n\); the universal proof is in RESULT.md. No independent audit is claimed.
