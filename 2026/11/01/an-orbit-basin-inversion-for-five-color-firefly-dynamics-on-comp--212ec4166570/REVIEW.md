# Review of the five-color bipartite firefly census

## Correctness

**PASS.** For the stated five-color inhibitory rule, a support pair consisting of the nonempty occupied-color sets on the two shores is a genuine deterministic factor: every neighbor decision depends only on the opposite shore's membership of blinking color \(2\). There are exactly \(961\) possible pairs independent of shore sizes. Equal-color vertices on the same shore never separate, so shore support cardinalities cannot increase. A periodic support orbit therefore induces bijections of the occupied colors, allowing exact determination of the microscopic period by its color-permutation order. A complete functional-graph enumeration on all \(961\) support pairs yields \(16\) support cycles and maximum transient \(25\); the exact finite graph is supplied in `support_attractors.csv`, and the individual cycles in `support_cycles.csv`. Surjection counting then yields all primitive-orbit and basin formulas. Direct microscopic simulations of \(97{,}525\) labelled states and \(64\) numerical parameter-pair identities independently support the derived statements; the all-size proof uses the factor-and-lifting argument, not extrapolation from these experiments.

## Originality

**PASS with documented risk.** H. Lyu's arXiv:1407.1103 introduces the rule, and arXiv:1610.00837 provides tree synchronization and time-complexity analyses. Their relevant definitions, theorems, tree/branch sections and conclusions were inspected in accessible primary full text. These papers do not give complete-bipartite primitive-orbit formulas, the exact six-period basin matrix, or the inversion between a typical orbit and a typical initial configuration. A previously documented complete-tripartite \(18\)-cycle formula applies only to three nonempty shores and does not supply the present bipartite transient and basin classification. An explicit numerical relation holds between its singleton-shore specialization and the bipartite \(18\)-cycle count, so the two enumerations are scientifically related, not independent constructions. Relevant mathematical-record searches returned no directly covering match; this is evidence of noncoverage among the inspected records, not an assertion of globally proved uniqueness.

## Value

**PASS.** Counting primitive orbits and determining their attraction basins are distinct natural invariants in finite oscillator networks. Here the longest cycles dominate the *population of periodic orbits* exponentially, whereas the shortest cycles capture asymptotically almost every *initial state*. This is not a routine consequence of known synchronization/no-synchronization theorems. The sharp size-independent \(25\)-step cutoff, exact \(5/6/18\) period spectrum, complete basin census, and absence of nonperiodic basin points for the longest cycles give a structural classification of an infinite natural graph family. The source model is a standard coupled-oscillator construction rather than an arbitrary finite table.

## Limitations and closest comparisons

The claims are only for the precise synchronous five-color rule on labelled complete bipartite graphs. Their finite certificate is exhaustive for an exactly proved quotient, but independent mathematical audit has not occurred. The closest literature concerns trees, including stars; a related tripartite enumeration has comparable \(18\)-cycle factors but does not contain the bipartite basin law. An unindexed historical treatment of biclique firefly oscillators cannot be completely excluded.

Self-review: passed. Independent audit: not yet performed.
