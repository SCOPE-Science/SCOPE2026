# Same-model review

## Correctness
PASS. The proof reduces an arbitrary three-column minor to equality of two geometric sums. The unit-circle conjugation identity separates the common value into the zero case, forcing three common \(N\)-th and \(m\)-th roots, and the nonzero case, where a second exact cross-multiplication forces three common \(N\)-th and \(m-1\)-st roots. The converse witnesses are immediate subgroup aliases of row \(m\) with row \(0\) or row \(1\). The verifier independently checks the determinant identity and arithmetic consequences exactly.

## Originality
PASS. The closest inspected source, *Full Spark Frames*, gives the general necessity of divisor-uniformity, prime-power sufficiency, and explicitly says the general DFT characterization is unavailable. The inspected Achanta et al. conference paper treats arithmetic progressions and single-row-deleted consecutive blocks; it does not imply this two-parameter family theorem and explicitly leaves a necessary-and-sufficient gap in its broader deleted-row parameters. Targeted published-finding corpus searches for the exact gcd criterion, the \(\{0,1,m\}\) family, geometric-sum formulation, and divisor-uniformity formulation returned no matching claim. The theorem subsumes the ledger's prior \(m=4\) case, so this is a genuine family extension rather than a separate routine increment.

## Value
PASS. The family is natural: it is the smallest nontrivial nonconsecutive Fourier-row family with one row normalized to \(0\) and another to \(1\). The result converts the general necessary divisor-uniformity condition into a complete all-composite-orders iff criterion for an infinite two-parameter class, with an elementary exact test via two gcds. This directly addresses the characterization gap emphasized by the foundational source without claiming a full general classification.

## Closest literature and limitations
The strongest overlap is with Alexeev–Cahill–Mixon's divisor-uniformity theorem and Achanta et al.'s coprimeness/vanishing-sum program. Neither inspected source states or implies the final iff criterion for all \(N,m\). The later Digital Signal Processing article was identified and compared through abstract/metadata but not read in full, leaving a residual access risk. A differently phrased or unindexed earlier statement is also possible.

Same-model review: passed. Independent audit: not yet performed.
