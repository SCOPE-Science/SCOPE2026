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

# Reproduction and limits

Use Python 3 to execute `python verify_mapping.py` from the directory containing that file. The checker has no nonstandard dependencies. It computes rational law and comparison identities exactly, enumerates every mapping on \(n=2,\ldots,7\), checks the induced conditional cyclic-vertex and component-count distributions by full in-degree vector, and explores all integer-partition degree representatives through \(n=11\). It covers the claimed balancing-transfer tails, mass-sign crossing, exact total variation, profile envelope and the length-five likelihood-ratio obstruction. The observed output was:

```
PASS exact_assertions=91476 enumerated_mappings=873611 distinct_labeled_indegrees=2352 elementary_transfers=2438 exhaustive_mapping_n=2..7 transfer_partitions_n=2..11 LR_first_counterexample_n=5
```

The verifier does not enumerate arbitrary sizes. The analytical proof instead uses a previously established prescribed-degree cyclic-set count, an exact symmetric-polynomial perturbation, normalized Newton inequalities and total positivity of the Stirling cycle kernel. These non-computational ingredients and the support boundaries are spelled out in `RESULT.md`. No independent audit has been performed.
