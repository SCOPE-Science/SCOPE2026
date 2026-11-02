# Scientific assessment

## Correctness — PASS

For each period-three configuration, summing updates forces an equal count of firings at every vertex. Excluding the all-fire and all-wait fixed states leaves one or two firings per vertex. The one-firing phases are classified exactly by predecessor-neighbor counts and independent integer height intervals; an edgewise summation gives the conserved total. An explicit chip complement relates the two-firing class, and the interval-support and reciprocity laws follow without extrapolating finite tests. Every constructed state meets the firing inequalities, and uniqueness under temporal phase rotation is accounted for. The standalone verifier independently matches 578,628 bounded initial configurations across 595 labelled graphs, plus further checks recorded in `verification_output.txt`.

## Originality — PASS, with residual risk

The 1994 Prisner general phase-partition construction, 2010 Jiang complement/uniformity results, and 2006 Dall'Asta cyclic orbit analysis are directly acknowledged as predecessors, and no novelty is attributed to those ingredients. Prisner's statement that all activity-one-over-period states arise from a phase construction is the closest antecedent: it strongly reduces the possible novelty of the local characterization. The assessed distinct claim is the exact arbitrary-graph energy-indexed coefficient formula and the derived universal *gap-free two-band* support and sharp endpoint populations, which do not appear as statements or tables in the accessible primary texts. The earlier exact period-two cut enumerator does not imply these period-three populations. A previously computed book-graph three-cycle total is refined by the explicit cumulative-binomial distribution at each chip energy, rather than counted again as a new unweighted fact. No exact equivalent was found in targeted mathematical-research and literature searches; a full published equivalence remains possible. The Bitar–Goles 1992 primary full text remained inaccessible, and its abstract cannot establish noncoverage.

## Value — PASS

The chip total is a conserved natural observable, and the question of which chip masses admit a given dynamical period is central to fixed-energy sandpiles. The theorem converts the full period-three orbit population, not merely possible cycle lengths, into a graph-coloring partition function. It proves that the mass support is two contiguous intervals with an exact forbidden gap, and counts both extremal populations; these restrictions are valid for arbitrary connected graphs and are more informative than a few small-case counts. The formula is exponential-time, but exact reproducibility and a graph-wide dynamical phase diagram make the invariant mathematically useful.

## Closest literature and limitations

The relevant sources are Prisner (1994), particularly Lemma 6.7 and Proposition 6.8; Dall'Asta (arXiv:cond-mat/0601267); Jiang (arXiv:1003.0943); Jiang–Scully–Zhang (arXiv:1211.6786); and Bitar–Goles (1992). This is not a claim to discover the known period-three existence criterion or phase construction. Residual risk: the exact polynomial could be implicit in an earlier treatment of those general constructive heights, and the 1992 paper was not accessible in full. All assertions exclude disconnected graphs, dissipative rules, and basin/transient classification.

Self-review: passed. Independent audit: not yet performed.
