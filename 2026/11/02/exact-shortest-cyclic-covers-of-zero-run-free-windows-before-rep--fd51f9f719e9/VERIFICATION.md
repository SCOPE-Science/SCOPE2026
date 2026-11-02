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

The standalone `verify.py` is executed with `python3 verify.py` and uses Python's standard library only. It independently generates all allowed windows; constructs a valid cyclic Euler-tour cover after shortest bridge insertion; compares its entire circular factor set to the required factor set; calculates source/target graph imbalances; tests graph-theoretic shortest distances by BFS; and calculates exact minimum-cost bijections with a subset-DP assignment algorithm when there are at most sixteen deficits.

Observed result:

```text
VERIFY_OK q=2..4 h=2..5 cases=37 admissible_edges=18274 checked_source_target_pairs=995 exact_assignment_instances=34
```

These checks cover finite parameters only. They are not a proof of the theorem at unbounded alphabet sizes or run lengths. The all-parameter argument is contained in `RESULT.md`; no external formal or independent validation has been performed.
