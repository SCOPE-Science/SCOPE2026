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

# Reproducibility and limits

Run `python3 verify.py` with Python 3.10 or newer. No network, third-party package, precomputed table, random seed or input file is required. All counts are integers. The executable builds every unlabeled tree class by leaf augmentation and canonical center-root encodings, computes the histogram of induced interaction edges for every vertex subset, and asserts the complete design classification.

The observed final markers from an actual execution of the supplied source were:

```text
TREE_SHAPES [(1, 1), (2, 1), (3, 1), (4, 2), (5, 3), (6, 6), (7, 11), (8, 23), (9, 47), (10, 106)]
OPTIMAL_ONE_DEPTH_SCHEMES {4: (3,), 5: (3, 4), 6: (4,), 7: (4, 5), 8: (5,)}
NINE_SINGLE_K_PAIR_COLLISIONS {2: 1081, 3: 117, 4: 10, 5: 1, 6: 1, 7: 7, 8: 96}
OPTIMAL_TWO_DEPTH_SCHEMES_9 ((4, 6), (5, 6), (5, 7), (6, 7), (6, 8))
VERIFY_OK
```

The executable also prints both edge sets for the ten-vertex full-data ambiguity. That ambiguity is already known in the cited graph-polynomial literature and is not presented as novel. The cardinality-specific optimal experiment design is the accepted result.

The verification covers exactly trees through ten vertices; the code does not establish any assertion for larger tree sizes. Full probability laws are idealized exact inputs and are not inferred here from a finite number of field observations. Independent audit has not been performed.
