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

The checker constructs \(H_n\) for \(3\le n\le10\), computes all-pairs distances, and tests visibility by blocking all selected vertices except the pair endpoints. It exhausts every set of sizes \(2n-1\) and \(2n-2\).

Recorded output:

```text
VERIFY_OK
n=3: mu=4, maximum_sets=1, omitted=a1,b3
n=4: mu=6, maximum_sets=1, omitted=a1,b4
n=5: mu=8, maximum_sets=1, omitted=a1,b5
n=6: mu=10, maximum_sets=1, omitted=a1,b6
n=7: mu=12, maximum_sets=1, omitted=a1,b7
n=8: mu=14, maximum_sets=1, omitted=a1,b8
n=9: mu=16, maximum_sets=1, omitted=a1,b9
n=10: mu=18, maximum_sets=1, omitted=a1,b10
candidate_sets_checked = 812
all maximum sets were exactly V(H_n) minus {a1,b_n}
```

The finite computation is exhaustive for the tested near-maximum levels and corroborative only for the arbitrary-order theorem.
