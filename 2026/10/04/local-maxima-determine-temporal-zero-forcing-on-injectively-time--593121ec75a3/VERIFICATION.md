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

The all-order theorem is proved in `RESULT.md`; finite enumeration is only an independent stress test.

`verify_temporal_paths.py` directly implements the synchronous process for paths in which each edge appears once at a distinct ranked time. For every edge-time permutation with one through eight edges, it searches seed sets by increasing cardinality, compares the optimum with the peak-chain formula, and separately computes a minimum cut set that hits every peak neighborhood. It also verifies the claimed worst-case value and an explicit extremal timing at each tested order.

Recorded execution:

```text
ALL CHECKS PASSED
permutations=46233
seed_sets_tested=1992563
maxima=n=2:TZ=1:witness=1;n=3:TZ=1:witness=1,2;n=4:TZ=2:witness=1,3,2;n=5:TZ=2:witness=1,3,2,4;n=6:TZ=2:witness=1,3,2,4,5;n=7:TZ=3:witness=1,3,2,4,6,5;n=8:TZ=3:witness=1,3,2,4,6,5,7;n=9:TZ=3:witness=1,3,2,4,6,5,7,8
```

The enumeration covers all \(46,233\) permutations for \(2\le n\le9\). This finite range does not certify the theorem for larger \(n\); the proof's cut-and-valley equivalence and interval-hitting argument provide the unrestricted conclusion.
