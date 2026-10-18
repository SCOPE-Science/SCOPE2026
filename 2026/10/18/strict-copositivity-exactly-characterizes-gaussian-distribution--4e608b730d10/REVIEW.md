# Self-review

## Correctness: PASS

The covariance-simplex minimum is the squared Euclidean distance from the origin to the convex hull of the rows of a Gaussian covariance factor. Its positive projection separates all rows with a common strictly positive loading. Conditioning on the orthogonal residual yields nonnegative pairwise conditional covariances by the independent-copy identity for monotone functions. The Hermite expansion and correlated-Gaussian regression identity independently establish a lower bound on each conditional variance. The resulting explicit constant is positive, and a nonnegative covariance null vector gives a zero-variance monotone linear witness in the complementary case. All coordinate normalizations, singular cases and strictly positive marginal variances are addressed. Exact supplementary algebraic checks passed; no finite test is used as a universal proof.

## Originality: PASS, with residual priority risk

The motivating primary paper (Sei, DOI 10.1007/s41884-021-00051-9, full text, Section 7 Conjecture 4 and Appendix E.2) explicitly identifies the singular case as conjectural and proves only nonsingular sufficiency. The current claim proves the general case, including a rank-two four-coordinate example with four negative covariance edges. The matrix survey of Hiriart-Urruty and Seeger (DOI 10.1137/090750391, publisher abstract inspected) concerns algebraic copositivity and does not supply the conditional nonlinear Gaussian inequality. Targeted searches for equivalence, positive common-factor reductions, singular-covariance criteria, and dominating results did not identify a complete prior theorem. An earlier equivalent proof under different terminology or in unindexed literature remains possible; no independence or priority certification is claimed.

## Value: PASS

This is a resolution of an explicitly formulated structural conjecture from the study of Stein-type probability transformations. It covers singular Gaussian vectors in every finite dimension, supplies a computable covariance-only coercivity certificate, and yields a concrete instance far beyond pairwise-negative matching patterns. It is not a textbook substitution or merely a finite numerical invariant. The bound is not asserted optimal and does not solve separate uniqueness conjectures.

## Closest literature and limitations

Sei (2021 online; *Information Geometry* 2022 issue) provides the actual definition, the conjecture and its nonsingular special case. The older copositive-matrix literature addresses the linear-algebraic half only. The proof requires Gaussian Hermite contraction and does not extend without change to general distributions or vanishing marginal variances. Independent priority assessment and independent proof verification have not been performed.

Self-review: passed. Independent audit: not yet performed.
