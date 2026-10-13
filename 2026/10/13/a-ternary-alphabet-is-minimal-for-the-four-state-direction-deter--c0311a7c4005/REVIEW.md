# Self-review

## Correctness
PASS. The published unrestricted theorem gives the four-state ceiling \(5\). The ternary witness rejects every shorter ternary word and accepts \(\mathtt{abbac}\). For binary alphabets, every direction split is exhaustively searched over all input transition maps and all relevant end-marker returns after symmetry reduction. The enlarged search-space maxima are \(0,3,4,3\), so binary length \(5\) is impossible; the displayed \(\mathtt{abba}\) witness proves binary sharpness at \(4\).

## Originality
PASS. The primary paper determines the unrestricted value and uses five input symbols in its four-state extremal construction. Earlier fixed-alphabet work gives asymptotic lower bounds, and the current journal refinement does not report a four-state alphabet threshold. Searches across equivalent formulations, exact parameters, witness strings, published findings, and current/prior ledgers found no covering statement.

A residual risk is an unindexed or unpublished small-state computation.

## Value
PASS. Fixed alphabet size is already identified in the literature as a separate shortest-string regime. The result pins down exactly when the sharp four-state direction-determinate bound becomes attainable: binary is deficient, while ternary is sufficient. This directly refines the source extremum and substantially compresses its printed five-symbol construction.

Self-review: passed. Independent audit: not yet performed.
