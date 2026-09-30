# Morse-Bott selection for the cell-polarization localization clock

## Corrected scope

Niethammer, Röger and Velázquez, *Localization properties of a free boundary problem for cell polarization* (arXiv:2609.20609v1), derive the slow-time localization problem and characterize limiting cap measures. An earlier accepted SCOPE record, `2026/09/19/self-similar-localization-cell-polarization-slow-flow--76b7ab9743ed`, already records the concentration clock `t G(omega(t)) -> 1`, its regular-variation inversion, and the resulting temporal laws for isolated homogeneous maxima. Those clock statements are used here as prior internal input and are **not** claimed as a new contribution of this record.

The new content retained here is the extension of that cap geometry to clean Morse-Bott maximum manifolds and the resulting selection rule, curve-specific scaling, and uniqueness of the geometric cap limit.

## Setting

Let `h=(g_max-g)/g_max >= 0` on a smooth two-dimensional membrane `Gamma`, and let

`G(s)=int_Gamma (s-h)_+ d sigma`.

For the infinite-cytosolic-diffusion slow-time problem, the known clock gives `t G(omega(t)) -> 1`. The source's subsequential long-time description identifies limiting measures through normalized positive-part caps.

## Morse-Bott cap asymptotics

Assume the maximum set `M={h=0}` is a finite disjoint union of compact embedded Morse-Bott components. For a component `M_j` of dimension `d_j in {0,1}`, let `q_j=2-d_j` be its normal codimension and let `H_j^perp` be the positive normal Hessian of `h`. Quadratic normal coordinates give

`int_{tube(M_j)} (s-h)_+ d sigma ~ K_{q_j} s^(1+q_j/2) int_{M_j} (det H_j^perp)^(-1/2) dvol`,

where

`K_q = 2^(1+q/2) Vol(B_q)/(q+2)`.

Thus `K_1=4 sqrt(2)/3` and `K_2=pi`. Components of smallest normal codimension dominate the cap mass. In particular, if any maximum curve is present, isolated nondegenerate maxima are lower order.

For maximum curves, with scalar normal Hessian `kappa`,

`C_curve=(4 sqrt(2)/3) int_M kappa^(-1/2) d ell`,

so `G(s)~C_curve s^(3/2)`. Combining this with the already-established clock yields

`omega(t)~(C_curve t)^(-2/3)`,

and the normal support thickness is order `omega(t)^(1/2)=t^(-1/3)`. The corresponding multiplier correction has order `t^(-2/3)` with the usual monotone-density prefactor inherited from the clock analysis.

If all maxima are isolated and nondegenerate, the familiar codimension-two coefficient is

`C_point=pi sum_j (det H_j)^(-1/2)`,

recovering the isolated-maxima formula already covered by the earlier SCOPE clock record.

## Limiting-measure selection

Define

`nu_s = (s-h)_+ d sigma / G(s)`.

The same tubular calculation shows that `nu_s` converges weakly to a probability measure supported on the Morse-Bott components of smallest normal codimension, with density

`d nu proportional to (det H^perp)^(-1/2) dvol_M`.

Hence maximum curves, when present, receive all limiting mass and are weighted by `kappa^(-1/2)` along arc length; isolated maxima then receive zero limiting mass. If only isolated nondegenerate maxima occur, the weights reduce to the familiar inverse-square-root Hessian weights.

Combining this unique small-cap limit with the cap-measure characterization in the primary source removes subsequence ambiguity under the stated Morse-Bott geometry. For the finite-diffusion slow-time problem this statement concerns the limiting-measure selection only; the explicit temporal clock is not asserted there.

## Verification example

On the unit sphere, take `h=z^2/2`. The maximum set is the equator, its normal Hessian is one, and its length is `2 pi`. Direct integration gives

`G(s)=(8 pi sqrt(2)/3) s^(3/2)`

for small `s`, exactly matching the formula above. Therefore `omega(t)` has the asymptotic scale `(8 pi sqrt(2)t/3)^(-2/3)` and the normal width is of order `t^(-1/3)`.

## Originality boundary

The concentration clock, regular-variation inversion, and isolated-maxima temporal laws are credited to the earlier accepted SCOPE record `2026/09/19/self-similar-localization-cell-polarization-slow-flow--76b7ab9743ed`. General Morse-Bott tubular/Laplace asymptotics and inverse-Hessian weighting are classical and are not claimed as new in isolation. The contribution of this record is the source-specific combination with the cell-polarization cap characterization: dominant-component selection on a maximum manifold, the continuous inverse-normal-Hessian limiting density, and the resulting curve localization regime.

## Limitations

The temporal exponents use the infinite-cytosolic-diffusion concentration clock. The finite-diffusion extension is only a limiting-measure statement. The geometry must be Morse-Bott with compact smooth components and positive normal Hessian; singular, intersecting, boundary, or degenerate maximum sets may have different asymptotics.

## References

- B. Niethammer, M. Röger, J.J.L. Velázquez, *Localization properties of a free boundary problem for cell polarization*, arXiv:2609.20609v1 (2026), https://arxiv.org/abs/2609.20609v1
- P. Ievlev, *Laplace Asymptotics near Stratified Minimum Sets*, arXiv:2608.02626v1 (2026), https://arxiv.org/abs/2608.02626v1
