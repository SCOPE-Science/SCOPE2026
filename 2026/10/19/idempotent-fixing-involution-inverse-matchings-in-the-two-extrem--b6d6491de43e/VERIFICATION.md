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
The included `check_extremal.py` exhaustively tests the rank-two and rank-\(n-1\) classes of every \(\mathcal O_n\) with \(3\le n\le8\). Its tests calculate the ordinary composition law, check that each output is again order-preserving of the same rank, and verify both mutual-inverse equations and involutivity, including fixed idempotents. Run `python3 check_extremal.py` from the extracted finding directory.

A finite test is not an argument for every \(n\). The universal proof is the explicit formula combined with the kernel/image transversal criterion in `RESULT.md`. No independent external certification or audit is claimed.
