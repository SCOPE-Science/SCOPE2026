# Scientific review: exact one-generator approximation threshold

## Correctness
**PASS.** For each fixed positive weight vector, homogeneous powers of the affine form are orthogonal in the radial total-degree norm. The polynomial remainder constraint is equivalent to a single exact interpolation equation; Cauchy–Schwarz determines its unique minimizer. A torus Parseval formula for the multinomial square sum has one strict maximum, whose positive-definite covariance Hessian has determinant equal to the product of the weights. The Gaussian limit and positive-series comparison establish every exponent and leading constant. The standalone rational arithmetic and numerical checks completed successfully. The proof does not substitute finite testing for infinite analysis.

## Originality
**PASS with residual literature risk.** The motivating Dirichlet-space paper [1] studies unrestricted cyclicity, including an averaging lift over a continuum of linear forms; its result does not furnish the exact fixed-form polynomial inverse-approximation error. The cyclic-polynomial theorem [2] proves *full* cyclicity, which does not imply cyclicity when the multiplier algebra is restricted to polynomials in one affine average; the new bidisk example demonstrates that distinction. Earlier [3,4] instead use product-coefficient weights. Published mathematical-record, source, alias, and relevant prior-claim comparisons did not establish a dominating or equivalent fixed-generator classification. Unindexed earlier treatments of affine-symbol composition subspaces remain possible.

## Value
**PASS.** The restriction is mathematically motivated by the known \(3/2\) barrier for elementary approximation methods and the later full-cyclicity theorem through \(2\). The exact all-degree error and the support-rank critical exponent explain why a natural one-linear-form strategy genuinely stops short of the full answer. The infinite family is not a single small example, and quantitative constants identify the mechanism. The result is not claimed to resolve unrestricted cyclicity anew.

## Limitations and closest literature
No uniform constants are proved as weights degenerate; no general unrestricted higher-dimensional theorem follows. Closest references: Beslikas–Torkinejad Ziarati (arXiv:2609.09952, including Lemma 3.8), Nailwal–Zalar (arXiv:2511.13441, Theorem 3.1), and the distinct product-weight spaces of Bénéteau and collaborators (arXiv:1310.4094; arXiv:1408.3616). The usual risk of an unindexed equivalent theorem remains.

Same-model review: passed. Independent audit: not yet performed.
