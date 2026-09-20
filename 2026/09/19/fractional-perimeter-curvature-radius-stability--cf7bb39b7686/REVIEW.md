# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**  The proof quantitatively strengthens the convex mechanism in
arXiv:2609.19052 without changing its sign structure.  On the central increment
window \(w\in[\pi/2,3\pi/2]\), the tangent-chord function
\(\phi(x)=2\sin(x/2)\) has the uniform quadratic supporting-line deficit
\[
\phi(w)+\phi'(w)(x-w)-\phi(x)
\ge \frac{\sin(\pi/8)}8(x-w)^2.
\]
The bound follows directly from the Taylor remainder after restricting to the
half-segment adjacent to \(w\).  After averaging, the linear term cancels
because the mean tangent-angle increment is exactly \(w\).

The source degree estimate and Hölder step then convert this tangent deficit
into a fractional-Willmore deficit.  The constants were recomputed from
\[
(2\pi)^{1+\alpha}(4\pi)^{-1-\alpha}=2^{-1-\alpha}
\]
and from the factor \(1/2\) in the source representation of \(W_\alpha\).
The Fourier calculation is exact:
\[
\min_{k\ne0}\int_{\pi/2}^{3\pi/2}(1-\cos kw)\,dw
=\pi-\frac23,
\]
with the minimum at \(|k|=3\).  This yields
\[
W_\alpha(K)-W_\alpha(B_1)
\ge
\frac{\alpha(\pi-\frac23)\sin(\pi/8)}{2^{4+\alpha}}D(K).
\]

For the normalized outer parallel body
\(\widetilde K_r=(K+rB_1)/(1+r)\), the curvature-radius formula is exact:
\[
\rho_r=(\rho+r)/(1+r).
\]
Changing from tangent angle to normalized arclength gives
\[
D(\widetilde K_r)
=
(1+r)^{-2}
\inf_b\int|h-b|^2\rho_r\,d\vartheta
\ge r(1+r)^{-3}\|\rho-1\|_{\dot H^{-1}}^2.
\]
Combining this with the homogeneity of \(W_{1-q}\), the first-variation formula
for \(C_q\), and the source asymptotic for outer parallel bodies gives the
stated chord constant because
\[
\int_0^\infty r(1+r)^{q-3}\,dr
=\frac1{(1-q)(2-q)}.
\]
Finally, the exact convex identity
\(P_s=[s(1-s)]^{-1}C_{1-s}\) gives the fractional-perimeter constant.

Adversarial checks included the direction of every deficit, the normalization
of the Fourier/primitive norm, invariance under the angular origin, the
parallel-body change of variables, all powers of \(1+r\), and the substitutions
\(\alpha=1-q\) and \(q=1-s\).  The estimate vanishes only when
\(\rho\equiv1\), as required.

## Originality

**PASS, to the best of our knowledge.**  The direct source
arXiv:2609.19052 proves the sharp planar fixed-perimeter inequality and develops
the chord-functional, fractional-Willmore and outer-parallel-body identities,
but no quantitative deficit is stated.  The independent recent solution
arXiv:2609.14513 proves the same fixed-perimeter maximization in a larger class;
no curvature-radius stability estimate was located there.

The closest explicit stability result found is
Alberti--Cozzi--Massaccesi--Mirmina, arXiv:2605.07543.  Its stated theorem is
local for nearly spherical sets and compares two fractional perimeters with
\(0<s<t<1\); the classical-perimeter endpoint \(t=1\) is outside the stated
parameter range.  Döhrer--Dohmen, arXiv:2604.02042, proves disk minimality for
fractional Willmore energies among convex planar sets, but a quantitative
deficit of the form used here was not located.  Blatt--Giacomin--Scheuer--
Schikorra, arXiv:2306.16941, studies a different subcritical fractional
curvature energy and proves a different sphere-stability statement.

Targeted searches used the recent source identifiers and equivalent
combinations involving fixed perimeter, fractional perimeter, chord functional,
fractional Willmore, curvature radius, negative Sobolev/H^{-1} control, and
outer parallel bodies.  The current SCOPE archive was searched by the same
objects and claim families.  No matching result was located.

Residual risk remains because the two fixed-perimeter solutions are extremely
recent and concurrent refinements may not yet be indexed.  There is also a
possibility that an endpoint limit of a different quantitative stability
framework implies a related local estimate, although no source was found that
states the global convex estimate or the explicit constants recorded here.

## Value

**PASS.**  The result upgrades a newly solved sharp inequality from
maximality/rigidity to a global quantitative statement in a natural smooth
convex class.  The curvature-radius \(\dot H^{-1}\) metric is intrinsic to the
parallel-body argument, the constants are explicit, and the proof simultaneously
produces a quantitative stability inequality for the chord functional.  The
argument also isolates a reusable mechanism: a uniform quadratic Jensen deficit
for tangent-angle increments propagates through a nonlocal curvature variation
to a global deficit.

## Limitations

The theorem is restricted to \(C^\infty\) strictly convex planar bodies with
positive curvature.  No extension to arbitrary finite-perimeter sets, general
domains, nonsmooth convex bodies, or flat boundary pieces is asserted.  The
metric is curvature-radius \(\dot H^{-1}\), not Fraenkel asymmetry or Hausdorff
distance.  The explicit constants are not optimized and are not claimed sharp.
Unindexed concurrent work and non-obvious endpoint consequences of other
stability theories remain the main originality risks.
