# Review

## Correctness

PASS. For the positive-weight monomial antinorm, the normal to the antisphere is the explicit gradient
\[
f_p(x)\left(p_1/x_1,\ldots,p_d/x_d\right).
\]
Orthogonality to a linear hyperplane with normal \(a\) is therefore equivalent to a reciprocal identity on every positive point satisfying \(a\cdot x=0\). Splitting the nonzero coefficients of \(a\) by sign turns the two equations into equality of total positive masses and equality of two reciprocal sums. If either sign class had two entries, varying two masses while preserving their sum would make one reciprocal sum nonconstant, contradicting the required identity. Hence exactly one positive and one negative normal coefficient remain, and their squared coefficients times the corresponding weights must agree. This gives precisely the weighted coordinate-pair seam. Direct substitution proves the converse.

The proof covers every dimension \(d\ge2\), every strictly positive probability vector of weights, and every linear hyperplane meeting the positive orthant. The standalone checker independently confirms the gradient/seam identity and stress-tests the reciprocal-sum obstruction.

## Originality

PASS with stated residual risk. The 2024 preprint and current 2025 publication were inspected at the definition of admissible hyperplanes, the lifting theorem, the smooth weighted geometric-mean example, Proposition 3, and the concluding open problems. Proposition 3 constructs one weighted coordinate-pair seam and proves that its gradient remains in the seam; coordinate permutation supplies all pairs. Neither the preprint nor the current publication states that these are the only linear everywhere-orthogonal seams.

The 2021 primary source introducing the self-dual weighted geometric-mean family was inspected at its self-duality proposition and surrounding classification discussion. It establishes the family and leaves higher-dimensional classification open, but does not classify orthogonal splitting hyperplanes for the family.

Targeted searches used the exact antinorm, weighted-coordinate equations, tangent-hyperplane orthogonality, admissible versus non-admissible seams, and uniqueness/exhaustiveness terminology. No equivalent converse theorem was located.

## Value

PASS. The later primary source makes admissible hyperplanes central to its inductive construction and explicitly asks whether non-admissible hyperplanes can play an analogous role in broader autopolar geometry. The weighted geometric-mean family is its canonical smooth self-dual example. Proving that every everywhere-orthogonal linear seam of this model is necessarily admissible gives a structural rigidity result at the precise interface between the smooth example and the lifting machinery. It identifies the full seam set, rather than checking another isolated coordinate pair, and cleanly separates what this canonical family can do from the genuinely non-admissible phenomena sought in the open polyhedral problem.

Same-model review: passed. Independent audit: not yet performed.
