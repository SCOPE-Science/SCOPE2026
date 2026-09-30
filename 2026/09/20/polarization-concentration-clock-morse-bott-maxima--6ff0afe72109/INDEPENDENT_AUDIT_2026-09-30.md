# Independent Audit — 2026-09-30

**Record:** `2026/09/20/polarization-concentration-clock-morse-bott-maxima--6ff0afe72109`  
**Title:** A concentration clock and Morse-Bott selection for cell-polarization localization  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `1fd003540d59fb215bc6e10b60a61b70f8b17e1a`  
**Disposition:** **REPAIRED**

## Three-axis assessment

- **Correctness — PASS:** The concentration-clock argument and Morse-Bott calculations are mathematically sound. From u=[u0+B(omega-h)]_+, the pointwise bound 0<=[u0+q]_+-q_+<=u0, A(t)=o(t), and the measure-zero maximum set give B(t)G(omega(t))->1 and hence tG(omega(t))->1. For a Morse-Bott component of normal codimension q, direct quadratic-normal integration gives K_q=2^(1+q/2)Vol(B_q)/(q+2), so K_1=4sqrt(2)/3 and K_2=pi; the smallest normal codimension dominates and the normalized cap measure has density proportional to (det H_perp)^(-1/2). The curve exponents t^(-2/3) for the threshold and t^(-1/3) for normal width follow correctly.
- **Originality — PASS_WITH_REPAIR:** The filed package overstates novelty of the concentration clock and isolated-maximum temporal laws: the already accepted SCOPE record `2026/09/19/self-similar-localization-cell-polarization-slow-flow--76b7ab9743ed` contains the same tG(sigma)->1 clock, regular-variation rates, and isolated-maxima consequences. The genuinely distinct contribution here is the Morse-Bott maximum-manifold extension: continuous selection on maximum curves/manifolds, inverse-normal-Hessian density, and the curve-specific 2/3 and 1/3 exponents. The primary Niethammer–Röger–Velázquez preprint treats isolated homogeneous/nondegenerate maxima in its examples, while generic Morse-Bott tubular asymptotics are prior art. A repair narrowing the originality claim is therefore required.
- **Scientific value — PASS:** After narrowing, the maximum-manifold extension is scientifically useful: it identifies a localization regime qualitatively different from isolated maxima, including which components dominate, the limiting density along them, and new temporal/support exponents. The contribution is incremental rather than a second independent discovery of the clock.

## Independent findings
- The core clock and isolated-maxima rate package duplicates the earlier accepted SCOPE slow-flow record and should be treated as prior internal work, not a new contribution of this record.
- For normal codimension q, the exact cap constant is 2^(1+q/2)Vol(B_q)/(q+2); this reproduces 4sqrt(2)/3 for curves and pi for isolated points on a two-dimensional membrane.
- If curve maxima and isolated maxima coexist, curve components dominate because their cap mass is order s^(3/2), versus s^2 for isolated nondegenerate points.
- The normalized cap measures converge to density proportional to (det H_perp)^(-1/2) on the dominant Morse-Bott components; this is the surviving record-specific refinement.

## Independent checks
- Re-derived the cap-clock limit from the exact positive-part representation and mass conservation.
- Integrated (s-|y|^2/2)_+ in dimensions q=1 and q=2 and checked all constants.
- Checked regular-variation inversion p=3/2 and the induced t^(-2/3), t^(-1/3) curve scales.
- Compared the claim against the earlier accepted SCOPE slow-flow record and against the primary arXiv preprint scope.

## Literature evidence
- https://arxiv.org/abs/2609.20609 — Niethammer, Röger and Velázquez (2026), primary slow-time localization preprint; its worked asymptotic examples concern isolated maxima rather than Morse-Bott maximum manifolds.
- https://arxiv.org/abs/2608.02626 — Ievlev (2026), recent treatment of Laplace asymptotics near Morse-Bott/stratified minimum sets; generic tubular inverse-Hessian weighting is prior art.

## Limitations
- The clock is for the spatially uniform-multiplier/infinite-cytosolic-diffusion slow-time problem; the finite-diffusion statement is only the limiting-measure selection inherited through the source cap characterization.
- Morse-Bott formulas require clean compact smooth components with positive normal Hessian; singular intersections and degenerate normal directions are outside scope.
- The repaired originality claim credits the earlier SCOPE clock record and claims novelty only for the source-specific Morse-Bott extension.

The assigned source tree remained unchanged from the source-tree-check interval through current main commit `eff2c6312cec5b0dee5115e5f42211a853092dfb`; the exact tree audited is `1fd003540d59fb215bc6e10b60a61b70f8b17e1a` and matches the assignment guard. GitHub was used only as read-only evidence; no repository writes were made. Audit timestamps and this audit-file date use UTC under the task-specific audit contract.
