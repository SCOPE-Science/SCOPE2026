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

The symbolic proof gives a deletion order valid for every \(n\ge2\). The executable check is deliberately finite and is used only to replay the stated combinatorics on representative dimensions.

`verify.py` reconstructs \(X_n\) from the level definition, constructs all ordered pairs of distinct points, and uses only the product order. For each \(2\le n\le10\), it verifies:

- the configuration space has \((2n+2)(2n+1)\) points;
- exactly \(4n(n+1)\) off-level points occur;
- at every deletion, the proposed witness is present and is the greatest element of the current strict lower set;
- the final set is exactly the \(2n+2\)-point anti-diagonal set \(A_n\);
- the order on \(A_n\) is exactly the level order of \(X_n\);
- \(A_n\) has no beat points.

Replay output:

`VERIFY_OK n=2:points=30,deletions=24,core=6 n=3:points=56,deletions=48,core=8 n=4:points=90,deletions=80,core=10 n=5:points=132,deletions=120,core=12 n=6:points=182,deletions=168,core=14 n=7:points=240,deletions=224,core=16 n=8:points=306,deletions=288,core=18 n=9:points=380,deletions=360,core=20 n=10:points=462,deletions=440,core=22`

No computation is used to infer the universal quantifier. The checker does not address unordered quotients or configurations of three or more points.
