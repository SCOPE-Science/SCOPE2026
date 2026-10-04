# Same-model review

## Correctness
PASS. The natural-spline equations leave one interior second derivative, and substituting it yields explicit cardinal coefficients on both subintervals. On each interval exactly one coefficient is nonpositive and the other two are nonnegative. Minimization over the data cube therefore reduces to one vertex, after which a single cubic shape factor has the exact maximum \(2/(3\sqrt3)\). Reflection gives the right-interval formula. The two branches cross only at \(r=1\), and elementary derivatives establish the unique equal-spacing minimum and skew-mesh divergence. The strictly positive variant follows from the partition of unity. The packaged exact-rational replay checks the algebraic identities and direct spline evaluations.

## Originality
PASS with explicit residual risk. Prior work already establishes that ordinary cubic interpolation can lose monotonicity and that a natural cubic spline through positive data can become negative; those facts are excluded from the novelty claim. Targeted semantic searches for three-knot natural splines, positivity defects, mesh-ratio bounds, cardinal-basis negativity, and the equivalent Lebesgue-constant formulation returned no implication-equivalent result. The inspected sources do not state the exact sharp function \(C(r)\), the extremizing cube vertices and locations, the unique equal-spacing minimizer, or the unbounded skew-mesh law. The strongest residual risk is the inaccessible full text of Fischer--Opfer--Puri and older spline-stability literature, either of which could contain an equivalent three-node operator-norm calculation.

## Value
PASS. Positivity is a fundamental shape constraint in interpolation, and three knots are the first nontrivial natural-spline case. The theorem does more than exhibit a counterexample: it gives the complete worst-case positivity defect as an explicit function of the mesh ratio, identifies exactly how mesh geometry controls the failure, and shows that bounded positive samples can produce arbitrarily large negative excursions. The equal-spacing optimum and the equivalent three-node Lebesgue constant provide concrete design and regression-test information.

Same-model review: passed. Independent audit: not yet performed.
