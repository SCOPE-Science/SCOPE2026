# Independent mathematical audit

## correctness

PASS

For fixed root t the optimal leaf is max(t,y_i), and strict convexity gives the unique root via the derivative of a_0(t−y_0)²+Σ_i a_i(t−y_i)_+². In edge coordinates d_i=y_i−y_0 the fitted root relative to y_0 on the pooled face S is Σ_{i∈S}a_i d_i/A_S, A_S=a_0+Σ_{i∈S}a_i. The output is zero on S and d_k minus that average off S. Its weighted ℓ¹ column norms are 1 for inactive columns and a_i Σ_{k∉S}w_k/(w_i A_S) for i∈S. The latter is bounded by the singleton column value. For every face, the weak active inequalities define a closed polyhedron and the affine formulas agree on shared faces. Their intersections with a segment are intervals, so summing the local bounds gives the global two-input bound, including ties. The strict feasible identity region attains 1. The given base y_0=1, y_i=0, other leaves 3 and the increase by 1/8 preserve the singleton face for any positive masses, attaining its fraction with positive denominator. This includes m=1, with constant 1. Unit weights first amplify at m=4; w_i=a_i gives Σ_j a_j≤a_0+2 min_i a_i. In this context contraction means nonexpansivity, not a strict Lipschitz constant below 1.

## originality

PASS

The supported distinction is the exact attained two-input edge-variation constant with independently varying positive observation and edge weights and its singleton-pooling reduction on a rooted star. An indexed theorem dated 2026/11/17 is substantively identical for m≥2 and is explicitly credited; it adds a different existence question for stabilizing weights. It is evidence of equivalent coverage there, not evidence the result predates the frozen record or of who discovered it first. The inspected earlier and same-day comparisons do not give this formula.

## value

PASS

The exact norm resolves when a branching order constraint can amplify graph variation in the difference of two fits, a stability question not answered by coordinatewise monotonicity or chain bounds. It replaces all pooled-face patterns by one-leaf tests, locates the first unit-weight amplification and supplies an exact criterion for prescribed matched masses. The finite attaining witnesses distinguish genuine amplification from an upper estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
