# Review of sharp square-root joint discrepancy

## Correctness

PASS. The individual automata follow from Campbell--Cloitre's explicit theorems and can be checked against the original nested recurrences. A precisely defined sixteen-state paired transfer has characteristic polynomial \(\lambda^8(\lambda-4)(\lambda-1)(\lambda^2+3\lambda+4)(\lambda^4-3\lambda^3+5\lambda^2-12\lambda+16)\), independently recomputed in exact integer arithmetic. The uniform leading eigendirection cancels against the sign observable, and each remaining nonzero eigenvalue has modulus at most two and is simple. Base-four interval decomposition proves the bound for every positive interval endpoint, not just powers. The distinct, surviving modulus-two frequencies and the exact eighth/ninth-block values establish sharpness. Finite verification checks the calculations without substituting for the algebraic proof.

## Originality

PASS with residual risk. The source paper provides individual DFAOs, morphisms, digit formulas and factor-complexity bounds, whereas this statement concerns their coupled one-position frequencies and optimal square-root discrepancy. The two OEIS pages provide the individual recurrences and tables but no joint spectral assertion. Directed full-text and mathematical-record comparisons found no theorem covering this coupled matrix's spectrum or discrepancy bound. The closest internally indexed morphic joint-statistic study uses a different recurrence and addresses nearest-neighbor frequencies within one word; it does not imply the present two-word result. Generic transfer-matrix methods make the calculation possible but do not imply the characteristic roots or cancellation without using these specific automata. Unindexed equivalent computations are a residual originality risk.

## Value

PASS. The source intentionally compares the two new balanced automatic sequences yet examines their factor complexities separately. Whether their outputs are jointly unbiased, and at what discrepancy scale, is a natural new question. The theorem establishes quantitative joint equidistribution for *every* prefix and proves that the square-root exponent cannot be improved on the natural radix-block subsequence. This is a structural interaction between the two nested-origin recurrences, not a recomputation of their separate frequencies or a finite table entry.

Self-review: passed. Independent audit: not yet performed.
