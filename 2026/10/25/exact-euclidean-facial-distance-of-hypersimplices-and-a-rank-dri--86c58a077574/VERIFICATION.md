---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

PASS: Facial distance is the minimum Euclidean separation from every nonempty proper face F to the convex hull of complementary vertices. The coordinates fixed to 0/1 give face parameters (a,b,r,j), and averaging closest pairs by within-block permutations is valid for convex sets under a common compact symmetry group. Every outside vertex incurs at least one unit of violation mass, u+v>=1; the block norm bound is u²/a+v²/b+(u-v)²/r. The equality witness is an actual convex combination of outside vertices whose one wrong fixed coordinate is uniformly distributed. This gives squared distance n/[n(a+b)-(a-b)²] for every positive-dimensional face; vertex distance n/[k(n-k)] is strictly larger for k,n-k>=2. Strict improvement as b increases and strict concavity in a imply H and exactly the claimed minimizing orbit pairs; explicit integer maximization independently checked all n=4..30 and 2<=k<=n-2 (378 rank cases). Source verify.py exact rational orbit witnesses and numerical QP are supporting finite checks, not proof for arbitrary n. All boundary n=4,k=2 and transition n=4t and 4t+1 agree.

## originality

PASS

On the inspected primary sources and independent comparison, the specified new exact evaluation/classification is not supplied by a stronger known theorem; scope and residual priority limitations are stated explicitly. Pyramidal width, facial distance and uniform-matroid terminology were compared at the level of definitions. The inspected results and abstracts do not supply this exact two-parameter metric evaluation; comparable face combinatorics alone does not determine a Euclidean distance. Neither known simplex endpoints nor the universal bound entails the phase transition in the proved domain. The separate convex-symmetry attainment and integer optimization are necessary additional facts, subject to inaccessible full-source caution.

## value

PASS

PASS: Facial distance/pyramidal width controls quantitative polytope-optimization geometry; computing its exact dependence on both rank and corank for all genuine hypersimplices and the complete minimizing-face transition is a natural structural classification. It is not a reformulation of a facet-only inradius calculation or a small finite-table gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
