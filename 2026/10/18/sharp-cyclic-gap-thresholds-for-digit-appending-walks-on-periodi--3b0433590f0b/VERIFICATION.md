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

# Reproducibility of the cyclic-gap theorem

The proof is given in `RESULT.md`. The dependency-free `verify.py` implements an independent finite oracle: it checks every disjoint placement of the critical correction values \(0,-1\) through period \(10\), compares directed cycle existence against the proposed cyclic-gap threshold for every cap up to \(h+1\), and tests 13,000 seeded periodic integer correction examples (bases \(2,3,7,10\)). These checks also compare actual integer digit appending with the correction-only condition at indices above the explicit rigidity threshold.

Run `python3 verify.py` from the extracted package directory. The observed output was:

```
VERIFY_OK subset_graph_comparisons=930021 sampled_recurrence_and_graph_checks=825308
```

The enumeration is exhaustive only for the explicitly stated finite graph patterns; random recurrence tests are finite consistency checks. The all-period result, unbounded-digit assertion, and global walk length bound follow from the analytic argument, not from this finite test. No independent external scientific audit has occurred.
