# Review of sharp compatible-witness size

## Correctness

**PASS.** The exact object is the minimal compatible-set cardinality for binary lazy cellular automata with finite neighborhoods in the additive integer group. The closure lemma is proved directly by partitioning the compatibility conditions for subsets of an already compatible set. A single allowed nonzero offset in the zero fiber makes the implication graph acyclic, giving the lower bound \(|S|\ge w(p)+3\) when \(w(p)\ge2\). The explicit construction uses disjoint parity classes to ensure copy agreement, a connected bidirected path to force all centers, and an independent concrete finite-support input showing non-idempotence. Boundary sizes \(m=2,3,4\) are addressed separately. The standalone checker reproduces all specified finite instances; the universal proof is not inferred from its output.

## Originality

**PASS on examined evidence.** The most directly relevant primary work, Alcalá-Arroyo et al., arXiv:2610.11811v2, establishes the compatibility criterion and the two-center Example 4.7. Those are explicitly credited. The new claim is the all-memory-size sharp extremum and an all-parameter family in which every active center is indispensable. The earlier arXiv:2411.03601v3 covers interval neighborhoods, where singletons suffice, and arXiv:2401.09593v2 covers special pattern types and minimal memory. Available mathematical-record searches did not identify an equivalent sharp formula. Residual risk: an independently discovered combinatorial version may exist under different vocabulary, and no negative search is a proof of priority.

## Mathematical value

**PASS.** A recent decision criterion requires finding an arbitrary nonempty compatible subset, and its motivating example shows that singleton search can fail. The theorem answers the natural extremal question of how large a smallest certificate can be relative to true neighborhood size. The sharp bound \(\max\{1,m-3\}\) and explicit optimal construction show that the witness cardinality is unbounded even in one dimension and with two symbols. This is a structural limitation of small-cardinality tests, not a mere restatement of the criterion, and not an unsupported claim of algorithmic hardness.

## Scope and risks

The analyzed primary sources were read beyond abstracts where accessible. The 2024 work was inspected in its complete arXiv PDF; the 2025 and 2026 papers were inspected in full arXiv HTML. A general historical-priority risk remains. The actual theorem assumes the binary alphabet, integer group, unconstrained finite sparse neighborhoods, and unique active transition. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
