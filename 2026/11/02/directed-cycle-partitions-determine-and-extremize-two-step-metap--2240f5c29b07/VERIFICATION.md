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

The exact mathematical proof is contained in `RESULT.md`. The attached `verification/check_cycle.py` is a standalone Python 3 standard-library script:

```
python3 verification/check_cycle.py
```

The checker was run against its actual source and printed `PASS: 12767 exact-rational assertions`. The checks include direct independent summation over every first-update survival and eligible colonization coin for all directed-cycle partitions of sizes two through seven, for three rational parameter pairs; all-partition and fixed-reciprocity optimization on sizes two through eighteen; recovery of the directed cycle lengths by factoring each generating polynomial for sizes two through twenty-two; and exact comparison of the three eight-patch examples.

A finite exhaustive check for bounded patch counts does not prove the theorem at arbitrary size. The general result follows from the conditional probability reduction and trace-product identity, strict cycle-splitting/convexity inequalities, and polynomial identity/lowest-exponent reconstruction, all explicitly justified in the proof. Other update orders, non-permutation networks, longer time horizons, and empirical viability are unverified and are not claimed.

The source paper's model description and the closest available full-text literature were compared to the final mathematical statement. A related article's full text remained inaccessible; priority is provisional. Independent audit has not been performed.
