# Independent mathematical audit

## correctness

PASS

The Luce normalization and admissible class agree with Theorem 3.13 and Lemma 3.14; the common scaling of the discrete weights is irrelevant. For y=1-exp(-exp(-βt)u), the time derivative has density b−βg(y), and the singular part is nonnegative (jumps increase y, and the diffuse singular derivative of u is multiplied by a positive coefficient). This is a global BV decomposition: integrating on compact subintervals bounds ∫b and total singular mass together by 1+β/e. At C>sqrt(β/e), let f(y)=1/[2(C+d_C(y))]. The pointwise tangent bound sqrt(b) ≤ C+f(y)(b−βg(y)) is exact only at b=(C+d_C)^2. Integration against time and the BV chain rule for a primitive of f give A≤C+∫_0^1 f: the endpoint range is at most [0,1], and the singular contribution to that primitive is nonnegative, strictly positive for nonzero singular variation. Equality forces y(0)=0, y(1−)=1, no singular variation and y′=2d_C(C+d_C); separation uniquely determines the path. This independently verifies the calibration in RESULT.md, including arbitrary jumps, singular-continuous parts and β=0 (y=t, K=1). The shooting time is strictly decreasing in C, tends to zero at infinity and diverges logarithmically at the critical C by the quadratic maximum of g. Time substitution gives both quadratures. Expanding with ∫g=1/4 gives C=1/2+3β/16+O(β²), K=1+β/8+O(β²). At large β, any fixed positive gap C²/β−1/e makes the time O(1/β), and K−C≤1/(2C), proving the stated limit. An independent quadrature replay obtained K(1)=1.127588768729963685062, K(4)=1.500518216474186096033 and (K(0.001)−1)/0.001≈0.12500376038.

## originality

PASS

The probabilistic theorem and functional are prior. No examined statement gives the exact exponential-Luce shooting quadrature and optimizer in the full admissible class. Credit the indexed result on strict geodesic concavity for its at-most-one conclusion on a narrower path class and broader profile family; this material overlap does not give existence, the path, its constant, or a singular-path equality case.

## value

PASS

This settles a concrete instance explicitly left open by the Luce LIS limit paper. It turns an infinite-dimensional variational problem into a uniquely solvable scalar equation and determines the optimizer even when the admissible class allows jumps or a singular-continuous part. Those equality cases and the all-β scale are not routine evaluations of the variational formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
