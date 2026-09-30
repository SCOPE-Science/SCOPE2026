# Independent audit — Sharp angular profile for facet-parallel central slices of the regular simplex

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/19/sharp-angular-profile-minimal-simplex-slices--9cd127ca909d`  
**Audited tree:** `eab028891e0818e2e1f30bfe599a89360b16fa2f`

## Disposition

**PASSED on a narrowed originality boundary.** The exact fixed-angle profile and equality arcs pass; the weaker secant stability bound and isotropic Hessian are prior SCOPE results and are not validated here as original.

## Correctness

**PASS.** The chamber formula follows from the edge-intersection simplex and the pyramid-volume identity. Writing a=cos(theta)u_0+sin(theta)v gives v_0=0, sum v_i=0 and sum v_i^2=1, hence the exact product formula A/A_*=sec(theta)/prod_i(1-(v_i/d)tan(theta)). At fixed theta the positive product factors have mean 1 and fixed variance; Rodin's sharp fixed-variance AM--GM theorem therefore gives exactly the displayed Phi_n and the equality pattern with one exceptional tangent coordinate. The angle endpoint, Webb normal, monotonicity and Hessian follow by direct algebra. As an independent numerical stress test, 5,000 random admissible tangent directions in each dimension n=2,...,8 produced no violation of A/A_*>=Phi_n (minimum gaps were numerical roundoff), and the equality tangent reproduced both Phi_n(theta_max) and the stated Webb endpoint to machine precision.

## Originality

**PASS.** Originality passes only on a narrowed boundary. Two earlier SCOPE records already contain the weaker one-positive-chamber sec(theta) stability inequality and the same local isotropic Hessian (after the dimension-index shift): `2026/09/18/one-positive-simplex-slice-stability--b3c9f941eb08` and `2026/09/19/minimal-simplex-section-angular-stability--47a8f9f119ab`, both committed before this record. Those components are therefore not independently original here. What remains distinct and substantial is the exact fixed-angle profile Phi_n throughout the chamber, its complete equality arcs, and the interpolation from the facet minimum to the Webb maximum. I found no earlier repository record containing that sharp profile. Rodin supplies the sharp variance AM--GM ingredient, and the Ambrus--Gárgyán public abstract supplies the global minimum theorem, neither the fixed-angle profile.

## Scientific value

**PASS.** After removing the already-known secant bound and Hessian from the novelty claim, the exact fixed-angular-distance optimization remains a meaningful strengthening: it determines the best section-volume lower bound at every admissible angle, all equality directions, and the endpoint connection to Webb's maximum. That is materially stronger than the earlier repository stability inequalities and has standalone geometric value.

## Independent checks

- Re-derived the edge-intersection/pyramid formula and the angular product identity.
- Reduced the fixed-angle problem to the fixed-mean/fixed-variance product extremum and checked Rodin's equality pattern algebraically.
- Randomly stress-tested the profile for 5,000 admissible tangent directions per dimension n=2,...,8 with no violation beyond floating-point roundoff.
- Checked the equality tangent and theta_max endpoint against the closed Webb ratio in dimensions 2 through 8.
- Compared repository chronology and separated the genuinely new exact profile from the already-present sec(theta) inequality and Hessian.

## Literature and repository prior-art boundary

- https://arxiv.org/abs/2609.12714 — Ambrus--Gárgyán, Minimal central slices of the regular simplex; public abstract states the global facet-parallel minimum theorem.
- https://arxiv.org/abs/1409.0162 — Burt Rodin, Variance and the Inequality of Arithmetic and Geometric Means; proves the sharp fixed-mean/fixed-variance geometric-mean extremizer used in the profile optimization.
- https://doi.org/10.1007/s00454-025-00758-x — Myroshnychenko--Tang--Tatarko--Tkocz, Stability of Simplex Slicing; concerns stability of the opposite, maximal-section problem.

- `2026/09/18/one-positive-simplex-slice-stability--b3c9f941eb08/RESULT.md` (blob `0a3342bcd416692aaee08dace12c7626d087c552`) — Earlier one-positive chamber sec(theta) deficit and isotropic Hessian; committed 2026-09-18T00:07:40Z.
- `2026/09/19/minimal-simplex-section-angular-stability--47a8f9f119ab/RESULT.md` (blob `551268a699f3f8e86dcf37944beabe411ad7ed76`) — Earlier same-day exact one-positive factorization, sec(theta) bound, global near-minimizer threshold, and isotropic Hessian; committed around 2026-09-19T03:58:00Z, before the assigned record at 20:05Z.

## Limitations

- The originality PASS does not cover the weaker sec(theta) stability inequality or the isotropic Hessian; both were already present in earlier SCOPE records.
- The sharp profile is chamber-wise, not a global fixed-angle theorem over all sign patterns.
- The Ambrus--Gárgyán preprint is very recent. Its public abstract was accessible in this run, but its full body was not retrievable through the available web interface; no claim is made to have read inaccessible text, so an equivalent unindexed statement there remains a residual originality risk.
