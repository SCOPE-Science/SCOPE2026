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

Graph Lipschitz dual polytope vertices correspond exactly to connected tight-edge graphs, as the active incidence matrix has rank 14-c where c is the number of tight graph components. On a connected bipartite tight-edge subgraph, all vertex heights have a fixed parity on each color class and every original incidence edge must have odd difference bounded by one, hence every edge is tight. For rooted integer heights, all seven Fano points have pairwise difference in {0,+/-2}, so either all 0 or root 0 and selected other six at +2 (or -2). For k of the six selected, there are m=7-k(7-k)/2 monochromatic Fano lines independently allowing two line heights; each mixed line is forced. Positive-envelope total sum_{k=0}^6 C(6,k)2^m=394; two envelopes overlap in 2^7=128 all-point-zero cases, giving 660. Direct level-count gives 2,252,406. The supplied verifier independently enumerates all 660 via a spanning-tree increment search and classifies under all 336 incidence automorphisms and sign. A separate exact reconstruction obtained the same 660 and 10 orbit sizes 168,112,112,84,56,42,28,28,28,2. Each facet has 21 tight signed edge molecules. Finite exhaustion proves the finite orbit census; nothing claimed for other geometries or the full affine polytope automorphism group.

## originality

PASS

The graph-metric duality criterion and Fano incidence construction are standard. The nontrivial 660 count, exact height strata and ten graph-automorphism/sign orbits are a specific full evaluation, not a restatement of general symmetric-edge-polytope facet criteria. Published Heawood cut-polytope numbers concern a different convex body. This is a bounded best-of-knowledge scientific judgment: an unsuccessful search cannot prove absolute priority.

## value

PASS

The Fano-plane incidence graph is a natural highly symmetric, nonplanar graph and its Lipschitz-free ball is a canonical 13-dimensional symmetric edge polytope. Its exact facet count and orbit stratification supply a nontrivial intrinsic invariant not given by the known general facet criterion; this is a motivated complete finite classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
