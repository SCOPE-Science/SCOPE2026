# Review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

The proof was checked at each of its two structural steps.

First, the marker metric is valid. Hedrlín--Pultr's rigid symmetric relation for every set of cardinality at least eight is automatically loopless when the set has more than one point, because a loop would make the corresponding constant map an endomorphism. Encoding edges by distance 1 and nonedges by distance 2 therefore gives a genuine metric with trivial isometry group. For three through seven points, the explicit three-distance construction has values in [1,2], hence satisfies the triangle inequality, and its unique 3/2 pair together with the distance-1 chain fixes every point.

Second, lattice rounding preserves the metric inequality because the ceiling function is subadditive on nonnegative reals after scaling. The rounded metric is uniformly discrete and therefore compatible with the given discrete topology. Adding a positive multiple of the marker metric preserves the triangle inequality. The resulting distances have an integer lattice part plus a marker residue lying strictly between consecutive lattice levels. Different marker values are separated by at least a sigma, so any sufficiently small uniform perturbation still forces every isometry to preserve the marker metric. The numerical constants were recomputed: the center lies within 5R/6 of the target, while the rigid-neighborhood radii are R/24 in general and R/12 for cardinality at least eight; both subballs remain inside the original radius-R ball.

Potential edge cases were checked. The argument allows unbounded target metrics because only a uniformly bounded additive change is made. The supremum distance may be extended-valued globally, but all balls used in the theorem have finite radius and the construction stays in the same finite-distance component. The small finite construction works already for three points. Cardinalities above the continuum cause no problem because the two-distance marker uses only graph structure rather than distinct real distances.

## Originality

The full current version of Ishiki's arXiv:2609.19773 was inspected at its rigidity results and Questions 6.1--6.2. Question 6.1 asks whether rigid metrics are uniformly dense for every metrizable space with at least three points; the paper records the strongly zero-dimensional answer only under a continuum-cardinality bound and separately handles compact and totally bounded cases. It explicitly notes that general target metrics remain open.

Ishiki's earlier arXiv:2210.02170 was inspected around its discrete-metric construction. Its lattice-rounding lemma is acknowledged here as prior art, and its strong-rigidity results require cardinality at most the continuum. Hedrlín--Pultr's 1966 paper was inspected at the definition, existence statement and final corollary establishing rigid symmetric relations for all cardinalities at least eight, including every infinite cardinal.

Searches covered the phrases and synonymous formulations rigid metrics on discrete spaces, dense interior of rigid metrics, nonrigid metrics nowhere dense, porosity/uniform porosity of nonrigid metrics, arbitrary-cardinality discrete metrics with trivial isometry group, and combinations with Ishiki's Question 6.1. No source was found that states the rigid-subball theorem, its cardinality-free discrete consequence, or the quantitative constants.

The originality claim does not include lattice rounding, existence of rigid graphs, or known density of strongly rigid metrics below the continuum. It is limited to the quantitative marker-plus-rounding theorem and its consequences: every ball contains a definite-proportion rigid subball, ordinary rigidity remains robustly generic on arbitrary-cardinality discrete spaces, and the nonrigid locus is nowhere dense/porous even where strong rigidity is impossible.

No inaccessible source was identified whose title or available metadata specifically indicates this same quantitative result. Because the motivating preprint was submitted on 17 September 2026, unindexed or unpublished parallel work remains a residual risk.

## Value

The theorem settles a natural, explicitly posed density question for the entire class of discrete spaces without any cardinality restriction, including the regime above the continuum that cannot be reached by strong-rigidity constructions. It also strengthens mere density to a quantitative local statement: every metric ball contains a proportionally large ball on which all metrics are rigid. This yields dense interior, nowhere-denseness of the nonrigid locus, and a porosity interpretation in one stroke.

## Limitations

The theorem does not address nondiscrete metrizable spaces and therefore does not resolve Question 6.1 in full. It does not determine whether the whole rigid locus is Borel, as asked in Question 6.2. The constants 1/24 and 1/12 are not claimed to be sharp. For cardinality at most the continuum, prior work already gives density through stronger distance-separation properties; the genuinely new content in that regime is the robust subball statement.
