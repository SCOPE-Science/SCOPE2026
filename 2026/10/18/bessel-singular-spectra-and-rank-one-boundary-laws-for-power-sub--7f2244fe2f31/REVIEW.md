# Self-review

## Correctness — PASS

The Gram kernel is exactly \(1-\max(t,s)^{1/\alpha}\). Differentiating its eigenvalue equation yields a Bessel equation and two boundary conditions; the vanishing weighted flux discards the inadmissible Bessel branch. Positive Bessel zeros therefore give all singular values. Classical simple-zero and large-zero properties yield simplicity and the sharp Schatten cutoff. The two moment sums are independent integrals of the kernel. A normalized Bessel series shows the first zero collapses at the small-exponent boundary, while the other zeros converge to those of \(J_1\); a uniform zero lower bound allows dominated convergence of their squared mass. Direct kernel-area integration verifies the rank-one Hilbert--Schmidt limit. The opposite endpoint follows from continuity of positive zeros at order zero. Finite discretizations and root checks are supplementary, not proofs of infinite-rank assertions.

## Originality — PASS with residual risk

The complete 2007 Domanov primary paper treats ordinary eigenvalues, ordinary eigenfunctions and spectral synthesis, not singular values. Its geometric point spectrum does not imply a Bessel singular sequence. The 2008 Domanov extension was compared through available bibliographic material and abstract, not claimed fully inspected. General singular-value theory for weighted Volterra kernels supports a first-order order-\(\(1/n\)\) law, which is not claimed new. Searches for the precise substitution kernel, its Brownian covariance alias and Bessel singular roots did not identify coverage of the combined exact singular spectrum and two boundary laws. The full literature may contain unindexed or differently named equivalents; priority is not independently certified.

## Value — PASS

This is a complete approximation-number invariant for an established nonnormal family with known ordinary spectrum. The exact sequence, strong rank-one transition with a nontrivial rescaled tail and first-order top singular correction, and the opposite large-exponent Bessel transition quantify behavior not encoded in ordinary eigenvalues or generic first-order asymptotics. The object and invariant are canonical: the original substitution-integration family on \(L^2\), its best finite-rank errors, and operator-ideal membership.

## Scope and remaining verification

The proof is for positive real exponents on unweighted complex \(L^2(0,1)\); fixed-rank endpoint limits are not uniform over all ranks. A historical equivalent treatment remains possible, notably in work on weighted Volterra singular systems or time-changed Brownian covariance kernels. Numerical tests do not substitute for the Bessel boundary argument. Independent review has not occurred.

Self-review: passed. Independent audit: not yet performed.
