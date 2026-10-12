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
# Verification procedure

Use Python 3 with standard library only: run `python3 verify.py` in the directory containing the supplied source. The script makes its own 15-state transducers, filters reachable states, performs exact Moore minimization to a stable quotient, and explores every reachable homogeneous path profile until a conflict or complete exhaustion. It repeats this for every mask from 0 to 255 inclusive. For each mask it separately compares automaton output with literal factor counting for integers from 0 to 2047 inclusive.

Expected output:

```
VERIFY_OK total=256 transparent=249 opacity_one=4 opacity_half=2 opacity_quarter=1 max_minimal_states=10 max_bfs_configurations=572
exception_witnesses={0: '01', 68: '10', 85: '101', 136: '10', 170: '110', 204: '10', 255: '1001'}
```

The code uses complete finite BFS with deduplication by an exact sufficient state (current automaton state and the input-label sets seen at each target), rather than bounding exploration by a chosen depth. The supplied assertions certify a 256-case finite classification; they do not imply similar classifications for longer patterns. No proof assistant or independent external audit was used. All scientific premises and limits are in RESULT.md.
