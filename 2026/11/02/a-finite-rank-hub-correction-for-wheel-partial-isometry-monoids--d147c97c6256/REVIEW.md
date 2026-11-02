# Review: A finite-rank hub correction for wheel partial-isometry monoids

## Correctness

**PASS.** The result is stated for the full wheel metric and every integer \(n\ge5\), not for induced-subgraph distances or the intrinsic cycle metric. The proof establishes a precise equivalence with induced graph isomorphisms because the wheel has diameter two. A cyclic-run count gives all ordinary rim-only maps; attaching a fixed hub gives an equally large disjoint family. The three exceptional cone automorphism types and three cone/rim type overlaps are exhaustive; their multiplicities give exactly the displayed correction. A standalone standard-library verifier checks all injective partial maps for rim lengths five through seven and reproduces the complete rank distributions and exceptional counts. These checks do not replace the universal proof.

## Originality

**PASS relative to inspected sources; priority provisional.** Fernandes, arXiv:2307.16257, is the closest same-object work. Its Lemma 1.1 and Theorem 2.4 already provide the small-rank exception bound and Green-class framework; the new claim is **not** that such exceptions are restricted to rank four. Rather, the new claim is their exact four-term enumerator and the all-rank identity linking the wheel to cycle induced-subgraph partial automorphisms. Jajcay et al., arXiv:1809.04422, gives the general class correspondence; Fernandes and Paulista, arXiv:2205.02196, addresses cycle intrinsic-metric isometries and therefore a different rim invariant. The closest-source implication comparison is documented in `AUDIT.json`. A stronger unlocated cone graph enumeration could subsume the answer, and exhaustive bibliographic priority has not been established.

## Mathematical value

**PASS.** All domain-rank layers of this natural family of inverse monoids are determined, including every canonical rank-ideal cardinality. The count of hub-moving maps gives an explicit and unexpectedly low-degree obstruction to a naive two-copy decomposition. This quantitatively complements prior Green-class and generating-set results and is not merely a low-dimensional census.

## Scope and evidence

The theorem covers labeled wheels with at least five rim vertices and all partial ambient-metric isometries. The included code exhaustively checks sizes up to eight wheel vertices and verifies cyclic path-profile multiplicities for larger finite cases. No claim is made about other cones, smaller wheels, cycle intrinsic distances, or independent certification. Scientific and bibliographic risks are listed in `AUDIT.json`.

Self-review: passed. Independent audit: not yet performed.
