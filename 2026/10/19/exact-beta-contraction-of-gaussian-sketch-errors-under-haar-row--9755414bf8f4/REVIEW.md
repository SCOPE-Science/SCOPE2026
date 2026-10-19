# Scientific review — exact Haar/Beta sketch-error law

## Correctness

PASS. The claim reduces least-squares error to an orthogonal coefficient norm, then represents the Haar sketch as the orthogonal complement of a standard Gaussian row space. The associated exact complementary-plane minimization identifies an isotropic Gaussian vector with random variance. Gaussian polar decomposition isolates a Beta projection length, and a Wishart Schur complement converts the remaining inverse quadratic form into an inverse chi-square. Independent Gaussian-regression integration yields the comparison Student vector law. The Gamma, Beta, and chi-square moments and regularly varying tails follow with the stated thresholds. Limiting cases \(\ell=r\) and \(\ell=n\) are treated separately. Numerical tests do not substitute for these steps.

## Originality

PASS, subject to the stated bibliographic risk. The closest recent source, Epperly–Webber (arXiv:2605.19096v1, Theorem 2.1 and Sections 5.1–5.4), derives exact expected sketch-and-solve loss and a matrix-Beta identity, but does not supply the asserted finite-sample vector coupling, strict all-threshold stochastic order, or higher-moment/tail coefficients. Dobriban–Liu (arXiv:1810.06089) addresses asymptotic efficiencies; Ahfock–Astle–Richardson treats Gaussian complete-sketch coefficient distributions. Related published research records checked include the sparse stochastic subspace descent Haar-moment result and the one-spike ellipsoid Haar-section Beta radius; neither entails this regression distribution. Classical matrix-variate regression literature could encode equivalent results under different language, and the full text of every potentially relevant work cannot be guaranteed inspected. No claim of exhaustive global novelty or independent validation is made.

## Mathematical value

PASS. The motivating exact *mean* formula is insufficient to describe individual sketch accuracy, especially when that mean diverges. This result determines the entire error-vector law for the same natural benchmark, sharp finite-threshold ordering and exact higher-moment existence boundaries, and quantifies how orthogonalization reduces *tail magnitude* without changing the heavy-tail exponent. These distinguish reliability and quantile performance from expected loss and supply a reference law for approximate fast sketches.

## Limits and relationship to prior work

The proof requires deterministic real data, one nonzero residual, an exactly Haar-orthonormal or standard Gaussian sketch, full column rank, and exact arithmetic. The Gaussian Student identity and Wishart/Beta formulas are classical ingredients. The 2026 source's mean comparison is not claimed as new. Prior equivalences from multivariate statistics, matrix-Jacobi ensembles, or orthogonal projection regressions remain possible; mathematical independence was not certified externally.

Self-review: passed. Independent audit: not yet performed.
