# Independent mathematical audit

## correctness

PASS

The original equations (6)–(7) preserve coordinate faces; all free-space benefit terms vanish at p+q+r=1. The remaining inward flux is (1−α)p+εβq+ξr+(1−ε)pq−(1−η)pr−(δ−εγ)qr. At (1,0,0) this forces α≤1. For fixed r the flux is concave in p, including the affine case ε=1, so a global minimum lies on p=0 or q=0. On either edge, writing u for the non-parasite fraction, the two mortality contributions divided by u(1−u) are d_i/(1−u)+ξ/u. Their infimum is (√d_i+√ξ)² by Cauchy–Schwarz, with the endpoint limit included when d_i=0. The edge endpoints are already inward or tangent, and strict violation yields negative flux at an interior edge point. The polytope tangent-cone criterion applies to this locally Lipschitz field, and compactness supplies global existence; a strictly negative flux gives immediate exit from the boundary. At the source parameters d_P=0, e_P=9/10 and the other edge satisfies the threshold at ξ=9/10 since (129/100−2/25−9/10)²=961/10000≤36/125=4(2/25)(9/10). Monotonicity and the prey edge establish the cutoff. Independent exact rational substitution directly into the three species equations returned ds/dt=−39/1000 and −1529/50000 at the two printed witnesses. The frozen verifier was inspected, not run. Contrary to the ancillary description in RESULT.md, it asserts only the first witness and computes an equivalent reduced flux rather than independently summing the original three equations. Its finite tests cannot certify the real-parameter theorem; the analytical proof and independent witness checks do not depend on that description.

## originality

PASS

The same model, numerical examples, and general mathematical tools are prior. The inspected original article describes physically meaningful starting states and boundedness of selected trajectories, not an all-start equivalent parameter test. Other inspected ecological models and indexed findings differ in their interaction coefficients or domain. The edge reduction, two sharp thresholds, and source-specific all-start cutoff distinguish the claim.

## value

PASS

For a published ecological model, a sharp all-start threshold tests whether the physical domain assumed by the model is actually respected. The source's standard parameter choice fails it, even at a strictly positive three-species boundary point. The exact reduction to two edges makes the criterion practical and explains why no interior full-occupancy minimization is needed. This is a domain-of-validity result, not a restatement of coordinate positivity or simulated boundedness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
