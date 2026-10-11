# Review of the sharp mixed-norm disk-projection modulus

## Correctness
PASS. Strict convexity gives a unique projection. Convex first-order optimality proves the positive normal-coordinate representation, whose two-by-two Jacobian yields the exterior derivative with an explicit positive denominator. Its maximum occurs as the normal displacement vanishes, and piecewise integration along arbitrary segments converts that local bound to the exact global bound. The quartic substitution reduces the remaining maximum to a one-variable rational function with a unique critical point. The standard-library checker verifies the displayed polynomial identity and independently samples the metric projection. Finite checks are corroborative, not a proof.

## Originality
PASS with historical risk. The 2014 half-space/subspace paper gives general projection representations but does not treat projection onto the Euclidean disk under a differing ambient norm. The 2024 ball-derivative paper treats balls in their own Banach norms, not Euclidean disks viewed in \(\ell_4^2\). Literature and mathematical-record searches for cross-norm disk projection, equivalent tangent-hyperplane formulations, and the specific quartic constant did not reveal a stronger encompassing result. An older equivalent convex-approximation calculation cannot be ruled out.

## Value
PASS. Nearest-point stability of a canonical smooth convex target depends on both its shape and the norm used for approximation. The theorem exactly identifies the cross-norm amplification, supplies a closed-form sharp non-Hilbert example, and proves a complete nonexpansivity boundary across all strictly convex real \(\ell_p^2\) metrics. The exact invariant answers a natural robustness question independently of any downstream theorem.

## Limits
Real two dimensions; \(1<p<\infty\); special closed form only at \(p=4\). This is not a statement about the radial retraction onto the ambient \(\ell_p\) ball.

Same-model review: passed. Independent audit: not yet performed.
