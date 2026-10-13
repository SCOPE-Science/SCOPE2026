# Scientific review: exact quadratic modal-depth spectrum

## Correctness — PASS

The formula concerns precisely the finite, two-equivalence, one-atom upper-triangular grid, with modal nesting depth rather than formula size. The proof first identifies the general finite-depth modal partition recurrence; it then proves an exact alternating end-peeling invariant for the row and column successor signatures. Counting the resulting rectangular blocks, including the unique two-colored middle block, yields precisely \((t+1)^2+1\) classes until depth \(n-2\), followed by \(n^2\) classes at depth \(n-1\). The standard finite characteristic-formula argument converts type counts into the stated Boolean algebra cardinalities and establishes sharpness. Special and terminal cases \(n=2\), empty middle intervals, and \(t\ge n-1\) are covered.

Computational checks executed from the packaged standalone script: `VERIFY_OK staircase_sizes=59 modal_depth_levels=1829 row_column_selector_sizes=30 direct_boolean_unions=1100 Boolean_modal_algebra_cases=3`. Exhaustive direct algebra-generation checks for \(n=2,3,4\) use a separate Boolean-set evaluation route; large finite grid checks compare the independently computed partitions with the induction's closed formulas. Neither route substitutes for the proof at arbitrary size.

## Originality — PASS, with residual risk

The source overlap is unusually close and has been treated explicitly. Bezhanishvili–Meadors (arXiv:2312.16754v1, Theorem 5.13) already use the upper-triangular valuation as a generator of the infinite Erdős–Tarski algebra. The construction and the existence of a single generator are **excluded from the novelty claim**. Their coloring theorem characterizes generated algebras, but their inspected treatment does not state a finite \(n\)-indexed **exact depth filtration**, a quadratic number of depth-bounded types, or the optimal linear depth threshold. Figallo–Mónica-Gomes (2023) classify finite diagonal-free two-dimensional cylindric subalgebras, but do not supply this marked-generator modal-depth invariant. The generic partition-refinement method is likewise known and is not claimed. Targeted exact-statement searches and mathematical-record comparisons did not find the claimed all-size formula.

This is not a claim of independently established historical priority. Earlier work on finite-variable fragments, modal depth, or cylindric algebras might contain an implicit presentation of the same calculation; such an antecedent would affect originality and remains a residual risk.

## Mathematical value — PASS

The precise question has a natural motivation: how quickly does a canonical one-proposition labeling of a two-agent S5 square generate the full Boolean modal algebra when formulas are stratified by nesting depth? The answer is a complete exact growth law, not a small-instance enumeration: the number of Boolean-definable subsets at depth \(t\) grows as \(2^{(t+1)^2+1}\) until a sharp depth \(n-1\) saturation. The proof reveals an alternating row/column end-peeling mechanism and an exact quadratic layer-size law. It quantifies modal expressive efficiency of the classical staircase generator and gives a benchmark family for finite-depth bisimulation refinement and algebraic-logic filtration.

Self-review: passed. Independent audit: not yet performed.
