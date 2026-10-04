# Same-model review

## Correctness
PASS. The proof has two independent parts. First, an internal up-beat witness remains below every point in every higher indexed fiber, and the dual statement holds for down-beat witnesses, so each fiber reduction replays inside the full lexicographic sum. Second, after every fiber is replaced by a nontrivial core, a hypothetical cross-fiber up-beat witness would force a global minimum in one core fiber; a cross-fiber down-beat witness would force a global maximum. A nontrivial minimal finite space has neither. These arguments cover arbitrary finite index posets and disconnected fibers.

The standalone verifier checks \(352\) finite lexicographic sums and \(320\) global replays of fiberwise beat deletions, then verifies that each terminal space is beat-point-free. It separately confirms the stated boundary counterexample.

## Originality
PASS with residual literature risk. The closest inspected finite-space source gives Stong's beat-point/core machinery but does not discuss lexicographic sums. The closest inspected lexicographic-sum source studies derived equivalence and does not state a result about beat points, strong deformation retracts, or Stong cores. Semantic database searches for combinations of “lexicographic sum”, “core”, “beat point”, “finite space”, and “homotopy” produced no statement implying the theorem.

The nearest earlier scientific result is the non-Hausdorff-suspension core formula, which is a single binary ordinal-sum specialization. That specialization does not imply the arbitrary-index, arbitrary-noncontractible-fiber theorem proved here.

## Value
PASS. Lexicographic sum is a standard poset substitution operation, so an exact compositional rule for Stong cores turns a global homotopy-reduction problem into independent reductions of the pieces. The theorem handles arbitrary index-poset shape and gives an exact core-cardinality formula. The noncontractibility assumption is mathematically substantive rather than cosmetic: a singleton lower fiber below a two-point antichain produces immediate extra cross-fiber collapse.

Same-model review: passed. Independent audit: not yet performed.
