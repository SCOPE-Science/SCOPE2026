# The isoperimetric threshold for eventual real Steiner roots of tall convex pyramids

## Finding
Let \(B\subset\mathbb R^2\) be any compact convex body with nonempty interior, area \(A\), and perimeter \(P\). Fix any horizontal apex projection \(q\in\mathbb R^2\). For \(h>0\) set
\[
K_h=\operatorname{conv}\bigl((B\times\{0\})\cup\{(q,h)\}\bigr)\subset\mathbb R^3.
\]
Write its ordinary Euclidean Steiner polynomial, regarded as a polynomial in the complex variable \(z\), as
\[
f_h(z)=\operatorname{Vol}(K_h)+S_hz+M_hz^2+\frac{4\pi}{3}z^3.
\]
Here \(S_h\) is surface area and \(M_h\) is the integrated mean-curvature coefficient. Define the planar isoperimetric quotient \(Q=4\pi A/P^2\in(0,1]\).

**Theorem (sharp eventual-root dichotomy, including equality).** There exists \(H=H(B,q)>0\) such that, for every \(h>H\):

* If \(Q\le3/4\), the polynomial \(f_h\) has three **distinct negative real** roots.
* If \(Q>3/4\), the polynomial \(f_h\) has precisely one negative real root and a **nonreal conjugate pair**.

More precisely, two roots converge, as \(h\to\infty\), to the roots of the universal quadratic
\[
g(z)=\pi z^2+\frac P2z+\frac A3.
\]
For \(Q\ne3/4\), the two limits are distinct and equal to
\[
z_\pm=\frac{P}{4\pi}\left(-1\pm\sqrt{1-\frac{4Q}{3}}\right),
\]
with the principal complex square root understood when \(Q>3/4\). The third root \(z_{\mathrm{far}}(h)\) satisfies
\[
\lim_{h\to\infty}\frac{z_{\mathrm{far}}(h)}h=-\frac34.
\]
At the boundary \(Q=3/4\), put \(z_0=-P/(4\pi)\). The two bounded roots split **along the negative real axis**, with the universal sharp scale
\[
\boxed{\displaystyle
z_\pm(h)=z_0\pm
\sqrt{\frac{P^3(13-3\pi)}{192\pi^3h}}
+O(h^{-1}).}
\]
In particular, the double root of the limit quadratic does **not** cause a persistent double root or a complex pair for sufficiently tall pyramids.

**Polygonal consequence.** Every nondegenerate triangular-base pyramid eventually has three distinct negative real Steiner roots, regardless of the triangle shape or horizontal apex location. In contrast, for a regular \(m\)-gon base with \(m\ge4\), every sufficiently tall pyramid has one negative real root and a nonreal conjugate pair. A rectangle with a suitable aspect ratio attains \(Q=3/4\), so the equality case occurs for ordinary polygonal bases.

## Assumptions and scope
A convex body is compact and convex with positive two-dimensional Lebesgue area. Its boundary is rectifiable and has length \(P\); no smoothness or strict convexity is assumed. The apex projection \(q\) need not belong to \(B\). All asymptotic statements hold as the physical height \(h\to+\infty\) with \(B,q\) fixed. Constants implicit in \(O(\cdot)\) can depend on \(B,q\). "Eventually" means all heights greater than some finite threshold depending on these data, not merely some unbounded subsequence.

For three-dimensional convex bodies, the coefficient \(M\) of \(z^2\) in the Steiner polynomial is \(2\pi\) times mean width. In particular, if \(H_K(u)\) is the support function of \(K\) and \(\langle\cdot\rangle\) denotes normalized spherical averaging over \(S^2\), then
\[
M=4\pi\langle H_K\rangle.
\]
This normalization gives \(M=3\pi\) for a unit cube.

## Proof
**1. Exact volume and two-term surface-area expansion.** Since the horizontal section of \(K_h\) at altitude \(th\) is a homothetic copy of \(B\), with area \((1-t)^2A\),
\[
V_h=\operatorname{Vol}(K_h)=\frac{Ah}{3}.
\]
Translate horizontally so that \(q=0\); translation does not affect the intrinsic volumes. Parameterize \(\partial B\) by arclength \(s\mapsto\gamma(s)\). Write \(n(s)\) for its outward normal, defined almost everywhere. The ruled lateral surface is parameterized by \(((1-t)\gamma(s),th)\) for \(0\le t\le1\). Its area element is
\[
(1-t)\sqrt{h^2+(\gamma(s)\cdot n(s))^2}\,ds\,dt.
\]
Consequently,
\[
S_h=A+\frac12\int_{\partial B}
\sqrt{h^2+(\gamma\cdot n)^2}\,ds
=A+\frac P2 h+O(h^{-1}).\tag{1}
\]
The integral formula holds for general convex boundaries by the almost-everywhere arclength tangent; boundedness of \(B\) gives the uniform remainder estimate.

**2. Two-term mean-width expansion.** With the horizontal translation already made, write a sphere direction as \(u=(u_\perp,u_3)\). The pyramid support function is exactly
\[
H_{K_h}(u)=\max\{H_B(u_\perp),h u_3\}.
\]
Choose \(R>0\) with \(B\subset R\mathbb B_2\). Outside the spherical belt \(|u_3|\le R/h\), the maximum is \(hu_3\) on the upper hemisphere and \(H_B(u_\perp)\) on the lower hemisphere. In that belt the discrepancy is uniformly bounded, and its normalized area is \(O(h^{-1})\). Thus
\[
\langle H_{K_h}\rangle
=\left\langle (hu_3)_++\mathbf1_{\{u_3<0\}}H_B(u_\perp)\right\rangle+O(h^{-1}).
\]
By spherical symmetry, \(\langle (u_3)_+\rangle=1/4\) and \(\langle |u_\perp|\rangle=\pi/4\). Cauchy's planar perimeter formula gives \((2\pi)^{-1}\int_0^{2\pi}H_B(e_\theta)\,d\theta=P/(2\pi)\). Therefore
\[
\langle H_{K_h}\rangle
=\frac h4+\frac P{16}+O(h^{-1}),
\qquad
M_h=\pi h+\frac{\pi P}{4}+O(h^{-1}).\tag{2}
\]
The belt estimate also covers off-center apices and nonsmooth bases.

**3. Limiting quadratic and generic root types.** Combining the exact volume with (1)--(2), uniformly for \(z\) in any fixed compact subset of \(\mathbb C\), gives
\[
\frac{f_h(z)}h=g(z)+\frac{k(z)}h+O(h^{-2}),\tag{3}
\]
where
\[
\begin{aligned}
g(z)&=\pi z^2+\frac P2z+\frac A3,\\
k(z)&=\frac{4\pi}{3}z^3+\frac{\pi P}{4}z^2+Az.
\end{aligned}
\]
The discriminant of \(g\) is
\[
\Delta_g=\frac{P^2}{4}-\frac{4\pi A}{3}
=\frac{P^2}{4}\left(1-\frac{4Q}{3}\right).
\]
If \(Q<3/4\), the two roots of \(g\) are distinct negative reals. By continuity of simple polynomial roots (or Rouché's theorem on disjoint small circles), two real roots of \(f_h\) converge to them: a nonreal pair could not place exactly one root in each sufficiently small conjugation-invariant disk. If \(Q>3/4\), the two roots of \(g\) are distinct nonreal conjugates with negative real parts; the corresponding roots of \(f_h\) remain nonreal for large \(h\).

In both cases the remaining root is real and negative: all coefficients of \(f_h\) are strictly positive, so no nonnegative real root is possible. The sum of all three roots is \(-3M_h/(4\pi)=-3h/4+O(1)\), proving the far-root limit.

**4. The critical isoperimetric quotient.** Suppose \(Q=3/4\), equivalently \(A=3P^2/(16\pi)\). Then
\[
g(z)=\pi(z-z_0)^2,
\quad z_0=-\frac P{4\pi},
\]
and direct substitution into \(k\) gives the strictly negative value
\[
k(z_0)=\frac{P^3(3\pi-13)}{192\pi^2}<0.
\]
Thus (3) implies \(f_h(z_0)<0\) for all sufficiently large heights, whereas \(f_h(z_0-\delta)>0\) and \(f_h(z_0+\delta)>0\) for every fixed sufficiently small \(\delta>0\) and all large \(h\). The intermediate value theorem forces two **distinct negative** real roots, one on either side of \(z_0\). The third is again real and negative by conjugation and coefficient positivity.

For the sharp splitting, substitute \(z=z_0+y/\sqrt h\) into (3) and multiply by \(h\): uniformly on bounded real \(y\),
\[
h\frac{f_h(z_0+y/\sqrt h)}h
=\pi y^2+k(z_0)+O(h^{-1/2}).
\]
The two simple real roots of the limiting expression occur at
\[
y=\pm\sqrt{-k(z_0)/\pi}=
\pm\sqrt{\frac{P^3(13-3\pi)}{192\pi^3}}.
\]
The sharper \(O(h^{-1})\) error in the original \(z\) follows by Taylor expansion near these simple rescaled roots; the right-hand remainder is \(O(h^{-1/2})\), uniformly there. This completes the classification for all three quotient regimes.

**5. Geometric sharpness and polygons.** By the sharp planar isoperimetric inequality, \(0<Q\le1\); the regular circle has \(Q=1\), while a sufficiently thin rectangle has \(Q<3/4\). A rectangle with side ratio \(r>1\) satisfying
\[
\frac{\pi r}{(1+r)^2}=\frac34
\quad\Longleftrightarrow\quad
r=\frac12\left(\frac{4\pi}{3}-2+
\sqrt{\left(\frac{4\pi}{3}-2\right)^2-4}\right)
\]
achieves equality, proving that the threshold is attained. For any triangle of fixed perimeter, area is at most the area of the equilateral triangle, giving \(Q\le\pi/(3\sqrt3)<3/4\). A regular \(m\)-gon has
\[
Q_m=\frac{\pi}{m\tan(\pi/m)},
\]
which increases with \(m\ge3\), and \(Q_4=\pi/4>3/4\). The stated polygonal consequence follows.

## Verification
The accompanying standalone `verify.py` performs the following checks from its own file: symbolic exact simplification of the critical coefficient \(k(z_0)\) and the square-root constant; independent polyhedral computation of volume, face areas, and dihedral-angle mean curvature for convex polygonal pyramids; root-type checks for regular \(3\)-, \(4\)-, \(5\)-, \(6\)-, \(8\)-, and \(16\)-gonal bases at height \(3000\), with an off-center apex; and three finite-height checks of the critical-rectangle split. These all passed in the supplied run. The source is included because numerical checks are supplemental only; the universal claims and the equality case follow from the analytical estimates above.

## Relationship to prior work
Hernández Cifre and Saorín (2007) established the general classification of three-dimensional Steiner-root types in terms of volume, area, and integral mean curvature. Their full 20-page paper was inspected; its examples include Platonic solids, cap bodies, and right circular **cylinders**, but not this arbitrary planar-base tall-pyramid threshold. The general classification is an essential antecedent and is not claimed as new.

Henk and Hernández Cifre (2007 preprint; 2008 publication) study root location and tangential convex bodies, with a high-dimensional square-base pyramid appearing in a separate construction. That result does not establish the two bounded-root limit, the shape-independent \(3/4\) criterion, or the equality splitting for three-dimensional pyramids.

Saorín (2008 thesis, 2009 article) derives Steiner coefficients for **right circular cones** and identifies their large-height nonreal regime. A subsequently published complete circular-cone phase diagram also applies to circular bases. Those are specializations to \(Q=1\) and do not entail the arbitrary-base threshold or the critical-rectangle splitting. Katsnelson (2008) gives further general Steiner-root theory but not the claimed pyramid classification. Searches for equivalent formulas, asymptotic cone-root laws, and triangle/square transitions found no dominating statement. This is evidence of noncoverage, not proof of historical uniqueness.

## Limitations
The theorem concerns eventual root type only; it does not determine the finite transition heights or their number, and it does not state an all-height classification. Its height threshold may depend on the full shape of \(B\) and the apex projection \(q\), even when the quotient \(Q\) is fixed. The limiting quadratic depends only on area and perimeter, but the higher asymptotic terms can depend on finer geometry. The theorem does not apply to oblique coordinate transformations that change the Euclidean metric. Historical-priority uncertainty remains for unindexed or differently formulated asymptotic results. The accompanying finite computations are not an exhaustive proof over all convex bases.

## References
1. M. A. Hernández Cifre and E. Saorín, *On the roots of the Steiner polynomial of a 3-dimensional convex body*, Advances in Geometry 7 (2007), 275–294, DOI: 10.1515/ADVGEOM.2007.016. Complete 20-page text inspected.
2. M. Henk and M. A. Hernández Cifre, *Notes on the roots of Steiner polynomials*, arXiv:math/0703373v1, publicly posted 2007-03-13; Revista Matemática Iberoamericana 24 (2008), 631–644, DOI: 10.4171/RMI/550.
3. E. Saorín Gómez, *On inner parallel bodies. From the Steiner polynomial to Poincaré inequality*, doctoral thesis, Universidad de Murcia, 2008.
4. E. Saorín, *On Hadwiger's problem on inner parallel bodies*, Banach Center Publications 84 (2009), 121–129, DOI: 10.4064/bc84-0-8.
5. V. Katsnelson, *On H. Weyl and J. Steiner polynomials*, arXiv:0803.2346v1, publicly posted 2008-03-16.
6. Henk, Hernández Cifre, and Saorín, *Steiner polynomials via ultra-logconcave sequences*, arXiv:1112.4741v1, publicly posted 2011-12-20.
7. *Complete two-transition Steiner-root phase diagram for right circular cones*, public published-finding corpus mathematical record (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-complete-two-transition-steiner-root-phase-diagram-for-right-cir--645636c244de.
