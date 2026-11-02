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

Verification uses `verify.py`, an independent finite-state search under the original two-for-one graph pebbling move rule, rather than the hub-budget reasoning of the proof.

Actual successful replay of `python3 verify.py`:

```text
CRITICAL_CONFIGURATIONS_OK 1 1 4
FULL_THRESHOLD_EXHAUSTIVE_OK 1 15
CACHED_REACHABILITY_STATES 1 64
CRITICAL_CONFIGURATIONS_OK 2 4 4
FULL_THRESHOLD_EXHAUSTIVE_OK 2 495
CACHED_REACHABILITY_STATES 2 2410
CRITICAL_CONFIGURATIONS_OK 3 6 6
FULL_THRESHOLD_EXHAUSTIVE_OK 3 18564
CACHED_REACHABILITY_STATES 3 91786
CRITICAL_CONFIGURATIONS_OK 4 8 8
CACHED_REACHABILITY_STATES 4 2190802
LOWER_BOUND_FAMILY_OK 2 2
LOWER_BOUND_FAMILY_OK 3 3
LOWER_BOUND_FAMILY_OK 4 4
VERIFY_OK
```

The critical layer enumeration includes every nonnegative integer configuration of the specified total on the labelled graph, with no sampling. The full threshold layer is exhaustively verified only for one, two and three triangles, not four or more. The arbitrary-size theorem relies on the symbolic harvesting, flux and last-hub-move arguments in the result, and is not inferred from this finite test. Independent mathematical assessment has not been performed.
