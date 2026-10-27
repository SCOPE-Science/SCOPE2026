# Self-review

## Correctness — PASS

The Gaussian null-line reduction makes the RRR generalized eigenvectors the two roots of the explicit quadratic (1), with a directly computed geometric sine-angle identity. The small-root analytic expansion on the good Gaussian event and a product-of-roots bound on its complement give uniform subcritical moments, an exponentially truncated inverse-square integral at order two, and an integrable fourth-moment remainder. In particular, integrating over the unit-exponential modulus of the denominator yields exactly one logarithm with coefficient one, not merely an unspecified order bound. The supplied standard-library checker independently tests the polynomial residual and geometry; its finite trials do not prove the asymptotic theorem.

## Originality — PASS (subject to independent priority confirmation)

Shao's full public v1 paper was read in its example, randomized-compression algorithm, high-probability theorem, Gaussian-inverse tail discussion, numerical experiments, and references. Its Example 1 provides the **same deterministic matrix and subspace**, and those data are explicitly credited. The result here is the different oracle-best randomized eigenvector moment spectrum and critical mean-square coefficient. Theorem 2 supplies confidence-dependent high-probability bounds but does not establish moment convergence or a sharp log coefficient; its \(\delta^{-1/2}\) dependence does not identify the finite-\(\varepsilon\) truncation of the two-root RRR problem. Related deterministic sketching and Gaussian invertibility results also do not imply that truncation. Actual published mathematical finding searches and accessible research records yielded related eigenvector/residual results without coverage. Remaining historical-priority risk concerns specialized random-polynomial-root and stochastic Petrov–Galerkin literature not exhaustively inspected.

## Mathematical value — PASS

In numerical eigenvector extraction, expected squared sine-angle error is a natural ensemble risk criterion. The theorem quantifies an unavoidable, sharp logarithmic penalty even for the best of two Gaussian RRR outputs, relative to the optimal deterministic projection on the same subspace. The subcritical moment spectrum pinpoints exactly which performance measures retain a clean linear rate, while the mean-square loss shows why pointwise or confidence-level convergence alone does not settle average accuracy. The critical cutoff and coefficient require the full quadratic root coupling; the mere Cauchy-ratio tail is classical.

## Scope and risk

Only the exact complex Gaussian, two-root, three-dimensional example is proved. The oracle is not an implementable selection algorithm, and no result is asserted for oversampling, nonlinear eigenproblems, or refined Ritz vectors. A mathematically independent review and comprehensive historical-priority confirmation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
