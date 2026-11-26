# Independent mathematical audit

## correctness

PASS

The translating arc overlap for circle separation d(u) yields the centered kernel K_s(u)=(s-d(u))_+-s² for 0<s<=1/2. Complementing the translated arc preserves V pointwise, giving the reduction for all 0<s<1. Expanding the square leaves deterministic Ns(1-s) plus twice the sum of unordered pair kernels. Each centered kernel has conditional mean zero given either input, so different pairs (including pairs with one shared point) are orthogonal. For s<=t<=1/2 the kernel inner product is 2∫_0^s (s-u)(t-u) du - s²t² = s²t(1-t)-s³/3, with prefactor 4*binom(N,2). The bracket is at least s³/6. Distinct widths give linearly independent kernels by successively testing the slopes between the two largest remaining knots, including the endpoint 1/2. The strict Gram determinant and complement reduction classify correlation one; N>=2 is essential. Substituting a=qb leaves correlation sqrt(q)*(1-b-q/3)/sqrt((2/3-qb)*(2/3-b)), proving both the fixed-ratio profile and the simultaneous ratio-to-zero equivalent. Independent piecewise-Simpson quadrature on 25 pairs differed by at most 1.1e-17; a five-width Gram factorization had positive pivots. Those checks are diagnostics only; the supplied checker was inspected, not executed.

## originality

PASS

The exact mixed-width covariance, its reduced-width rank, and the microscopic ratio profile are distinct in the inspected record. The diagonal case and kernel technique are prior; the new mixed moment is a short but genuinely additional calculation, not determined by the known marginal variance or distribution.

## value

PASS

The motivating statistic is compared across window sizes, wherever its known marginal variance is insufficient. The full finite-sample covariance, its exact rank apart from complementation, and the microscopic correlation as a function of the ratio provide concrete information for multiscale use, not merely a new decimal or a repeated diagonal calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
