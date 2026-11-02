# Review of the Fano-incidence rowmotion classification

## Correctness — PASS

The recurrence follows by explicitly classifying minimal complementary points and lines. Exact orbit certificates use seven stated mask pairs, verify the rowmotion period and cardinality sum of each, enumerate all \(168\) binary-linear collineations, and obtain seven pairwise disjoint group orbits. These orbits contain \(458\) ideal states, equal to the independently checked complete ideal count, proving exhaustion. A separate C++ program builds the Fano lines differently and checks every one of the \(2^{14}\) possible bit patterns. Both provided programs were executed successfully from the packaged sources. Limit: no statement about larger projective planes is proved.

## Originality — PASS (best-knowledge, with risk)

Compared against the public preprints by Striker–Williams, Striker, and Einstein–Propp (arXiv:1108.1172, 1601.03710 and 1310.5294). These explain the toggle and rowmotion operation and give orbit/homomesy theorems on other poset families, especially products of chains and positive-root posets. Their inspected definitions, theorem scopes, relevant introductory sections and searchable full texts do not supply this seven-type Fano-specific equality or a stronger result implying it. Research-record and historical-claim comparisons also found dynamically different incidence posets, and separate graph-theoretic invariants of the Fano incidence graph; these do not imply rowmotion on its point–line partial order. Remaining risk: equivalent claims could exist under an unsearched name or in unindexed materials. Novelty has not been independently certified.

## Value — PASS

The smallest nontrivial projective plane produces a natural and symmetric height-two poset. The exact order \(105\), restriction to odd periods \(3,5,7\), exhaustive seven-orbit collineation classification and failure of constant ideal-cardinality averages are mathematically motivated dynamical information not determined by the number of ideals. The example distinguishes projective incidence order from the common products-of-chains setting and provides a fully reproducible test object for rowmotion and symmetry.

Self-review: passed. Independent audit: not yet performed.
