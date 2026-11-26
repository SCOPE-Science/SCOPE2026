# Exact area of the seven-preimage target region for a harmonic cubic

## Finding

For the harmonic polynomial \(F(z)=z^3-\overline z^{\,2}\), let \(U_7\) be the set of regular targets with exactly seven distinct preimages. This set is a bounded, connected open set with fivefold rotational symmetry. More precisely, it is a punctured radial domain: there is a positive continuous radial function \(\rho\) such that
\[
U_7=\{re^{i\phi}:0<r<\rho(\phi)\}.
\]
The filled domain \(U_7\cup\{0\}\) is star-shaped about zero. The boundary of \(U_7\) consists of the isolated point \(0\) together with five smooth caustic arcs that join at five transverse double points of the caustic. Its planar Lebesgue area is
\[
\operatorname{area}(U_7)=\frac{160}{243}\left(\arccos\frac14-\frac{2\pi}{5}+\frac{\sqrt{15}}{64}\right)=0.0803255144042085\ldots.
\]
For \(F_b(z)=z^3-b\overline z^{\,2}\), \(b>0\), the analogous regular-target area is \(b^6\operatorname{area}(U_7)\).

## Assumptions and scope

The Jacobian is \(9|z|^4-4|z|^2\), so the critical points are zero and the circle of radius \(2/3\). Regular targets omit all images of those points, including the origin. Counts are without multiplicity. The result concerns this harmonic cubic and its positive-coefficient rescalings.

## Proof

**Caustic and winding.** The image of the critical circle is
\[
C(t)=\frac8{27}e^{3it}-\frac49 e^{-2it}=\frac4{27}e^{-2it}(2e^{5it}-3),\qquad t\in\mathbb R/(2\pi\mathbb Z).
\]
It avoids zero, and its argument decreases strictly through two full turns in one period: the second factor in parentheses winds zero times about zero, and
\[
\operatorname{Im}(\overline C C')=-\frac{32}{243}(1+\cos5t)
\]
is negative except at isolated parameters. Thus every ray has exactly two intersections counted by parameter, even if both parameters give the same image. On an outward radial ray, the winding about the target is minus the number of those intersections farther from zero than the target. This follows by counting signed crossings of the ray from the target to infinity, and extends to rays with a nontransverse crossing by continuity at any target off the caustic. As a multiset, the two radii vary continuously locally in angle by strict monotonicity of the lifted polar angle; their minimum \(\rho\) is positive and continuous.

The proper map \(F\) has degree three: on a sufficiently large circle the leading term dominates both the conjugate-quadratic term and any fixed target. All regular preimages in the open disk of radius \(2/3\) reverse orientation; all others preserve it. The degree in the disk equals \(\operatorname{wind}(C,w)\), so the negative count is \(-\operatorname{wind}(C,w)\), and the total count is \(3-2\operatorname{wind}(C,w)\). Consequently the regular seven-preimage set is the radial region inside both intersections, with zero deleted. Near zero, it has two orientation-reversing preimages in the disk and five orientation-preserving preimages outside. The deletion leaves the domain connected but introduces the isolated boundary point; no point of the punctured domain is a star center, since its antipodal ray also has points in the domain.

**Double points and the inner arcs.** For two distinct parameters with the same image, choose their midpoint \(m\) and half-separation \(0<h\le\pi/2\) on a shorter parameter arc. The equality reduces to
\[
2e^{5im}\sin(3h)+3\sin(2h)=0.
\]
Dividing by \(2\sin h\) and writing \(x=\cos h\) gives \(e^{5im}(4x^2-1)+3x=0\). Hence \(|4x^2-1|=3x\), and the only solution in \([0,1)\) is \(x=1/4\); it forces \(e^{5im}=1\). Set \(h_0=\arccos(1/4)\). The pair \(\pm h_0\) gives the image \(5/27\), and the other four double points are its rotations by \(e^{6\pi i j/5}\), by the covariance \(C(t+2\pi/5)=e^{6\pi i/5}C(t)\). At \(h_0\), \(C'=(5\sqrt{15}-25i)/18\), and at \(-h_0\) the derivative is the negative conjugate of that vector. The two tangents are nonparallel; rotation propagates this transversality.

Let \(\delta=h_0-2\pi/5>0\). The images of \(-\delta\) and \(\delta\) are the double points on the rays of angles \(6\pi/5\) and \(4\pi/5\), respectively. The arc between them through \(t=0\) traverses precisely the sector between these rays containing the negative real axis, by strict monotonicity and the continuous lift of the argument. On the negative real ray the two parameters are \(0\) and \(\pi\); the radii there are \(4/27\) and \(20/27\). Thus the arc through \(t=0\) supplies the smaller radius on that ray. By continuity it stays smaller up to the sector endpoints, since radii can exchange order only at a double point. The other sectors are the four rotations of this sector. In each sector the arc is smooth (the zeros of \(C'\) lie at \(5t=\pi\bmod 2\pi\), off the selected arcs). These five arcs form the outer boundary of \(U_7\).

**Area.** Apply Green's theorem to the filled domain, whose area equals that of the punctured domain. Increasing \(t\) traverses the selected arcs clockwise, so
\[
\operatorname{area}(U_7)=-\frac52\int_{-\delta}^{\delta}\operatorname{Im}(\overline C C')\,dt=\frac{160}{243}\left(\delta+\frac{\sin(5\delta)}5\right).
\]
Here \(\sin(5\delta)=5\sqrt{15}/64\) follows from the quintuple-angle identity and \(\cos h_0=1/4\). Finally, \(F_b(bu)=b^3F(u)\) maps the regular seven-preimage regions by the target dilation \(b^3\), which scales area by \(b^6\).

## Reproducibility

The same caustic parametrization and area integral can be corroborated numerically by inverting the two branches of the lifted angle and integrating one-half the square of their smaller radius over a full turn. A periodic midpoint grid of 4,000 evenly spaced rays with bisection for both radii gives approximately \(0.0803254871\). This is a numerical comparison only; the proof uses exact intersection classification and exact integration.

## Relationship to prior work and limitations

Winding of critical-image curves already gives zero counts for families of harmonic trinomials; that counting machinery and the occurrence of seven distinct roots are not the contribution here. The exact area uses the smaller radial envelope and counts a fixed map's regular target locus, not a multiplicity-weighted image area. The argument uses this specific caustic and does not establish areas for general harmonic polynomials. Historical priority for this particular area expression remains subject to mathematically equivalent caustic-cell calculations in the literature.

## References

1. M. Brilleslyper, J. Brooks, M. Dorff, R. Howell and L. Schaubroeck, *Zeros of a one-parameter family of harmonic trinomials*, Proc. Amer. Math. Soc. Ser. B **7** (2020), 82–90, DOI 10.1090/bproc/51.
2. J. Brooks, M. Dorff, A. Hudson, E. Pitts, C. Whiffen and A. Woodall, *Zeros of a Family of Complex-Valued Harmonic Trinomials*, Bull. Malays. Math. Sci. Soc. **45** (2022), 1079–1091, DOI 10.1007/s40840-021-01230-8.
