# Review of exact tricylinder central-section areas

## Correctness — PASS

The cylindrical radial gauge is \\(\\rho(u)=R/\\sqrt{1-\\min_i u_i^2}\\). Each of the twelve generic direction sectors has one active cylindrical inequality, and projection onto the complementary coordinate pair has Jacobian \\(|n_i|\\). Circular-sector area under this projection gives the stated twelve arctangents exactly. Dominated convergence handles degenerate normal directions. The lower area bound is pointwise sharp, and its equality proof excludes all non-coordinate planes. Four symmetric zero-crossing layers yield the exact uniform cubic correction \\(-4(|p|^3+|q|^3)\\delta^3/3\\). In a local tangent chart the cubic term is not a polynomial, so third-order differentiability fails.

The packaged checker compared the formula with independently parameterized polar integration at 240 generic directions (maximum discrepancy less than \\(8\\times10^{-10}\\)) and direct section-polygon reconstruction at 24 directions (discrepancy less than \\(9\\times10^{-9}\\)). It also checked three exact symmetry examples and four cubic-ray tests. These finite checks support, but do not prove, the analytic claims.

## Originality — PASS, with residual historical risk

The complete Angell–Moore 1987 paper was inspected, including its geometric illustrations and its derivation of volumes and surface areas of intersections of cylindrical bodies. Its orthographic drawings are *projected views*, not arbitrary intrinsic planar-section area formulas. Moore 1974 was accessible only as an abstract and bibliographic entry. The 2013 Illinois report could be identified and dated but could not be inspected in full. The accessible MathWorld treatment gives the classical volume and surface, not the stated directional area formula and third-order local jet.

Comparisons against mathematical-record searches for tricylinders, sectional area, arctangents, and cubic regularity, as well as known studies of an intersecting two-cylinder body, produced no mathematical statement implying this exact three-cylinder central-section theorem. Non-identification by search is not a proof of historical priority. The inaccessible older works remain a material uncertainty, although no observed statement decisively covers this theorem.

## Mathematical value — PASS

The tricylinder is a canonical curved convex body whose volume and surface were known long ago. A complete **direction-dependent central-section area rule** and a sharp equality case answer natural slicing questions, and the uniform cubic layer expansion reveals a geometric non-smoothness invisible to the isotropic quadratic term. These joint structural properties are more than a restatement of classical volume calculations or a finite table.

## Scope and risks

All results concern equal-radius, concurrent, pairwise-orthogonal cylinders. The global maximum is not established. Numerical calculations alone cannot certify the continuum formula or uniform asymptotics; those rely on the geometric and analytic proof. The 1974 article and 2013 project report were not available for complete text-to-claim comparison; mathematical priority remains provisional.

Self-review: passed. Independent audit: not yet performed.
