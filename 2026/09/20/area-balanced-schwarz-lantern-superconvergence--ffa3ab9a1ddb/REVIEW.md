# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The exact Schwarz-lantern area formula reduces the problem to the
one-variable expression
\[
Q_{m,n}
=
\frac{\sin x}{x}
\sqrt{1+(R m/H)^2(1-\cos x)^2},
\qquad x=\pi/n.
\]
For fixed \(n\), this is strictly increasing in \(m>0\), begins below \(1\),
and tends to infinity, so the exact balance point exists uniquely and is
obtained by direct algebra. The displayed asymptotic coefficients were
checked by direct Taylor expansion of the exact formula. The
generic linear-regime coefficient vanishes at one and only one positive
slope, \(2H/(\sqrt3\pi R)\). Re-expansion at that slope gives the quartic
coefficient \(-11\pi^4/180\). Re-expansion at the exact balance point plus
a bounded perturbation \(\delta\) gives the cubic rounding term and the
stated uniform error order. Numerical substitutions at several \(n\)
agree with the signs and rates.

## Originality

**PASS, to the best of our knowledge.**

The classical facts are separated from the proposed contribution.
Kobayashi--Tsuchiya (2017) records the exact Schwarz-lantern area formula
and the classical convergence condition \(m/n^2\to0\); those are not
claimed as new. Brewin (2015) derives error bounds for the ordinary lantern
and obtains a fourth-order estimate after replacing the Euclidean edge
lengths by curvature-corrected ones; that is a different estimator, not an
aspect-ratio optimization of the ordinary lantern. Lachaud--Romon--Thibert--
Coeurjolly (2020) treats difficult polygonal meshes in corrected-curvature
estimation.

Searches were made under *Schwarz lantern*, *Schwarz polyhedron*, *Chinese
lantern*, *surface-area approximation*, *area error*, *convergence rate*,
*optimal aspect ratio*, *balanced triangulation*, *superconvergence*, and
equivalent formulations of the exact-area equation and its leading
constant. No located source states the finite-\(n\) exact balance point,
the unique bias-cancelling linear slope, the quartic cancellation, or the
integer cubic rounding law.

Residual originality risk remains: all claims are elementary consequences
of the classical closed formula, so an equivalent observation may occur in
older approximation-theory, numerical-analysis, or finite-element
literature under different terminology.

## Value

**PASS.**

The result turns the Schwarz lantern from a qualitative pathology into a
quantitatively tunable benchmark. It gives an exact finite-resolution
under/over-estimation boundary and a distinguished mesh aspect ratio that
improves the generic linear-regime area error from quadratic to quartic in
the real relaxation. The integer version gives a practical cubic error
law and an \(O(F^{-3/2})\) area rate in the number of faces.

## Limitations

- Only the standard staggered cylindrical Schwarz lantern is treated.
- Only total lateral area is optimized; no claim is made for curvature,
  normals, Hausdorff distance, or element quality.
- Exact equality uses a real band-count relaxation; integer meshes use the
  quantified rounding result.
- Originality is to the best of our knowledge; elementary-derivation
  folklore risk remains.

## Sources checked

- K. Kobayashi and T. Tsuchiya, *Approximating surface areas by
  interpolations on triangulations*, Japan J. Ind. Appl. Math. 34 (2017),
  509--530. https://doi.org/10.1007/s13160-017-0253-0
  and https://arxiv.org/abs/1610.06054
- L. Brewin, *Curvature corrected estimates for geodesic arc-length*,
  arXiv:1512.03461 (2015). https://arxiv.org/abs/1512.03461
- J.-O. Lachaud, P. Romon, B. Thibert, D. Coeurjolly,
  *Interpolated corrected curvature measures for polygonal surfaces*,
  Computer Graphics Forum 39 (2020), 41--54.
  https://doi.org/10.1111/cgf.14067
