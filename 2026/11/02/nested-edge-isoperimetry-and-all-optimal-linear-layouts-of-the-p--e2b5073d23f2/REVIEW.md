# Review: nested edge-isoperimetry of the Pappus graph

## Correctness

**PASS.** The cubic-neighbourhood recurrence evaluates the exact boundary of all \(262{,}144\) vertex subsets. An independent point-line incidence construction directly counts all 27 cut edges per subset, with an explicit checked graph isomorphism. Both programs produce the same 19 cut minima and minimizer multiplicities; both verify the nested cyclic order and the exact number \(31{,}850{,}496\) using independent backward and forward chain-count recurrences. The standard sum-of-prefix-cuts identity makes \(99\) and cutwidth \(8\) rigorous lower bounds, met by the exhibited order. Equality of the nonnegative sum shows that the chain count is precisely the number of all optimum minimum-linear-arrangement permutations.

## Originality

**PASS, with historical risk.** Horton–Parker–Borie (2000), §3, already states the \(\sigma\)-good definition and its *general* minimum-linear-arrangement equivalence: those implications are credited. Abiad et al. (arXiv:2601.17519), Appendix Table A4, gives only the rounded scalar Pappus isoperimetric ratio \(0.78\), not its complete cardinality profile or optimal-order census. Other inspected linear-layout papers handle different classes. Searches under the names Pappus Levi graph, honeycomb toroidal graph, cutwidth, cardinality-constrained cuts, and nested isoperimetric orders identified no explicit full profile or 31,850,496 exact count. Unindexed historical tables remain a residual risk.

## Value

**PASS.** The Pappus graph is a natural 18-vertex cubic symmetric incidence graph. For a graph layout, a single optimal ordering need not realize every constrained cut minimum; proving simultaneous attainment for this classical graph and counting all optimum orders gives a complete nontrivial finite test case linking graph expansion to layout geometry. The sharp optimum and its degeneracy are independently motivated by established minimum-cut and layout questions, not by an arbitrary selected subset size. The result is finite and does not claim an extension to all cubic graphs.

## Remaining limitation

Independent scholarly priority evaluation and independent audit have not been performed. Any equivalent unindexed Pappus layout table could reduce the novelty of part of the exact data.

Self-review: passed. Independent audit: not yet performed.
