# Sharp two-regime convexity defect of Euclidean ellipsoids

## Finding

Let \(d\geq2\) and let \(E\subset\mathbb R^d\) be the **boundary** of a nondegenerate centered Euclidean ellipsoid. Write \(a\) and \(b\) for its largest and smallest semiaxes, so \(0<b\leq a\). For a nonempty subset \(S\subset E\), let \(\operatorname{Rad}(S)\) denote the radius of its smallest enclosing Euclidean ball. Define the convexity defect at scale \(t\geq0\) by

\[
 h_E(t)=\sup\{\operatorname{dist}(z,E):z\in\operatorname{conv}(S),\ \varnothing\ne S\subset E,\ \operatorname{Rad}(S)\leq t\}.
\]

Set

\[
 R=\frac{b^2}{a},\qquad
 t_*=b\sqrt{1-\left(1-\frac{b^2}{a^2}\right)^2}
     =R\sqrt{2-\frac{b^2}{a^2}}.
\]

**Theorem (sharp initial regime, sharp endpoint, and plateau).** For every such ellipsoid in every dimension \(d\geq2\),

\[
 \boxed{\ h_E(t)=a\left(1-\sqrt{1-\frac{t^2}{b^2}}\right)\quad (0\leq t\leq t_*),\qquad
 h_E(t)=b\quad(t\geq b).\ }
\]

For every **nonround** ellipsoid \(a>b\), the displayed initial expression is a universal upper bound on \([0,b]\) and is **strict** for every \(t\in(t_*,b]\). Thus \(t_*\) is exactly the largest scale through which that natural affine-circle bound is attained. At the transition \(h_E(t_*)=R\), and \(R<t_*<b\) when \(a>b\). For a round sphere \(a=b\), the first formula holds for the entire interval \([0,b]\) and joins the plateau at \(t=b\).

In particular, as \(t\downarrow0\), the exact first regime gives

\[
 h_E(t)=\frac{a}{2b^2}t^2+\frac{a}{8b^4}t^4+O_{a,b}(t^6).
\]

This fourth-order coefficient, the saturation scale, and the plateau depend **only** on the extreme semiaxes, regardless of intermediate axes or ambient dimension. The theorem does not assert a closed formula for the intervening nonround interval \((t_*,b)\).

## Assumptions and scope

All enclosing balls, hulls, and distances are Euclidean. The set \(E\) is the ellipsoid *surface* rather than the filled convex ellipsoid (whose convexity defect vanishes). The definition of \(h_E\) uses the enclosing **radius**, not half of the diameter; for arbitrary subsets these are different. Orthogonal changes of coordinates and translations leave the claim unchanged. We may therefore write \(E=A\mathbb S^{d-1}\), where \(A\) is diagonal, positive definite, and has singular values between \(b\) and \(a\), attaining each extreme. Compactness and Carathéodory's theorem allow the supremum to be taken over convex hulls of at most \(d+1\) points, without imposing any finite sampling restriction.

The initial-scale transition is meaningful because the normal focal radius at a major-axis tip is \(R=b^2/a\), whereas the exact affine-circle regime persists to the strictly larger scale \(t_*\) when the ellipsoid is nonround.

## Proof

**1. Exact spherical scale-hull bound.** Let \(0\leq r<1\) and let \(S\subset\mathbb S^{d-1}\) lie in a closed ball \(B(c,r)\). Necessarily \(c\ne0\). For every \(u\in S\),

\[
 \left\langle u,\frac{c}{\|c\|}\right\rangle
 \geq\frac{1+\|c\|^2-r^2}{2\|c\|}
 \geq\sqrt{1-r^2},
\]

where the last inequality is arithmetic--geometric mean. Consequently every \(w\in\operatorname{conv}(S)\) has \(\|w\|\geq\sqrt{1-r^2}\), so

\[
 \operatorname{dist}(w,\mathbb S^{d-1})=1-\|w\|
 \leq1-\sqrt{1-r^2}.
\]

Equality is attained by the midpoint \(\rho e\), with \(\rho=\sqrt{1-r^2}\), of the two spherical points \(\rho e\pm r f\), where \(e\perp f\) are unit vectors. Their enclosing radius is exactly \(r\). Moreover, equality in the distance inequality forces \(\|w\|=\rho\) and, from the supporting cap inequality, \(w=\rho c/\|c\|\). Thus the exact spherical convexity defect is \(1-\sqrt{1-r^2}\) for \(r<1\). At \(r=1\), an antipodal pair gives the unit-ball center, hence the value is \(1\).

**2. Dimension-free affine upper bound.** If \(S\subset E\) has \(\operatorname{Rad}(S)\leq t\), then \(A^{-1}S\) is contained in a ball of radius \(t/b\), because \(\|A^{-1}\|_{\mathrm{op}}=1/b\). Each \(z=Aw\in\operatorname{conv}(S)\) satisfies \(w\in\operatorname{conv}(A^{-1}S)\). For \(0\leq t\leq b\), the spherical bound and \(\|A\|_{\mathrm{op}}=a\) give

\[
 \operatorname{dist}(z,E)
 \leq a\operatorname{dist}(w,\mathbb S^{d-1})
 \leq a\left(1-\sqrt{1-t^2/b^2}\right).
\]

(The second step uses the nearest unit vector \(w/\|w\|\) for \(t<b\), and follows by continuity at \(t=b\).)

**3. Exact nearest distance on a major axis.** Choose orthogonal unit eigenvectors \(e\) and \(f\) of \(A\) for the eigenvalues \(a\) and \(b\). For \(x\in[0,a]\), minimizing distance from \(xe\) to \(A\mathbb S^{d-1}\) reduces to a single coordinate \(u=\langle v,e\rangle\in[-1,1]\):

\[
 \|xe-Av\|^2\geq(au-x)^2+b^2(1-u^2).
\]

For each prescribed \(u\), equality is achieved by choosing the component of \(v\) orthogonal to \(e\) along \(f\). The right-hand side is a quadratic in \(u\) with its unconstrained minimum at \(u=ax/(a^2-b^2)\) when \(a>b\). It follows that

\[
 \operatorname{dist}(xe,E)=
 \begin{cases}
 a-x,&x\geq a-b^2/a,\\[2pt]
 b\sqrt{1-x^2/(a^2-b^2)},&0\leq x<a-b^2/a,
 \end{cases}
\]

for \(a>b\). When \(a=b\), the distance is \(a-x\) for every \(x\in[0,a]\).

**4. Matching witness throughout the exact regime.** For \(0\leq t\leq b\), put \(\rho=\sqrt{1-t^2/b^2}\) and select

\[
 p_\pm=a\rho e\pm t f\in E.
\]

Their enclosing radius is \(t\) and their midpoint is \(z=a\rho e\). The condition \(a\rho\geq a-b^2/a\) is equivalent to \(t\leq t_*\). In that range Step 3 yields

\[
 \operatorname{dist}(z,E)=a-a\rho
 =a\left(1-\sqrt{1-t^2/b^2}\right).
\]

This matches Step 2 exactly. At \(t=t_*\), the common value is \(b^2/a\).

**5. Strictness beyond the sharp transition.** Suppose \(a>b\) and \(t_*<t<b\). The scaled hull \(\operatorname{Hull}(E,t)\) is compact: by Carathéodory every point has a representation using at most \(d+1\) points, whose weights and positions range over compact spaces; the condition on their smallest-enclosing-ball radius is closed. Therefore the supremum defining \(h_E(t)\) is attained.

If equality held in Step 2, then for a maximizing \(w=A^{-1}z\), equality in the spherical step would force \(\|w\|=\rho=\sqrt{1-t^2/b^2}\), while equality in the operator-norm step would force the radial unit vector \(v=w/\|w\|\) into the eigenspace of \(A\) with eigenvalue \(a\). Thus \(z=a\rho v\). The candidate nearest ellipsoid point used to produce equality would have to be \(av\), at distance \(a(1-\rho)\). But \(t>t_*\) means \(a\rho<a-b^2/a\); Step 3 applied in the two-dimensional plane spanned by \(v\) and any least-axis vector gives a point of \(E\) strictly closer to \(z\) than \(av\). This contradicts equality. At \(t=b\), the proposed upper expression equals \(a>b\), while Step 6 shows \(h_E(b)=b\), so strictness holds there as well.

**6. Exact saturation for large scales.** The maximum of \(\operatorname{dist}(z,E)\) over the filled ellipsoid is \(b\), attained at its center: through every interior \(z\), the line parallel to a least semiaxis intersects the ellipsoid in a segment of length at most \(2b\), so one endpoint is no farther than \(b\). The antipodal points \(\pm bf\in E\) have enclosing radius \(b\) and midpoint \(0\). Hence \(h_E(t)=b\) for all \(t\geq b\).

Finally, the fourth-order expansion follows from the Taylor expansion of \(1-\sqrt{1-s}\) at \(s=0\). This completes the proof.

## Verification

The finite standalone check `verification.py` evaluates the matching witness, the transition, strict inequality for the chord witness after the transition, and direct planar nearest-boundary minimization for several semiaxis pairs. It uses only the Python standard library. Running `python verification.py` produced `PASS: 2455 finite arithmetic and projection checks`. These tests corroborate the algebra but are not relied on for the all-dimensions theorem; the quantified upper bound, equality construction, and strictness are the arguments above.

## Relationship to prior work

The scale-dependent convex hull and convexity-defect function were introduced by Attali, Lieutier, and Salinas (conference 2011, journal 2013); they give general comparison properties and upper bounds for shapes with positive reach. Berenfeld, Harvey, Hoffmann, and Shankar (arXiv 22 January 2020; journal 2021/2022) connect the defect to reach and prove a general local \(t^2/(2R_\ell)+O(t^4)\) expansion and curvature-based upper bounds. The present result treats a specific natural geometric model but identifies a complete exact **initial interval**, a **sharp endpoint** of the affine-circle inequality, the **fourth-order coefficient**, and a **large-scale plateau**, uniformly in dimension. Those conclusions do not follow merely by substituting the ellipsoid's focal radius into the general circular majorant. For \(a>b\), the fourth-order coefficient of the focal-radius circular majorant is \(a^3/(8b^6)\), strictly larger than the actual coefficient \(a/(8b^4)\).

## Limitations

The intermediate profile for \(t\in(t_*,b)\) on a nonround ellipsoid is not determined. The theorem concerns the surface of a centrally symmetric quadratic ellipsoid with the Euclidean norm; it does not directly apply to general convex hypersurfaces, affine norms, sampled point clouds, or the alternate center-based defect. The proof gives no new statistical risk bound for reach estimation. Search and full-text comparisons support a best-knowledge distinction from the cited general bounds but do not certify global publication priority; independently checking the wider specialist literature remains worthwhile.

## References

1. D. Attali, A. Lieutier, and D. Salinas, *Vietoris--Rips Complexes Also Provide Topologically Correct Reconstructions of Sampled Shapes*, Proceedings SoCG (2011), Computational Geometry 46 (2013), 448--465. DOI: 10.1016/j.comgeo.2012.02.009. Author-hosted full text: https://dattali.github.io/Publications/2012-cgta-Rips.pdf (definitions in Section 3 and bounds in Section 5).
2. C. Berenfeld, J. Harvey, M. Hoffmann, and K. Shankar, *Estimating the Reach of a Manifold via its Convexity Defect Function*, arXiv:2001.08006 (first public submission 2020-01-22), Discrete & Computational Geometry 67 (2022), 403--438. DOI: 10.1007/s00454-021-00290-8 (especially Definition 4.1 and Propositions 4.3--4.4). Full text: https://link.springer.com/article/10.1007/s00454-021-00290-8.
