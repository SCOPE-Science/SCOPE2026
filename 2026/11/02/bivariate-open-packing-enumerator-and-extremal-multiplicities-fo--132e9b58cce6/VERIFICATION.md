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

The mathematical proof uses a complete local word bijection, a four-state weighted transfer, and an exhaustive *symbolic* classification of the occupancy patterns attaining the largest possible cardinality. This is an infinite proof for integer parameters \(m\geq3\), \(n\geq1\), independent of finite experiments.

Run the included `verify_open_packing.py` with Python 3.9 or later (`python3 verify_open_packing.py`). The program needs no third-party packages and uses no network resources. It constructs graph adjacency independently, enumerates all subsets on 16 small graphs, and compares both vertex-count and induced-edge-count coefficients with the transfer polynomial. It then tests the formal-power-series recurrence and maximum coefficients for six clique orders and 27 path lengths, or 162 cases.

Observed output:

```
VERIFY_OK: 16 independent all-subset graph cases; 162 exact recurrence/maximum cases
```

The tested finite ranges are not an exhaustive check of the infinite family. Source comparisons do not certify worldwide publication priority. Independent audit has not been performed.
