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

# Reproducibility and verification

Run `python3 verify_singleton_profiles.py` from the directory containing this document. No external packages or datasets are needed.

The included exact-arithmetic checker completed with:

`VERIFY_OK finite_cases=2233 partition_comparisons=191588 difference_identities=129648 direct_draw_checks=568 transition_examples=3 macroscopic_instances=4`

It enumerates the complete set of nondecreasing positive integer abundance profiles for every \(2\le N\le28\), \(2\le S\le\min\{7,N\}\), and \(2\le k\le N\). It compares each actual maximum with the proposed one-exception balanced-tail family, and checks marginal identities over \(N\le74\). Separate enumeration of individual-size-\(k\) samples in small cases checks the expectation independently. It also checks the three nine-individual transition profiles and four larger finite benchmark instances.

The unbounded-integer and fixed-richness asymptotic claims are justified by the pair-transfer and uniform-limit proofs in `RESULT.md`, not by enumeration. The large-number instances do not constitute a proof of eventual uniqueness. In particular, the checker makes no claim at reciprocal sampling-fraction thresholds and does not attempt to reconstruct all possible finite ties.
