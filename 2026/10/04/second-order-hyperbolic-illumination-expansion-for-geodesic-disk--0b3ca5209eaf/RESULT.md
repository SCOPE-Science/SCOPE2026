# Second-order hyperbolic illumination expansion for geodesic disks
## Finding
For every \(r>0\), let \(B_r\) be the geodesic disk of radius \(r\) in the hyperbolic plane of constant curvature \(-1\), and let \(\mathcal I_\delta(B_r)\) denote its illumination body. Write \(\tau=\tanh r\). Then, as \(\delta\downarrow0\),
\[
\operatorname{area}(\mathcal I_\delta(B_r))-\operatorname{area}(B_r)
=C_1(r)\delta^{2/3}+C_2(r)\delta^{4/3}+O_r(\delta^2),
\]
with
\[
C_1(r)=\pi 3^{2/3}(\sinh r)^{2/3}(\cosh r)^{1/3}
\]
and
\[
C_2(r)=\frac{\pi 3^{4/3}\cosh r}{20\,\tau^{2/3}}\bigl(\tau^2+8\bigr).
\]
In particular, the first correction beyond the known leading term is positive for every \(r>0\).

Equivalently, if symmetry is used to write \(\mathcal I_\delta(B_r)=B_{r+\varepsilon_\delta}\), then
\[
\varepsilon_\delta=A_r\delta^{2/3}+\frac{\tau^2+3}{10\tau}A_r^2\delta^{4/3}+O_r(\delta^2),
\qquad
A_r=\frac{3^{2/3}}{2\tau^{1/3}}.
\]

## Assumptions and scope
The ambient surface is \(\mathbb H^2\) with sectional curvature exactly \(-1\). The radius \(r\) is fixed and positive while \(\delta\) tends to zero through positive values. The illumination body is the standard geodesic-convex-hull illumination body: a point belongs to \(\mathcal I_\delta(B_r)\) when the hyperbolic area added by adjoining it to \(B_r\) is at most \(\delta\). The remainder constant may depend on \(r\). No assertion is made here for arbitrary convex bodies, higher dimensions, or variable curvature.

## Proof
The cited projective-geometry source proves that illumination bodies of geodesic balls are geodesic balls. Fix a boundary-exterior point \(P\) at distance \(r+\varepsilon\) from the center \(O\), and let \(T\) be one of the two tangency points of the geodesics from \(P\) to \(B_r\). Set \(\alpha=\angle POT\), and let \(\gamma\) be the complement of \(\angle OPT\). Hyperbolic right-triangle identities give
\[
\cos\alpha=\frac{\tanh r}{\tanh(r+\varepsilon)},
\qquad
\cos\gamma=\frac{\sinh r}{\sinh(r+\varepsilon)}.
\]
The added region is the union of two right triangles minus the disk sector of central angle \(2\alpha\). Since a hyperbolic right triangle with acute angles \(\alpha\) and \(\beta\) has area \(\pi/2-\alpha-\beta\), while a disk sector of angle \(2\alpha\) and radius \(r\) has area \(2\alpha(\cosh r-1)\), the added area is exactly
\[
\delta(\varepsilon)=2\gamma-2\cosh r\,\alpha.
\]
Taylor expansion of the two inverse-cosine expressions at \(\varepsilon=0\) has cancellation at orders \(\varepsilon^{1/2}\), and yields
\[
\delta(\varepsilon)
=L_r\varepsilon^{3/2}+M_r\varepsilon^{5/2}+O_r(\varepsilon^{7/2}),
\]
where
\[
L_r=\frac{2\sqrt{2\tau}}{3},
\qquad
M_r=-\frac{\sqrt2(\tau^2+3)}{10\sqrt\tau}.
\]
Series inversion therefore gives
\[
\varepsilon_\delta
=L_r^{-2/3}\delta^{2/3}
+\frac{\tau^2+3}{10\tau}L_r^{-4/3}\delta^{4/3}
+O_r(\delta^2).
\]
Because \(L_r^{-2/3}=3^{2/3}/(2\tau^{1/3})=A_r\), this is the radius expansion stated above.

Finally,
\[
\operatorname{area}(B_s)=2\pi(\cosh s-1).
\]
Expanding this at \(s=r\), substituting the radius expansion, and collecting the \(\delta^{2/3}\) and \(\delta^{4/3}\) terms gives exactly \(C_1(r)\) and \(C_2(r)\) displayed in the finding.

## Verification
The leading coefficient provides an independent normalization check. In dimension two the published theorem has \(c_2=3^{2/3}/2\). A geodesic circle of radius \(r\) has boundary length \(2\pi\sinh r\) and geodesic curvature \(\coth r\), so its floating area is \(2\pi\sinh r\,(\coth r)^{1/3}\). Multiplication by \(c_2\) reproduces precisely \(C_1(r)\).

The accompanying `verify.py` evaluates the exact cap formula and the two asymptotic formulas at several radii and shrinking positive increments using only the Python standard library. It checks the predicted \(\varepsilon^{3/2}\) and \(\varepsilon^{5/2}\) cap terms and the \(\delta^{2/3}\) and \(\delta^{4/3}\) area terms. These numerical checks are consistency tests; the universal claim rests on the analytic identities and Taylor-series argument above.

## Relationship to prior work
Assouline, Besau, and Werner prove the leading-order illumination-volume asymptotic in constant-curvature spaces and state that illumination bodies of geodesic balls remain geodesic balls, with the new radius determined implicitly by the added cap volume. Their theorem gives only the \(\delta^{2/3}\) term in dimension two, while their ball example leaves the radius relation implicit. Assouline, Schütt, and Werner subsequently extend the leading-order formula to Riemannian manifolds and explicitly describe the established illumination-volume result as a leading-order expansion. The second coefficient above is not implied by those first-order limit statements; obtaining it requires the next nonzero term after the square-root cancellation in the exact hyperbolic cap geometry.

The coefficient also sharpens the canonical model against which a future general second-order Riemannian illumination expansion would have to specialize. Its explicit dependence on \(\tanh r\) records ambient-curvature effects that are invisible in the first-order exponent alone.

## Limitations
The result is restricted to geodesic disks in \(\mathbb H^2\) of curvature \(-1\). It does not provide a second-order formula for nonsymmetric convex bodies, does not address higher-dimensional balls, and does not identify a general curvature-measure invariant producing the second term. The literature comparison cannot exclude an unindexed older computation of the same special-family coefficient, although targeted statement-level searches and inspection of the closest primary sources found no such formula.

## References
1. R. Assouline, F. Besau, E. M. Werner, *Illumination Bodies in Projective Geometries*, arXiv:2605.25122v1 (2026). Theorem 1.2 and Example A.2.
2. R. Assouline, C. Schütt, E. M. Werner, *Illumination bodies on Riemannian manifolds*, arXiv:2606.21112v1 (2026).
3. E. Werner, *Illumination bodies and affine surface area*, Studia Mathematica 110 (1994), 257–269.
