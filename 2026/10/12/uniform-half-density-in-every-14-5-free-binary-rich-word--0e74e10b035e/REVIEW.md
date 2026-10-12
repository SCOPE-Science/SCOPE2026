# Self-review

## Correctness
PASS. The proof uses the published suffix theorem exactly as stated. The signed ternary weight \((-1,0,1)\) is converted by \(f\) to binary imbalance and is preserved by both \(g\) and \(h\). Thus level-\(n\) source blocks have imbalance at most one while their minimum length is at least \(2^n\). Complete blocks plus two boundary fragments give the claimed factor bound, and the finite prefix preceding the selected suffix is absorbed into \(C_n\). Sending the factor length and then \(n\) to infinity proves uniform half-density.

## Originality
PASS. The direct source states the structural theorem and analyzes a particular extremal construction, but does not state a frequency law for every \(14/5\)-free binary rich word. Later papers checked concern one lexicographically least extremal word or symmetry properties of selected minimizers. Searches under frequency, density, discrepancy, morphism, and repetition-threshold formulations found no covering class-wide statement.

The closest internal overlap is a finite cutoff result using the same morphism \(f\) and the same \(14/5\)-free rich condition on finite preimages; it does not concern infinite words, frequencies, or the arbitrarily deep suffix decomposition used here. A residual risk remains for an unindexed short corollary of the source theorem.

## Value
PASS. Uniform one-letter frequency over all long factors is a structural property of the entire low-repetition rich class. The result is stronger than computing the prefix density of a single fixed point, and the explicit \(2^{-n}\) slope mechanism records how arbitrarily deep structural decompositions force the asymptotic rigidity.

Self-review: passed. Independent audit: not yet performed.
