# Self-review

## Correctness
PASS. A published structural fact says every binary completely reachable automaton has a full-cycle letter, so fixing it as \(b(q)=q+1\pmod n\) is exhaustive for the whole binary class. The compiled census exhausts all \(n^n\) second-letter maps for every \(2\le n\le8\), and exact subset breadth-first search supplies all reaching thresholds. There are no Don violations through \(7\) states and exactly \(544\) at \(8\), each with one six-state target at distance \(17\). The displayed representative is independently replayed and reaches every nonempty subset.

## Originality
PASS. Zhu's published counterexample family starts at even \(n\ge10\). The 2026 general complete-reachability paper still summarizes that family as the known binary codimension-two lower-bound construction, explicitly notes the necessary full-cycle letter, and does not state an eight-state or minimal binary example. Exact and alias searches found no published \(8\)-state boundary or \(544\)-presentation census. The closest prior finite codimension-two claim about rank-\((n-1)\) circular automata concerns words with exactly two singular-letter occurrences and does not imply the three-occurrence hard target or the complete-reachability census.

Residual risk remains for an unindexed or unpublished small-state computation.

## Value
PASS. The first state size at which the binary completely reachable class violates a central reaching-threshold conjecture is a sharp structural boundary. Lowering the published onset from \(10\) to the exact binary minimum \(8\), while classifying all normalized first-layer violations, is mathematically informative beyond a single computational witness.

Self-review: passed. Independent audit: not yet performed.
