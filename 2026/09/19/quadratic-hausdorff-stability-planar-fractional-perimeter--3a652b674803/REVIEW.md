# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The proof was checked at the level of the four structural steps needed for the theorem.

1. **Quantitative Willmore gap.** The source proof of the sharp fractional Willmore-type inequality was read at the level of its tangent-angle identity, degree lower bound, Hölder step, and Jensen step. Keeping the Jensen deficit on a fixed middle interval of chord parameters gives a quadratic \(L^2\) control of the tangent-angle increment. A Fourier spectral gap on that interval converts this to
   \[
   W_\alpha(K)-W_\alpha(B_1)\gtrsim_\alpha
   \inf_c\int|\theta(u)-u-c|^2\,du.
   \]
   The endpoint singularities of \(\sin(w/2)^{-\alpha}\) are avoided by using only \(w\in[\pi/2,3\pi/2]\).

2. **Parallel-body transfer.** For a perimeter-\(2\pi\) smooth strictly convex body, writing the radius of curvature as \(\rho\) and
   \[
   F(\beta)=\int_0^\beta(\rho-1)
   \]
   gives an exact formula for the tangent-angle defect of \((K+rB_1)/(1+r)\). On \(1\le r\le2\) this defect is bounded below by a fixed multiple of
   \[
   J(K)=\inf_b\int|F-b|^2.
   \]
   Combining this with the established scaling of \(W_s\) and the established first variation
   \[
   \frac{d}{dr}C_q(K+rB_1)=2qW_{1-q}(K+rB_1)
   \]
   yields a chord-functional deficit bounded below by \(J(K)\). The sign is consistent with the known sharp chord inequality because
   \(C_q(K+rB_1)\le C_q(B_{1+r})\).

3. **Hausdorff conversion.** The support-function Fourier relation
   \[
   \rho_k=(1-k^2)h_k
   \]
   gives
   \[
   J(K)=2\pi\sum_{|k|\ge2}\frac{(k^2-1)^2}{k^2}|h_k|^2.
   \]
   Translation occupies only the \(k=\pm1\) modes, and the weight above dominates a fixed multiple of the \(H^1\) weight for \(|k|\ge2\). Sobolev embedding on the circle and the support-function formula for Hausdorff distance then give the claimed squared Hausdorff control.

4. **Nonsmooth bodies and scaling.** The cited source proves smooth strictly convex Hausdorff approximation together with continuity of perimeter and chord functional. Passing to the limit is therefore valid. Scaling gives the factor \(R^{-s}\), which has the correct homogeneity:
   \(R^{-s}d_H^2\) and \(P_s\) both have dimension \(2-s\).

The local sharpness family \(h_\varepsilon=1+\varepsilon\cos2\theta\) was also checked: its curvature radius is \(1-3\varepsilon\cos2\theta>0\) for \(|\varepsilon|<1/3\), its perimeter is exactly \(2\pi\), its translation-optimized Hausdorff distance to the unit disk is exactly \(|\varepsilon|\), and the cited chord-functional support perturbation formula has no linear term because \(\cos2\theta\) has zero mean. Hence the deficit is \(O_s(\varepsilon^2)\).

## Originality

**PASS, to the best of our knowledge.**

The closest sources inspected were:

- Lin–Yang–Yang–Yuan–Zhang, arXiv:2609.19052. Their full accessible text was checked for the sharp planar fractional-perimeter comparison, exact convex chord identity, fractional Willmore argument, first variation along outer parallel bodies, support-function perturbation expansion, and smooth convex approximation. The paper proves the sharp qualitative inequality but does not state the global quadratic Hausdorff deficit above.
- Frank–Ivanisvili, arXiv:2609.14513. The accessible paper/abstract states the sharp fixed-perimeter comparison for arbitrary planar finite-perimeter sets. Searches for stability/deficit formulations did not reveal a quantitative Hausdorff estimate.
- Alberti–Cozzi–Massaccesi–Mirmina, arXiv:2605.07543. This gives local quantitative stability for a ratio of two fractional perimeters \(0<s<t<1\) among nearly spherical sets. It does not cover the endpoint \(t=1\), global convex bodies, or the Hausdorff deficit above.
- Giannetti–Stefani, DOI 10.12775/TMNA.2024.019, gives Hausdorff lower bounds for differences of nonlocal perimeters of nested convex bodies. That is a different nested-monotonicity problem and does not imply the fixed-classical-perimeter disk-maximizer stability statement.
- Blatt–Giacomin–Scheuer–Schikorra, arXiv:2306.16941, studies a different fractional mean-curvature/Willmore-type energy and derives a small-energy sphere-stability statement. Its functional and hypotheses are different from the fixed-classical-perimeter fractional-perimeter deficit here.
- Döhrer–Dohmen, arXiv:2604.02042, proves disk minimality/rigidity for other nonlocal curvature energies among convex planar sets; no quantitative fixed-perimeter fractional-perimeter deficit of the present form was found.

Exact and synonymous searches included combinations of: fractional perimeter / classical perimeter, fixed perimeter, reverse fractional isoperimetric inequality, convex body, disk maximizer, quantitative stability, Hausdorff deficit, chord functional stability, fractional Willmore stability, and the recent source identifiers. No equivalent theorem or stronger result was found. Current SCOPE records were also searched by these objects and formulations without a collision.

Residual risk remains because the two direct sharp-comparison papers are very recent, and an equivalent convex-geometric estimate could appear under different terminology. No inaccessible paper produced concrete evidence of prior coverage.

## Value

**PASS.**

The result upgrades a newly solved sharp extremal inequality from qualitative equality information to a global quantitative geometric estimate on the natural convex class. It identifies a concrete coercive mechanism—tangent-angle Jensen deficit, outer-parallel transfer, and support-function spectral control—and establishes the locally optimal Hausdorff exponent \(2\). The result also supplies an endpoint counterpart, at classical perimeter \(t=1\), to recent local stability work for two fractional perimeters.
