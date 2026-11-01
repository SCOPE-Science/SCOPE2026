# Scientific review of exact balanced multipartite metric-graph spline stability

## Correctness — PASS

The projected function is globally continuous and affine on each graph edge, so its essential supremum is the largest vertex magnitude. The Gram entries \(d/3\) and \(1/6\) come from direct integrals of nodal hats. Multiplication of the explicit candidate inverse by the Gram matrix checks all three orbit types, rather than inferring invertibility from finite examples. On each kernel edge, the absolute integral is exactly \((a^2+b^2)/(2(a+b))\) for endpoints of opposite sign. Counting incident, same-part-adjacent and other-part edges yields the exact formula, attained by a kernel sign input. Exact algebra proves the sharp threshold and limits. The independently assembled full graph matrices passed 4,690 rational assertions on 26 parameter pairs. General correctness comes from the symbolic proof; finitely many checks alone would not suffice.

## Originality — PASS, with stated residual risk

Kayumov (2004) analyzes interval splines and orthogonal projection rather than branched balanced multipartite graphs. Pesenson (2005) treats quantum-graph polynomial splines built through Sobolev-energy minimization and spectral approximation. Arioli–Benzi (2015 technical report, later 2017 publication) presents finite-element mass matrices and operator equations on metric graphs, but its inspected analysis concerns PDE discretization and mass-matrix conditioning rather than an exact \(L^\infty\)-norm formula for this graph family. Searches over matching graph types, Gram matrices, aliases for least-squares spline projections and positivity defects did not identify the identical or a stronger statement. Existing endpoint estimates on a single metric star do not determine the constants for balanced multipartite graphs with multiple independent vertices in each part. Unindexed earlier exact graph-spline calculations remain possible; a failed search is not a uniqueness proof.

## Mathematical value — PASS

The central invariant is the optimal \(L^\infty\) stability constant of the canonical arclength least-squares projector, not an artificial auxiliary parameter. The result classifies an unbounded two-parameter family of vertex-transitive but increasingly branched metric graphs, with exact extremizers and an unexpected topology-dependent threshold: amplification exceeds two if and only if every part has at least four vertices. The sharp unattained family supremum \(7/3\) already approached by graphs without pendant vertices, the two distinct dense limits, strict part-size monotonicity and sharp positivity failure quantify concrete approximation instability beyond the earlier one-junction case. This gives useful exact benchmarks for finite-element mass-matrix inversion and network approximation, without claiming a downstream theorem.

## Closest literature and limits

A. Kayumov, *Least-squares approximation by second-order L-splines*, arXiv:math/0408418 (2004-08-30); I. Pesenson, *Polynomial splines and eigenvalue approximations on quantum graphs*, J. Approx. Theory 135 (2005) 203–220, DOI 10.1016/j.jat.2005.04.007; M. Arioli and M. Benzi, *A finite element method for quantum graphs*, Emory technical report TR-2015-009, subsequent IMA J. Numer. Anal. 38 (2018) 1119–1163, DOI 10.1093/imanum/drx029. This is not an assertion of publication priority over inaccessible work. It does not treat unequal part sizes, variable densities, subdivided edges, or complex scalar spaces.

Self-review: passed. Independent audit: not yet performed.
