# Exact Geometric Dilation and Its Unique Minimizer Among Convex Kites

## Finding
Let \(K\) be the boundary of a strictly convex Euclidean kite. Up to a rigid motion and scale, its vertices in positive cyclic order are
\[
 A=(0,p),\quad B=(q,0),\quad C=(0,-r),\quad D=(-q,0),
 \qquad p,q,r>0.
\]
Interchange the two axial tips if necessary to take \(p\ge r\). Put
\[
 s=\sqrt{p^2+q^2},\qquad t=\sqrt{r^2+q^2},\qquad
 \alpha=\arctan(p/q),\quad \beta=\arctan(r/q).
\]
For the ordinary Euclidean geometric dilation (maximal ratio of shorter boundary-path length to chord length), the complete shape formula is
\[
 \boxed{\displaystyle
 \delta(K)=\max\left\{\frac{s}{q},
 \frac{\sqrt{q^2(s+t)^2+(pt+rs)^2}}{q(p+r)}\right\}
 =\max\left\{\sec\alpha,
 \frac{2\cos((\alpha-\beta)/2)}{\sin(\alpha+\beta)}\right\}.}
\]
This formula identifies two competing shortest perimeter-halving chord types.

There is, furthermore, exactly one similarity class of **globally dilation-minimizing strictly convex kites**. Its angles \((\alpha_*,\beta_*)\) are the unique solution in
\(\pi/4<\alpha<\pi/3\), \(0<\beta<\alpha\) of
\[
 \boxed{\displaystyle
 2\cos\frac{\alpha-\beta}{2}\cos\alpha=\sin(\alpha+\beta),
 \qquad
 \cot(\alpha+\beta)=\frac12\tan\frac{\alpha-\beta}{2}.}
\]
In particular, the sharp constant and normalized optimal dimensions are
\[
 \boxed{\displaystyle
 \min_{K\ \mathrm{kite}}\delta(K)=\sec\alpha_*
 =1.9237956679610035\ldots,
 \quad p/q=1.6434688229673007\ldots,
 \quad r/q=0.4014691586273084\ldots.}
\]
The symmetry of the kite does **not** force equal axial tip lengths: the unique optimizer is neither a rhombus nor a square. The minimum is attained, not merely approached.

## Assumptions and scope
A kite is a strictly convex four-vertex polygon with two pairs of adjacent equal sides; its boundary is given its Euclidean intrinsic arclength metric. The dilation is
\[
 \delta(K)=\sup_{x\ne y\in K}
 \frac{\min\{\ell_1(x,y),\ell_2(x,y)\}}{|x-y|},
\]
where \(\ell_1,\ell_2\) are the lengths of the two connecting boundary arcs. All formulas hold for every \(p,q,r>0\); relabeling permits \(p\ge r\). No claim is made for arbitrary quadrilaterals or for nonconvex kites. The classification is up to Euclidean similarity, rigid motions and interchange of axial tips.

## Proof
**1. Halving chords.** A standard theorem for convex closed curves states that
\(\delta(K)=L/(2h)\), where \(L\) is the perimeter and \(h\) is the smallest chord between points whose two connecting arcs each have length \(L/2\) [1, Lemma 1]. Here \(L=2(s+t)\); set \(H=s+t=L/2\). Parameterize the boundary from \(A\) to \(B\) to \(C\) to \(D\) and back to \(A\), by distance \(u\). Reflection across the axial diagonal and the halving involution let us minimize over \(0\le u\le H/2\). Because \(s\ge t\), the first endpoint lies on \(AB\). When \(0\le u\le t\), the other endpoint lies on \(CD\), and their difference vector has the form
\[
 \left(qu\left(\frac1s+\frac1t\right),\quad
 p+r-u\left(\frac ps+\frac rt\right)\right).
\]
The unconstrained minimum length of this affine vector over the real line is
\[
 h_0=\frac{q(p+r)(s+t)}{\sqrt{q^2(s+t)^2+(pt+rs)^2}}.
\]
When \(t\le u\le H/2\), the other endpoint instead lies on \(DA\), and the difference vector is
\[
 \left(q\left(1+\frac ts\right),\quad
 p\left(1+\frac{t-2u}{s}\right)\right).
\]
Its minimum occurs at \(u=H/2\), yielding \(h_1=q(1+t/s)\).

For rigor, an unconstrained minimizer of the first affine vector might lie beyond \(u=t\). Write
\[
 E=q^2(s+t)^2+(pt+rs)^2,
 \qquad F=E-s^2(p+r)^2,
 \qquad G=q^2(s+t)^2-p(s-t)(pt+rs).
\]
We have \(h_0<h_1\) precisely when \(F>0\), whereas the first unconstrained minimizer lies before \(u=t\) precisely when \(G>0\). The identity
\[
 G-F=ps(p+r)(s-t)\ge0
\]
shows that whenever \(h_0\) is the better candidate, it is attained within its legitimate interval. Otherwise \(h_1\) is attained and is no larger than the first-interval minimum. Consequently \(h=\min\{h_0,h_1\}\), and \(\delta(K)=H/h\) gives the first boxed formula. The trigonometric version follows upon substituting \(p=q\tan\alpha\), \(r=q\tan\beta\).

**2. Optimize the two branches.** Consider
\[
 f(\alpha,\beta)=\frac{2\cos((\alpha-\beta)/2)}{\sin(\alpha+\beta)},
 \qquad 0<\beta\le\alpha<\pi/2.
\]
For \(\alpha\le\pi/4\), let \(X=(\alpha+\beta)/2\), \(Y=(\alpha-\beta)/2\). Since \(2X+Y=(3\alpha+\beta)/2\le\pi/2\), one has \(\cos Y\ge\sin(2X)\), hence \(f\ge2\). These shapes cannot attain the global value below \(2\).

Fix \(\pi/4<\alpha<\pi/2\). The derivative of \(\log f\) in \(\beta\) is
\[
 g_\alpha(\beta)=\frac12\tan\frac{\alpha-\beta}{2}-\cot(\alpha+\beta),
 \quad g'_\alpha(\beta)=\csc^2(\alpha+\beta)-\frac14\sec^2\frac{\alpha-\beta}{2}>0.
\]
Indeed, \(\csc^2\ge1\) and the second summand is less than \(1/2\). Also \(g_\alpha(\alpha)=-\cot(2\alpha)>0\). Thus the unique minimizing \(\beta_\alpha\) either equals \(0\) in the closed extension or is the unique interior zero of \(g_\alpha\). In either case its angle sum is less than \(\pi/2\): an interior zero has positive cotangent, while a boundary zero has \(\alpha<\pi/2\). Set \(m(\alpha)=\min_{0\le\beta\le\alpha}f(\alpha,\beta)\). By the envelope theorem or direct one-sided comparison,
\[
 \frac{d}{d\alpha}\log m(\alpha)
 =-\frac12\tan\frac{\alpha-\beta_\alpha}{2}-\cot(\alpha+\beta_\alpha)<0
\]
wherever the derivative is taken, including the boundary formula when \(\beta_\alpha=0\). Thus \(m\) is continuous and strictly decreasing, whereas \(\sec\alpha\) is strictly increasing. At \(\alpha=\pi/4\), one has \(m=2>\sqrt2=\sec\alpha\); toward \(\alpha=\pi/2\), \(\sec\alpha\) diverges while \(m\le f(\alpha,0)\) remains bounded. Their curves cross exactly once, and
\[
 \delta(K)\ge\max\{\sec\alpha,m(\alpha)\}
\]
is globally minimized precisely at that crossing, with \(\beta=\beta_\alpha\).

At \(\alpha=\pi/3\), choosing \(\beta=\pi/6\) gives \(m\le2\cos(\pi/12)<2=\sec\alpha\), proving \(\alpha_*<\pi/3\). On \((\pi/4,\pi/3)\), one has \(g_\alpha(0)<0<g_\alpha(\alpha)\), so the optimal \(\beta\) is strictly interior. The crossing and its stationarity are exactly the two boxed equations, establishing existence and uniqueness. Finally, the boundary \(\beta\downarrow0\) is not optimal there, and reflected or rescaled copies account for every optimizer.

## Verification
The standalone standard-library script `verify_kite.py` computes the dilation a second way: it parameterizes **all** perimeter-halving chords, splits at edge changes, and minimizes each squared affine chord exactly over its parameter interval. For a fixed sample of \(1000\) widely varied positive triples, its results agree with the analytic two-branch formula to maximum relative error \(5.28\times10^{-16}\). An independent bisection solves the stationarity/crossing equations and yields the displayed numerical constant; \(21{,}945\) angle-grid comparisons supply an additional finite diagnostic. Run `python verify_kite.py` from the directory containing this document. These finite checks do not establish the universal inequalities or uniqueness: those follow from the proof above.

## Relationship to prior work
Dumitrescu, Ebbers-Baumann, Grüne, Klein and Rote [1] establish the general perimeter-halving characterization and lower bounds for geometric dilation of polygons. In their Section 8.2, their four-gon corollary gives the universal lower bound \(4\tan(\pi/8)\) rather than the kite-specific sharp value, and their centrally symmetric polygon bound yields the rhombus/square benchmark. Neither result gives the two-branch shape formula or the asymmetric kite optimizer. The earlier WADS 2005 version [3] likewise gives only general lower bounds for polygons and symmetric subfamilies, not exact kite optimization. Ebbers-Baumann, Grüne and Klein [2] study broad lower bounds for closed convex curves. This paper has not been checked in complete full text; its treatment is a residual historical-overlap risk. The identity and minimizer above are asserted only for the specified kites and do not imply an all-quadrilateral optimum.

## Limitations
The global minimum is for strict convex kites, not arbitrary quadrilaterals. The source comparisons establish no guarantee that the formula or constant is absent from all historical, unindexed work; a closely related dissertation and another full paper were not accessible for complete comparison. The minimizer is uniquely specified by a nonlinear system, with numerical values from bisection rather than a polynomial minimal representation. Reproduced finite diagnostics are not a substitute for the analytical proof. Independent validation has not been performed.

## References
[1] A. Dumitrescu, A. Ebbers-Baumann, A. Grüne, R. Klein, and G. Rote, *On the geometric dilation of closed curves, graphs, and point sets*, arXiv:math/0407135, first public posting 2004-07-08, https://arxiv.org/abs/math/0407135 , DOI:10.1016/j.comgeo.2005.07.004. Consulted: full 31-page arXiv PDF, particularly Lemma 1 and Section 8.2.

[2] A. Ebbers-Baumann, A. Grüne, and R. Klein, *Geometric dilation of closed planar curves: New lower bounds*, Computational Geometry 37 (2007), 188–208, DOI:10.1016/j.comgeo.2004.12.009. Consulted: bibliographic data and abstract only; complete text unavailable during comparison.

[3] A. Dumitrescu, A. Ebbers-Baumann, A. Grüne, R. Klein, and G. Rote, *On geometric dilation and halving chords*, WADS 2005, https://page.mi.fu-berlin.de/rote/Papers/pdf/On+geometric+dilation+and+halving+chords.pdf , DOI:10.1007/11534273_22. Consulted: full 12-page PDF, especially Section 5.2.
