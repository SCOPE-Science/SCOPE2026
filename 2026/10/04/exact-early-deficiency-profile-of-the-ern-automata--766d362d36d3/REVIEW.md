# Same-model review

## Correctness
**PASS.** Each rank decrease requires an effective \(b\), each \(b\) decreases cardinality by at most one, and after an effective \(b\) there must be at least two intervening \(a\)'s before another effective \(b\). This gives the lower bound \(3s-2\). The explicit word \(b(a^2b)^{s-1}\) has the stated missing-set induction and reaches rank exactly \(n-s\) for \(s\le\lceil n/2ceil\). Breadth-first search independently confirms every admissible case for \(3\le n\le12\).

## Originality
**PASS, with residual bibliographic risk.** Pin's 1977 and 1978 results give broad prescribed-rank bounds; Rystsov's 2025 theorem concerns minimal monoid rank; and the closest 2026 record for the same automaton gives the maximum prescribed-set avoidance threshold \(kn\), not the minimum deficiency threshold. Exact-phrase, alias, and implication searches did not locate the formula \(3s-2\). An older equivalent statement under subset-reachability terminology remains possible.

## Value
**PASS.** The deficiency profile is a natural intermediate-rank invariant of the canonical extremal family in synchronization theory. The result exactly determines the entire first half of that profile and complements the known worst-target avoidance threshold for the same automata.

Same-model review: passed. Independent audit: not yet performed.
