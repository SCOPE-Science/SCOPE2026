---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Checked the exact curvature convention, domain and orientation against Ghomi Theorem 1.1 in the author-hosted 14-page original full text: the inequality is for p-q=λe, λ>=0, open chord in int K, 1<=m<=d-1. It indeed yields an affine hyperplane reflection. All reflection planes contain the centroid; translate to linear reflections. Since <v,S_e1 v>=1/3, the product S_v S_(S_e1 v) rotates by 2 arccos(1/3), an irrational multiple of 2π (otherwise 2/3 is rational algebraic integer). Continuous rotations in span(v,e1) are in the closure. Conjugating by S_ej and subtracting generators obtains e_j wedge e1 for j=2..d-1; v_d nonzero gives e_d wedge e1; Lie brackets generate so(d), so full O(d) invariance and a ball. Independently checked full generator rank d(d-1)/2 for d=3,4,5,7. For any <=d-1 directions choose orthogonal w; the nonround ellipsoid |x|²+η<x,w>²<=1 has all those reflection planes and thus equal chord endpoint curvatures. The finite rank checks only corroborate the analytic Lie proof.

## originality

PASS

Ghomi proves each one-direction curvature-order-to-reflection implication; it does not state a finite-dimensional sharp d-direction generating set. A published three-dimensional Resultary theorem proves a different concrete 3-direction special case and already establishes d=3 minimality, which is explicitly credited. The surviving contribution is a single explicit d-vector family and the sharp count for every d>=4, together with the universal lower bound; no claim of new 3D threshold.

## value

PASS

Finite spherical rigidity under pointwise curvature order is a natural observation problem. The construction reduces infinitely many directional comparisons to the minimum possible d tests for all dimensions and exhibits a universal ellipsoid obstruction below d; this is a motivated sharp structural theorem beyond a special symmetry example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
