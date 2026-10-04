# Same-model review

## Correctness
PASS. The barycentric mass matrix and its inverse give an explicit reproducing kernel. Minimization over the box \(0\le f\le M\) is exactly the negative kernel mass. Writing the evaluation point as a barycentric convex combination and applying convexity of \((1-(d+2)s)_+\) shows that this negative mass is maximized at a vertex. The remaining beta integral is elementary and yields the displayed closed form. The exact \(L^\infty\) norm follows from kernel normalization. The packaged exact-rational checker independently verifies the matrix identities and beta-integral formula through dimension fifty.

## Originality
PASS with residual literature risk. Classical work covers stability and max norms of \(L^2\) projectors, one-dimensional spline and polynomial projector constants, and finite-element \(L^p\) stability. Those results are treated as prior work. published-finding corpus and literature searches under positivity, max-norm, Lebesgue-function, reproducing-kernel, affine-polynomial, and simplex aliases did not expose the all-dimensional formula \(C_d\), its indicator extremizer, or the dimension-linear positivity law. The strongest residual risk is multivariate approximation-theory literature that may encode the same quantity as a simplex polynomial-projector Lebesgue constant.

## Value
PASS. Element-local \(L^2\) projection onto linear finite-element spaces is a standard numerical primitive. The theorem completely quantifies a basic shape failure of that primitive, independent of simplex geometry: it gives the exact worst negative value, exact \(L^\infty\) amplification, an explicit extremizing region, a strictly positive witness, and the high-dimensional growth law. The fact that the defect exceeds the full input amplitude already in three dimensions makes the constant directly relevant to positivity-sensitive discretizations.

Same-model review: passed. Independent audit: not yet performed.
