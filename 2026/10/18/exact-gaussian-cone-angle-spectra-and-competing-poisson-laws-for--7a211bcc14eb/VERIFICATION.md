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

Run `python3 verify_angles.py` in a directory containing that one file. The checker requires Python 3's standard library only. It performs exhaustive permutation grouping for each \(n\) from 2 through 8 and all matching sizes, verifies exact integer/rational spectra and collision identities, and raises an error on any discrepancy. The 23 complete cases passed in the original execution. The input \(n=2,k=1\) is intentionally used as a boundary test; the theorem itself assumes \(n\ge3\).

The analytic argument, not the finite test, proves the claim for all dimensions: it relies on the exact orientation-class size, inclusion--exclusion, and a uniformly dominated generating-function limit. The counts of permutations, acyclic orientations and vertex-collision probabilities are three separate comparisons. Primary sources were inspected for stronger covering results, with the prior total-count formula explicitly excluded from novelty. No formal proof assistant or independent audit has been used.
