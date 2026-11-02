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

Read complete RESULT.md blob 70b9bd7ba9fd951286c7c6f8489f4d2d91da43d4 and verifier source. Oriented tree incidence columns form independent generators of an intrinsic parallelotope. Cauchy–Binet counts n nonzero full minors, giving volume sqrt n; deleting an edge yields forest components of a,n−a, with exactly a(n−a) nonzero maximal minors and two facets of area sqrt(a(n−a)). This supplies exact surface formula. Every split has sqrt(k(n−k))≥sqrt(n−1), equality only pendant; star is unique minimum. Nonstar must contain ≥1 interior edge with k in [2,n−2], causing gap ≥2(sqrt(2(n−2))−sqrt(n−1)), uniquely attained by subdivided star. Strict transfer of smallest branch from degree≥3 vertex to a leaf of another branch increases every changed split product since n>2s+a, reduces leaf count, and eventually reaches a path; equality is strict except tree already path. Among three-leaf tripods, transferring edges from short to long arms strictly increases sum until arms (1,1,n−3), giving unique near-maximum B−Δ. Integral of sqrt(x(1−x)) yields ratio ~πsqrt(n)/8. Independent Prüfer tree enumeration through n=6 confirmed both nearest gap extrema; no inference of all n from enumeration.

## originality

PASS

Best-of-knowledge PASS: incidence Gram-minor surface formula itself is standard and credited, while published width-variance result concerns a distinct directional statistic even though for same trees it reverses the star/path order. General graph-zonotope deformation literature and phylogenetic leaf-split indices do not state these rigid vertex-split second extrema in the material inspected. A general split-functional theorem might nevertheless imply the arm transfer and remains a residual risk.

## value

PASS

Graphical zonotopes of trees are combinatorially cubes with exactly the same intrinsic volume yet markedly different Euclidean boundary measure. The exact first and second metric extremal shells identify nearest competitors and a surprising equality of two gaps. This supplies natural geometric stability data for an important family rather than merely reapplying the known forest Gram identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
