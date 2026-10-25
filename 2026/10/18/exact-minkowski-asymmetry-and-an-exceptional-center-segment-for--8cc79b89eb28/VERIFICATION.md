---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For P_n=conv(0 and 0-1 consecutive interval indicators), n>=2, positive variation V+(w)=sum_i max(0,w_i-w_{i-1}) characterizes membership among nonnegative w exactly, by layer-cake decomposition into superlevel interval runs (zero vertex handles coefficient slack). Minkowski containment translates to ((s+1)c-v)/s in P_n for each vertex. Coordinate 0<=w_i<=1 and alternating triple w_i-w_j+w_k<=1 with minimum -1 enforce s>=3/2 for n3 and s>=2 for n>=4 using overlapping triple inequalities; square n2 has s1. c=1/3 1 attains s2 because complement of a single interval has <=2 runs; n3 c=(2/5,3/5,2/5) checked by exact 3D facet inequalities. Equality cases at s2 force nonnegative offsets d_i=c_i-1/3 with d_i-d_j+d_k<=0 and all overlapping quadruple extremes d_i=d_l=0; n4 leaves d2=d3 in [0,1/3], and n>=5 forces all zero. Both n4 segment endpoints meet reflection criterion: second verified exhaustively on 11 vertices. Independently checked exact reflected-vertex membership for proposed centers n2..16 via Fraction; universality is supplied by symbolic proof. Check proof uses s>=1 convention and the zero-inclusive body throughout.

## originality

PASS

Primary Bruckamp–Chimani–Juhnke 2023/2025 connected-block polytope paper identifies the same zero-inclusive path family, facets and type-A connection, but does not address Minkowski reflection factors and full minimizing-center locus. Published Resultary full same-family result c3b8e999d5d4 computes EUCLIDEAN inradius and its (n−3)-dimensional incenter locus; this differs from affine Minkowski center, which is unique from n5. Full Resultary order-polytope Minkowski classification 2f48aab3ef81 studies finite poset order polytopes with height-determined asymmetry and different inequalities; cannot transfer without an unproved affine equivalence. No inspected earlier statement yields the exact exceptional n4 segment; hidden type-A root-polytope duality is a residual priority risk.

## value

PASS

Complete classification of a fundamental affine invariant and ALL equality-case centers for a canonical interval/root-related lattice-polytope family, with a distinct dimension-four segment exceptional locus. It separates metric incenter geometry from affine reflection geometry and is not merely calculating an arbitrary low-dimensional example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
