# Independent Audit — 2026/09/19/fractional-perimeter-curvature-radius-stability--cf7bb39b7686

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `397cc8b238bf53a43a004c97d1992327b94670b4`
- Disposition: **PASSED**

## Correctness

**PASS** — The quantitative proof closes correctly. The central-window tangent inequality follows from the integral Taylor remainder for phi(x)=2 sin(x/2): on the half-segment adjacent to w∈[pi/2,3pi/2], -phi'' is bounded below by sin(pi/8)/2 and both the retained length and Taylor weight are at least |x-w|/2, giving sigma=sin(pi/8)/8. A fresh dense-grid check found no violation beyond roundoff. After integration the linear term cancels because the average tangent increment is w. The source Hölder estimate for the fractional-Willmore integrand, the Fourier lower bound min_{k≠0}∫_{pi/2}^{3pi/2}(1-cos kw)dw=pi-2/3, and the parallel-body identity rho_r=(rho+r)/(1+r) combine to give D(tilde K_r)≥r(1+r)^-3 E(K). Homogeneity then yields the stated r(1+r)^{q-3} deficit, whose integral is 1/((1-q)(2-q)); substituting q=1-s in the exact chord/perimeter relation gives the displayed constant and sign.

## Originality

**PASS** — Lin-Yang-Yang-Yuan-Zhang prove the sharp fixed-classical-perimeter fractional isoperimetric inequality and provide the chord-functional, fractional-Willmore and outer-parallel-body machinery used here, but do not state this global curvature-radius H^{-1} stability estimate. Frank-Ivanisvili give an independent qualitative sharp comparison in a broader planar class; Alberti-Cozzi-Massaccesi-Mirmina treat local stability for a ratio of two genuinely fractional perimeters with 0<s<t<1; Döhrer-Dohmen establish disk minimality for related nonlocal curvature energies. Targeted searches for a global fixed-classical-perimeter endpoint estimate controlling the H^{-1} curvature-radius defect found no equivalent theorem. The audited theorem therefore constitutes a quantitative refinement rather than merely a restatement of the source inequality.

## Scientific value

**PASS** — The theorem upgrades a sharp but qualitative fixed-perimeter maximization result to an explicit global deficit estimate on smooth strictly convex bodies. The controlled H^{-1} curvature-radius metric is natural for the outer-parallel-body argument, gives rigidity immediately, and exposes how a quantitative fractional-Willmore gap propagates to the fractional perimeter. Although the constant is not optimized and the geometry class is restricted, the result supplies a reusable stability mechanism at the classical-perimeter endpoint.

## Sources

- A Sharp Planar Fractional Isoperimetric Inequality (Xiaosheng Lin; Dachun Yang; Sibei Yang; Wen Yuan; Yangyang Zhang): https://arxiv.org/abs/2609.19052 — Primary source for the sharp inequality and the chord/fractional-Willmore/outer-parallel-body identities used by the audited quantitative refinement.
- Sharp comparison between the perimeter and its fractional analogue in two dimensions (Rupert L. Frank; Paata Ivanisvili): https://arxiv.org/abs/2609.14513 — Independent qualitative fixed-perimeter maximization in a larger class; no matching curvature-radius H^{-1} deficit was located.
- Stability of the ball in isoperimetric inequalities between two fractional perimeters (Giovanni Alberti; Giovanni Cozzi; Andrea Massaccesi; Jacopo Mirmina): https://arxiv.org/abs/2605.07543 — Nearby quantitative stability result for ratios of two fractional perimeters, in a different local regime and not the t=1 endpoint.
- A Fenchel Theorem for the Gauss maps and uniqueness of minimizers of nonlocal curvature energies (Elias Döhrer; Alexander Dohmen): https://arxiv.org/abs/2604.02042 — Prior disk-minimization theorem for fractional Willmore-type energies; no equivalent global H^{-1} deficit found.

## Limitations

- Restricted to C-infinity strictly convex planar bodies with strictly positive curvature.
- The controlled distance is an H^{-1} curvature-radius defect, not Fraenkel asymmetry, Hausdorff distance, or transport distance.
- The explicit constant is not claimed optimal.
- Very recent neighboring results leave a residual risk of concurrent unindexed endpoint stability work.

## Independent checks

```json
{
  "central_tangent_inequality_dense_grid": true,
  "minimum_grid_residual": -2.22e-16,
  "constant_chain_recomputed": true,
  "source_tree_unchanged": true
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation was performed. Open-access/preprint sources were checked first. The scientific conclusions above are independent of the record's same-model review.
