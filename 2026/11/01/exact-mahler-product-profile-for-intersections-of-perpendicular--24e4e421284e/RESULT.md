# Exact Mahler-product profile for intersections of perpendicular ellipses

## Finding
For each \(t\ge1\), let
\[
E_t^{(x)}=\{(x,y):x^2/t^2+y^2\le1\},\qquad
E_t^{(y)}=\{(x,y):x^2+y^2/t^2\le1\},
\]
and put \(K_t=E_t^{(x)}\cap E_t^{(y)}\). These are congruent ellipses with perpendicular long axes and a common center. Writing \(\phi=\arctan(1/t)\), the exact area and polar area are
\[
|K_t|=4t\phi,\qquad
|K_t^\circ|=\frac{4\phi}{t}+2(1-t^{-2}).
\]
Consequently their Mahler products are
\[
\boxed{\mathcal M(t)=|K_t|\,|K_t^\circ|=16\phi^2+8(t-t^{-1})\phi.}
\]
The map \(t\mapsto\mathcal M(t)\) is strictly decreasing for \(t>1\), from \(\mathcal M(1)=\pi^2\) to the unattained limit \(8\). More precisely,
\[
\pi^2-\mathcal M(t)=4(t-1)^2+O((t-1)^3)\quad (t\downarrow1),
\]
\[
\mathcal M(t)-8=\frac{16}{3t^2}+O(t^{-4})\quad (t\to\infty).
\]
The limiting body is the square \([-1,1]^2\), whose polar is the unit diamond and whose area product is \(8\).

## Assumptions and scope
All areas are two-dimensional Lebesgue areas in \(\mathbb R^2\). For an origin-containing convex body \(K\), the polar is \(K^\circ=\{u:\langle u,z\rangle\le1\text{ for every }z\in K\}\). The two defining ellipses are concentric, have semiaxes \(t,1\), and differ by a right-angle rotation; arbitrary translated, unequal or nonorthogonally rotated pairs are not considered. The center is the Santaló point by central symmetry. The parameter \(t\) ranges through every real \(t\ge1\); the infinite value is only a Hausdorff limit, not a member of the finite family.

## Proof
**1. Area of the intersection.** The body has symmetry under all coordinate sign changes and coordinate interchange. On the angular sector \(0\le\theta\le\pi/4\), its radial function is
\[
\rho_t(\theta)^2=(\cos^2\theta+t^{-2}\sin^2\theta)^{-1}.
\]
The radial area formula and the substitution \(u=\tan\theta\) therefore give
\[
|K_t|=4\int_0^{\pi/4}\rho_t(\theta)^2\,d\theta
=4\int_0^1\frac{du}{1+u^2/t^2}
=4t\arctan(1/t).
\]

**2. Exact polar area.** The polar of an intersection of two convex bodies containing the origin in their interiors is the convex hull of their polars. Here
\[
K_t^\circ=\operatorname{conv}\left(\{t^2u^2+v^2\le1\}\cup\{u^2+t^2v^2\le1\}\right).
\]
For \(t>1\), its first-quadrant upper boundary consists of an arc of the ellipse \(u^2+t^2v^2=1\), a straight supporting segment with exterior normal \((1,1)\), and the reflection of that arc across the diagonal. The first arc has the parametrization \((\cos s,t^{-1}\sin s)\) for \(0\le s\le\phi\). Its final point is
\[
a=\left(\frac{t}{\sqrt{1+t^2}},\frac{1}{t\sqrt{1+t^2}}\right),
\]
and the segment joins \(a\) to its diagonal reflection \(b\). Both endpoints have the same coordinate sum; the line through them supports both polar ellipses. For the counterclockwise first-quadrant boundary, Green's formula \(\frac12\int(u\,dv-v\,du)\) gives two equal arc contributions totaling \(\phi/t\), plus the triangle contribution
\[
\frac12\det(a,b)=\frac12(1-t^{-2}).
\]
This is one-fourth of the total polar area. Hence
\[
|K_t^\circ|=\frac{4\phi}{t}+2(1-t^{-2}).
\]
At \(t=1\), the supporting segment degenerates and the same formula gives the polar disk area \(\pi\).

**3. Strict monotonicity.** Since \(t=\cot\phi\) and \(t-t^{-1}=2\cot(2\phi)\), the product is
\[
\mathcal M(t)=F(\phi):=16(\phi^2+\phi\cot(2\phi)),
\quad 0<\phi\le\pi/4.
\]
Direct differentiation yields
\[
F'(\phi)=\frac{16\cos(2\phi)}{\sin^2(2\phi)}
\bigl(\sin(2\phi)-2\phi\cos(2\phi)\bigr).
\]
The parenthetical factor vanishes at \(\phi=0\) in the limiting sense and has derivative \(4\phi\sin(2\phi)>0\) for \(0<\phi<\pi/4\). Every other factor is positive on this interval. Therefore \(F'(\phi)>0\), while \(\phi=\arctan(1/t)\) is strictly decreasing in \(t\), proving strict decrease of \(\mathcal M\).

**4. Limits and sharp coefficients.** Elementary limits give \(F(\pi/4)=\pi^2\) and \(\lim_{\phi\downarrow0}F(\phi)=8\). Near \(\phi=\pi/4\), \(F(\phi)=\pi^2-16(\pi/4-\phi)^2+O((\pi/4-\phi)^3)\); since \(\pi/4-\phi=(t-1)/2+O((t-1)^2)\), the first expansion follows. At the other endpoint, \(\cot(2\phi)=(2\phi)^{-1}-(2\phi)/3+O(\phi^3)\), so \(F(\phi)=8+16\phi^2/3+O(\phi^4)\). Since \(\phi=t^{-1}+O(t^{-3})\), the second expansion follows. The defining inequalities converge on compact sets to \(|x|\le1\) and \(|y|\le1\), which proves the asserted square limit.

## Verification
The standalone reproducibility program `check.py` checks the differentiated identity and the endpoint coefficients symbolically, and compares both closed area formulas against **independent** quadratures. For the polar, the independent quadrature uses the support-function formula \(|K_t^\circ|=\frac12\int_{0}^{2\pi}h_{K_t}(\theta)^{-2}\,d\theta\), splitting at the active ellipse-to-corner tangent angle \(\arctan(t^{-2})\); it does not use the convex-hull Green calculation. The program also tests ordering across a finite grid. The observed run completed 649 checks. Its finite checks do not establish an infinite-family theorem; the exact proof above does.

To replay from this package, save `check.py` next to this file and run `python check.py` in a Python environment with SciPy and SymPy installed. The assertions terminate with a nonzero status if any check fails.

## Relationship to prior work
Hughes and Chraibi give a general exact ellipse-overlap area procedure using ellipse sectors and Green's formula. That framework concerns overlap areas, not the polar of the intersection or monotonicity of an area product. Böröczky, Makai, Meyer and Reisner establish sharp planar Mahler lower bounds and stability results; those characterize endpoint extremizers, not the strict ordering of the intermediate perpendicular-ellipse intersections. Meyer and Reisner's shadow-system theorem proves convexity of the reciprocal polar volume for families satisfying the shadow-system hypothesis. It neither identifies this ellipse-intersection family as such a system nor yields this explicit family-wide product profile. The current statement is a direct calculation and comparison for this specific family, not a stronger general convex-body inequality.

## Limitations
The result concerns a one-parameter, fourfold-symmetric planar family. It does not claim a general monotonicity principle for ellipse intersections, higher dimensions, arbitrary rotations or unconstrained geometric deformations. The analytic calculations establish correctness; a targeted literature comparison has not established worldwide historical priority. Strict ordering is claimed only for distinct finite parameters above one; the square appears solely as a limit.

## References
- M. Meyer and S. Reisner, *Shadow systems and volumes of polar convex bodies*, arXiv:math/0606305, initial public version 2006-06-13; *Mathematika* 53 (2006), 129–148.
- G. B. Hughes and M. Chraibi, *Calculating ellipse overlap areas*, arXiv:1106.3787, initial public version 2011-06-19.
- K. J. Böröczky, E. Makai Jr., M. Meyer and S. Reisner, *On the volume product of planar polar convex bodies — lower estimates with stability*, arXiv:1507.01481, publicly posted 2015-07-06; *Studia Sci. Math. Hungar.* 50 (2013), 159–198.
