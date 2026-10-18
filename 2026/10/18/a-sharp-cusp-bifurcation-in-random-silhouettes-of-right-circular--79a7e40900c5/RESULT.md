# A sharp cusp bifurcation in random silhouettes of right circular cones

## Finding

For a solid right circular cone with circular base radius \(r>0\) and perpendicular height \(h>0\), let \(k=h/r\). A viewing direction is Haar-uniform on the sphere, and its orthogonal silhouette area divided by \(r^2\) is denoted \(Y\). There exists an exact critical aspect \(k_*\) for which the qualitative distribution of \(Y\) changes.

Define \(\beta_*\) as the unique number in \((\pi/4,\pi/2)\) satisfying
\[
\tan(2\beta_*)=-2(\pi-\beta_*),\qquad
k_* = \sqrt{\frac{2(\pi-\beta_*)}{\sin(2\beta_*)}}=2.14553929088975\ldots .
\]
For \(0<k<k_*\), the area profile is strictly increasing with inclination-coordinate \(t\). At \(k=k_*\) a stationary cubic inflection appears, and the probability density of \(Y\) has an interior cusp with exponent \(-2/3\). For \(k>k_*\), precisely two simple stationary points appear: first a strict local maximum, then a strict local minimum, yielding distinct, one-sided inverse-square-root density singularities.

The exact area profile is classical in substance: the finding asserted here is the **sharp bifurcation, uniqueness of the critical aspect, and its probability-density singularity classification**, not the unqualified novelty of the area formula.

## Assumptions and scope

Let \(t=|\langle n,e_3\rangle|\), where \(n\) is a uniform unit normal to the projection plane. Then \(t\) is uniform on \([0,1]\). Set \(t_0=k/\sqrt{1+k^2}\) and \(B_k(t)=Y\) for the direction with inclination-coordinate \(t\). The cone includes its filled base disk and apex. At all positive aspects,
\[
B_k(t)=
\begin{cases}
\displaystyle \pi t+\sqrt{k^2-(1+k^2)t^2}
-t\arccos\!\left(\frac{t}{k\sqrt{1-t^2}}\right),&0\le t<t_0,\\[5pt]
\pi t,&t_0\le t\le1.
\end{cases}
\]
The values at endpoints and joints are taken by continuity, so \(B_k(0)=k\) and \(B_k(1)=\pi\). We state probability-density asymptotics only at interior critical *values* and interpret the density away from its isolated critical values. All extrema in the theorem are interior in the inclination-coordinate interval \((0,t_0)\).

## Proof

**Silhouette reduction.** Choose the base plane horizontal. Orthogonally projecting the circular disk creates an ellipse of semiaxes \(r\) and \(rt\); the projected apex lies at distance \(h\sqrt{1-t^2}\) from its center along the ellipse's shorter-axis direction. Projection commutes with taking convex hull. The apex is inside this ellipse precisely when \(t\ge t_0\), giving the branch \(\pi t\). Otherwise an affine map taking the ellipse to the unit disk takes the apex to height \(q=k\sqrt{1-t^2}/t>1\). The hull of the disk and that point has area
\[
\pi+\sqrt{q^2-1}-\arccos(1/q).
\]
Indeed, adjoining the two tangent triangles and subtracting the circular cap gives that expression. The affine Jacobian is \(r^2t\). Multiplication gives the displayed profile; the limit \(t\downarrow0\) is \(k\). This establishes the forward formula without relying on any unsupported source-specific assertion.

**Stationary-point reduction.** For \(0<t<t_0\), set
\[
\beta=\arccos\!\left(\frac{t}{k\sqrt{1-t^2}}\right)\in(0,\pi/2).
\]
The change of coordinates \(t=k\cos\beta/\sqrt{1+k^2\cos^2\beta}\) maps \(\beta=\pi/2\) to \(t=0\) and \(\beta=0\) to \(t=t_0\) monotonically. Direct differentiation, with cancellation of the derivative of the square root against part of the arccosine derivative, yields the exact identity
\[
B_k'(t)=\pi-\beta-\frac{k^2}{2}\sin(2\beta).
\]
Thus zeros of \(B_k'\) are exactly the solutions of
\[
k^2=H(\beta),\qquad H(\beta)=\frac{2(\pi-\beta)}{\sin(2\beta)}.
\]
The function \(H\) diverges at both endpoints of \((0,\pi/2)\). On \((0,\pi/4]\) its derivative is strictly negative. On \((\pi/4,\pi/2)\), the equation \(H'(\beta)=0\) is equivalent to \(G(\beta)=0\), where
\[
G(\beta)=\tan(2\beta)+2(\pi-\beta).
\]
Here \(G'(\beta)=2\tan^2(2\beta)>0\), while \(G\to-\infty\) at the left endpoint and \(G\to\pi\) at the right endpoint. There is exactly one solution \(\beta_*\), the strict global minimizer of \(H\). If \(k<k_*\), then \(B_k'>0\) everywhere. For \(k=k_*\) there is one double zero of the derivative but the area profile remains strictly increasing. For \(k>k_*\) there are exactly two simple zeros, and the derivative's sign on increasing \(t\) is positive, negative, positive. Since \(B_k'(t)=\pi\) for \(t\ge t_0\), these are the only stationary points of the entire silhouette-area profile. This proves the sharp bifurcation.

**Probability density and cusp.** Since \(t\) is uniform on \([0,1]\), the density at any regular value \(y\) has the exact inverse-branch representation
\[
f_Y(y)=\sum_{\substack{t\in(0,1):\\B_k(t)=y}}\frac{1}{|B_k'(t)|}.
\]
The mapping has no constant interval, hence no probability atoms. At \(k=k_*\), write
\[
t_c=\frac{k_*\cos\beta_*}{\sqrt{1+k_*^2\cos^2\beta_*}},
\quad y_c=B_{k_*}(t_c),
\quad D=B_{k_*}'''(t_c).
\]
The first two derivatives vanish there, but
\[
D=2k_*^2\sin(2\beta_*)\,[\beta'(t_c)]^2>0,
\qquad
\beta'(t)=-\frac{1}{(1-t^2)\sqrt{k_*^2-(1+k_*^2)t^2}}.
\]
Consequently \(B_{k_*}(t)-y_c=D(t-t_c)^3/6+O((t-t_c)^4)\). Inverting this cubic and differentiating gives the two-sided asymptotic
\[
\boxed{f_Y(y)\sim\frac13\left(\frac6D\right)^{1/3}|y-y_c|^{-2/3}}
\qquad(y\to y_c).
\]
Numerically \(t_c\approx0.8019164250\), \(y_c\approx2.8016694244\), \(D\approx70.5407011\) and the coefficient is approximately \(0.146593902\).

For \(k>k_*\), the two distinct critical points have nonzero second derivatives. The ordinary quadratic Taylor expansion yields a one-sided singularity \(\sqrt{2/|B_k''(t_j)|}\,|y-B_k(t_j)|^{-1/2}\) on the locally attained side of each critical value; additional regular inverse branches contribute bounded density. The full density, including every branch and all endpoints, is determined by the preceding exact inverse-branch formula. No closed elementary inversion of the arccosine branch is asserted.

## Verification

The independent geometric computation in `check.py` projects a 1,536-vertex polygonal approximation of the cone's base and the apex, constructs a fresh monotone-chain convex hull, and compares its shoelace area with the analytic formula for 64 configurations. It separately checks analytic derivatives, confirms five quadrature means against Cauchy's formula, and numerically checks the zero/two stationary-point regimes. Executing `python3 check.py` produced:

`CONE_BRIGHTNESS_BIFURCATION_OK hull_samples=64 expectations=5 cusp_threshold=2.145539290890`

The exact mean check is
\[
\mathbb E[Y]=\frac\pi4\left(1+\sqrt{1+k^2}\right),
\]
which follows independently from Cauchy's projection theorem and the cone's surface area \(\pi r^2+\pi r\sqrt{r^2+h^2}\). Finite checks corroborate, but do not replace, the all-parameter proof.

## Relationship to prior work

Pennell and Deignan (1989) previously computed arbitrary-direction projected areas of right circular cones. Their prior projected-area computation, the cone silhouette geometry, and Cauchy's mean formula are **not** claimed to be new. Their full paper was not accessible for a conclusive priority check of any stationary-point discussion; its publisher abstract and bibliographic record were examined. Vickers (1996), read in accessible full text, develops distributions for ellipsoids and cylinders and explicitly distinguishes cones from those families; it does not cover the cone bifurcation proved here. Related published work on cone directional widths concerns a different measurement, and work on cylinder shadow mixed moments does not imply the conical stationary-point threshold. The originality assessment is therefore provisional pending broader historical checks of cone-optics literature.

## Limitations

The result concerns filled *right circular* cones, Euclidean orthogonal projection, Haar-uniform orientations, and the area statistic. It does not establish results for oblique cones, truncated cones, silhouettes sampled with nonuniform orientation, or noisy finite-sample inference. The exact projected-area profile predates this analysis; the asserted contribution is the qualitative phase theorem and precise singularity exponents. Full access to the 1989 source was unavailable, so definitive historical priority and independent mathematical validation remain open. A print issue of that source is dated June 1989, but its precise original public day was not established; the accompanying date metadata records the verified 2011-05-03 electronic availability of the background survey, not the original 1989 print priority date.

## References

1. S. Pennell and J. Deignan, *Computing the Projected Area of a Cone*, SIAM Review **31** (1989), 299–302. DOI: `10.1137/1031052`. Publisher confirms online posting 2012-02-17; original print issue June 1989.
2. G. T. Vickers, *The projected areas of ellipsoids and cylinders*, Powder Technology **86** (1996), 195–200. DOI: `10.1016/0032-5910(95)03049-F`.
3. S. Kötzer, *Geometric identities in stereological particle analysis*, Image Analysis and Stereology **25** (2006), 63–74. DOI: `10.5566/ias.v25.p63-74`.
4. Classical Cauchy surface-area/mean-projection formula, used here only as an independent numerical normalization check.
