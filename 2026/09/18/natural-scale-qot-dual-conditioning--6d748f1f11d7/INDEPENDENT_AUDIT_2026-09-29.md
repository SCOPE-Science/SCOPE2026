# Independent audit — 2026-09-29

**Record:** `2026/09/18/natural-scale-qot-dual-conditioning--6d748f1f11d7`
**Disposition:** **PASSED**

## Correctness

**PASS** — The natural-scale coercivity and Hessian scalings are internally consistent with the section geometry at width ell=epsilon^(1/(d+2)). A finite-range difference energy over ell-neighbour pairs contributes ell^(d+2)=epsilon, the active-section mass O(ell^d) divided by epsilon gives the O(ell^-2) smoothness scale, and explicit test directions give matching upper/lower spectral bounds. The exact periodic circle model independently reproduces lambda_min -> 1/2 and kappa*r^2 -> 12.

## Originality

**PASS** — The accessible September 2026 geometry paper supplies sharp support localization, section radii and potential Hessian control, while the earlier PL and linear-convergence papers supply local optimization theory at weaker or fixed-epsilon scales. I did not locate the stated epsilon-uniform core-coercivity theorem, natural L-infinity strong-concavity radius, or Theta(epsilon^(-2/(d+2))) dual-Hessian condition number in those accessible sources. The source record itself identifies an unpublished/unavailable Part II working paper as a concrete contemporaneous-overlap risk, so originality is limited to the accessible literature.

## Scientific value

**PASS** — The result converts sharp small-regularization geometry into an explicit conditioning law, a parametrically larger certified local basin, and the natural local step-size scale. This is a useful optimization consequence rather than a restatement of the geometry theorem.

## Independent checks

- Re-derived ell^(d+2)=epsilon coercivity from local overlap plus a finite-range Poincare energy and checked that the weighted-edge mean component is controlled by the same energy.
- Checked the active-section upper bound O(ell^d)/epsilon=O(ell^-2), the constant-direction lower bound for lambda_max, and the Brenier anti-mode upper bound for lambda_min.
- Evaluated the one-dimensional periodic formulas independently at decreasing epsilon; lambda_1^- tends to 1/2 and kappa*r^2 tends to 12.

## Findings

- No mathematical defect was found in the scaling argument or the exact periodic sanity model.
- The lower Hessian scale remains O(1) while the upper scale is Theta(ell^-2), so the claimed condition number and local fixed-step scale follow.
- Originality remains conditional on accessible literature because the motivating paper cites a companion Part II working paper for which no public full text or identifier was located.

## Literature evidence

- https://arxiv.org/abs/2609.20400 — Gonzalez-Sanz and Nutz, Geometry and Convergence of Quadratically Regularized Optimal Transport I; current arXiv abstract states support thickness epsilon^(1/(d+2)), section ball bounds, and uniform two-sided Hessian bounds for the potentials.
- https://arxiv.org/abs/2605.27175 — Gonzalez-Sanz, Nutz and Riveros Valdevenito, PL inequality for quadratically regularized optimal transport; accessible source for the earlier local PL theory with explicit epsilon-dependent constants.
- https://arxiv.org/abs/2509.08547 — Earlier linear-convergence paper for quadratically regularized optimal transport at fixed regularization.
- https://www.alberto-gonzalez-sanz.com/publications — Public author publication page checked for a publicly available Geometry and Convergence Part II; none was located during this audit.

## Limitations

- The theorem is local and assumes the strong smooth uniformly convex setting of the 2026 geometry paper.
- The cited companion Part II working paper was not accessible, so no claim is made about its contents.
- The periodic model is only a scaling check, not a proof of the general theorem.

## Publication consequence

The audited claim may remain at its source path. This audit does not modify the research statement; it adds only the independent-audit evidence and updates the independent-audit verification channel.
