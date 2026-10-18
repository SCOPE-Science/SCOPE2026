# Scientific review: Dimension-free leverage control of E-optimal two-row Krylov sketch distortion

## Correctness — PASS
For two positive squared singular values, the squared condition number equals the selected squared Frobenius trace divided by the smaller value, minus one. E-optimality orders smaller values. The ratio of the selected traces is at most the row-leverage ratio, yielding the exact theorem. Equal leverage forces a common trace and hence equivalence of optimizers. The explicit orthonormal family and symmetric Krylov realization follow from exact orthogonality and exhaustive algebraic classification of four possible nonsingular pair types. A standalone checker corroborates 231 symbolic family/Krylov identities and 1,320 additional randomized frame inequalities; the infinite theorem follows from the proof, not enumeration.

## Originality — PASS, with residual risks
Bergermann (arXiv:2604.07158v1) motivates the minimum-singular-value sketch objective and records the link to subspace distortion. The previously published *A sharp-order E-versus-K row-selection gap for two-dimensional orthonormal frames* (identifier c6e6e137-5749-46ec-a56f-965b079a30f5) already establishes an order-square-root ambient-dimensional gap and Krylov realizability. That distinction is prior work and not claimed new. The present dimension-free **leverage-dependent** guarantee and exact uniform-leverage optimizer agreement are not implied by that result. The closest relevant sensor-design work by Uciński and Patan (2022) is only bibliographically accessible; analogous general theorems cannot be excluded. See the exact query comparisons and scope limits in AUDIT.json.

## Mathematical value — PASS
A previously established bad worst case makes the motivating minimum-singular-value criterion appear unreliable. The new theorem identifies a natural, verifiable geometric condition under which it is reliable independently of dimension, and pinpoints the precise uniform-leverage compatibility boundary. For leverage ratio \\(1+\\delta\\), the E-optimal distortion is at most \\(\\sqrt{1+2\\delta}\\) times the globally minimum distortion. This is a motivated structural guarantee rather than a routine change of notation; the bounds concern selected-subspace conditioning, not downstream solver convergence.

## Limitations
Only real two-column orthonormal frames, unweighted selections of precisely two rows, positive row leverage, and spectral condition number are covered. The leading constant in the leverage-dependent estimate is not proved optimal. The strongly nonuniform example confirms order sensitivity but overlaps a known dimensional phenomenon. Some primary technical literature remains inaccessible, notably the 2022 related sensor-design reference. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
