# Scientific review

## Correctness

**PASS.** The directed error-ball overlap is exactly the six-neighbor triangular adjacency condition on ordered one-position pairs. The congruence class is pairwise nonconfusable. The explicit three-row partition consists of triangles, one edge, and one singleton and yields an exact upper bound at each induction step. Checked all boundary cases \(n=2,3,4\) and the floor recurrence. `verify.py` reproduces all finite checks claimed in the result, including exact independent-set enumeration at lengths through nine; the proof, not the census, establishes the infinite statement.

## Originality

**PASS with documented residual risk.** The closest two-token result concerns both swap directions; its length-four optimum differs (two versus three). The 2023 asymmetric-shift treatment provides constructions for general combined channels, not this sharp fixed-composition theorem. A 2024 three-token study concerns a different weight and bidirectional channel. Other records and accessible earlier mathematical claims were compared for the same result and for stronger implications. A hidden equivalent specialization in the older peak-shift literature remains plausible; Kløve's 1995 complete text was not accessible in this comparison.

## Mathematical value

**PASS.** One-sided bit-shift noise is a recognized coding channel. Exact maximum code size at all lengths for a natural sparse constant-weight layer quantifies its combinatorial correction capacity, and the proof gives a constructive decoder plus a reusable three-row clique-packing method. The outcome is not just a weight-two count or an immediate substitution into a bidirectional bound.

## Scope and risk

All statements assume at most one `01` to `10` swap, zero-based labeled linear positions, exactly two ones and no reverse swaps. The result establishes optimal cardinality and an explicit attaining family, not an enumeration of all optimum codes. Search cannot prove absolute priority; no independent external audit has taken place.

Self-review: passed. Independent audit: not yet performed.
