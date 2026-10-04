# Review

## Correctness
**PASS.** The claim is finite. Exhaustive breadth-first dynamic programming on the complete reachable subset automaton proves that the first singleton layer is \(32\) for both alphabets. Exact shortest-path counting gives \(331{,}776\) words for \(\{a,e\}\), all ending at state \(4\), and \(1{,}327{,}104\) words for \(\{a,b,e\}\), split as \(663{,}552\) to each of states \(3\) and \(4\). The embedded verifier reconstructs the source transition table, checks every pre-threshold subset transition, and replays the published length-\(32\) witness. The source theorem separately fixes the threshold at \(n^2-3n+4=32\) for \(n=7\).

## Originality
**PASS.** The primary full text was inspected at the construction and proof of Theorem 3. It proves the reset thresholds of \(A^{-cd}\) and \(A^{-bcd}\), but does not state the seven-state shortest-word counts or the factor-\(4\) multiplicity comparison. Searches using both “shortest synchronizing words” and “shortest reset words,” the family name, the exact threshold, and the exact counts found no published statement implying these numbers. The closest published repository records concern other automata or different invariants. Residual risk remains that an unindexed enumeration exists.

## Value
**PASS.** The source is explicitly about the effect of alphabet size on slow synchronization and itself treats counts of shortest synchronizing words as informative for small critical examples. The seven-state instance is the first state count beyond the source's exhaustive global census \(n\le6\). Holding the reset threshold fixed while adding one letter gives a natural robustness question: the exact answer is a fourfold increase in the number of optimum words plus a new optimum target state. This is a motivated finite invariant, not an arbitrary parameter slice.

## Closest literature and limitations
The closest source is de Bondt--Don--Zantema, arXiv:1609.06853 / DOI 10.1016/j.ic.2020.104614. It determines the same construction and threshold but not the claimed multiplicities. Published records `2026/9/7/SCOPE007`, `2026/9/9/SCOPE010`, and `2026/9/17/SCOPE-cerny-k-avoiding-thresholds--5cdbaf373a0f` concern different automata or different quantities and do not imply the claim. The result is restricted to \(n=7\), and no all-\(n\) count is asserted.

Same-model review: passed. Independent audit: not yet performed.
