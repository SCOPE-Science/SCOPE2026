# Review

## Correctness

PASS. For the standardized variable \(Y\), the Gram determinant of \(1,Y,Y^2\) is exactly
\[
\kappa-\gamma^2-1.
\]
For three support points the same Gram matrix factors as a Vandermonde matrix, the positive mass diagonal, and the transpose Vandermonde matrix. This proves the exact product formula, including all powers of \(\sigma\).

After positive-affine normalization, the gap is the explicit rational function \(G(r)\). Its derivative is a positive factor times the negative of a cubic whose coefficient sequence has exactly one sign change. The cubic is negative at zero and positive at infinity, so it has exactly one positive zero. The endpoint limits are zero, proving the exact range and unique maximizer.

## Originality

PASS, with residual older moment-problem literature risk. The complete Hürlimann article was inspected at its moment-inequality discussion and its final comparison section. It records Pearson's universal inequality and the sharp two-atom equality case, but not a three-atom determinant factorization or fixed-mass support optimum.

The full 2025 Klaassen--van Es article was inspected through its skewness--kurtosis-set theorem. It treats \(\kappa-\gamma^2\) explicitly and constructs a three-valued distribution to fill the entire universal region, but its probability weights vary with the desired point. It does not state the fixed-\((a,b,c)\) product formula or the unique maximizing gap ratio.

The Rohatgi--Székely 1989 paper is highly relevant by title and abstract but was only partially accessible. It is retained as a residual risk rather than treated as a whole-document noncoverage certificate.

## Value

PASS. The Pearson gap \(\kappa-\gamma^2-1\) is itself used as a distribution-shape parameter in modern skewness--kurtosis inference. The theorem gives it an exact geometric meaning for the smallest non-binary discrete class: it is the normalized squared Vandermonde volume separating the law from the two-point boundary. Fixing the masses then yields a complete and unique support-shape optimum, rather than only a universal inequality.

The equal-mass corollary gives the simple sharp benchmark
\[
1<\kappa-\gamma^2\le\frac32,
\]
with the arithmetic progression as the unique upper extremizer.

Same-model review: passed. Independent audit: not yet performed.


Exact-rational replay: `VERIFY_OK determinant_checks=48000 normalized_checks=48000 derivative_checks=24000 optimizer_checks=96000 equal_mass_checks=6`.
