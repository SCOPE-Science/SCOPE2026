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

# Reproduction and limitations

Run `python3 verify.py` using Python 3.9 or later. The code uses only the standard library and no downloaded data. It constructs the graph directly from its vertex/edge sets, detects conflicts by scanning all possible third edges, and independently constructs the finite-state adjacency rules. It checks all exact integer entries of the critical \(17\times17\) matrix identity and traces, not a floating-point approximation.

Full exhaustive independent graph enumeration for cyclic prism orders seven through eleven verifies the complete extremal counts. Orders seven through fourteen have independently checked local conflict pairs; a separate transfer recurrence checks all orders seven through eighty-four. These bounded tests are corroboration; the all-order proof uses the exact finite matrix identity and unique six-cycle, which the executable also checks.

Expected output (the actual execution is captured separately as `verification_output.txt`):

```
DIRECT 7 maximum 6 optimal_sets 14 feasible_sets 1079
DIRECT 8 maximum 7 optimal_sets 16 feasible_sets 2979
DIRECT 9 maximum 8 optimal_sets 36 feasible_sets 8410
DIRECT 10 maximum 9 optimal_sets 20 feasible_sets 22583
DIRECT 11 maximum 10 optimal_sets 44 feasible_sets 61579
CERTIFICATE_OK states=17 transitions=37 zero=24 unit=13 B0^8=B0^2 unique_zero_cycle=6
TRACES a[1..8]=1,1,4,2,4,6,2,2; transfer_orders=7..84; local_rules=7..14
```

No independent audit has occurred. Bibliographic coverage is limited to the referenced inspected primary sources and actual search results; no absolute uniqueness claim is made.
