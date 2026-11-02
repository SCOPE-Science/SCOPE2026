# Scientific assessment: positive quadratic quadrature from random nodes

## Correctness — PASS

The exactness condition on the three monomials is equivalent to containment of \((1/2,1/3)\) in the convex hull of the sampled parabola. The criterion \(\ell r<1/12<LR\) follows from the polygon's upper chord and consecutive-node lower hull. Separating the two disjoint failure modes and integrating their jointly distributed nearest and extreme points yields the stated one-dimensional integral with all constants retained. Endpoint Laplace analysis produces two extra units of \((2/3)^m\) failure beyond the explicit first unit, proving the sharp constant three. The \(95\%\) cutoff is certified with exact rational-series bounds for \(\log3\). The standalone exact-arithmetic and independent-barycentric checker passed; finite tests alone are not the proof.

## Originality — PASS, subject to historical priority uncertainty

The general random-node existence and weight-box guarantees of Neumayer–Schäfer–Ullrich (arXiv:2610.32699v1, Sections 1–2) do not state the exact sample-size-specific probability here. Hayakawa–Lyons–Oberhauser (doi:10.1007/s00440-022-01186-1, Sections 1 and 6) gives random convex-hull bounds and cubature applications but does not state the all-integer quadratic-uniform formula or sharp leading failure prefactor. The previous three-node probability is recognized as already covered, and only the full \(m\)-family and exact tail are assessed as new. Broad moment-curve and random-polytope literatures might contain an equivalent older result; no exhaustive priority claim is made.

## Mathematical value — PASS

The count of random nodes needed for positive moment exactness is a natural practical design question. The full probability sequence answers it without asymptotic approximations at small samples, gives the first exact \(95\%\) budget \(m=11\), and separates the nearest-node obstruction from the extreme-node obstruction in the sharp asymptotic. This is not just the three-node case or an arbitrary parameter substitution. The model is limited to the uniform quadratic interval and permits arbitrarily uneven positive weights; stronger weight-box feasibility is not established.

Self-review: passed. Independent audit: not yet performed.
