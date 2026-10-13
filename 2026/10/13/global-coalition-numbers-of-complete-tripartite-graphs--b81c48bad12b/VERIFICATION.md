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

The mathematical proof in `RESULT.md` is the primary verification. It proves the global-domination support lemma, constructs partitions attaining each claimed value, and proves the three matching upper bounds by defect counting.

The packaged `verify.py` is an independent finite corroboration at the level of definitions. For every sorted positive triple \(a\ge b\ge c\) with total order from \(3\) through \(10\), it enumerates all set partitions, recognizes global-coalition partitions using the three-part support criterion derived directly from global domination, and computes the exact maximum number of blocks. It then compares that maximum with the claimed formula.

Expected output:

`ALL CHECKS PASSED; profiles=31; orders=3..10`

This computation does not certify orders above \(10\) and is not treated as a substitute for the analytic proof. No independent audit has been performed.
