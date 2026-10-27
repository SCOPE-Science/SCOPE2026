# Scientific review

## Correctness — PASS

The apex case uses explicit cycle substitution for excluded deletions and two-coloring of the surviving original path for the two infinite optimizer types. The apex-retained case forces colors via undeleted shadows and uses the remaining-original independent-set obstruction, yielding the five exceptional Grötzsch optimizers. A separate intersection analysis obtains every exchange edge and its distance enumerator; the degree-three deletion lower bound is proved. The independent traversal and parity-union-find implementations check every candidate of size at most three through odd order 25, and the exchange metrics have independent finite comparisons. The infinite result is established symbolically and is not extrapolated from these checks.

## Originality — PASS (qualified by residual risks)

Jansen and Kratsch (2011, arXiv:1107.3658) give the general OCT algorithmic setting (abstract inspected; full text not inspected). Esperet and Stehlik (2015, arXiv:1509.07716) give broader results on projective quadrangulations (material full-text sections inspected), without determining the entire optimizer set and exchange geometry here. Dabrowski et al. (2018, DOI:10.4230/LIPIcs.MFCS.2018.63) study independent OCT in different graph classes and do not subsume this statement. Direct searches also covered the synonyms vertex bipartization and induced bipartite complements and were compared with published research-record abstracts and accessible prior claims. No covering exact formula was found, but this is not a global uniqueness proof. Unindexed earlier enumerations and uninspected sections of the general kernel paper are residual risks.

## Mathematical value — PASS

The ordinary Mycielskian construction is a canonical source of triangle-free four-chromatic graphs. A complete family-wise description of every optimal three-vertex odd-cycle deletion set, the sharp Grötzsch exception, and its Petersen-versus-decorated-cycle exchange structure provides a motivated optimization classification and exact reconfiguration benchmarks beyond knowing the scalar deletion number.

## Limitations and audit status

The proof concerns ordinary Mycielskians of odd cycles of length at least five and one-for-one exchanges only. It does not assert results for arbitrary bases, iterated Mycielskians, weighted OCT, or alternate adjacency. The accompanying code checks a finite range but is not an infinite proof. Independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
