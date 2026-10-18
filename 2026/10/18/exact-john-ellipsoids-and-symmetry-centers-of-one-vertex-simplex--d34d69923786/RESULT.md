# Exact John ellipsoids and symmetry centers of one-vertex simplex frusta

## Finding
For every integer \(n\ge2\) and every \(0\le t<1\), consider the \(n\)-dimensional simplex frustum
\[
F_{n,t}=\{x\in\mathbb R^n:x_i\ge0\ (1\le i\le n),\quad t\le\sum_{i=1}^n x_i\le1\}.
\]
Let \(e=\mathbf{1}/\sqrt n\), \(P_{\parallel}=ee^\top\), and \(P_{\perp}=I-P_{\parallel}\). Its unique maximum-volume inscribed (John) ellipsoid is
\[
E_{n,t}=\{x:(x-c)^\top Q^{-1}(x-c)\le1\},\quad
c=\frac{h}{n}\mathbf{1},\quad Q=pP_{\perp}+qP_{\parallel},
\]
where, with \(t_*=(n-1)/(n+1)\),
\[
\boxed{
(h,p,q)=\begin{cases}
\left(\dfrac{n}{n+1},\dfrac1{n(n+1)},\dfrac1{n(n+1)^2}\right),&0\le t\le t_*,\\[6pt]
\left(\dfrac{1+t}{2},\dfrac{t}{n(n-1)},\dfrac{(1-t)^2}{4n}\right),&t_*\le t<1.
\end{cases}}
\]
The formulas agree at \(t_*\). Below the transition, the \(n\) coordinate facets and the upper-sum facet touch the ellipsoid, while the new lower-sum facet does not. At the transition, the lower-sum facet first touches. Above it, all \(n+2\) facets touch. In particular the John center **remains fixed while the truncated simplex changes** for every \(0\le t\le t_*\).

Define the Minkowski symmetry coefficient by
\[
\operatorname{sym}(F)=\max\{\alpha\ge0:\exists z\in F\text{ with }-\alpha(F-z)\subseteq F-z\}.
\]
For every \(n\ge2\) and \(0\le t<1\), this body has the exact coefficient and **unique** Minkowski center
\[
\boxed{\operatorname{sym}(F_{n,t})=\frac1{n-t},\qquad z_{n,t}=\frac1{n+1-t}\mathbf{1}.}
\]
The Minkowski center differs from the John center whenever \(t>0\).

Finally the exact **John-centered containment factor** (not necessarily the least factor achievable using another ellipsoid) is
\[
\boxed{\rho_{n,t}:=\inf\{\rho\ge1:F_{n,t}\subseteq c+\rho(E_{n,t}-c)\}
=\begin{cases}
n,&0\le t\le t_*,\\[3pt]
\sqrt{1+(n-1)^2/t},&t_*\le t<1.
\end{cases}}
\]
Thus the fixed John ellipsoid remains a sharp \(n\)-rounding through the initial truncation regime, whereas its own required dilation decreases strictly after the transition.

## Assumptions and scope
The dimension is an integer \(n\ge2\) and the truncation depth is real \(0\le t<1\); the excluded endpoint \(t=1\) is lower dimensional. At \(t=0\), \(F_{n,0}\) is the original simplex with vertices \(0,e_1,\ldots,e_n\); for \(t>0\), the vertices are precisely \(e_i\) and \(te_i\), \(1\le i\le n\). The ambient Euclidean metric is inherited from \(\mathbb R^n\). The \(n\) coordinate facets are always present, and the lower-sum hyperplane is a genuine facet for \(t>0\). The eigenvalues of \(Q\) are squared Euclidean semiaxis lengths; the ellipsoid volume is exactly \(\kappa_n p^{(n-1)/2}q^{1/2}\), where \(\kappa_n=\pi^{n/2}/\Gamma(n/2+1)\). No assertion is made about the globally optimal ellipsoidal rounding factor of \(F_{n,t}\) when the ellipsoid is allowed to change.

## Proof
**1. Every supporting facet and the two regimes.** An ellipsoid with center \(c=(h/n)\mathbf{1}\) and shape \(Q=pP_\perp+qP_\parallel\) lies in \(F_{n,t}\) if and only if its minimum coordinate is nonnegative and its extreme coordinate sums lie in \([t,1]\). These independent support-function inequalities are
\[
\frac hn\ge\sqrt{\frac{(n-1)p+q}{n}},\qquad
h-\sqrt{nq}\ge t,\qquad h+\sqrt{nq}\le1.\tag{1}
\]
In the first regime, substitution of the stated parameters gives equality in the coordinate and upper-sum inequalities, while the minimum coordinate sum equals \((n-1)/(n+1)=t_*\). Hence the lower-sum constraint is slack for \(t<t_*\), active at \(t=t_*\). In the second regime, \((n-1)p+q=h^2/n\) and \(\sqrt{nq}=(1-t)/2\). All three inequalities in (1) are then equalities. The matrices are positive definite for every indicated \(n,t\).

**2. Explicit contact certificate for global maximality.** Normalize \(E_{n,t}\) to the unit ball via \(x=c+Q^{1/2}u\). Each coordinate facet touches at its unique unit vector
\[
u_i=-\frac{Q^{1/2}e_i}{h/n},\quad 1\le i\le n.
\]
Write \(s=\sqrt{nq}/h\); by (1) at equality, the vectors satisfy
\[
\langle u_i,e\rangle=-s,\quad
\sum_i u_i=-ns\,e,\quad
\sum_i u_iu_i^\top=\frac{n(1-s^2)}{n-1}P_\perp+ns^2P_\parallel.\tag{2}
\]
In the first regime, \(s=1/n\). Give each \(u_i\) weight \(n/(n+1)\), and give the upper-sum contact \(+e\) the same weight; these \(n+1\) positive weights have zero weighted first moment and weighted second moment \(I\). Since the lower truncation does not destroy containment, John's contact theorem proves the stated ellipsoid is the **unique** global maximal-volume inscribed ellipsoid, including at \(t=t_*\).

For \(t>t_*\), \(s=(1-t)/(1+t)<1/n\). Both axial contacts \(+e\) and \(-e\) are present, along with the \(n\) side contacts. Assign to each side contact the weight
\[
w=\frac{n-1}{n(1-s^2)},
\]
and to the upper and lower contacts respectively
\[
w_+=\frac{1+ns}{2(1+s)},\qquad w_-=\frac{1-ns}{2(1-s)}.\tag{3}
\]
All weights are positive. Substituting (2) into (3) gives the exact John identities
\[
w\sum_i u_i+w_+e-w_-e=0,
\qquad w\sum_i u_iu_i^\top+(w_++w_-)ee^\top=I.
\]
The ellipsoid is contained by (1), so John's sufficiency criterion again proves unique global maximality. At \(t=t_*\) the lower-contact weight vanishes, consistently with the first regime. Because the ellipsoid is strictly convex, each supporting facet has exactly one tangency point, establishing the entire facet-contact classification. These arguments do not assume that an arbitrary competing ellipsoid is permutation symmetric.

**3. Exact Minkowski symmetry and uniqueness of its center.** Suppose \(-\alpha(F_{n,t}-z)\subseteq F_{n,t}-z\), for some \(\alpha\ge0\) and \(z\in F_{n,t}\). Apply the coordinate lower bounds to the reflected image of a vertex \(e_i\). Every coordinate gives
\[
(1+\alpha)z_i\ge\alpha.\tag{4}
\]
Apply the upper-sum bound to the reflected image of a point of total coordinate sum \(t\). This gives
\[
(1+\alpha)\sum_i z_i-\alpha t\le1.\tag{5}
\]
Summing (4) and combining with (5) yields \(n\alpha\le1+\alpha t\), and therefore \(\alpha\le1/(n-t)\). At equality in this bound, (4) and (5) force every coordinate of \(z\) to equal \(1/(n+1-t)\), showing uniqueness of any possible maximizing center.

Conversely, take \(\alpha=1/(n-t)\) and \(z=\mathbf{1}/(n+1-t)\). The minimum transformed coordinate in the reflected image is exactly zero, its largest possible sum is exactly one, and its smallest possible sum is \((n-1)/(n-t)\ge t\), because
\[
(n-1)-t(n-t)=(1-t)(n-1-t)\ge0.
\]
All defining halfspaces are respected, proving both the claimed coefficient and the unique center. For \(0<t\le t_*\), its coordinate sum \(n/(n+1-t)\) strictly exceeds \(h=n/(n+1)\); for \(t>t_*\), it exceeds \(h=(1+t)/2\), since their difference equals \((1-t)(n-1-t)/(2(n+1-t))>0\). Thus the two centers coincide only at \(t=0\).

**4. Exact John-centered rounding.** A convex quadratic attains its maximum over a polytope at a vertex. For a vertex of form \(ae_i\), where \(a\in\{1,t\}\), the squared ellipsoid norm from the John center equals
\[
R(a)=\frac{(n-1)a^2}{np}+\frac{(a-h)^2}{nq}.\tag{6}
\]
In the first regime, \(R(1)=n^2\), while each \(te_i\) lies on the segment from \(0\) to \(e_i\), both inside the dilation by \(n\); therefore \(R(t)\le n^2\). In the second regime, (6) simplifies exactly to
\[
R(1)=1+\frac{(n-1)^2}{t},\qquad R(t)=1+(n-1)^2t.
\]
Because \(0<t<1\), the first is strictly larger. Taking the square root and evaluating at a maximizing vertex proves the claimed **sharp factor for this prescribed ellipsoid**, including agreement at \(t_*\). No claim about an unrestricted optimal rounding factor is needed.

## Verification
The standalone `verify.py` uses exact rational arithmetic to verify the support inequalities, the two John moment identities, all Minkowski inclusion inequalities, and both extreme vertex distances for \(258\) distinct dimension/parameter pairs with \(2\le n\le30\). It also independently tests \(4601\) randomly generated feasible symmetric ellipsoids against the claimed determinant bound. Executing `python3 verify.py` returns `VERIFY_OK`. These are consistency tests only: the full all-parameter statement rests on the analytic arguments and the classical John contact theorem above.

## Relationship to prior work
Eydelzon's September 7, 2026 simplex John-ellipsoid work determines a corner-volume characterization for an **untruncated simplex**, but not the transition under facet-parallel truncation. Xiong and Freund (August 31, 2026) prove general symmetry-dependent ellipsoid rounding bounds; their proof and extremal reflected-simplex constructions do not compute this frustum's John ellipsoid, Minkowski center, or exact John-centered radius. Mordhorst (arXiv:1509.06023, Section 6) explicitly employs a selected truncated simplex whose John ellipsoid remains the parent simplex ellipsoid; that is qualitatively analogous to the **first** regime here, not a classification for all truncation depths. Prior calculations of opposite-body mixed volumes for this same frustum address a different functional, with no stated implication to its maximum-volume inscribed ellipsoid. The new content is the complete all-dimensional second regime, its exact facet-contact certificate, and the accompanying sharp Minkowski-center and rounding profiles.

## Limitations
The full shape and formulas apply only to **one** simplex vertex removed by a hyperplane parallel to its opposite facet. No formulas for arbitrary oblique truncations, simultaneous removals, or nonsimplex polytopes follow. The upper endpoint \(t=1\) is excluded because full-dimensional John ellipsoids cease to exist. The value \(\rho_{n,t}\) is sharp relative to the **John** ellipsoid, not necessarily among all inscribed or arbitrary ellipsoidal roundings. Earlier equivalent calculations in nonindexed geometric-design or optimal-ellipsoid literature cannot be excluded solely by literature searches.

## References
1. A. Eydelzon, *From the Steiner Inellipse to the John Ellipsoid of a Simplex: A Corner-Volume Characterization*, arXiv:2609.08045v1, first public 2026-09-07, especially Theorem 1 and Section 4; https://arxiv.org/html/2609.08045v1.
2. Z. Xiong and R. M. Freund, *Symmetry-dependence in Rounding of a Convex Body*, arXiv:2608.30876, first public 2026-08-31, especially Theorem 1.1 and Section 5; https://optimization-online.org/wp-content/uploads/2026/08/arxiv-sep23.pdf.
3. O. Mordhorst, *New results on affine invariant points*, arXiv:1509.06023v3 (2016), Section 6, pages 16–17; https://arxiv.org/pdf/1509.06023.
4. F. John, *Extremum problems with inequalities as subsidiary conditions*, in *Studies and Essays Presented to R. Courant* (1948), 187–204. See also K. Ball, *Ellipsoids of maximal volume in convex bodies*, Geom. Dedicata 41 (1992), 241–250.
