# Review of the binary length-six MDS symbol-pair code census

## Correctness — PASS

The result concerns exactly sixteen-word subsets of binary length-six words with cyclic pair distance at least four. The critical reduction is explicit: two distinct words have pair distance at most three if and only if their disagreement support lies within an adjacent cyclic two-position interval. Thus six four-coordinate erasure projections must all be bijections, yielding an exact-cover problem with 96 columns and 64 six-column rows. The supplied exact-cover code exhausts every 16-row exact cover and finds 76; a logically different 64-vertex compatible-clique recursion also finds 76 and lists exactly the same sets. Both independently calculate the full catalog; the Python code additionally verifies all 120 pairwise distances per code, the 44/32 affinity split, and five complete isometry orbits. The written graph and exact-cover recursion invariants justify completeness. No partial search or computational limit is passed off as a proof.

## Originality — PASS, with remaining uncertainty

Chee et al. (arXiv:1211.1728, §§2--4, Corollary 3.2(iv)) proved the known bound and existence of binary length-six distance-four MDS symbol-pair codes; those are not new. Ding et al. (arXiv:1605.08859, §§1--6) develop linear constructions in other distance regimes and do not count nonaffine MDS codes. The closest indexed mathematical records involve cyclic linear codes at other lengths and distances, or the binary length-five pair-distance-four full-optimum count; none of their stated results imply 76 length-six optimizers, 32 nonaffine optimizers, and five complete orbits. Exhaustive source comparisons and alternate wording searches found no stronger covering classification. The original Cassuto–Blaum paper's full publisher text was unavailable during the present comparison; the possibility of earlier unindexed counts or equivalent erasure-array classifications remains an originality risk.

## Value — PASS

Maximum-distance symbol-pair codes were introduced for overlapping read channels. The Singleton bound determines how many codewords are possible but says nothing about all equality cases. The six-coordinate/adjacent-two-erasure equivalence makes 16 the exact information-theoretic maximum and makes classification of all optimal erasure layouts an intrinsic next question. The presence of 32 nonaffine optimal codes and a single 32-element nonaffine orbit gives meaningful structural information unavailable from linear constructions or a single witness. The five orbit representatives reduce full design enumeration to small canonical choices. This is a self-contained natural finite classification, not a claim of an infinite new bound or a minor numerical improvement to one.

## Residual limitations

The originality claim concerns the complete finite classification and does not assert priority over the existence theorem. The search cannot exclude unindexed technical reports or unviewed closed publisher appendices. The package has no independent external mathematical audit.

Self-review: passed. Independent audit: not yet performed.
