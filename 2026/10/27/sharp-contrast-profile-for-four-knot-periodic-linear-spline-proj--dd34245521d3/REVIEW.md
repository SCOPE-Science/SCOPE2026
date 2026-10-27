# Self-review

**Correctness — PASS.** For each positive contrast, the four-by-four nodal Gram matrix is positive definite; the displayed inverse row is verified by multiplication. Every edge-kernel has opposite-sign endpoint coefficients, giving an exact absolute-integral identity and hence the projector norm. Rational substitution and the strictly positive factored numerator establish the sharp bound and unique maximizing mesh. An independent standard-library rational checker reproduced 221 exact rational-contrast cases. Tests are supporting evidence; the analytic factorization proves the universal claim.

**Originality — PASS, with residual risk.** Passenbrunner's periodic-spline theorem gives uniform knot-independent boundedness but no exact shape profile on a four-arc ring. The Ciesielski–Kamont formulas concern interval spline projections, not cyclic Gram matrices. Existing related infinite alternating grids and uniform finite circles determine distinct special regimes but do not give this full two-periodic finite-circle profile. Actual database and accessible historical checks did not identify an implication proving the result. An overlooked explicit calculation in earlier spline literature cannot be ruled out; unavailable historical versions remain a limitation.

**Value — PASS.** This is the smallest closed mesh in which a nonconstant two-periodic knot-spacing pattern is possible. The exact all-contrast stability law identifies the unique worst allocation of knots and the limiting stability improvement under mesh degeneration. Both the natural finite configuration and the entire parameter classification, rather than a selected numerical example, motivate the fact.

Self-review: passed. Independent audit: not yet performed.
