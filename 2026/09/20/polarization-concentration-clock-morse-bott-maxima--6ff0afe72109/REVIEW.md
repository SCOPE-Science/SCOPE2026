# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The cap representation follows algebraically from the source representation after setting `A(t)=int_0^t varphi`, `B=t+A`, and `omega=A/B`. The clock law follows from mass conservation, `0 <= [u0+q]_+-q_+ <= u0`, `A=o(t)`, and dominated convergence under the source's measure-zero maximum-set hypothesis. Regular variation yields the threshold rate by inversion of `G`; the multiplier rate follows from the source's monotonicity of `alpha` by a standard monotone-density argument. The Morse-Bott coefficient follows from quadratic normal coordinates and direct integration of `(s-|y|^2/2)_+`; its codimension-two constant reproduces the source's isolated nondegenerate coefficient `pi/sqrt(det H)`.

The spherical verification example checks the curve coefficient, exact cap law, clock convergence, and multiplier prefactor using only the displayed mathematical equations.

## Originality

**PASS, narrowly scoped.** The primary source arXiv:2609.20609v1 was inspected through its reduced representation, monotonicity result, long-time concentration theorem, finite-diffusion analogue, and Section 4 examples. Section 4 specializes to finitely many isolated zeros of the signal deficit and computes isolated homogeneous/nondegenerate cases; no temporal localization rate is stated there.

General Morse-Bott and stratified minimum-set asymptotics are prior art. Ievlev, arXiv:2608.02626v1, explicitly describes the classical Morse-Bott quadratic-normal mechanism and broader stratified Laplace asymptotics. No originality claim is made for tubular/Morse-Bott integration itself, inverse-Hessian weighting as a general asymptotic principle, or regular-variation inversion in isolation.

Earlier papers on this cell-polarization free-boundary model were checked for scope: arXiv:2006.16155 derives the parabolic obstacle model and proves stability properties; arXiv:2202.06289 studies support continuity and jumps; arXiv:2402.03034 studies interface behavior; arXiv:2605.03553 studies stationary small-mass positivity-region shapes. These works do not provide the source-specific long-time concentration clock identified here.

The claimed contribution is restricted to: (i) the exact `B(t)G(omega(t))->1` and `tG(omega(t))->1` clock for the new slow-time reduced dynamics; (ii) the consequent explicit temporal exponents for the source's homogeneous maxima; and (iii) combining the source's cap-measure theorem with Morse-Bott geometry to obtain maximum-manifold selection and uniqueness of the limiting measure.

A residual priority risk remains that an equivalent clock identity may occur in earlier obstacle-problem literature under different variables. This does not affect correctness, but it could reduce novelty of the general clock mechanism. No absolute first-discovery claim is made.

## Value

**PASS.** The result converts the source's qualitative long-time concentration and subsequential cap characterization into quantitative temporal power laws and gives a geometrically distinct localization regime when the signal maximum is a curve rather than isolated points. The curve case changes both the threshold exponent (`2/3` instead of `1/2`) and the normal support-width exponent (`1/3` instead of `1/4`), and supplies a continuous limiting density along the maximum manifold.

## Limitations

The temporal clock and multiplier rates are proved for the infinite-cytosolic-diffusion slow-time reduced problem, not the finite-diffusion problem. The finite-diffusion conclusion here is only uniqueness and geometric identification of the limiting measure via the source's Theorem 3.12. The Morse-Bott result assumes clean smooth quadratic normal minima of the normalized signal deficit. It does not cover singular or intersecting maximum sets, degenerate normal Hessians, or the original unscaled bulk-surface PDE at fixed mass.
