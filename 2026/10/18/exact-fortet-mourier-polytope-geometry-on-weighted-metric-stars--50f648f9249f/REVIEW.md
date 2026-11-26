# Independent mathematical audit

## correctness

PASS

The star triangle bound makes all leaf-pair constraints redundant. The residual description has interior at zero and each of the fibers at fixed center t has two distinct endpoints per leaf because ρ_i>0. Arm strips with ρ_i≥2 follow from the cube; for the remaining facet inequalities I checked the strict witnesses in the proof: near a center cap choose leaves slightly toward the interior, for a leaf cap use t=1−ρ_i/2 when ρ_i<2 and t=0 otherwise, and for a tight strip use t=−ρ_i/2 with the distinguished leaf at ρ_i/2. Negation handles opposite signs. Every vertex must use one endpoint per coordinate; at an endpoint t=±1 the center is pinned and all fiber corners have full active rank. At an interior corner without a doubly active chosen endpoint, all chosen endpoints are affine near t and admit a two-sided perturbation. At a doubly active endpoint its cap and strip determine t, and the other endpoint equations determine all leaves, so the point is extreme. If one leaf can pin t using either endpoint, every corner qualifies; otherwise precisely 2^(m−s(t)) corners avoid all pins. Counting at most 2m events of 2^(m−1) corners each proves the sharp maximum, and the claimed generic conditions separate those events. In a signed objective, use the upper endpoint for a positive coefficient and the lower endpoint for a negative coefficient. This produces a continuous concave piecewise-affine function; its slopes and all interior breakpoints give the stated exact formula and O(m log m) sweep, with ρ_i=2 contributing no interior event. The frozen support was inspected, not executed; the dimension-uniform conclusions follow analytically.

## originality

PASS

The supported increment is the all-length weighted-star face/vertex classification, including a collision count and exact attainable maximum, together with a one-coordinate breakpoint formula for the maximum-type norm on this geometry. General extreme-point and FM optimization theory are antecedents. The strongest same-day weighted-star result found treats the sum norm, not an equivalent copy of this polytope or norm formula. The sweep bound is valid but is not a claim of optimality or the source of the main structural novelty.

## value

PASS

These stars are a natural nongeneric family of pointed Lipschitz polytopes. Knowing exactly which fiber corners remain extreme when lengths coincide, become complementary, hit one or two, or exceed two gives useful all-parameter information that a generic face vector or general LP does not deliver. It also yields a short evaluation rule for arbitrary signed data with no equal-mass condition. The main value is the exact classification and degeneracy analysis, not a claim of an optimal sweep or of a new general FM solver.

The dated certificate retains the supplied scientific assessment, sources and limitations.
