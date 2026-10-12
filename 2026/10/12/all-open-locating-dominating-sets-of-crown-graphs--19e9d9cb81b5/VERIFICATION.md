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

The theorem is proved symbolically in `RESULT.md`. The executable `verify_old_crown.py` is an independent finite stress test of the definition.

It constructs the crown graph directly and, for every subset of vertices for \(3\le n\le8\), checks both:

1. the OLD condition from open-neighborhood signatures; and
2. the claimed criterion \(|S\cap A|\ge n-1\) and \(|S\cap B|\ge n-1\).

It also checks that the only nonzero size counts are \(n^2\) at size \(2n-2\), \(2n\) at size \(2n-1\), and \(1\) at size \(2n\).

Packaged replay output:

`VERIFY_OK n_range=3..8 subsets=87360 old_sets=271 minimum_sets=199 max_order=16`

The exhaustive range is finite and does not certify the theorem for larger \(n\); the general proof is the evidence for the infinite statement. No external solver or unbounded computation is required.
