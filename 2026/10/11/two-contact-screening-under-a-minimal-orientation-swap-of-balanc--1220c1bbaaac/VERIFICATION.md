---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Reconstructed the equal-norm barycentric certificate: if c=sum w_i v_i (nonnegative w sum1) has <c,v_i>≥||c||², with equality on support, then radius²=2−||c||² is globally minimal and center unique by weighted variance identity. For k≥4 the two directed arms have Gram diagonal 2, neighboring −1, shared-source +1. The explicit quadratic arm weights sum 1/2 per arm and solve the discrete second-difference equations, yielding ||c||²=3(2k−1)/[(k−1)k(k²−k+1)]. The two omitted arcs have strict dot-product clearance giving 6(k²−4k+2)/[(k−1)k(k²−k+1)] for k≥4. k=3 separately has six positive weights and R²=28/17. Independent exact rational tests covered k=3,4,5,8,30 with all vertex distances and contacts; full result follows from symbolic all-k identities, not the tests.

## originality

PASS

Numata–Takahashi–Tamaki characterize faces of directed edge polytopes, and Kálmán–Tóthmérész develops semi-balanced graph root polytopes; neither inspected source statement provides the Euclidean active-set/radius formula. The full published semi-balanced canonical-sphere theorem was separately inspected: it gives only an all-vertex sphere and a feasibility criterion, and explicitly leaves true smaller minimum sphere unspecified when infeasible, precisely this k≥4 case. The separate path one-reversal result concerns a tree and one excluded contact rather than a cycle and two. O passes best-of-knowledge with terminology risk.

## value

PASS

A single adjacent sign swap is the smallest natural nontrivial balanced perturbation of a two-block orientation, preserving face lattice but changing Euclidean sphere geometry. The exact all-dimensional minimum radius, exceptional k=3 threshold, precisely two screened vertices, positive contact weights, and strict clearances resolve the geometric active-set transition unavailable from combinatorics alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
