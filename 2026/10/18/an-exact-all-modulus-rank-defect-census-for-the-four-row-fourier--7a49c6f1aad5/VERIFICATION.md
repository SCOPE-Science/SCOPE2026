---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For distinct roots a left-null row polynomial supported on 0,1,3,4 must be proportional to the monic quartic with these roots, so singularity means its z² coefficient e₂ vanishes and nullity is one. The six terms of e₂ decompose by the prior minimal vanishing-sum classification into opposite pairs, cube-root triples, or a primitive weight-six relation. Opposite edge products sharing a vertex force two roots to be antipodes; if all paired edges are disjoint the equations force a squared ratio of one, again yielding antipodes by distinctness. Substitution requires the remaining pair product u². A three-edge star or triangle forces a complete ternary coset; two complementary paths instead force all four distinct roots into one ternary coset, impossible. For the primitive relation S={5,25,6,12,18,24}, zero is the only residue hit by three pair sums, giving the unique opposite-edge matching. There are at most 48 label placements and exactly 24 relabelings in each projective class since all six product terms are distinct; root ratios are uniquely read from ratios of products sharing a vertex. The two displayed configurations realize the two distinct classes, with circular gaps (12,1,6,11) and (6,1,12,11), hence free translation orbits. The primitive product ratios include exact order 30. Counting unordered inverse partners after removing ±u yields (N−2)/2 choices per designated antipodal pair. Double counting within that family is exactly the fourth-root cosets, and overlap with ternary cosets is exactly a ternary coset plus the negative of one member. This gives the two subtractions and the 2N exceptional contribution. Independent anchored-set cyclotomic arithmetic verified totals at N=5,7,18,28,30,31,54,60,90, including 510,2055,4680 at 30,60,90 and exactly two normalized primitive classes there.

## originality

PASS

The Schur determinant, shape of both infinite ambiguity families, and both exceptional orbit representatives are covered by Matter et al. for the same row pattern, and the earlier exact full-spark result already says when the census is zero. The supported distinct contribution is the all-modulus arithmetic multiplicity of distinct unordered singular minors: it counts admissible partners on each cyclic grid, proves when a grid set is counted more than once, and accounts for the exceptional translation orbits. The total with the fourth-root and ternary/antipodal overlap corrections does not follow by merely substituting N into a prior formula. No earlier enumeration of this count was located in the bounded comparison.

## value

PASS

For the established four-sensor row pattern, the number of rank-deficient four-column selections is a natural measure of how frequent reconstruction ambiguities are beyond merely knowing that a bad selection exists. The closed formula captures the actual multiplicity at each modulus, including a distinct anti-overcounting correction at multiples of 4, interaction at multiples of 6, and exceptional jumps at multiples of 30. These are useful in answering an exact census question without scanning the binomial number of possible selections.

The dated certificate retains the supplied scientific assessment, sources and limitations.
