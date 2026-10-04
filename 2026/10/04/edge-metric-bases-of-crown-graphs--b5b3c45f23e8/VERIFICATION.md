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

The proof has three independently checkable steps.

1. For every edge \(e_{ij}=a_i b_j\) with \(i\ne j\), direct graph distances yield the exact \(0/2/1\) coordinate formula at every matched index.
2. If two matched pairs are absent from a candidate generator, a third index produces two distinct edges with identical representations, proving the lower bound \(n-1\).
3. If one matched pair is absent and every other pair contributes exactly one landmark, each represented index distinguishes tail, head, and neither; equality of all coordinates therefore forces equality of the edges.

`artifacts/verify.py` independently constructs the graphs and breadth-first-search distance matrices, then exhaustively checks all subsets smaller than \(n-1\) and every subset of size \(n-1\) for \(3\le n\le8\). Replay output:

`VERIFY_OK n_range=3..8 subset_checks=34896 basis_checks=1788 distance_formula_checks=2176 max_order=16`

The exhaustive range is finite corroboration and is not used as evidence for the universal quantifier beyond checking proof boundary cases and implementation consistency.
