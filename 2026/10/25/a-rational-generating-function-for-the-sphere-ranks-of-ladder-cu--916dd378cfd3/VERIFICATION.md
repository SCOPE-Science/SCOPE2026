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

Run `python3 VERIFY.py` using only the Python standard library. It tests \(3\le n\le7\), \(3\le k\le\min(2n-3,8)\), a total of 21 pairs; compares the transfer-weight enumerator against direct connected induced-subset enumeration; checks the count of deletion-robust induced subsets; checks the sign-correct reduced Euler characteristic from explicit cut-complex faces whenever \(n\le5\); and checks the symbolic five-cut formula. Successful execution prints `VERIFY_OK`. The program checks finite examples only. The all-parameter proof is written in `RESULT.md`, where the only external topological input is the already-published shellability theorem.

The word-generating-function derivation is algebraic and exact. Unreproduced checks include independently reconstructing a shelling from the cited paper, exhaustive screening of all future publications, and an independent audit. No claim of either is made.
