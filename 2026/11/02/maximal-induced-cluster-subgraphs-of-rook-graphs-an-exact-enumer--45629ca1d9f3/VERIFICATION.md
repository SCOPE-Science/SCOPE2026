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

# Reproducibility

Run `python3 verify_cluster_rook.py` with the Python 3 standard library. It enumerates all labeled vertex subsets of twelve rook graphs, directly tests the induced cluster property and inclusion-maximality against the original rook adjacency, and compares the coefficient dictionaries to a separately implemented labeled-star recurrence with restricted partitions. It then tests exact predicted supports on 221 additional dimension pairs. Recorded output:

```text
VERIFY_OK direct_graphs=12 direct_subsets=120694 support_pairs=221
```

The test covers all subsets of the listed twelve graphs, but the program does not exhaust infinitely many dimensions. Infinite correctness uses the explicit proof in `RESULT.md`. Source comparisons concern inspected cited material and are not an independent publication-priority certificate. Independent mathematical audit has not been performed.
