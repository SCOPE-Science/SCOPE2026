# Scientific review: exact random equilateral zonogon deficit

## Correctness — PASS

The perimeter of a sum of \(n\) unit segments is \(2n\), and the area is the sum of all pairwise absolute determinants. The absolutely convergent Fourier expansion of \(|\sin t|\) leads to a nonnegative, exact representation of the disk-area deficit in squared empirical angular Fourier coefficients. For i.i.d. uniform directions, all overlapping pairwise area terms are uncorrelated because the conditional expectation is constant, giving exact finite mean and variance. Orthogonality of distinct trigonometric frequencies and the multivariate central limit theorem yield independent limiting complex-normal modes; their squared magnitudes are independent exponentials. A *uniform positive expected-tail bound* justifies passing from finitely many to infinitely many modes. Euler's sine product establishes the closed Laplace transform, while an exponential-convolution argument and an explicit telescoping product establish the sharp positive-tail prefactor. These steps are analytic; the finite checker supplies separate reproducibility checks.

Boundary and normalization checks: the model starts at \(n\ge2\), uses unoriented angles uniform modulo \(\pi\), unit-length rather than radius-random generators, perimeter \(2n\), and exact normalized deficit \((n^2/\pi-A_n)/n\). The limiting law is weak convergence, not asserted to be convergence in \(L^2\) on an unspecified coupling. The expectation \(1/\pi\) and variance \(1/4-2/\pi^2\) agree with the finite formulas in the limit.

## Originality — PASS, with residual priority risk

The nearest geometric primary paper, Joós–Lángi (arXiv:2206.03204), provides zonotope determinant formulas and deterministic extremal isoperimetry; neither its finite-generator extremal theorems nor its large-generator estimates assert the random-angle deficit law. Schneider (arXiv:2202.06774) treats sums of i.i.d. random segments and is closer probabilistically. Its Gaussian theorem requires a strictly positive first Hoeffding-projection variance; here the conditional expected determinant is identically \(2/\pi\), so this projection vanishes. The generic degenerate \(U\)-statistic principle anticipates a weighted chi-square law, but does not by itself supply the exact eigenvalues, elementary Laplace transform, or sharp tail constant. Buffière–Marchal (arXiv:2303.18045) studies lattice-constrained random zonotopes and different Gaussian boundary fluctuations. Rahmani–Pinoli–Debayle (2017) treats Feret-diameter descriptions and zonotope approximations with prescribed directions. No implication in the inspected materials subsumes the complete explicit claim. Broader-source searches and relevant published-result comparisons did not show a direct equivalent. The remaining risk of less-indexed circular-kernel spectral or degenerate-\(U\)-statistic literature is real; search absence is not a proof of priority.

## Mathematical value — PASS

The quantity is not an arbitrary statistic: it is the Euclidean area shortfall from the optimal circle at a fixed *deterministic* perimeter in a canonical family of random equilateral zonogons. The theorem determines its exact positive spectral decomposition, natural linear fluctuation scale, full non-Gaussian limit, elementary closed transform, and sharp upper-tail rate with prefactor. It sharply distinguishes fixed-length isotropic generators from the nondegenerate Gaussian regimes of random-length zonotopes. The full-law and sharp-tail results provide geometric information that cannot be inferred from a mean/variance computation alone.

## Literature boundary and integrity

Sources and precise scope comparisons are in `RESULT.md`, `AUDIT.json`, and the bibliography. The argument does not establish the same law for higher dimensions, nonuniform directions, or random segment lengths; it does not claim priority beyond the checked corpus. Numerical checks are finite and independent mathematical audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
