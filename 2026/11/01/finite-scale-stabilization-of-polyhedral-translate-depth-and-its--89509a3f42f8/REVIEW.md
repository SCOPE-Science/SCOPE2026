# Scientific review of finite-scale polyhedral translate depth

## Correctness — PASS

The definition of translate depth is used with closed translates and strict exclusion of the query. The upper bound comes from a violated facet inequality; it is valid even for atomic distributions. For the reverse bound, each facet-interior point supplies strictly positive inactive-facet slacks, and a witness from the convex hull of the compact support at the prescribed active-facet level supplies a translate covering the entire selected support halfspace once each projected width is below its corresponding scaled slack. Taking supremums over strict levels correctly keeps atoms on the query hyperplane excluded. The quantile-region statement follows from left continuity of strict distribution functions. Cartesian-product intervals prove the improved parallelotope threshold; a uniform full box witnesses its optimality. The included exact rational checker independently tests concrete witnesses, but universality is proved analytically.

## Originality — PASS with residual historical-priority risk

Molchanov and Nagy's arXiv:2610.26108 (first public 2026-10-19) supplies the translate-depth definition, general asymptotic tangent-cone convergence under a boundary-null condition, and a general arrangement method for finite samples; it does not state the distribution-uniform finite cutoff, explicit facet-width/slack certificate, or sharp box cutoff proved here. Fraiman and Pateiro-López's 2012 work on directional quantiles establishes that quantile-defined depth regions as such are old; the new assertion is their exact identification with finite-dilation translate depth. A previously available calculation of the depth of a uniform simplex under homothetic simplex testers is a special case, not an all-polytope/all-law result. Searches of relevant mathematical records and accessible literature returned no equivalent finite-scale theorem. This does not establish universal historical priority; inaccessible or differently named earlier work remains a risk.

## Value — PASS

A qualitative limiting depth theorem becomes an exact finite-scale identity for every compactly supported law and every polyhedral test body, with a finite, explicitly computable affine-covariant certificate. This removes the need for translate arrangements after stabilization: all levels are polytopes determined by finitely many marginal quantiles. The parallelotope case has a strictly sharper and distribution-uniformly optimal threshold of half the largest affine-coordinate width. The distinction between eventual exactness for polyhedral testers and mere asymptotic convergence in the smooth case is geometrically meaningful, and the atomic-law extension is substantive.

## Closest literature and limitations

The 2026 tangent-cone convergence result is the closest source and explains the correct limiting object; the finite cutoff is not logically supplied by its asymptotic theorem. The general cutoff here is sufficient, not always minimal. Strict projection inequalities cannot be changed to nonstrict ones for atomic laws. The support must be compact. Complete historical originality and independent mathematical validation remain open.

Self-review: passed. Independent audit: not yet performed.
