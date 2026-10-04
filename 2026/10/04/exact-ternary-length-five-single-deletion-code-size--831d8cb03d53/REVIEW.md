# Same-model review

## Correctness
**PASS.** The lower bound is an explicit 24-word code whose distinct deletion shadows are checked pairwise disjoint. The upper bound is an exact rational dual certificate: 81 nonnegative output weights have numerator sum \(348\) at common denominator \(14\), and every one of the \(243\) length-five words has distinct-shadow weight at least \(14\). Disjointness then gives \(14|C|\le348<350\), hence \(|C|\le24\). The package verifier replays all finite checks with integer arithmetic.

## Originality
**PASS** to the best of current bibliographic knowledge. Kulkarni–Kiyavash explicitly tabulate the same \(q=3,n=5\) row with rounded fractional upper bound \(24\) and best-known Tenengolts size \(17\), so their statement does not imply exactness. The closest published exact deletion-code record found concerns \(q=5,n=4\), not this parameter. published-finding corpus and web searches across exact-parameter, hypergraph-matching, insertion-deletion, and Tenengolts aliases found no indexed size-24 theorem. The Li–Houghten 2012 conference paper is a genuine residual access risk because its abstract reports experiments on nonbinary Tenengolts extensions but the full text was not available for inspection.

## Value
**PASS.** The parameter is not an arbitrary slice: the 2012 primary table singles out \(q=3,n=5\) with a seven-codeword gap between the best listed construction and the fractional upper bound. Closing that gap establishes a natural exact small-alphabet synchronization-code value, and the compact rational dual certificate makes the upper bound independently reproducible.

## Closest literature and limitations
Kulkarni–Kiyavash provide the exact-parameter fractional upper-bound table and hypergraph formulation but no size-24 code. The later quinary length-four exact result demonstrates the same optimization interface at different parameters. The present result neither classifies all extremizers nor generalizes to other lengths or alphabets.

Same-model review: passed. Independent audit: not yet performed.
