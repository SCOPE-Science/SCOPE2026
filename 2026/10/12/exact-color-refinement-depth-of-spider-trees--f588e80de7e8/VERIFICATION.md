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
The proof is uniform for all spider trees with at least three legs. The attached `verify.py` independently constructs spiders and implements ordinary color refinement.

It checks every nondecreasing leg-length tuple with \(3\) through \(6\) legs and lengths from \(1\) through \(10\), totaling \(7942\) graphs. For every nonstable refinement round in those graphs, it compares the actual color partition with the typed clipped-distance partition from the proof, totaling \(57570\) round-level comparisons. It also exhaustively checks the fixed-order extremal formula for \(d=3,4,5\) over \(54\) order/leg-count pairs.

The checker returns:

`VERIFY_OK depth_checks=7942 descriptor_round_checks=57570 extremal_checks=54`

These computations are corroborative only. They do not replace the all-parameter proof in `RESULT.md`.
