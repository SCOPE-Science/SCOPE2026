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

The analytic proof is the primary evidence.

`artifacts/verify.py` exhaustively checks every nondecreasing complete-multipartite part profile of total order \(2\) through \(7\), for every \(1\le k\le4\). It enumerates all labels \(0,1,\ldots,k\), evaluates the open-neighborhood rainbow condition directly, compares that result with the part-count criterion, groups feasible functions by count matrices, verifies the multinomial coefficient contribution, and compares the brute-force minimum with the closed subset-capacity formula.

Replay output:

`ALL CHECKS PASSED; profiles=37; enumerators=148; labelings_checked=1591634; orders=2..7; colors=1..4`

The finite computation is corroborative only. The theorem for arbitrary part sizes and arbitrary \(k\) is proved in `RESULT.md`.
