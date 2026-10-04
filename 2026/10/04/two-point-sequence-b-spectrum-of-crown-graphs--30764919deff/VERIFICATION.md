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

The proof is analytic and applies to every integer \(n\ge3\). It uses only the adjacency rule of the crown graph and the definition of a color-dominating vertex.

A finite stress test is supplied in `verify.py`. It reconstructs \(\operatorname{Cr}_n\) independently, enumerates every set partition of the vertex set for \(n=3,4,5\), retains exactly the proper colorings, computes every CDV from closed neighborhoods, and tests whether each class contains at least two CDVs. It also classifies each realizing color class as \(A\)-pure, \(B\)-pure, or a deleted-matching pair.

Expected replay output:

`ALL CHECKS PASSED; n_range=3..5; set_partitions=120318; proper_partitions=4520; realizing_partitions=6; details=[(3, [2, 3], {2: 1, 3: 1}), (4, [2, 4], {2: 1, 4: 1}), (5, [2, 5], {2: 1, 5: 1})]`

The enumeration is exhaustive only for the displayed finite range and is not used as a proof for arbitrary \(n\). The universal conclusion rests on the case split in `RESULT.md`.
