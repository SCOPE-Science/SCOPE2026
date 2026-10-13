# Self-review

## Correctness
PASS. Positive affine invariance reduces every ordered three-point support to \(\{0,t,1\}\) with \(0<t<1\). Exact counting of all \(27\) samples gives the displayed first and second moments and mixed moment. These yield the stated covariance, variances, and squared-correlation rational function. Its derivative factors exactly into terms with fixed signs except \(2t-1\), so the unique global maximizer is \(t=1/2\), where the correlation equals \(1/4\). The finalized checker reproduces every symbolic identity.

## Originality
PASS. The 2022 lead source proves a discrete support-geometry extremal theorem only for two iid draws and recalls the universal order-statistic correlation bound for larger samples. The 1999 sample-size-three source proves a covariance bound over arbitrary parent distributions, not a fixed-mass three-point correlation optimization. Final searches over minimum/maximum aliases, three-atom/discrete-uniform terminology, the exact constant \(1/4\), and arithmetic-progression equality found no covering statement. The closest indexed result changes the probability vector on an equally spaced three-point support for two draws, a different parameter space and sample size.

## Value
PASS. This is the smallest support on which interior spacing geometry can vary and the first sample size beyond the two-draw problem treated by the motivating discrete Terrell theorem. The result gives a complete sharp classification, improves the universal three-draw extreme-order correlation bound from \(1/3\) to \(1/4\) on this natural finite model, and identifies the unique equality geometry. The statement is a natural finite benchmark rather than an arbitrary parameter slice.

## Closest literature and limitations
The closest sources are Papadatos's 2022 discrete Terrell paper and his 1999 covariance theorem for sample size three. The theorem here is restricted to exactly three equally weighted atoms, and an older unlocated equivalent calculation remains a residual originality risk.

Self-review: passed. Independent audit: not yet performed.
