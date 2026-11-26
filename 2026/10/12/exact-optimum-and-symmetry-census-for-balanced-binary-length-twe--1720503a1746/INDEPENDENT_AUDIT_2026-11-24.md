# Independent mathematical audit

## correctness

PASS

Begin with all 924 weight-six words; imposing self-overlap exclusions leaves 272 unbordered words. For distinct vertices an edge requires both cross-overlap orders to pass for every k=1,...,11 and aligned Hamming distance at least 4. This gives exactly the admissible codes as cliques in a graph with 11,206 edges. The independent enumeration (independent_enum.py, initialized by a 40-vertex measured run) used pivoted Bron–Kerbosch and found 4,887,344 maximal cliques, with counts by size 6–13 of 2648, 40764, 437600, 1883356, 1870068, 584172, 63740 and 4996. In each call P and X contain unvisited and already assigned common neighbors; a maximal extension not already assigned must meet P outside the pivot neighborhood, since otherwise the pivot would extend it. Moving each processed branch vertex to X partitions the extensions, and P=X=empty emits exactly a maximal clique. Hence no larger code can exist and all 4996 optima are included. Reversal and complement preserve the graph and commute; independent checks of all optima give zero fixed codes for each of the three nonidentity maps, 1249 orbits of size four, and distance exactly 4 in every optimum. The newly generated 844324-byte catalogue is byte-for-byte identical to the frozen optimizers.txt, with SHA-256 63a11362c2775f93caebe0a2c00b94afddf3d4e2aab491055efdb9dabf18fdea. The frozen scripts were inspected but not executed. This is exhaustive at length 12 alone; it makes no claim of substitution-robust framing.

## originality

PASS

The inspected closest claims cover the all-overlap definition and related balanced/error-correcting constructions or relaxed exact maxima, but not this simultaneous length-12 distance-constrained optimum and all its equality cases. Neither a prior exact table in a different feasible family nor related older construction literature is credited as deciding this census. Two plausible historical source checks have unresolved access limits, not negative coverage conclusions.

## value

PASS

This is a useful finite benchmark at a block length already tabulated for the balanced framing problem. The added distance floor is the natural one-aligned-substitution correction requirement at fixed weight, not an arbitrary extra filter. The maximum gives a precise capacity comparison with the balance-only value 72; the full classification lets a researcher select among, or benchmark searches against, all optimal designs up to the two natural global symmetries. Neither the relaxed capacity nor a single construction supplies these facts. No biological application or robustness of boundary detection under errors is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
