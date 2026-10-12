# Review of Minimum perfect Italian functions of rook graphs

## Correctness
PASS. At a zero cell \((i,j)\), feasibility is exactly \(r_i+c_j=2\). A zero row and zero column therefore cannot coexist. In the square optimum this forces every row and column sum to be one, hence exactly a permutation matrix. In the rectangular case, weight below \(2m\) is impossible: a zero column forces every row sum to two, while with all columns positive any row of sum at least two must be full and already forces the \(2m\) lower bound. At equality, a zero column forces all positive columns to be full, leaving exactly one column of twos or two columns of ones. With no zero column, the weight budget forces the sharp boundary \(n=m+1\), exactly one full all-one row, and row-column equations force every remaining row's unique one into a common column. Direct bounded-weight computation on seven small rectangles matches the complete classification.

## Originality
PASS. The closest primary result is Theorem 4.4 of Varghese and Lakshmanan, which already gives the scalar minimum values for \(K_m\square K_n\). The new claim does not reassert that value as novel; it classifies every equality case and counts all minimum functions. The inspected full text contains no “minimum functions” or “permutation” occurrence, and its product proof does not enumerate equality structures. Lauri and Mitillos contain only the small regular example \(K_3\square K_2\), not a general rook-graph theorem. Targeted semantic searches under rook, Cartesian-product, permutation-matrix, and minimum-function formulations found no equivalent classification. The principal residual risk is an unindexed or differently worded equality-case treatment.

## Value
PASS. The exact scalar value on rook graphs was already known, so the mathematically motivated gap is the equality geometry. The classification reveals two qualitatively different optimizer structures that the value formula hides: permutation matrices on squares, column-supported minima in genuinely rectangular boards, and an additional row-column-cross phase occurring only at the sharp boundary \(n=m+1\). The resulting closed counts provide a natural refinement useful for enumerative domination and symmetry questions.

Self-review: passed. Independent audit: not yet performed.
