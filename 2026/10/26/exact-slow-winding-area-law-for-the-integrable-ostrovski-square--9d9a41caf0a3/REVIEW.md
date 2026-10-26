# Self-review

## Correctness — PASS

For the special map of [1], the proof uses its already-proved polygon itinerary and annular foliation. Matching a starting point at \(rP_4\) to its quarter-turn after \(K\) corner and \(N\) shear steps gives exactly \(r=(1+N\delta)^{-1}\). The constant successive corner determinant follows from \(\det B=1\), while every bottom-triangle shear has the same signed determinant. The telescoped center term in the shoelace formula then yields the polygon area with exact endpoints, including \(N=0\). Monotonic foliation supplies the sublevel sets; the gap between consecutive thresholds gives a uniform \(O(\varepsilon^2)\) interpolation error. Tail integration rigorously proves infinite reciprocal mean. Finite numerical polygon-area checks for four parameter choices corroborated, but do not replace, the symbolic all-parameter proof.

## Originality — PASS (bounded comparison)

Ostrovski's accessible full text [1], especially Theorem 5.1, Corollary 5.4 and the appendix, establishes **existence** and **rotation numbers** of special invariant polygons, but does not state their Lebesgue areas or the small-winding area law. Searches for the source title, the special parameter relation, polygon areas, slow-winding measure and equivalent tails found no matching formula. Bullett [2] and Lagarias–Rains [3] concern different piecewise-linear dynamical families; their accessible abstracts were checked without claiming full-text negative coverage. Residual risk remains from unindexed sources and uninspected extended literature. This is a quantitative refinement of [1], not a claim to originate its invariant circles.

## Mathematical value — PASS

Rotation number is the key invariant of the paper's integrable annuli, but the amount of conserved planar area carried by low rotation numbers is a distinct measurable quantity. Exact all-\(N\) area and the sharp coefficient at the zero-rotation boundary yield the heavy-tailed reciprocal winding frequency and its nonintegrability. This describes the prevalence of slow motion in an entire infinite family of area-preserving maps and provides a natural statistical complement to qualitative foliation.

## Scope and limits

Only the distinguished angles \(\theta_K\) with integers \(K\ge3\) and the outer foliated annuli are covered. The result does not concern generic parameters, the central region or temporal mixing. The independence of any future external validation is not claimed. References and residual novelty risks are recorded in the structured review.

Self-review: passed. Independent audit: not yet performed.
