# Review of zero-padding rigidity for reverse multiples

## Correctness
PASS. The two-digit elimination from the paired carry identities proves that hypothetical highest adjacent zero carries imply \(n^2-1\mid c_1^2\), conflicting with \(1\le c_1\le n-1\). All quantifiers, nonzero end-digit assumptions, carry bounds, and the short case are stated explicitly. The padding classification then uses only the top-carry obstruction and the necessary final zero and positive first carry. The independent exact checker passed 3,103,793 candidate digit strings, found 150 valid examples, and passed 117,810 modular tuple checks; the infinite argument does not rely on enumeration.

## Originality
PASS with a priority caveat. Holt (2014), Corollary 2, contains the carry identity and Theorem 3 its bounds, while Holt (2016), Section 2, defines the two outer-zero padding patterns and expressly leaves other possible derived patterns open in Section 7. Their stated conclusions do not include the square-divisibility contradiction or the universal ban on double highest zeros. The new theorem is intentionally restricted to *contiguous, outer-zero padded* carry encodings, so it does not claim that the broad 2016 question is entirely resolved. Kendrick (2015) studies Young graph isomorphism classes and does not state this universal boundary theorem in material checked. Further literature or implicit formulations may narrow the priority claim.

## Value
PASS. The two highest carry positions are central to constructing larger reverse multiples from the digits of smaller ones. The theorem rules out every outer-zero-padding pattern beyond the two shapes singled out in Holt's derived-family constructions, uniformly across all bases and multipliers. It is a structural exclusion related to a published open-ended construction question, not a parameter tweak, isolated small calculation, or rebranded digit identity.

## Limitations
This necessary obstruction neither proves that either surviving shape is realizable nor excludes other derived constructions with interior modifications or permutations. The finite checks are supplementary. Unindexed equivalent statements or more general graph-language consequences remain possible. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
