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

# Reproducible verification

The standalone standard-library Python 3 program `verify.py` enumerates all 75 set partitions on at most five labeled points, with every threshold \(2\le k\le |X|+1\). For every map \(f:X\to X\), it compares the structural theorem with direct preservation of both counting operations, tested on every subset. For every frame it separately computes the predicted endomorphism count, all exact image-cardinality counts, and the idempotent spectrum; independent direct enumeration checks each prediction. It also checks the inclusion/strictness condition for adjacent thresholds. The six-point \((1,2,3)\) example is independently computed by formula.

Command:

```shell
python verify.py
```

Observed output:

```text
VERIFY_OK partition_shapes 75 grade_instances 340 function_grade_comparisons 828282 endomorphism_instances 28803 idempotent_instances 3748 distinct_nonzero_rank_cases 931 filtration_jump_comparisons 265 boundary_counts_1_2_3 [12, 18, 39]
```

These finite computations verify the implementation against direct finite semantics over the stated tested range. They cannot establish any unrestricted theorem; the complete proof is provided separately. Independent mathematical and priority assessment has not been performed.
