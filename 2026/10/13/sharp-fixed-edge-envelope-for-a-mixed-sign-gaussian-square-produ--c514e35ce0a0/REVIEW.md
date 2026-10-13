# Self-review

## Correctness
**PASS.** The correlation-matrix constraint is exactly the Schur-complement interval \(|c-ab|\le\sqrt{(1-a^2)(1-b^2)}\). Conditional Gaussian expansion plus Isserlis' formula reduces the normalized moment to a convex quadratic in \(d=c-ab\). The Gaussian absolute-moment recurrence is valid for \(0<\alpha<1\), and projection of the unconstrained minimizer onto the full admissible interval gives both regimes and the optimizer. The strict comparison with the earlier factor follows from an explicit positive difference. Singular covariance endpoints are included by continuity and direct positive-semidefinite Gaussian construction.

## Originality
**PASS.** The closest primary theorem gives only the product-of-residual-variances lower factor. A later arbitrary-dimensional mixed-sign paper explicitly recovers that same specialization rather than the fixed-edge optimization. Targeted database searches for the moment, covariance aliases, optimizer \(c=\alpha ab\), residual-covariance formulation, and the phase boundary found no covering result. A later series-formula paper on structured correlation families is a residual literature risk because only its public description was available, but its stated scope does not resolve the arbitrary fixed-edge envelope.

## Value
**PASS.** The result sharpens a published lower bound using exactly the correlation information that bound leaves unused, gives the best possible constant for every fixed pair of incident correlations, classifies the minimizing remaining correlation, and exposes a natural interior-to-singular phase transition. It is therefore a structural sharpness result rather than a numerical special case or routine recomputation.

## Closest literature and limitations
The closest prior statements are Zhou--Zhao--Hu--Song, arXiv:2308.13740v1, Theorem 1.1, and Lan--Ouimet--Sun, arXiv:2505.09976v2. The result is limited to a standardized Gaussian triple with one negative exponent \(-\alpha\), \(0<\alpha<1\), and two square factors. An equivalent result under different terminology remains a residual indexing risk.

Self-review: passed. Independent audit: not yet performed.
