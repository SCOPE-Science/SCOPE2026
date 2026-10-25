# Independent mathematical audit

## correctness

PASS

For all integers n>=2 and real s>=1/2, the transport norm is 1/2 sum |x_i|+(s-1/2)|sum x_i|; reverse dual potentials use levels s and s-1, valid under the metric triangle bound. The polar range constraint |f_i|<=s, |f_i-f_j|<=1 gives volume 2ns-n+1 by integrating range r<=1. Splitting primal coordinates by signs, integrating positive and negative totals and applying Vandermonde gives 2/(n!s^n) sum_{j=0}^{n-1} binom(n-1+j,j)s^j. Differentiation factors as 2(1-s)/(n!s^(n+1)) times a polynomial with all positive coefficients, hence the strict equilateral maximum at s=1 and both endpoint identities. Independently checked symbolic derivative identities for n=2..11 using SymPy and inspected exact-orthant/hull reproducer. The polynomial proof, not the finite n test, establishes universal quantifiers.

## originality

PASS

A parameterized affine volume product with strict monotonicity for an equiradial hub-and-leaf metric is not stated in the inspected finite-Lipschitz-free-space volume-product primary text. The familiar tree/equilateral endpoints and the transport norm formula alone do not determine the continuous polynomial. Best-of-knowledge only.

## value

PASS

Exact continuous interpolation and unique finite-family optimum for a naturally parameterized finite Lipschitz-free unit ball are nontrivial and useful: different volume normalizations require a genuine orthant integration and yield an explicit boundary transition. It is not a renamed endpoint, and the result is intentionally limited to equiradial metrics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
