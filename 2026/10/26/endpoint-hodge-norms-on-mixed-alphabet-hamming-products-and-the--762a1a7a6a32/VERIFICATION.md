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

The included `check_exact.py` uses only the Python 3 standard library. Executing `python3 check_exact.py` builds every indicated Cartesian-product graph, constructs the full integer graph Laplacian, exactly inverts its grounded principal minor using rational Gauss–Jordan elimination, reconstructs each projector column, and compares its induced absolute column sum and diagonal entry against the closed formulas.

The mixed parameter tuples tested are `(2,2,3)`, `(2,3,3)`, `(2,3,4)`, `(3,3,4)`, `(2,2,2,3)`, `(2,2,3,3)`, and `(2,2,2,2,3)`. They comprise 12, 18, 24, 36, 24, 36, and 48 vertices respectively, with 24, 45, 72, 126, 60, 108, and 144 oriented edges. **All 579 exact rational edge-column checks passed.** Every tested parameter tuple also passed the smallest-factor maximum and strict unequal-factor direction comparisons for both projections.

Exact sampled values include cut/cycle operator norms \(14/5\) and \(28/9\) for the \((2,3,4)\) product, and \(20/7\) and \(1037/315\) for the \((3,3,4)\) product. The analytical proof uses a positive heat-kernel resolvent and exact rational inequalities for every allowed parameter, independently of these finite enumerations.

No external or independent mathematical audit has been conducted. The tests do not establish any optimality among arbitrary nonorthogonal projections and cannot substitute for the all-parameter proof.
