# Review

## Correctness

PASS. Under the stated silent history, the source first- and second-moment recurrences collapse exactly to a vector numerator \(c_1g\) and a scalar denominator \(c_2\lVert g\rVert_2/\sqrt d+\epsilon\). The sharp coordinate bound follows from \(|g_j|\le\lVert g\rVert_2\), one-sparse impulses prove sharpness, and the fixed-state-budget frontier is the exact pigeonhole optimum over integer block sizes.

Scientific risk: the theorem isolates an impulse response; nonzero accumulated second moments can reduce the effect.

## Originality

PASS. The Adam-mini source qualitatively identifies dilution from averaging zeros in sparse embedding blocks and reports instability from inappropriate partitions, but it does not state the sharp support-size law or the exact minimax tradeoff over a fixed number of scalar second-moment states. Later spike-aware and block-anisotropy work addresses different mechanisms, and focused published-record searches did not identify an implication-equivalent theorem.

Residual risk: an equivalent block-normalization inequality may exist in unindexed technical notes; later BORA full publisher text was not available in the inspected access path.

## Value

PASS. Adam-mini's principal design goal is second-moment memory compression, so a sharp lower bound relating the number of retained block states to worst sparse-coordinate response directly characterizes a cost of the defining mechanism. The result also quantifies the source's qualitative warning that sparse zero patterns and coarse partitions can distort block learning rates.

Self-review: passed. Independent audit: not yet performed.
