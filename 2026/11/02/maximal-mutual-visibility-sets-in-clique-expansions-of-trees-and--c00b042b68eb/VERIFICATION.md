---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Between distinct fibers a geodesic projects to the unique base-tree path, and any representatives in the intermediate fibers work. Thus on the Steiner hull of occupied fibers, each internal fiber must have a hole, as witnessed by occupied leaves on opposite sides. Conversely those holes suffice. Maximality forces full leaves and exactly one hole per internal fiber, including the case of a width-one empty internal fiber. A neighbor outside the hull at an internal vertex allows a harmless one-vertex extension. If instead every internal vertex has all its tree neighbors in the hull, each external vertex attaches at a leaf, so adding it makes a full leaf fiber block visibility to another leaf. Filling any internal hole also blocks visibility. The full leaf fibers recover the hull and each omission is recoverable, proving the bijection and labeled multiplicities. Empty and single-fiber sets are not maximal in a nontrivial tree; a single base vertex yields its whole clique. On P_n an interval of j+2 fibers has n−j−1 positions, m^j omissions and order 2m+j(m−1). Summation gives the stated totals, and equal-length intervals at consecutive integer starts with length 3/2, then rescaled, represent exactly those graphs. Independently compared distance-preserving deletion tests against the full predicted cardinality counts on six expansions, including branching and width-one internal fibers.

## originality

PASS

The weighted hull classification and exact labeled maximal-set enumerator are distinct from the inspected total-visibility product results, ordinary-tree leaf and maximum-set results, lower visibility numbers and all-visible-set polynomials. Credit both the Steiner criterion and the known width-one maximum layer as prior; the pass is for the variable-width maximal configuration theorem and its refined clique-path consequence.

## value

PASS

The hull bijection isolates exactly how maximality interacts with full fibers and exterior branches, rather than only reproducing a visibility extremum. It gives full-size multiplicities even with unequal widths, and the path specialization gives unbounded gaps between consecutive attainable sizes in a connected and familiar graph class (unit interval graphs, n≥3).

The dated certificate retains the supplied scientific assessment, sources and limitations.
