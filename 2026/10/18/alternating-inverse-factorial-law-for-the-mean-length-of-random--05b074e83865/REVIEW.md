# Review of the random convex-chain mean-length law

## Correctness
PASS. The only support directions contributing to the perimeter deficit are the southwest quadrant, where the fixed-vertex support difference is the capped minimum of independent linear projections. For thresholds at most the smaller normal coordinate, the cap-area probability is exactly the square of the threshold divided by the normal-coordinate product. Integrating the independent survival probabilities gives the stated two-dimensional formula. The substitutions and Tonelli's theorem give the exact kernel, and the classical beta integral and Taylor's theorem supply the factorial coefficients with their strict signed remainder. The remainder decays fast enough for absolute convergence even with no random points. The numerical checker directly independently tests the quadrature, exact small cases, and finite inequalities.

## Originality
PASS on available source comparison, with residual priority risk. The source arXiv:2510.15807v1 computes area moments and arXiv:2510.16793 computes combinatorial vertex-number limit laws of the **same model**. Earlier primary papers by Buchta (2006) and Gusakova–Thäle (2021) compute counts and generating functions. The Euclidean lower-chain length, equivalently perimeter minus a fixed edge, is not the same statistic. Efron's broad expected-perimeter integral approach and Cauchy's support formula are acknowledged; the nontrivial finite-\(n\) coefficient evaluation, absolutely convergent inverse-factorial representation, and signed error hierarchy require further work beyond those general identities. Search evidence, source-reading scope, and residual possibilities are documented in AUDIT.json. Unindexed earlier calculations cannot be ruled out.

## Mathematical value
PASS. This resolves the exact mean of a natural Euclidean geometric observable complementary to the recently studied area and vertex-number distributions. The leading \(n^{-1/2}\) mean-length deficit differs from the known \((\log n)/n\) mean-area deficit, while the \(n^{-2}\) correction isolates the two end directions. Every number of sampled points admits systematically improvable explicit upper/lower rational corrections, which is useful for rigorous finite-sample benchmarking; it is not a numerical table or arbitrary low-order example.

## Scope and outstanding limitations
Only Euclidean mean length in the specified right-triangle model is established; no exact variance or general-triangle affine transfer is asserted. Literature priority remains provisional and independent audit is outstanding. The checker verifies sampled computations but the analytic proof carries the general claim.

Self-review: passed. Independent audit: not yet performed.
