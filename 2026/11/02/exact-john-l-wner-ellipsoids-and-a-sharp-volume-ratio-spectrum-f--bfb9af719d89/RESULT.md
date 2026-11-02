# Exact John–Löwner ellipsoids and a sharp volume-ratio spectrum for one-vertex simplex frusta

## Finding
For every integer \(d\ge3\) and \(0\le t<1\), define the parallel-truncated simplex
\[
K_{d,t}=\{x\in\mathbb R^d:x_i\ge0\ (1\le i\le d),\quad t\le\sum_{i=1}^d x_i\le1\}.
\]
Let \(\mathbf1=(1,\ldots,1)^T\), \(P=\mathbf1\mathbf1^T/d\), and \(P^\perp=I-P\). Write an ellipsoid with center \(\mu\) and positive shape matrix \(Q\) as \(E(\mu,Q)=\{x:(x-\mu)^TQ^{-1}(x-\mu)\le1\}\).

**John ellipsoid.** Set
\[
s=\min\left\{\frac1{d+1},\frac{1-t}{2}\right\}.
\]
The unique maximum-volume ellipsoid in \(K_{d,t}\) is \(E(\mu_J,Q_J)\), where
\[
\boxed{\mu_J=\frac{1-s}{d}\mathbf1,\qquad
Q_J=\frac{s^2}{d}P+\frac{1-2s}{d(d-1)}P^\perp.}
\]
Its coordinate facets and top sum facet are tangent for all \(t\). The lower sum facet becomes tangent exactly at the sharp threshold \(t_c=(d-1)/(d+1)\), and remains tangent thereafter.

**Löwner ellipsoid.** Let \(r\in[1/d,1)\) be the unique solution of
\[
\boxed{t^2r^2+d(1-t^2)r=1,}
\]
and put \(\lambda=1/(1+r)\), \(y=t+(1-t)\lambda\), and \(m_2=t^2+(1-t^2)\lambda\). The unique minimum-volume ellipsoid containing \(K_{d,t}\) is \(E(\mu_L,Q_L)\) with
\[
\boxed{\mu_L=\frac yd\mathbf1,\qquad Q_L=(1-t)^2\lambda(1-\lambda)P+m_2P^\perp.}
\]
All vertices \(e_i\) and \(t e_i\) lie on this ellipsoid. When \(t=0\), the \(d\) latter vertices coincide at the origin; for \(0<t<1\) all \(2d\) distinct vertices are contacts.

**Sharp ratio.** If \(\mathcal R_d(t)=\operatorname{vol}_d(E_L)/\operatorname{vol}_d(E_J)\), then
\[
\boxed{\mathcal R_d(t)=\frac{\sqrt d(1-t)\sqrt{\lambda(1-\lambda)}}s
\left(\frac{d(d-1)m_2}{1-2s}\right)^{(d-1)/2}.}
\]
This function is strictly decreasing on \([0,1)\), and
\[
\boxed{\mathcal R_d(0)=d^d,\qquad
\lim_{t\uparrow1}\mathcal R_d(t)=d^{d/2}(d-1)^{(d-1)/2}.}
\]
The upper bound is attained only at the untruncated simplex; the lower bound is an unattained sharp limit of nondegenerate frusta. In addition, \(\log\mathcal R_d(t)\) is continuously differentiable but not twice differentiable at \(t_c\); its right-minus-left second derivative there is \((d+1)^3/[4(d-1)]\).

By affine covariance, these statements transfer to every simplex truncated at one vertex by a hyperplane parallel to the opposite facet, with the same affine truncation parameter.

## Assumptions and scope
The parameter \(t\) is the remaining barycentric sum at the new truncating face: \(t=0\) is the original simplex, \(0<t<1\) gives a full-dimensional frustum, and \(t=1\) is excluded because the body loses dimension. The volume ratio is Euclidean volume in any affine realization; it is affine invariant because both extremal ellipsoids transform covariantly. The matrices \(Q_J,Q_L\) describe squared semiaxes, not the matrices defining the inverse quadratic forms. The higher-dimensional theorem is asserted for integers \(d\ge3\). All formulas also specialize to the planar case, but the established theory of extremal ellipses of trapezoids and quadrilaterals means no novelty is claimed in \(d=2\).

## Proof
**1. Symmetry reduction and the John optimizer.** Uniqueness of the maximal-volume inscribed ellipsoid and invariance under all coordinate permutations force its center to be \((y/d)\mathbf1\) and its shape to be \(a^2P+b^2P^\perp\) with \(a,b>0\). Put \(s=\sqrt d\,a\) and \(q=d(d-1)b^2\). Exact support-function tests against the \(d+2\) defining halfspaces are
\[
q+s^2\le y^2,\quad y-s\ge t,\quad y+s\le1.
\]
For fixed \(s\), the positive determinant factor is proportional to \(s q^{(d-1)/2}\); it increases with \(q\). The largest feasible center sum is \(y=1-s\), and then the largest feasible transverse variable is \(q=(1-s)^2-s^2=1-2s\). This is feasible precisely for \(0<s\le(1-t)/2\). Thus the entire optimization reduces to maximizing \(s(1-2s)^{(d-1)/2}\) on that interval. Its logarithmic derivative equals \(1/s-(d-1)/(1-2s)\), which changes sign once at \(s=1/(d+1)\). This proves the John formula and uniqueness. The support equalities imply tangency to every coordinate facet and the top facet; the bottom facet touches exactly when \(1-2s=t\).

**2. A positive contact certificate for the Löwner optimizer.** The frustum is the convex hull of the two vertex orbits \(\{e_i\}_{i=1}^d\) and \(\{t e_i\}_{i=1}^d\). Give each outer vertex probability \(\lambda/d\) and each inner vertex probability \((1-\lambda)/d\). This probability measure has mean \(\mu_L=(y/d)\mathbf1\) and covariance \(Q_L/d\), since the transverse variance is \(m_2/d\) and the axial variance is \((m_2-y^2)/d=(1-t)^2\lambda(1-\lambda)/d\).

The quadratic equation for \(r\) is equivalent to \(m_2=(d-1)/(d-r)\). The squared ellipsoid gauge at each outer vertex is
\[
\frac{(1-y)^2}{d(1-t)^2\lambda(1-\lambda)}+\frac{d-1}{d m_2}
=\frac1d\left(r+\frac{d-1}{m_2}\right)=1.
\]
The weighted mean squared gauge of all vertices is \(d^{-1}\operatorname{tr}(Q_L^{-1}Q_L)=1\), so the inner orbit also has squared gauge one because both weights are positive. This directly proves containment of every vertex, hence of the convex hull. After mapping \(E(\mu_L,Q_L)\) to the unit ball, the positive vertex weights have zero first moment and second moment \(I/d\). Multiplying these weights by \(d\) gives the necessary and sufficient Löwner contact identities. Therefore the proposed ellipsoid is globally minimum-volume and unique, without assuming that a competing ellipsoid is permutation symmetric.

**3. Ratio and strict monotonicity.** The axial and transverse semiaxes of the John ellipsoid are \(s/\sqrt d\) and \(\sqrt{(1-2s)/[d(d-1)]}\); those of the Löwner ellipsoid are \((1-t)\sqrt{\lambda(1-\lambda)}\) and \(\sqrt{m_2}\). Multiplying semiaxes gives the displayed volume ratio.

For \(0\le t\le t_c\), the John ellipsoid is constant. The volume of the Löwner ellipsoid decreases strictly as \(t\) increases: for \(t_1<t_2\), the inner vertices \(t_2e_i\) are strict interior points of the ellipsoid at \(t_1\), being proper convex combinations of its distinct contacts \(t_1e_i\) and \(e_i\). If the two Löwner volumes were equal, uniqueness and nesting would force the same ellipsoid at both parameters, contradicting the just-proved inner-vertex tangencies at \(t_2\).

For \(t>t_c\), the John volume is proportional to \((1-t)t^{(d-1)/2}\). The outer volume is proportional to \((1-t)\sqrt{\lambda(1-\lambda)}m_2^{(d-1)/2}\). The above quadratic relation for \(r\) is also the stationarity equation for the outer volume factor as a function of \(\lambda\). Differentiating along its optimal \(\lambda\) by the envelope identity therefore gives
\[
\frac{d}{dt}\log\mathcal R_d(t)
=(d-1)\left[\frac{t(1-\lambda)}{m_2}-\frac1{2t}\right]
=\frac{(d-1)(t^2r-1)}{2t(1+r)m_2}<0.
\]
The last inequality holds because \(0<t<1\) and the positive root satisfies \(r<1\). This proves strict decrease everywhere, including across the continuous junction. At \(t=0\), substitution gives \(\mathcal R_d(0)=d^d\). As \(t\uparrow1\), the root tends to \(r=1\), so \(\lambda\to1/2\) and \(m_2\to1\), giving the second endpoint.

**4. Sharp phase regularity.** The outer-volume formula is smooth through \(t_c\). The John volume is constant below \(t_c\) and proportional to \((1-t)t^{(d-1)/2}\) above it. Its logarithmic first derivative from above vanishes at \(t_c\), whereas its logarithmic second derivative there equals \(-(d+1)^3/[4(d-1)]\); below it both derivatives vanish. Subtracting logarithms proves the stated one-sided second-derivative jump in \(\log\mathcal R_d\).

## Verification
Run `python3 verify.py` from the extracted package directory (standard-library Python 3). This verifies exact support equalities of the candidate inscribed ellipsoid, both outer-vertex contact-orbit gauges, the covariance/contact identities, ratio bounds, and finite-grid monotonicity for \(2\le d\le16\) at 225 dimension/parameter configurations. Its expected final line begins `VERIFY_OK`. As a separate numerical cross-check, independent constrained optimizations over center and two semiaxes were run for dimensions \(2,3,5\) and truncations \(0.05,0.25,0.6,0.9\). All 24 numerical optimizer problems terminated successfully; the maximum difference of the fitted parameters from the formulas was below \(3.2\times10^{-9}\). Finite checks are corroboration, not substitutes for the exact proof.

## Relationship to prior work
The classical characterization of extremal ellipsoids by weighted contact identities is due to John and Löwner and is used here rather than claimed as new. Lin, Ge and Leng (arXiv:1001.4223, first submitted 24 January 2010) determine the John ellipsoid and contacts for untruncated simplices; they do not give the truncated family. Lasserre (arXiv:1302.1056, first submitted in 2013; version inspected 23 December 2014) develops a much more general minimum-volume polynomial covering framework and recalls Löwner contact conditions; no frustum-specific all-parameter ellipsoid formula is presented there.

In dimension \(d=2\), Rublev and Petunin (1998) already determined the minimum-area enclosing ellipse of arbitrary trapezoids, while Hayes and colleagues (2019) treat largest-area inscribed ellipses of arbitrary convex quadrangles. The two-dimensional specializations here are therefore not assessed as novel. The claimed contribution starts in dimension three.

An exact mixed-volume profile for precisely the same truncated simplex body was published under the title *Exact Godbersen mixed-volume profile for one-vertex simplex truncations*. Its full scientific statement concerns coefficients of \(\operatorname{vol}(K_{d,t}+u(-K_{d,t}))\), not inscribed/circumscribed ellipsoids, contact distributions, or their ratio. *Universal Santaló and volume-product laws for homothetic frusta* treats the same shape class from the viewpoint of polar volumes and Santaló centers; affine volume products do not determine either extremal ellipsoid. *Three-phase John ellipsoid of a capped hypercube* studies the distinct body \([0,1]^d\cap\{\sum x_i\le\tau\}\), whose facet orbit structure differs. Search comparisons included the terms simplex frustum, truncated simplex, one-vertex truncation, John/Löwner, minimum-volume ellipsoid, homothetic simplices, and optimal design. These searches and inspected texts did not identify a prior source giving the present complete ellipsoid pair and sharp monotone ratio, though search absence cannot establish universal historical priority.

## Limitations
The truncation plane must be parallel to the facet opposite the removed vertex, and the two new vertex layers must be homothetic about the same original vertex. Multiple cuts, skew truncations, and arbitrary prismatoids are not covered. The strict ratio lower bound is approached only as the frustum degenerates; it is not attained by a full-dimensional body. This work does not establish optimal volume ratios among all polytopes or convex bodies. The planar trapezoid cases are specifically excluded from any novelty assertion. An equivalent higher-dimensional calculation in older unindexed convex-geometry or optimal-design literature remains possible and requires independent historical review.

## References
1. S. Lin, X. Ge and G. Leng, *The John Theorem for Simplex*, arXiv:1001.4223v1, first submitted 24 January 2010; https://arxiv.org/abs/1001.4223.
2. J. B. Lasserre, *A generalization of Löwner–John's ellipsoid theorem*, arXiv:1302.1056v4, 23 December 2014; https://arxiv.org/html/1302.1056v4.
3. *Exact Godbersen mixed-volume profile for one-vertex simplex truncations*, published published-finding corpus mathematical record, 11 October 2026, identifier `SCOPE-exact-godbersen-mixed-volume-profile-for-one-vertex-simplex-trun--dda979276949`.
4. *Universal Santaló and volume-product laws for homothetic frusta*, published published-finding corpus mathematical record, 11 October 2026, identifier `SCOPE-universal-santal-and-volume-product-laws-for-homothetic-frusta--3dbfdaf0b359`.
5. *Three-phase John ellipsoid of a capped hypercube*, published published-finding corpus mathematical record, 11 October 2026, identifier `SCOPE-three-phase-john-ellipsoid-of-a-capped-hypercube--9b8726b32127`.
6. B. V. Rublev and Yu. I. Petunin, *Minimum-area ellipse containing a finite set of points. II*, Ukrainian Mathematical Journal 50 (1998), 1253–1266, §4 (trapezoids); https://www.mit.edu/~hlb/ellipse-paper.pdf.
7. K. Hayes, B. Copeland, P. Zsombor-Murray and H. Gfrerrer, *Largest Area Ellipse Inscribing an Arbitrary Convex Quadrangle*, 2019 (quadrilateral inscribed-ellipse theory).
