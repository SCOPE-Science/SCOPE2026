# Review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**PASS.** The source paper supplies the exact bounded-mark intensity expansion, the fact that any correct shift equals \(\log\rho^d+o(\log\rho^d)\), and a Poisson-process approximation for large-inradius exceedances. The first mark-sensitive coefficient simplifies exactly to \(d(v_d\gamma)^{2/d}\). On the proposed endpoint scale \(m=A-y/a_{d,\rho}\), its exponent changes by \(-2Ay+o(1)\), while every higher mark-dependent term changes by \(o(1)\). Fixed-distance marks are exponentially suppressed. Karamata's Laplace–Stieltjes theorem then converts the endpoint law \(\mathbb P(A-M\le y)\sim Cy^\kappa\) into the Gamma(shape \(\kappa\), rate \(2A\)) tilted limit. The source Poisson-approximation argument is unaffected by deterministic relabeling of the output mark, so the refined intensity convergence lifts to the stated marked Poisson-process convergence. The maximum-cell corollary follows from the unique top point of the limiting Poisson process.

For \(d=3\), substituting the endpoint Laplace asymptotic into the source paper's exact equation (1.7) gives the displayed centering. The claimed \(+\log\gamma\) correction to v1 equations (3.23) and (3.24) follows algebraically from (1.7); in the discrete case it is also required by the constant-mark Poisson–Voronoi specialization. A standalone high-precision verification checks the endpoint Laplace constants, the Gamma Laplace transform, and the constant discrepancy in the continuous example.

## Originality

**PASS, to the best of our knowledge, with a narrow claim.** Schulte–Švarc Petráková (arXiv:2609.20750v1) prove the first-order large-inradius point-process limit and, for bounded marks in \(d\ge3\), only the degenerate unscaled mark limit at the endpoint \(A\). Their theorem and Poisson approximation are not claimed. Classical Karamata theory supplies the endpoint Laplace asymptotics and is not claimed. Calka–Chenavier and later Poisson–Voronoi work cover the constant-mark extreme-radius problem and are not claimed.

Searches for Poisson–Laguerre extremal-mark endpoint scaling, Gamma limits, and second-order bounded-mark refinements found no equivalent result. Lautensack–Zuyev (2008) is the main older Laguerre reference; its accessible abstract concerns geometric characteristics, typical faces, contact distributions and convergence to Poisson–Voronoi tessellations, not large-inradius endpoint-mark extremes. The complete text was not inspected here, so it remains the clearest residual originality risk. Generic exponential-tilting and regular-variation theory could imply the scalar Gamma tilt abstractly, but the claimed novelty is its all-dimensional Poisson–Laguerre extremal-process realization, independence from the Gumbel height, the explicit scale, and the consequent centering refinement.

The two source-example constant corrections are elementary consequences of the source's own equation (1.7); they are useful errata-level observations rather than the main originality claim.

## Value

**PASS.** The result resolves information that is lost in the source paper's degenerate \(\delta_A\) mark limit. It identifies the exact logarithmic concentration scale, recovers the endpoint-tail exponent as a non-degenerate Gamma law, and shows that the refined extremal mark asymptotically decouples from both location and Gumbel height. The \(d=3\) corollary turns endpoint regularity into an explicit \(-\kappa\log\log\rho^3/3\) centering correction and also catches a constant-level inconsistency in two displayed examples.

## Limitations

- Bounded marks with a regularly varying right endpoint \(Cy^\kappa\), \(\kappa>0\), only; endpoint atoms and non-regular endpoints need separate treatment.
- The refined Gamma law is stated for \(d\ge3\); the planar bounded-mark regime is different.
- No quantitative convergence rate is claimed.
- The result inherits the geometric model and Poisson-approximation framework of arXiv:2609.20750v1.
- The complete Lautensack–Zuyev (2008) text was not inspected; only its abstract and descriptions in later sources were checked.
- Cross-model review has not been performed.
