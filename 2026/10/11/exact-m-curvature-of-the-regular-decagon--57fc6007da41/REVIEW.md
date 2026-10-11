# Review

## Correctness
**PASS.** The Minkowski-unit condition is converted exactly to a boundary condition on the chord difference vector. For each difference vector, maximizing the normalized line height is a two-dimensional linear program on \(P_{10}\cap(P_{10}-d)\). Dihedral symmetry reduces the boundary to one half-edge. On that interval, two explicit pairs of active constraints cover all parameters, and the objective normal is a nonnegative combination of the active normals. The remaining half-space inequalities are affine in the parameter and are certified at interval endpoints. This yields two exact quadratic height-ratio formulas. Their endpoint values, convexity, and monotonicity prove the global maximum and hence the stated M-curvature. The packaged checker replays the active-set algebra and interval certificates from the actual package path.

## Originality
**PASS, with residual unindexed-work risk.** The primary 2000 article defines M-curvature and explicitly conjectures that the regular \(10\)-gon is globally extremal, but the materially inspected section does not evaluate its M-curvature. The 2010 thesis reports computer evidence that the \(10\)-gon is extremal within certain regular-polygon families, but the inspected discussion supplies neither the exact value \((7-3\sqrt5)/2\), nor the piecewise profile, nor the equality-direction classification. Exact-value, alias, golden-ratio, and M-curvature searches found no covering statement. The residual risk is that the thesis's underlying unpublished computer work contained the exact calculation.

## Value
**PASS.** The result computes exactly the invariant of the canonical body singled out by the original M-curvature conjecture. It supplies a reusable analytic benchmark for any attempted proof or refutation of the global extremal problem and reveals a nontrivial two-active-set mechanism with two distinct equality-direction families. This is materially stronger than a numerical evaluation or a routine substitution.

Same-model review: passed. Independent audit: not yet performed.
