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

# Reproducibility and scope

Run `python verify_rank_two.py` with Python 3.9+; no third-party packages are required. The exact checker enumerates every ordered triple from a 64-element group, constructs all nontrivial forbidden supports, and applies complete increasing-label depth-first search. Target size eight yields 12,288 rooted sets; target nine yields no rooted sets. It then enumerates every two-by-two matrix over the ring modulo eight with odd determinant and computes all normalized affine classes.

Expected final line begins `VERIFY_OK` and contains `forbidden_edges=31152 rooted_eight=12288 size_nine=0 nodes8=57143 nodes9=16096 affine_orbits=[3072, 3072, 3072, 3072] total_extremizers=98304`. The displayed outputs were obtained by executing the packaged checker, not by relying on a stale transcript. The exhaustive finite proof follows from the inverse-of-three identity and the explicitly implemented pruning invariant; no infinite cases are asserted.

The original scientific literature supplies the motivation and comparison, not the computational counts. This record has self-review only. Independent audit has not been performed.
