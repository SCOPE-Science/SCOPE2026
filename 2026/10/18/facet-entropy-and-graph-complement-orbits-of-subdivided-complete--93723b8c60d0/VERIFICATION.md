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

On a finite unit-edge graph, the active incidence vectors at a polar vertex span the zero-sum hyperplane iff its tight-edge subgraph is connected and spanning. For a connected bipartite graph, a tight spanning tree makes every height integral with fixed bipartition parity; all other edges then have odd differences <=1, hence are tight. For the incidence subdivision S(K_n), every original pair shares a subdividing vertex, so original heights differ by 0 or 2 and global range <=2; a constant level yields 2^M midpoint choices, whereas two height classes of sizes k,n-k force cross-midpoints and free within-class choices, proving the exhaustive binomial formula. For n>=4 degrees distinguish originals and subdivisions, hence graph automorphisms are S_n; graph complement under global sign and pair-class interchange give the Burnside orbit formula, including parity at k=n/2. The k=1,n-1 term contributes n2^(2-n), and remaining terms admit the claimed O(n^2 2^(-2n)) tail. Independently enumerated all tight assignments n=2,3,4,5 (4,20,152,1984). These exact finite checks corroborate, but the spanning/height-class proof establishes all n.

## originality

PASS

The established all-edge-tight theorem and facet-subgraph framework are acknowledged. The evaluated full-subdivision count, asymptotic concentration, and classification by graph-isomorphism/complement types do not follow as an already stated expression from inspected primary mathematical passages. Equivalent unpublished graph enumeration is an explicit priority risk.

## value

PASS

A canonical infinite family of graph-metric Lipschitz-free balls receives a complete facet enumeration plus a nontrivial bridge from facet symmetries to unlabeled graphs/complement classes. The exponential concentration and parity-sensitive equal-class orbit term are structural information needed to study symmetric edge polytopes and are not a single toy numeric example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
