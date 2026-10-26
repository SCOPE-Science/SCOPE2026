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

# Verification

Run:

`python3 verify.py`

The checker reconstructs the 37-element algebra, reconstructs every endomorphism from each possible generator image, verifies preservation of 0, 1, meet, join, box, and diamond, compares each map image with the generated subalgebra of its generator image, checks idempotence and squaring behavior, and deduplicates generated subalgebra/retract images.

Expected terminal output:

```text
endomorphism_rank_distribution {2: 2, 4: 4, 5: 10, 6: 2, 8: 4, 10: 2, 12: 2, 13: 1, 16: 2, 17: 2, 22: 1, 23: 2, 29: 2, 37: 1}
idempotent_rank_distribution {2: 2, 4: 4, 5: 6, 6: 2, 8: 2, 10: 2, 12: 2, 13: 1, 16: 2, 17: 2, 22: 1, 23: 2, 29: 2, 37: 1}
one_generated_subalgebras 33
retract_subalgebras 27
nonretract_size_distribution {5: 4, 8: 2}
VERIFY_OK 123662 exact assertions; 37 endomorphisms reconstructed and checked operation-by-operation
```

A separately reconstructed truth-vector/term-closure calculation, based on the primary PDF diagram, verified 104118 operation-preservation assertions and independently reproduced all rank, idempotence, generated-image and retract-image distributions. The original uploaded script was not executed for this reconstruction. The checks are exhaustive for the stated finite object by the universal property; they are not independent audit or external verification.
