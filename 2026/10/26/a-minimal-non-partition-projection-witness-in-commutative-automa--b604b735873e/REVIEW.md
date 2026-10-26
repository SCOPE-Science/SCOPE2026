## Correctness

The transition tables commute on every state. The accepted language is exactly the empty word together with words having an odd number of visible-letter occurrences; the projection has three pairwise distinguishable residual states. The hidden-closure subsets are exactly \(\{1,2\},\{0\},\{1\}\), so the state-partition property fails. The two-state lower bound follows by classifying the possible visible transition maps (identity, transposition, or constant) and using commutation with every hidden letter.

## Originality

The closest primary result proves an at-most-input-size bound for projections of commutative automata and provides a non-state-partition example, but that example's projected language has one state. The present statement adds an infinite projected language whose minimal state complexity equals the three-state input and proves that no two-state example with these conditions exists. The inspected state-partition literature defines the structural property but does not state this exact boundary result. Search coverage is finite, so global novelty is not claimed.

## Value

The example isolates a meaningful boundary between the projected language's minimal state complexity and the stronger state-partition condition used for subset constructions. The exact smallest witness prevents the structural distinction from being dismissed as an artifact of a projection whose language collapses to one state.

Self-review: passed. Independent audit: not yet performed.
