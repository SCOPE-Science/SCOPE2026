# A universal surface–volume identity for hulls of concurrent circular disks

## Finding

For \(k\ge2\) congruent disks in distinct planes sharing their center and a common diameter, write their successive unoriented plane-angle gaps as \(\delta_1,\ldots,\delta_k>0\) with \(\sum_j\delta_j=\pi\). If the disks have radius \(R>0\), their convex hull \(K\) satisfies

\[
\operatorname{Vol}_3(K)=\frac{4R^3}{3}\sum_{j=1}^k\sin\delta_j,\qquad
\operatorname{Area}_2(\partial K)=2\pi R^2+2R^2\sum_{j=1}^k\sin\delta_j.
\]

Consequently the **surface–volume identity**

\[
\operatorname{Area}_2(\partial K)=2\pi R^2+\frac{3}{2R}\operatorname{Vol}_3(K)
\]

holds independently of the number and angular arrangement of the disks. For a fixed number \(k\) of distinct planes, volume and surface area are jointly maximized only when consecutive plane angles are equal:

\[
\operatorname{Vol}_3(K)\le\frac{4kR^3}{3}\sin\frac{\pi}{k},\qquad
\operatorname{Area}_2(\partial K)\le 2\pi R^2+2kR^2\sin\frac{\pi}{k}.
\]

The two sharp infima, neither attained for distinct planes, are respectively \(0\) and \(2\pi R^2\). When \(k\to\infty\), the maximizing hulls converge to the radius-\(R\) Euclidean ball, and their volumes and areas converge to \(4\pi R^3/3\) and \(4\pi R^2\).

## Assumptions and scope

Let \(L\) be a line through the common center, and choose orthonormal coordinates \((x,y)\in\mathbb R\times\mathbb R^2\) with \(x\) along \(L\). The unoriented supporting planes are \(\mathbb R\times\mathbb R u_j\), where \(u_j=(\cos\theta_j,\sin\theta_j)\) and the angles are chosen so that

\[
0\le\theta_1<\cdots<\theta_k<\pi,\qquad
\theta_{k+1}=\theta_1+\pi,\qquad
\delta_j=\theta_{j+1}-\theta_j.
\]

Each disk is \(D_j=\{(x,tu_j):x^2+t^2\le R^2\}\). Define the full-dimensional centrally symmetric cyclic polygon \(Q=\operatorname{conv}\{\pm u_1,\ldots,\pm u_k\}\subset\mathbb R^2\). All measures are ordinary Euclidean volume and two-dimensional Hausdorff surface area; no probability measure is involved.

## Proof

**1. Exact sections.** Let \(g_Q\) be the gauge of \(Q\), a norm because \(Q\) is centrally symmetric with nonempty interior. The set

\[
B=\{(x,y)\in\mathbb R\times\mathbb R^2:x^2+g_Q(y)^2\le R^2\}
\]

is convex. Indeed \(g_Q\) is convex and nonnegative, and the Euclidean norm on \(\mathbb R\times[0,\infty)\) is convex and nondecreasing in the second coordinate. Every \(D_j\) lies in \(B\). Conversely, for fixed \(|x|\le R\), the section \(B_x=\sqrt{R^2-x^2}\,Q\) is the planar convex hull of the sections \((D_j)_x=[-\sqrt{R^2-x^2}u_j,\sqrt{R^2-x^2}u_j]\) of the original disks. Its points therefore belong to \(\operatorname{conv}(\bigcup_j D_j)\), using convex combinations within that same section. Thus \(K=B\), with the exact section formula

\[
K_x=\sqrt{R^2-x^2}\,Q\quad(-R\le x\le R).
\]

**2. Volume.** For the \(2k\) vertices of \(Q\), the cyclic successive angular gaps are the \(k\) values \(\delta_1,\ldots,\delta_k\), each repeated twice. The shoelace formula on the unit circumcircle gives

\[
\operatorname{Area}_2(Q)=\frac12\sum_{\text{all }2k\text{ gaps }\gamma}\sin\gamma
=\sum_{j=1}^k\sin\delta_j.
\]

Fubini applied to the exact sections yields

\[
\operatorname{Vol}_3(K)=\int_{-R}^R(R^2-x^2)\operatorname{Area}_2(Q)\,dx
=\frac{4R^3}{3}\operatorname{Area}_2(Q).
\]

**3. Surface area.** The lateral surface associated with a side of \(Q\), between consecutive unit vertices \(u,v\) subtending \(\gamma\in(0,\pi)\), admits the parametrization, initially for \(R=1\),

\[
F(x,t)=\big(x,\sqrt{1-x^2}\,[(1-t)u+tv]\big),\qquad -1<x<1,\quad0<t<1.
\]

The cross-product Jacobian has magnitude

\[
\lVert\partial_xF\times\partial_tF\rVert
=2\sin(\gamma/2)\sqrt{1-x^2\sin^2(\gamma/2)}.
\]

Integration over \(x\in[-1,1]\) and \(t\in[0,1]\) gives exactly \(\gamma+\sin\gamma\), using \(0<\gamma<\pi\) to identify \(\arcsin(\sin(\gamma/2))=\gamma/2\). Patches overlap only along curves of zero surface area. Summing over all \(2k\) sides gives \(2\pi+2\sum_j\sin\delta_j\). Scaling by \(R^2\) completes the surface formula and the surface–volume identity.

**4. Sharp optimization.** Each gap satisfies \(0<\delta_j<\pi\) and \(\sum_j\delta_j=\pi\). Since sine is strictly concave on \((0,\pi)\), Jensen's inequality yields

\[
\sum_{j=1}^k\sin\delta_j\le k\sin(\pi/k),
\]

with equality only for the equal-gap configuration. All pairs of distinct planes are represented by these gaps, up to a global angular rotation. To approach the lower endpoints, let \(k-1\) positive gaps tend to zero, so the remaining gap tends to \(\pi\), and all sine terms tend to zero. For each nondegenerate configuration all terms are positive, so the infima are unattained. Finally, \(k\sin(\pi/k)\to\pi\), establishing both limits.

## Verification

The accompanying `verify.py` uses two independent numerical methods. It constructs actual three-dimensional point sets from evenly sampled boundary circles and computes the convex-hull volume and surface area with `scipy.spatial.ConvexHull`, then compares against the exact formulas. Separately, Gauss–Legendre quadrature of the lateral Jacobians checks the integrated surface expression. Cases include two perpendicular disks, a nonright pair, generic configurations with three or four disks, and the regular five-plane case. For 300 samples per circle, relative polyhedral errors are below \(1.1\times10^{-4}\). A fixed-seed check of 2,030 random positive angular-gap vectors and regular cases for \(2\le k\le19\) checks the sharp extremal inequality numerically. Running `python verify.py` prints `VERIFY_OK`. The proof is analytic and does not depend on these finite tests.

## Relationship to prior work

Finch's *Convex Hull of Two Orthogonal Disks* (first public arXiv version 2012-11-19, arXiv:1211.4514) establishes the special case of two perpendicular, concentric unit disks, obtaining \(V=8/3\) and \(S=2(2+\pi)\); those constants are not claimed here as new. Finch also studies two other two-disk configurations with displaced centers. Bäsel (arXiv:1604.07245) studies the displaced-center oloid, and Nash–Pir–Sottile–Ying (arXiv:1612.09382) classify algebraic boundaries and face lattices of hulls of two circles, not simultaneous metric identities for an arbitrary finite common-diameter family. The all-\(k\), arbitrary-plane-angle surface–volume identity and its equality-classified optimal arrangements are not supplied by these inspected results. This comparison is not a proof of historical priority.

## Limitations

The equal radii, common centers and common diameter are essential hypotheses; neither the identity nor the extremal classification is asserted for displaced or unequal disks, arbitrary ellipses, or general families of circles. The theorem concerns Euclidean surface area, not mean width. The two-disk right-angle case is established prior work. Related earlier sources not located by the literature searches could affect priority. Independent external validation has not been performed.

## References

1. S. R. Finch, *Convex Hull of Two Orthogonal Disks*, arXiv:1211.4514, first submitted 2012-11-19; https://arxiv.org/abs/1211.4514. Relevant material: opening and Section 1, especially the exact area and volume calculations.
2. U. Bäsel, *The mean width of the oloid and integral geometric applications of it*, arXiv:1604.07245, first submitted 2016-04-25; https://arxiv.org/abs/1604.07245. Relevant material: introduction and Sections 2–3.
3. E. D. Nash, A. F. Pir, F. Sottile, L. Ying, *Convex Hull of Two Circles in \(\mathbb R^3\)*, arXiv:1612.09382, first submitted 2016-12-30; https://arxiv.org/abs/1612.09382. Relevant material: introduction and the edge-surface/face-lattice analysis.
