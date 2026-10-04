# Same-model review

## Correctness

PASS. The projection branches are exhaustive by convex projection optimality. If a single-ball projection is feasible for the other ball, set inclusion makes it optimal for the intersection. If neither is feasible, zero or one active constraint is impossible, so both boundaries are active. The common boundary is the classical radical-hyperplane sphere, and orthogonal decomposition gives its nearest point in one normalization. Nonempty interior removes external tangency; containment and concentric cases are already caught by the one-ball branches.

A standalone standard-library replay compares the formula against Dykstra on deterministic edge cases and hundreds of random instances. The finite replay supports but does not replace the proof.

## Originality

PASS. The recent optimization source explicitly uses a two-multiplier dual system or Dykstra for this exact projection. The closest exact geometric prior gives projection onto the intersection of two sphere boundaries, and is credited as such; it does not state the complete convex lens projector with the active-set tests. An earlier optimization application also uses Dykstra for a two-ball intersection.

Targeted searches over closed-ball intersections, lens projection, KKT formulations, radical hyperplanes, and nearest-point formulas did not locate an equivalent complete projector. Residual risk remains that the elementary active-set synthesis appears in older computational-geometry or software literature under different terminology.

## Value

PASS. The two-ball projection is a repeated, exact, load-bearing primitive in the certified stochastic-acceleration analysis. A finite \(O(n)\) expression removes the source's iterative projection subproblem without changing its stochastic-gradient theorem and makes the exact-real oracle directly implementable. The result deliberately does not claim to solve floating-point projection-error robustness.

Same-model review: passed. Independent audit: not yet performed.
