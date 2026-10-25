# Review

## Correctness

The affine Gram matrix is diagonal by sign symmetry, with coordinate variance \(2/[d(d+1)]\). This yields the exact kernel \(1+d(d+1)x\cdot y/2\). Convexity reduces the row-norm maximization to cross-polytope vertices; the signed Dirichlet marginal then gives the displayed integral and closed form. The positivity-defect formula follows from the row kernel having integral one. Dimension one is handled separately.

## Originality

The closest inspected literature treats \(L^\infty\)-stability of least-squares projectors in kernel approximation, while related simplex-projector and cross-polytope metric-projection results use different spaces or measures. Exact-query comparisons did not return an equivalent statement for the uniform Hausdorff boundary measure. This is a best-knowledge novelty assessment, not a claim of exhaustive priority proof.

## Value

The formula supplies a sharp finite-dimensional stability constant and exact positivity defect for a canonical family of polyhedral boundaries, with linear growth in dimension. These constants are directly relevant to whether affine least-squares approximation preserves boundedness and positivity.

Self-review: passed. Independent audit: not yet performed.
