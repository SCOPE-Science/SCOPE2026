---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

At rank n-1 the upper partition has one doubleton. The extra lower point either forms a singleton lower-only block, giving a transformation (idempotence fixes its image), or belongs to a transversal doubleton. In the latter case idempotence requires the two doubletons to match to avoid rank loss, and then the transversal permutation must be the identity. These yield exactly the three listed idempotents per pair. In a rank-preserving singular product each factor has rank n-1. Upper kernel is inherited from the first factor and lower equivalence from the last: joining two transversal blocks would reduce rank, and lower-only blocks of the last factor are untouched. Consequently every e_ij is forced. If neither transformation on a pair is present, a word with that first kernel must start with e_ij, which can only multiply rank-preservingly on the right by another generator with that kernel, namely itself. Such words cannot give either transformation on the pair. For the upper bound, Howie's strongly connected tournament theorem supplies all singular transformations. Given any singular full-domain diagram, map each upper block to one chosen lower representative of its transversal block; multiplying this singular transformation by the projection for the diagram's lower partition recovers the diagram, including lower-only blocks. This projection is a join-product of the e_ij or the identity, which does not have to be generated. For n=2 the sole upper block is transversal and the three nonempty choices of lower part give a right-zero semigroup as asserted.

## originality

PASS

The examined full-domain results give idempotent generation and factorization but not the exact optimum. Those inputs together with classical transformation-semigroup generation supply the proposed upper bound; the separate full-domain rank-preservation obstruction forcing two distinct generators per pair is needed for the matching lower bound. No covering exact minimum was found in the compared indexed or primary material.

## value

PASS

This determines the exact idempotent rank of the maximal proper ideal, a concrete part of the historical ideal-rank question. It explains why the available idempotent generating family can be reduced but also why no further reduction is possible, and gives explicit optimal sets for every n>=3. The pairwise obstruction is structural rather than a small-case census or a change of notation for the transformation result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
