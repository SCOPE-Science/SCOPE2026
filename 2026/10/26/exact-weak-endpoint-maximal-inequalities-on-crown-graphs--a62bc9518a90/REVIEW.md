# Scientific review: sharp weak endpoint on crown graphs

## Correctness — PASS

The graph balls are explicitly determined at radii zero through three. For thresholds too low, cardinality alone gives the required bound. At higher thresholds, the complementary radius-one balls of a deleted matched pair force a rigid distinction between one-sided and mixed-side coverage. The mixed-side case is bounded from aggregate mass (with a separate six-vertex endpoint argument); the one-sided case admits a mass-preserving transfer that reduces the optimization to elementary inequalities in one bipartition. The largest-cardinality case supplies the factor \(2(n-1)/n\). A uniform-side input attains the weak rearrangement quasinorm. The breadth-first-search exact-fraction script passed 15,796 assertions. The proof, not the samples, covers all \(n\ge3\).

## Originality — PASS within accessible evidence

The 2014 foundational paper by Soria–Tradacete develops general weak bounds using graph overlaps but does not report the exact crown-graph constant. Two 2020 maximal-operator papers by González-Riquelme–Madrid concern variation or strong-type estimates for complete/star graphs and do not imply this sharp weak result. Published search records under crown, matching-deleted biclique, weak \(\ell^1\), and centered maximal operators were compared by implication; the closest crown results address other invariants. Residual risk: older finite-cycle and neighborhood-averaging papers may contain a synonymously formulated exact calculation.

## Value — PASS

The centered graph maximal function has a well-established sharp weak-endpoint literature, while exact constants for finite natural families remain scarce. Crown graphs are the canonical regular example produced by removing just one perfect matching from a complete bipartite graph. The strict, quantitative change \(2/[n(n+1)]\) isolates a geometry-sensitive difference invisible to the generic minimum-degree bound, and the full all-order proof supplies a reusable threshold/coverage reduction, rather than a single finite computation.

Self-review: passed. Independent audit: not yet performed.
