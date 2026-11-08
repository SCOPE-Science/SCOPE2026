---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For inclusion-maximal rather than maximum independent sets, a fixed eight-vertex spider S(1,2,4) has exactly eight maximal independent-set membership masks; checking all 56 triple restrictions gives VC=2, while the 8-leaf depth-three decision certificate gives Littlestone=3. The all-forest first-boundary theorem reduces to an exhaustive tree enumeration: leaf deletion gives a complete generator, and canonical center-rooted code removes isomorphisms. An independently implemented NetworkX census regenerated 1,1,1,2,3,6,11,23 nonisomorphic trees and found exactly one eight-vertex gap with degrees (3,2,2,2,2,1,1,1). The Cartesian-product lemma adds VC and Littlestone dimensions across disconnected components; induction on hypothesis partitions proves Ldim additivity for products. Thus (2s,3s) for disjoint s copies holds at every s, not only enumerated cases.

## originality

PASS

Graph classes formed by maximal independent sets are studied in enumerative combinatorics, while Littlestone questions appear in model theory and learning. Drmota et al. derive asymptotic numbers and size distributions, not membership-query adaptive depth. Michel–Scott study reconstruction of an unknown graph via a maximal-independent-set-valued oracle, not learning a fixed unknown maximal independent set from vertex bits. Guingona et al. prove equality for special linear zero-set classes, not forests. No published Resultary match provided the asserted small-order unique spider.

## value

PASS

There is a direct mathematical question whether adaptive membership trees can exploit more information than static shattering on a canonical independent-set concept class. The exact smallest connected witness and complete eight-vertex census give a meaningful threshold; disjoint-union additivity yields an unbounded quantitative family. This is stronger than a named example or arbitrary finite computer table because it proves minimality and an infinite amplification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
