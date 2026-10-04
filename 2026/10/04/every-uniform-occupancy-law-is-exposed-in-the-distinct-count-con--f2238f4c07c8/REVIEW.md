# Same-model review

## Correctness
PASS. For \(x=1/m\), the occupancy coordinates are the polynomials \(p_{n,k}(x)=S(n,k)x^{n-k}\prod_{j=1}^{k-1}(1-jx)\). Their distinct lowest powers \(x^{n-k}\) make them a basis of all polynomials of degree at most \(n-1\). When \(n\ge3\), each finite parameter \(m_0\) is therefore exposed by the linear functional corresponding to \(-\left(x-1/m_0\right)^2\), while the limiting point is exposed by the functional corresponding to \(-x\). Any point of the convex hull outside the generating set is a nontrivial finite convex combination and cannot be extreme. No limiting, numerical, or closure argument is needed.

## Originality
PASS. The motivating paper explicitly states the all-\(n\) extreme-point assertion as Conjecture 2(i), proves only \(n=3\), identifies the higher-dimensional statement as a first step, and reports numerical convex-hull checks only for bounded \(n\) and \(m\). The current arXiv text still contains that conjecture. Targeted semantic-database and web searches for the exact conjecture, Stirling-coordinate convex hulls, occupancy moment curves, exposed uniform occupancy laws, and later citations found no theorem covering the all-\(n\) result.

Residual risk: the proof is short once the polynomial parametrization is noticed, so an equivalent argument may exist in poorly indexed convex-geometric or occupancy literature under terminology not mentioning Zhu's notation.

## Value
PASS. This resolves one complete half of the main conjecture in the motivating paper for every dimension parameter \(n\ge3\), strengthening finite numerical evidence to an exact structural theorem. The result also identifies the geometry: the uniform occupancy laws are not merely extreme but exposed, with explicit quadratic exposing functions in the reciprocal box count.

## Closest literature and limitations
The closest source is Zhu's own paper, which supplies the exact coordinates and poses the extreme-point statement as Conjecture 2(i). Search results on pairwise-independent occupancy, Stirling-number distributions, and random-polytope moment curves study different objects and do not imply this convex-hull theorem. The stronger Conjecture 2(ii), characterizing all distinct-count laws from infinite exchangeable sequences, is not addressed.

Same-model review: passed. Independent audit: not yet performed.
