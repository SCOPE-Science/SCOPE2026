# Two sharp ellipsoid-contact transitions for symmetrically truncated cross-polytopes

## Finding
For every integer \(d\ge3\) and \(0<t\le1\), consider the centrally symmetric coordinate truncation
\[
K_{d,t}=\{x\in\mathbb R^d:\sum_{j=1}^d|x_j|\le1,\ |x_1|\le t\}.
\]
Put \(m=d-1\) and the distinct thresholds
\[
t_{\mathrm L}=1-\sqrt{m/d},\qquad t_{\mathrm J}=d^{-1/2},\qquad 0<t_{\mathrm L}<t_{\mathrm J}<1.
\]
For positive \(A,B,U,V\), write
\[
E(A,B)=\left\{x:\frac{x_1^2}{A^2}+\sum_{j=2}^d\frac{x_j^2}{B^2}\le1\right\},\quad
E(U,V)=\left\{x:\frac{x_1^2}{U^2}+\sum_{j=2}^d\frac{x_j^2}{V^2}\le1\right\}.
\]
The **unique** maximum-volume inscribed (John) ellipsoid of \(K_{d,t}\) is \(E(A,B)\), where
\[
(A,B)=\begin{cases}
\left(t,\sqrt{(1-t^2)/m}\right),&0<t\le t_{\mathrm J},\\
\left(d^{-1/2},d^{-1/2}\right),&t_{\mathrm J}\le t\le1.
\end{cases}
\]
The **unique** minimum-volume containing (Löwner) ellipsoid is \(E(U,V)\), where
\[
(U,V)=\begin{cases}
\left(\sqrt d\,t,\sqrt{d/m}\,(1-t)\right),&0<t\le t_{\mathrm L},\\
\left(\sqrt{t/(2-t)},1\right),&t_{\mathrm L}\le t\le1.
\end{cases}
\]
At the shared endpoints, the two formulas in each piece agree. The Löwner ellipsoid acquires the \(2m\) surviving original vertices as additional contacts at \(t_{\mathrm L}\). The coordinate slabs cease touching the John ellipsoid only after \(t_{\mathrm J}\), giving two different contact thresholds.

Define the ratio of their Euclidean volumes, \(\mathcal R_d(t)=\operatorname{vol}_d(E(U,V))/\operatorname{vol}_d(E(A,B))\). Then its complete exact profile is
\[
\mathcal R_d(t)=\begin{cases}
d^{d/2}\left(\frac{1-t}{1+t}\right)^{m/2},&0<t\le t_{\mathrm L},\\
\displaystyle\frac{m^{m/2}}{\sqrt{t(2-t)}\,(1-t^2)^{m/2}},&t_{\mathrm L}\le t\le t_{\mathrm J},\\
d^{d/2}\sqrt{\frac{t}{2-t}},&t_{\mathrm J}\le t\le1.
\end{cases}
\]
In particular it has a **unique global minimum** at the unique \(t_d\in(t_{\mathrm L},t_{\mathrm J})\) satisfying
\[
\boxed{\quad (d-1)t_d^2(2-t_d)=(1-t_d)^2(1+t_d).\quad}
\]
For every \(0<t<1\), \(\mathcal R_d(t)<d^{d/2}=\mathcal R_d(1)=\lim_{t\downarrow0}\mathcal R_d(t)\). As \(d\to\infty\), the minimizing truncation and its improvement over the untruncated cross-polytope satisfy the sharp laws
\[
\sqrt{2d}\,t_d\longrightarrow1,
\qquad
\frac{\min_{0<t\le1}\mathcal R_d(t)}{d^{d/2}}
\sim (2ed)^{-1/4}.
\]
Thus the optimal truncation improves the ellipsoid-volume ratio by an unbounded factor of order \(d^{1/4}\).

## Assumptions and scope
All ellipsoids, volumes, coordinate slabs and norms are Euclidean in the fixed standard coordinate system; \(d\ge3\), \(0<t\le1\). The body is full-dimensional for exactly these positive parameters. The limit as \(t\downarrow0\) is a degenerate-body limit and does not assert the existence of a full-dimensional extremal ellipsoid at \(t=0\). No arbitrary-orientation or multiple-coordinate-slab statement is claimed.

## Proof
**1. Symmetry and the John problem.** The body is invariant under independent coordinate sign changes and under permutations of coordinates \(2,\dots,d\). Uniqueness of John and Löwner ellipsoids forces each ellipsoid to inherit these symmetries. Both therefore have center zero and diagonal semiaxes \((A,B,\dots,B)\) and \((U,V,\dots,V)\).

The \(\ell_1\)-norm is the maximum of the \(2^d\) signed linear forms. Each such form has maximum \(\sqrt{A^2+mB^2}\) on \(E(A,B)\). Its maximal first-coordinate absolute value is \(A\). Hence containment in \(K_{d,t}\) is **equivalent** to
\[
A\le t,\qquad A^2+mB^2\le1.
\]
The ellipsoid volume is the unit-ball volume times \(AB^m\). At any maximum the second inequality is tight. For \(0<A<1\), the derivative of the logarithm of \(A((1-A^2)/m)^{m/2}\) has the sign of \(1-dA^2\). Thus the unique maximizing axial semiaxis is \(A=\min(t,d^{-1/2})\), giving the asserted \(B\). This global reduction uses the uniqueness theorem, not an unproved guess of the center or axis alignment.

**2. Every vertex and the Löwner problem.** For \(0<t<1\), intersecting the cross-polytope with \(|x_1|\le t\) preserves the \(2m\) vertices \(\pm e_j\) for \(j\ge2\) and cuts precisely the edges from \(\pm e_1\) to \(\pm e_j\). The resulting \(4m\) additional vertices are \(\pm t e_1\pm(1-t)e_j\), with independent signs and \(j\ge2\). At \(t=1\), these formulas collapse to the original vertex set. Hence \(K_{d,t}\subseteq E(U,V)\) holds if and only if
\[
V\ge1,\qquad \frac{t^2}{U^2}+\frac{(1-t)^2}{V^2}\le1.
\]
With positive precision variables \(\alpha=U^{-2}\), \(\beta=V^{-2}\), minimizing \(UV^m\) is equivalent to maximizing the **strictly concave** function \(\log\alpha+m\log\beta\) subject to
\[
\beta\le1,\qquad t^2\alpha+(1-t)^2\beta\le1.
\]
The second constraint is tight at the optimizer. Ignoring \(\beta\le1\) gives \(\alpha=(dt^2)^{-1}\) and \(\beta=m/(d(1-t)^2)\). This point is feasible precisely when \(t\le1-\sqrt{m/d}=t_{\mathrm L}\). Otherwise strict concavity forces the maximum onto \(\beta=1\), with \(\alpha=(2-t)/t\). Taking reciprocal square roots proves both Löwner branches, including the endpoint \(t=1\). The indicated contact classification follows from checking equality at the two vertex orbits: the new cut-edge vertices always touch; the old \(\pm e_j\) touch exactly for \(t\ge t_{\mathrm L}\).

**3. Explicit contact certificates.** For the John ellipsoid, the \(2^d\) facet contacts are the points with coordinates \((\pm A^2,\pm B^2,\dots,\pm B^2)\), which lie on the relevant facets because \(A^2+mB^2=1\). For \(t\le t_{\mathrm J}\) the additional slab contact pair is \(\pm t e_1\). Normalize these contacts by applying \(\operatorname{diag}(A^{-1},B^{-1},\dots,B^{-1})\), then give the signed facet orbit total probability \(\theta=m/[d(1-t^2)]\) and the slab pair total probability \(1-\theta\). The normalized centered covariance is exactly \(I_d/d\). When \(t\ge t_{\mathrm J}\), use only the signed facet orbit, whose normalized coordinates are all \(\pm d^{-1/2}\). These are positive isotropic John contact measures.

For the Löwner ellipsoid when \(t<t_{\mathrm L}\), distribute probability equally over the \(4m\) cut-edge vertices. After normalization by \(\operatorname{diag}(U^{-1},V^{-1},\dots,V^{-1})\), their covariance is \(I_d/d\). For \(t\ge t_{\mathrm L}\), give the cut-edge orbit total mass \(\eta=1/[dt(2-t)]\), and give the old vertex orbit mass \(1-\eta\); these are nonnegative and have normalized covariance \(I_d/d\). In each case the normalized orbit has mean zero. Thus the global optimality assertions also possess explicit positive contact certificates.

**4. Ratio and unique minimizer.** Cancelling the common unit-ball volume gives \(\mathcal R_d=UV^m/(AB^m)\), and substitution gives the stated three formulas. The first branch is strictly decreasing and the third strictly increasing. On the middle branch,
\[
\frac{d}{dt}\log\mathcal R_d(t)
=-\frac{1-t}{t(2-t)}+\frac{mt}{1-t^2}.
\]
Its sign is that of
\[
H_d(t)=mt^2(2-t)-(1-t)^2(1+t).
\]
On \((0,1)\), the first term is strictly increasing (its derivative is \(mt(4-3t)>0\)), and the subtracted term is strictly decreasing (its derivative is \((t-1)(3t+1)<0\)); hence \(H_d\) increases strictly. The branch derivatives agree at both thresholds; their signs are negative at \(t_{\mathrm L}\) and positive at \(t_{\mathrm J}\). Therefore \(H_d\) has exactly one zero \(t_d\) between them. This gives strict descent then strict ascent of the entire ratio, and the endpoint value follows from its first and third formulas.

**5. High-dimensional law.** Since \(t_d<t_{\mathrm J}=d^{-1/2}\), one has \(t_d\to0\). The defining equation then gives \((d-1)t_d^2\to1/2\), hence \(\sqrt{2d}\,t_d\to1\). At this point the middle ratio, divided by \(d^{d/2}\), is exactly
\[
\frac{1}{\sqrt d\sqrt{t_d(2-t_d)}}
\left(1-\frac1d\right)^{(d-1)/2}
(1-t_d^2)^{-(d-1)/2}.
\]
The latter two factors tend to \(e^{-1/2}\) and \(e^{1/4}\), respectively, while \(\sqrt{t_d(2-t_d)}\sim2^{1/4}d^{-1/4}\). Their product gives \((2ed)^{-1/4}\), as claimed.

## Verification
The companion `verification.py` checks containment at all vertex/facet orbits, verifies the isotropic contact-measure identities, independently solves the two strictly concave two-variable optimization problems numerically, and checks the unique minimum and asymptotic normalization. It passed 88 finite parameter configurations in dimensions \(2,3,4,5,7,10,16,30\) (dimension \(2\) is a boundary sanity test, not part of the claim). It checks \(\mathcal R_3(2/5)=125/42\) exactly to floating tolerance. Further asymptotic checks use dimensions \(100,1000,10000\). These finite checks are not an infinite proof; Parts 1–5 above establish the quantified results analytically. Run using Python 3 with NumPy and SciPy: `python verification.py`.

## Relationship to prior work
The classical John and Löwner optimality and symmetry reductions are foundational, not new. Güler and Gürtuna (2007) develop them systematically and compute ellipsoids of Euclidean ellipsoid slabs and truncated second-order cones; their body is not the coordinate-clipped \(\ell_1\) cross-polytope. Liu and Tkocz (2019) study **volumes of hyperplane/slab sections of the cross-polytope**; their Theorem 5 concerns the minimum volume of the slab intersection over slab orientations, not inscribed or enclosing ellipsoids or their ratio. Related ellipsoid formulas for separately clipped Euclidean balls, one-sided capped cubes, and simplex frusta are not logical coverings of the present exact three-phase ratio and its unique minimizer. The contribution assessed here is the simultaneous all-dimensional two-ellipsoid classification for \(K_{d,t}\) together with its two distinct contact thresholds, unique volume-ratio minimum, and sharp \(d^{-1/4}\) relative law—not the general optimality principle itself.

## Limitations
The formula concerns the **one-coordinate symmetric cut** of a regular cross-polytope only. It does not determine ellipsoids for several coordinate cuts, rotated slabs, nonsymmetric truncations, or other norms. A numerical verifier alone would not establish the all-dimensional classification. Although the cited primary texts and accessible relevant research records were compared, no exhaustive independent historical-priority review is claimed; an unindexed older special-case computation remains a residual risk.

## References
1. Osman Güler and Filiz Gürtuna, *The extremal volume ellipsoids of convex bodies, their symmetry properties, and their determination in some special cases*, first public preprint 2007-09-05, arXiv:0709.0707, https://arxiv.org/abs/0709.0707 .
2. Ruoyuan Liu and Tomasz Tkocz, *A note on the extremal noncentral sections of the cross-polytope*, first public preprint 2019-10-15, arXiv:1910.06993, https://arxiv.org/abs/1910.06993 .
