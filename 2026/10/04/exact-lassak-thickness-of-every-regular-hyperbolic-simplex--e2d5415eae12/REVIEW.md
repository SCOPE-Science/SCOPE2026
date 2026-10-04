# Review

## Correctness

PASS. In the hyperboloid model, a supporting hyperplane with unit spacelike normal \(n\) is encoded by the nonnegative vertex pairings \(s_i=\langle v_i,n\rangle\), with at least one zero. For every point of the hyperbolic simplex, normalization of a positive combination of the vertices can only decrease the corresponding pairing relative to the maximum vertex pairing, because \(\cosh\ell>1\). Thus the support width is exactly \(\operatorname{arsinh}(\max_i s_i)\).

The regular-simplex Gram matrix and its inverse give the exact unit-normal constraint. After normalization by the largest pairing, minimizing the width becomes maximizing a quadratic functional on coordinate faces of the unit cube. Its face Hessian is positive definite, forcing every maximizer to be a zero-one vertex. The remaining one-variable discrete objective has a unique maximum at \(k=\lceil d/2\rceil\). This proves the formula and, by tracing equality, the complete minimizer classification.

The symbolic checker independently verifies the Gram inverse, the objective and difference identities, the face Hessian eigenvalue, and the three-dimensional reduction to Lassak's edge-supported expression.

## Originality

PASS with residual risk stated below. Lassak's full open-access preprint was inspected at the definition of width and thickness, the regular-simplex facet-width discussion, and the tetrahedral edge-support example. It computes a particular edge-supported width in dimension three and proves it is below the facet width, but it does not optimize over all supporting hyperplanes, identify the thickness, classify the minimizing supports, or give the all-dimensional formula.

The earlier Dekster papers use a different notion called equidistant thickness and provide estimates for simplices with edge lengths in a range. Later hyperbolic isominwidth work uses Lassak width for volume problems but does not determine the regular-simplex thickness. Targeted exact-form and alias searches found no covering statement.

## Value

PASS. Thickness is the central minimum-width invariant in the motivating paper, and the regular simplex is the canonical symmetric test body. The result converts an exhibited three-dimensional witness into an exact global optimum, classifies every minimizer, and reveals a parity-dependent support-face dimension in all dimensions. This also supplies a direct all-dimensional explanation for the nonreducedness mechanism suggested by the motivating source.

Closest-literature limitations: several inequivalent hyperbolic width notions coexist, so only statements using Lassak's support-hyperplane width are implication-relevant. The short Gram-matrix argument could have appeared under different terminology, which remains the principal residual originality risk.

Same-model review: passed. Independent audit: not yet performed.
