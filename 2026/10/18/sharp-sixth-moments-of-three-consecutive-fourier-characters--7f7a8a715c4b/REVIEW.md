# Scientific review: Sharp sixth moments of three consecutive Fourier characters

## Correctness — PASS

The exact Haar-orthogonality identity reduces the sixth moment to squares of the coefficients of the cube of a three-term polynomial, collected modulo character order. Phase majorization is valid coefficientwise. Exact multivariate polynomial identities reduce the nonnegative optimization to the variables \(u,v,p\), whose dependence on \(p\) is strictly increasing at fixed \(u>0\). This forces equal endpoint magnitudes. The five remaining one-variable functions have rigorously factored derivatives; Descartes' rule or a quadratic in the squared parameter gives each unique global maximum, and grouped-phase equality gives all optimizers. The standard-library checker confirms exact convolution identities and derivative factorizations, plus numerical finite-group illustrations. The proof, not the illustrations, handles every compact Abelian group. Neither a computational timeout nor partial enumeration is used as an impossibility argument.

## Originality — PASS, with residual bibliographic risk

Gorbachev (arXiv:2609.32072v1, 2026-09-25) surveys sharp Bernstein–Nikolskii inequalities and generic kernel bounds, but his displayed norm comparisons do not give these fifth-, sixth-, and stable seventh-order torsion cases. The Ling–Geng–Li–Wang 2026 paper proves expected Nikolskii-factor orders for Gaussian random coefficients, not an optimal deterministic sixth moment. Ash–Ganzburg (1999) optimize the largest individual Fourier coefficient relative to a norm; their Theorem 2.1 cannot imply this synthesis extremum. Indexed findings on the three-frequency Fourier projection norm, Sidon constant, and even phase moments have different optimization data and cannot supply these maxima. A previously known fourth-moment bound is insufficient to determine these sixth-moment constants: the maximizing ratios at infinite character order differ. Older unindexed low-degree results remain the main risk; literature searches do not constitute an absolute uniqueness certificate.

## Value — PASS

This is an exact, natural finite-dimensional spectral-synthesis invariant at the next genuinely nonlinear even moment. Unlike the lower fourth moment, the sixth-moment alias analysis has two additional exceptional torsion orders and a new positive quintic optimizer. It identifies every equality phase, demonstrates a sharp transition at order seven, and provides constants useful for sharp higher-moment concentration comparisons. The five regimes are one integrated structural classification, not a collection of isolated numerical examples. No larger downstream application is claimed.

## Limits and comparison

The theorem concerns only three consecutive characters and the sixth moment. Numerical finite-group checks are supplemental. Prior article inspection resolves differences in stated optimization quantities but does not exclude every older specialized inequality. Independent review remains outstanding.

Self-review: passed. Independent audit: not yet performed.
