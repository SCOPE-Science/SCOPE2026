# Review of A countable affine Skoda test family detects plurisubharmonicity

## Correctness

PASS. If the Levi form fails to be positive semidefinite, a strictly negative trace against a positive definite Hermitian matrix exists. The source proves that such matrices are exactly those arising from invertible complex affine coordinate changes.

Strict negativity is open in both the center and the affine matrix. Because a nonzero holomorphic function has zero set with empty interior, the center can be moved inside the strict negative set to a point where the fixed Bergman function is nonzero. Gaussian-rational centers and invertible Gaussian-rational matrices are dense, so the strict inequality survives discretization.

After the affine change of coordinates, the assumed tuple is exactly the source's
\[
(z_1,\ldots,z_n,M)
\]
test. The source proof for fixed
\[
M
\]
uses a limit as the Skoda exponent tends to infinity and obtains
\[
\operatorname{tr}
i\partial\bar\partial\varphi(0)
\ge
-\frac{n^2}{M^2}.
\]
All of those limits remain valid along positive integers. Applying the conclusion for integer
\[
M
\]
and then letting integer
\[
M
\]
tend to infinity gives the required contradiction.

## Originality

PASS. The 2026 source defines Skoda divisibility using every generator count, every zero-free holomorphic tuple, and every positive real exponent. Its proof narrows the mechanism to affine-normalized \((n+1)\)-generator radial tests, but it still works with continuous center, matrix, radial, and exponent parameters and does not state a countable determining family.

The 2024 precursor uses a formally stronger division estimate. It therefore does not cover the claim that a countable family of tests for the original Skoda estimate suffices.

Searches under countable-test, Gaussian-rational, rational-affine, and restricted-parameter formulations found no implication-equivalent published theorem.

## Value

PASS. The result replaces an infinite-dimensional universal testing condition by an explicit countable family while retaining an if-and-only-if characterization on bounded pseudoconvex domains.

This is a structural reduction rather than a numerical parameter improvement: it shows that differential positivity everywhere is encoded by countably many rigid affine-radial division problems. The reduction is potentially useful whenever one needs a separable, enumerable, or measurable positivity criterion and it identifies precisely which continuous freedoms in the source theorem are inessential.

Same-model review: passed. Independent audit: not yet performed.
