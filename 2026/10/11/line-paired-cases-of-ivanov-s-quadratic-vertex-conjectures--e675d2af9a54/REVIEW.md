# Same-model review

## Correctness

PASS. Polarity turns the line-paired convex hull into a parallelotope inside the Euclidean ball. A zero-mean product distribution on its vertices gives
\[
\sum_i\frac{\|w_i\|^2}{\alpha_i\beta_i}\le1.
\]
Biorthogonality gives \(\|w_i\|\ge1\), reducing the quadratic and linear claims to sharp scalar inequalities. Equality propagates through every step and forces an orthonormal basis with radii \(\sqrt d\). For line-paired tight frames, tightness forces the directions to be orthonormal; the polar is an axis box and its Gaussian vertex second moment is an explicit diagonal covariance plus a positive rank-one mean term. Operator monotonicity of square root then gives the sharp \(\sqrt2 d\) trace bound.

## Originality

PASS. The primary recent source explicitly leaves both quadratic statements open, records only the equal-norm consequence for the first, and cites exact low-dimensional coverage from Bezdek--Litvak. The new line-paired class allows unequal opposite radii in every dimension. Searches across asymmetric cross-polytopes, paired lines, dual parallelotopes, vertex-index sums, and tight-frame box formulations found no theorem implying the two sharp inequalities and equality classification.

## Value

PASS. The result resolves both recent quadratic conjectures on the canonical \(2d\)-vertex cross-polytope combinatorial class and simultaneously proves the stronger Bezdek--Litvak linear benchmark there. It is an all-dimensional structural theorem with rigidity, rather than a finite computation or an arbitrary numerical slice.

Same-model review: passed. Independent audit: not yet performed.

## Closest literature and limitations

The closest source is Ivanov, arXiv:2609.38394v1, whose Section 5 poses the quadratic conjectures and explains their relation to the vertex index. Bezdek--Litvak supply the older all-dimensional conjecture and exact dimensions two and three. General vertex-index estimates do not imply this paired-line result.

The theorem requires exactly one positive and one negative vertex on each of \(d\) independent lines. Arbitrary \(2d\)-point configurations and arbitrary tight frames remain open. An older equivalent parallelotope formulation under different terminology is the main residual bibliographic risk.
