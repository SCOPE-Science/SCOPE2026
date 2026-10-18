---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS. For all odd p=2m+1>=5, the even induced facets reduce to T_a={a,a+1,a+m+1} mod p; there are p vertices, 2p edges, p triangles and one boundary p-cycle, with every vertex link a path, yielding a Mobius band. For a retraction onto even vertices, A_{2k} fixes the even edge and constrains the odd image to states x_k in {k,k+1,k+m+1}; A_{2k+1} permits only (0,0),(1,0),(1,1),(1,2),(2,0),(2,2). In a cyclic sequence any 0 forces all 0; absent 0 any 2 forces all 2; otherwise all 1. The three maps v↦v-1,v+1,v+p on odd vertices preserve every A_i,B_i and fix even vertices. Odd parity follows by translation. Hence exactly three for each band and H_1 split injectivity. Independently constructed parity complexes and exhaustively counted 3 retractions for each p=5,7,9,11; family proof is symbolic, not inferred from sample p.

## originality

PASS

Best-of-knowledge PASS after exact-object and logical-implication comparison. The general fact that Klein bottle decomposes into two Mobius bands lacks simplicial inducedness and exact retraction count; Datta–Upadhyay supplies facets but no three-retraction theorem. The published same-family four-edge systole theorem computes minimum homology carriers, not target subcomplex retractions. An indexed-search miss alone is not treated as novelty proof.

## value

PASS

PASS. The family-wide classification is a rigid simplicial mapping theorem on canonical weakly regular Klein-bottle triangulations. The fact that each parity half is an induced Mobius band is structural, but the exact 3-map count and homological split for every m>=2 are not consequences merely of Klein-bottle decomposition. This is a natural exact infinite-family structural lemma rather than an arbitrary small-instance census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
