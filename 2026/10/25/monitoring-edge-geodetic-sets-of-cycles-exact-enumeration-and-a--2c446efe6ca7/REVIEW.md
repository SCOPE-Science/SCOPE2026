# Scientific review: monitoring edge-geodetic sets of cycles

## Correctness — PASS

The shortest-path definition of monitoring is equivalent on a cycle to covering its edges by unique shortest paths between selected vertices. Lemma 1 proves exactly that the successive selected-vertex gaps are less than half the circumference. Lemma 2 double-counts labeled subsets via a marked first selected vertex. Lemma 3 derives the necessary-and-sufficient condition for inclusion-minimality from deletion of a single vertex; summing adjacent-gap inequalities bounds minimal-set size at three for odd cycles and four for even cycles. At the even four-set boundary, equality forces two antipodal vertex pairs. Inclusion-exclusion counts all minimum triples. There are no unproved infinite extrapolations or unjustified edge cases: cycles of length three and four are handled explicitly. The supplied direct shortest-path verifier exhausts every subset for fourteen graph sizes, from three through sixteen vertices, and reproduces both enumerators.

## Originality — PASS (bounded priority assessment)

Dev et al., arXiv:2210.03774, Theorem 3.4, is the closest primary result: it establishes only the minimum cardinality of an MEG-set on a cycle. A minimum-cardinality statement and a single construction do not imply the full polynomial of all sets or classify inclusion-minimal sets of cardinality four. Haslegrave, arXiv:2210.08955, Theorem 1, concerns products and uses scalar MEG numbers of factors; it does not give the cycle counting polynomial. Foucaud et al., arXiv:2403.09122, study general vertex mandatory conditions, extremal bounds, and operations, while arXiv:2409.19067 studies decision and approximation algorithms, not an exact cycle-set census. Search comparisons for cyclic gaps, MEG sets, inclusion-minimality, antipodal pairs, counting polynomials and equivalent edge-deletion monitoring language did not locate the assessed result. This is a best-knowledge claim; absence of a database hit is not a novelty proof.

## Mathematical value — PASS

Network monitoring benefits from counting all feasible probe placements rather than knowing only the least number of probes. Inclusion-minimal sets represent placements in which every probe is essential; the fact that even cycles admit irredundant four-probe solutions despite an optimum of three, while odd cycles do not, is a genuine structural boundary with exact multiplicities. Both complete polynomials describe a natural infinite graph family and can serve as exact benchmarks for monitoring algorithms. The minimum MEG number itself is not presented as new.

## Sources and residual risks

Inspected primary source material: Dev et al. full arXiv Section 3.2 and cycle proof; Haslegrave arXiv Section 2 product theorem and proof; Foucaud et al. accessible arXiv definitions, relevant structure, main results and algorithms sections. Residual priority risk: literature using different terms for irredundant geodetic monitoring sets, unindexed enumeration results or other full papers not located by focused searches. Scope risk: no corresponding claim for weighted cycles, graphs with chords or arbitrary unicyclic graphs.

Self-review: passed. Independent audit: not yet performed.
