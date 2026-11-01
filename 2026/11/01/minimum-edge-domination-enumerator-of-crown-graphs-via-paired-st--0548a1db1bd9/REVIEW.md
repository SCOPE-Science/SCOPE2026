# Scientific assessment

## Correctness — PASS

The uncovered-vertex criterion reduces edge domination on the crown graph to a rigid three-case support classification. Each deletion-minimal family is distinguished by its uncovered vertices, so the cases are exhaustive and disjoint. The one-hole case retains its essential uniqueness-of-preimage condition; dropping that condition would introduce nonminimal sets. Double counting is excluded. The formal-power-series formula follows from the labeled two-sort exponential formula and inclusion–exclusion over the deleted matching. The derivations of both extremal cardinalities and multiplicities explicitly separate the small boundaries.

An independent direct edge-neighborhood checker evaluated all 1,052,740 subsets of edges over crown graphs with 2 through 5 matched pairs, comparing classification and every polynomial coefficient with exact arithmetic. Additional star-forest coefficient checks and extremal boundary tests passed. These calculations test finite cases only; the proof supplies the general quantifiers.

## Originality — PASS, with residual priority uncertainty

The closest inspected full texts are Bonamy et al., arXiv:1810.00789, on algorithmic enumeration of minimal dominating sets in forbidden-induced-subgraph classes, and Anderson–Kuenzel–Rall, arXiv:2110.07133, on well-edge-dominated graphs. The latter establishes structural results including the undeleted complete balanced bipartite family, not the complete minimal-edge-domination enumerator for the crown. Total edge domination (Pan et al., arXiv:1910.02431) is a different invariant. Searches also considered line-graph domination, star-forest enumeration, derangements, the upper edge domination number, and the deleted-matching bipartite formulation. No exact equivalent was identified in the inspected material or the queried mathematical record. An unindexed prior count remains a genuine priority risk; this is not an assertion of guaranteed global novelty.

## Mathematical value — PASS

Minimal edge domination combines natural covering and minimality constraints. Unlike an extremal scalar, the full distribution distinguishes many nonmatching minimal configurations and quantifies how the removal of one perfect matching changes the well-edge-dominated behavior of the balanced biclique. The decomposition into restricted endofunctions and spanning star forests is structural, not merely a mechanical substitution. Its sharp upper and lower counts can benchmark enumeration algorithms and study robustness under a matching deletion.

## Limitations

The formula is for balanced complete bipartite graphs with a full deleted perfect matching, not general bipartite graphs. The generating-function evaluation is exact but not claimed to be polynomial-time in binary input length. Publication priority has not been independently certified. A different representation of the same family may occur in unindexed literature; no independent mathematical audit was carried out.

Self-review: passed. Independent audit: not yet performed.
