# Antipodal distance tails recover cyclic spherical footballs

## Finding
Let \(F_{q,R}\) be the metric quotient of the round sphere of radius \(R>0\) by the cyclic group of order \(q\ge1\) acting by rotations about one fixed axis. Equip the quotient with intrinsic distance and normalized spherical area. For independent points \(X,Y\) with this measure, put \(D_{q,R}=d(X,Y)\). Every such quotient has diameter \(\pi R\).

For \(q=1\), the ordinary sphere,
\[
 \Pr(D_{1,R}>\pi R-\varepsilon)
 =\frac{1-\cos(\varepsilon/R)}{2}
 \sim \frac14(\varepsilon/R)^2.
\]
For every integer \(q\ge2\),
\[
 \Pr(D_{q,R}>\pi R-\varepsilon)
 = C_q(\varepsilon/R)^4+o((\varepsilon/R)^4),\qquad
 C_q=\frac1{32}\left[\csc^2\left(\frac\pi q\right)-\frac q\pi\cot\left(\frac\pi q\right)\right].
\]
The constants \(C_q\) are strictly decreasing in integer \(q\ge2\), with \(C_2=1/32\) and \(\lim_{q\to\infty}C_q=1/48\). Thus the complete two-point intrinsic-distance law, indeed its diameter and sharp endpoint tail, uniquely determines both \(R\) and \(q\) within this family. For \(q\ge2\), the quotient has precisely two cone points, each with cone angle \(2\pi/q\).

## Assumptions and scope
The ambient sphere is round. The cyclic group rotates about a common polar axis; no action by reflections or other finite groups is included. Area is the normalized two-dimensional quotient Hausdorff/Riemannian measure, whose cone points have zero mass. All distances are shortest intrinsic quotient distances, not ambient Euclidean chord lengths. The expansion fixes \(q\) and \(R\) and sends \(\varepsilon\downarrow0\); no uniform-in-\(q\) remainder is asserted. The event uses a strict inequality, which is immaterial at the endpoint for continuous sampling.

## Proof
Scaling reduces to \(R=1\). Fix \(q\ge2\) and write \(a=\pi/q\in(0,\pi/2]\). Use polar colatitude \(\theta\in[0,\pi]\) and quotient longitude \(\phi\in\mathbb R/(2a\mathbb Z)\). A uniform point has colatitude density \(\sin\theta/2\) and independent uniform longitude. For two independent points, the shortest longitude separation \(\psi\in[0,a]\) is therefore uniform on \([0,a]\), independent of the colatitudes. The quotient metric follows by minimizing the round-sphere distance over group translates:
\[
 \cos D=\cos\theta_1\cos\theta_2
 +\sin\theta_1\sin\theta_2\cos\psi.
\]
In particular, \(D\le\pi\), while the two fixed poles are separated by \(\pi\). This proves the diameter.

Take \(0<\varepsilon<\pi/2\). Because \(\cos\psi\ge0\), if \(D>\pi-\varepsilon\), then
\[
 \cos\theta_1\cos\theta_2\le\cos D<-\cos\varepsilon.
\]
Thus the two colatitudes belong to opposite polar caps of angular radius \(\varepsilon\); there are no other nearly diametral configurations. In one of the two orientations set \(u=\theta_1\) and \(v=\pi-\theta_2\), both between zero and \(\varepsilon\). For \(\delta=\pi-D\),
\[
 \cos\delta=\cos u\cos v-\sin u\sin v\cos\psi.
\]
Accounting for both polar orientations and the normalized area factors gives the exact expression
\[
 \Pr(D>\pi-\varepsilon)=\frac1{2a}
 \int_0^a\!\int_0^\varepsilon\!\int_0^\varepsilon
 \sin u\sin v\,\mathbf1\{\cos u\cos v-\sin u\sin v\cos\psi>\cos\varepsilon\}
 \,dv\,du\,d\psi.
\]
Set \(u=\varepsilon s\), \(v=\varepsilon t\). Taylor expansion of the cosine inequality, uniformly on the compact parameter cube, reduces its interior to
\[
 s^2+t^2+2st\cos\psi<1.
\]
Its boundary has zero three-dimensional Lebesgue measure. Dominated convergence, including the factors \(\sin(\varepsilon s)/\varepsilon\to s\) and \(\sin(\varepsilon t)/\varepsilon\to t\), therefore yields
\[
 \lim_{\varepsilon\downarrow0}\varepsilon^{-4}\Pr(D>\pi-\varepsilon)
 =\frac1{2a}\int_0^a I(\psi)\,d\psi,
 \quad I(\psi)=\int_{s,t\ge0}\!st\,\mathbf1\{s^2+t^2+2st\cos\psi<1\}\,ds\,dt.
\]
For \(0<\psi\le\pi/2\), put \(x=(s+t)/\sqrt2\), \(y=(s-t)/\sqrt2\), then \(y=xz\). This gives the elementary integral
\[
 I(\psi)=\frac14\int_0^1
 \frac{1-z^2}{((1+\cos\psi)+(1-\cos\psi)z^2)^2}\,dz
 =\frac{\sin\psi-\psi\cos\psi}{8\sin^3\psi}.
\]
It extends continuously to \(I(0)=1/24\). Direct integration using the derivative of \(\cot\psi\) gives
\[
 \int_0^a I(\psi)\,d\psi
 =\frac1{16}\bigl(a\csc^2a-\cot a\bigr),
\]
which proves the displayed formula for \(C_q\).

For fixed \(s,t>0\), the quadratic form \(s^2+t^2+2st\cos\psi\) decreases strictly as \(\psi\) increases through \([0,\pi/2]\). Consequently \(I(\psi)\) strictly increases there: the indicator domain gains positive two-dimensional measure. Hence its average \(\frac1a\int_0^a I(\psi)\,d\psi\) strictly increases with \(a\). As \(a=\pi/q\) strictly decreases with \(q\), the constants \(C_q\) strictly decrease. The endpoint evaluations follow from \(I(0)=1/24\) and \(a=\pi/2\).

For \(q=1\), rotational invariance of the round sphere makes \(\cos D\) uniform on \([-1,1]\), proving the exact quadratic endpoint law. Finally, diameter \(\pi R\) recovers \(R\). The quadratic exponent singles out \(q=1\); otherwise \(C_q\) determines the integer \(q\), which proves the inverse statement.

## Verification
`orbifold_metric_check.py` checks 400 independent point pairs for each of four cyclic orders by comparing the quotient cosine formula against explicit minimization over all group rotations. It also compares the asymptotic constants to exact, finite-\(\varepsilon\) two-dimensional Gaussian quadrature for four \(\varepsilon\)-values. `orbifold_quadrature_check.py` provides the quadrature independently of the asymptotic integral; `CHECK_RESULTS.txt` records its evaluation. The maximum tested metric discrepancy is below \(2\times10^{-14}\); the smallest tested normalized tail ratio differs from its analytic limit by less than \(10^{-4}\). These numerical checks corroborate, but do not replace, the analytic proof. Reproduce with Python 3, NumPy, SciPy, and `python orbifold_metric_check.py` in the folder containing the two scripts.

## Relationship to prior work
Borzellino, Jordan-Squire, Petrics and Sullivan study geodesics on spherical orbifolds of revolution, and identify the relevant cone-point geometry; their work does not give random pair-distance endpoint laws. Bacher and Sturm define spherical cones and the spherical cosine-distance formula in a general metric-measure setting; the cosine formula itself is not new here. Tu and Fischbach study Euclidean distances between random points inside spherical balls, rather than intrinsic quotient-sphere distances. Balch, Peterson and Shonkwiler derive full distance distributions for *three-dimensional homogeneous lens spaces*, quotients of the three-sphere by free cyclic actions; the two-dimensional rotation quotient used here has fixed cone points and is not one of their lens spaces. The present contribution is the evaluated fourth-order antipodal tail, its strict dependence on the cone-point order, and the resulting inverse characterization.

## Limitations
Only the stated cyclic rotation quotients of round two-spheres are classified. This does not classify arbitrary spherical metrics, nonsymmetric footballs, unequal cone angles, three-dimensional lens spaces, or general orbifolds. Search results and inspected literature do not constitute a proof of unprecedented novelty; a specialized earlier treatment may exist. The limiting coefficient has a fixed-order asymptotic and no sampling-error bounds are asserted. Independent mathematical assessment remains outstanding.

## References
- J. E. Borzellino, C. R. Jordan-Squire, G. C. Petrics, D. M. Sullivan, *On the Existence of Infinitely Many Closed Geodesics on Orbifolds of Revolution*, arXiv:math/0602595 (first public version 2006-02-27), especially Sections 1, 2, and 7.
- K. Bacher, K.-T. Sturm, *Ricci Bounds for Euclidean and Spherical Cones*, preprint available at https://www.iam.uni-bonn.de/fileadmin/WT/Inhalt/people/Karl-Theodor_Sturm/papers/paper59.pdf, Section 1.1.
- B. Balch, C. Peterson, C. Shonkwiler, *Distributions of Distances and Volumes of Balls in Homogeneous Lens Spaces*, arXiv:2004.13196, especially Sections 1 and 4.
- S.-J. Tu and E. Fischbach, *Random Distance Distribution for Spherical Objects: General Theory and Applications to n-Dimensional Physics*, arXiv:math-ph/0201046 (first public version 2002-01-22), Sections 1 and 2.
