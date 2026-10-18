# Review of affine projection volume/cone comparison

## Correctness — PASS

The complete analytical proof is in RESULT.md. Radial disintegration gives the independent variables \(Y=RZ\), with \(R\) having density \(d r^{d-1}\). The covariance identity \(\operatorname{Cov}(Y)=d\operatorname{Cov}(Z)/(d+2)\) fixes the affine kernel normalization without an unspecified constant. The one-sign-change positive-part integral is evaluated explicitly, and its excess over \((s-1)_+\) is positive exactly when \(s>d/(d+2)\). The exact pointwise difference and its equality criterion follow. For symmetric bodies, a support-functional/Cauchy--Schwarz estimate forces \(u_x(-x)\le-1\) at each boundary point, which proves strictness on a positive cone-measure neighborhood. The maximum for the boundary projector exists on the boundary by convexity. The disk constants are independently integrated. The companion checker passes 91 finite consistency assertions; it does not replace the proof.

## Originality — PASS within examined sources

The closest published geometric source is Böröczky--Henk, arXiv:1407.7272, which introduces cone-volume measure and proves subspace concentration/stability inequalities, not affine projection Lebesgue-function comparisons. Hangelbroek--Narcowich--Sun--Ward, arXiv:1005.2424, proves bounds for \(L^2\) kernel least-squares projectors on manifolds under local-basis conditions, not the present comparison of two measures on a convex body. The publicly available simplex volume-projector calculation treats only one measure. Published mathematical-record searches returned no statement implying the all-body pointwise inequality, exact equality criterion, or strict symmetric-body norm separation. A different formulation in the extensive projector-norm and cone-measure literature could have escaped these searches; priority is not independently certified.

## Value — PASS

Volume sampling and cone-boundary sampling are canonical alternatives on a convex body. The theorem answers a motivated stability-ordering question uniformly across all centered convex bodies rather than computing a chosen polygon or an arbitrary isolated constant. The full pointwise comparison is stronger than a final norm inequality, the exact threshold identifies when the improvement is strict, and central symmetry yields a shape-independent strict norm theorem. The unit interval and disk give explicit benchmark gaps relevant to positivity loss of unconstrained affine least squares. The method is limited to affine degree and does not assert an extension to higher-degree polynomial projection.

## Residual risks

Equivalent historical terminology involving radial disintegration and reproduction kernels remains possible. The public literature comparison used pertinent sections and targeted text searches within two available primary full texts, a published closely related exact simplex result, and open searches; it does not establish exhaustive bibliographic uniqueness. The result has not received independent mathematical or literature review.

Self-review: passed. Independent audit: not yet performed.
