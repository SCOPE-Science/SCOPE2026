# Strict volume monotonicity and a sharp two-term defect for orthogonal hypercylinders

## Finding

For each integer \(n\ge 2\), let
\[
 C_n=\bigcap_{i=1}^{n}\left\{x\in\mathbb R^n:\sum_{j\ne i}x_j^2\le1\right\}
 =\left\{x\in\mathbb R^n:\|x\|_2^2-\min_i x_i^2\le1\right\},
\]
and let \(\kappa_n=\pi^{n/2}/\Gamma(1+n/2)\) be the volume of the unit Euclidean ball. The normalized volume \(R_n=\operatorname{Vol}_n(C_n)/\kappa_n\) has the exact integral representations
\[
 \boxed{R_n=\frac{2n}{\sqrt\pi}\int_0^\infty\operatorname{erfc}(t)^{n-1}\,dt
 =n\int_0^1(1-u)^{n-1}\exp\big((\operatorname{erf}^{-1}u)^2\big)\,du.}
\]
**The normalized volume decreases strictly with dimension:**
\[
 \boxed{\frac4\pi=R_2>R_3>R_4>\cdots>1.}
\]
Its excess over the ball volume has the **sharp two-term asymptotic**
\[
 \boxed{R_n=1+\frac{\pi}{2(n+1)(n+2)}
 +\frac{7\pi^2}{4(n+1)(n+2)(n+3)(n+4)}+O(n^{-6}).}
\]
In particular \(\lim_{n\to\infty}n^2(R_n-1)=\pi/2\), whereas the maximal radial excess \(\max_{x\in C_n}\|x\|_2-1=\sqrt{n/(n-1)}-1\) has order \(1/n\). The dimension-dependent volume and radial defects therefore decay at different orders.

## Assumptions and scope

A cylinder in the definition means the unbounded unit-radius \((n-1)\)-dimensional Euclidean cylinder about the \(i\)-th coordinate axis; the intersection is bounded and full-dimensional. Volume is Lebesgue measure with the stated Euclidean normalization. The family is defined for **all integers \(n\ge2\)**. The asymptotic is as \(n\to\infty\) along integers. \(\operatorname{erf}\) and \(\operatorname{erfc}=1-\operatorname{erf}\) are the standard Gaussian error and complementary error functions; \(\operatorname{erf}^{-1}\) denotes the inverse on \([0,1)\). No asymptotics for nonorthogonal or unequal-radius cylinders are asserted.

## Proof

**1. An exact minimum-coordinate dissection.** Apart from measure-zero tie sets, each \(x\in C_n\) has one uniquely least-magnitude coordinate, say \(x_i\). On this chamber the strongest of the defining constraints is \(\sum_{j\ne i}x_j^2\le1\). For each selection of the other coordinates \(y\in B_2^{n-1}\), the permissible \(x_i\) range is the interval \([-m(y),m(y)]\), where \(m(y)=\min_j|y_j|\). Symmetry of the coordinate choices thus gives
\[
 \operatorname{Vol}_n(C_n)=2n\int_{B_2^{n-1}}m(y)\,dy.
\tag{1}
\]
Set \(k=n-1\) and let \(U\) be uniform on the unit sphere \(S^{k-1}\). The polar-coordinate radial integral is \(\int_0^1r^k\,dr=1/(k+1)=1/n\), while the sphere area is \(k\kappa_k\). Consequently (1) becomes
\[
 \operatorname{Vol}_n(C_n)=2k\kappa_k\,\mathbb E\min_{1\le j\le k}|U_j|.
\tag{2}
\]
This computation also covers \(n=2\), when the sphere is the two-point set \(S^0\).

**2. Gaussian reduction and normalization.** Let \(Z_1,\ldots,Z_k\) be independent standard normals and put \(T=(\sum_jZ_j^2)^{1/2}\). In the independent polar decomposition \(Z=TU\),
\[
 \mathbb ET=\sqrt2\,\frac{\Gamma((k+1)/2)}{\Gamma(k/2)},\qquad
 \mathbb E\min_j|Z_j|=\int_0^\infty \operatorname{erfc}(s/\sqrt2)^k\,ds.
\]
Combining these identities with \(\kappa_k=\pi^{k/2}/\Gamma(1+k/2)\) in (2), then substituting \(s=\sqrt2t\), yields
\[
 \operatorname{Vol}_n(C_n)=\frac{4\pi^{(n-1)/2}}{\Gamma(n/2)}
 \int_0^\infty\operatorname{erfc}(t)^{n-1}\,dt.
\]
Division by \(\kappa_n=\pi^{n/2}/\Gamma(1+n/2)\) gives the first boxed identity. Set \(u=\operatorname{erf}(t)\). Since \(dt=(\sqrt\pi/2)\exp((\operatorname{erf}^{-1}u)^2)\,du\), the second identity follows.

**3. Strict dimension monotonicity.** Define \(f(u)=\exp((\operatorname{erf}^{-1}u)^2)\), which is strictly increasing on \((0,1)\). If \(W\) is uniform on \((0,1)\), then \(U_n=1-W^{1/n}\) has density \(n(1-u)^{n-1}\) on \((0,1)\). For every \(0<W<1\), \(U_{n+1}<U_n\); hence
\[
 R_{n+1}=\mathbb Ef(U_{n+1})<\mathbb Ef(U_n)=R_n.
\]
All expectations are finite: for \(t>0\),
\[
 e^{t^2}\operatorname{erfc}(t)
 =\frac2{\sqrt\pi}\int_0^\infty e^{-v^2-2tv}\,dv<1,
\]
so \(f(u)<1/(1-u)\), and \(R_n<n/(n-1)\) for \(n>1\). Since \(f(u)>1\) for \(u>0\), also \(R_n>1\). At \(n=2\), the body is the square \([-1,1]^2\), giving \(R_2=4/\pi\). Together these facts prove the strict chain and convergence to one.

**4. Exact leading coefficients and a controlled remainder.** Near \(u=0\), inversion of the error-function series and exponentiation yield the convergent local expansion
\[
 f(u)=1+\frac\pi4u^2+\frac{7\pi^2}{96}u^4+O(u^6).
\tag{3}
\]
For \(U_n\sim\mathrm{Beta}(1,n)\), its moments are
\[
 \mathbb E(U_n^j)=\frac{j!}{(n+1)(n+2)\cdots(n+j)},\qquad j\ge1.
\tag{4}
\]
Fix any \(\delta\in(0,1)\). On \([0,\delta]\) the error in (3) is bounded by a constant times \(u^6\), and its expectation is \(O(n^{-6})\) by (4). On \([\delta,1)\), the estimate \(f(u)\le(1-u)^{-1}\) bounds its expectation by \(n(1-\delta)^{n-1}/(n-1)\), exponentially small. The tails of the polynomial terms in (3) are also exponentially small. Integrating (3) against the beta density and applying (4), with \(2!=2\) and \(4!=24\), proves precisely the two displayed coefficients and an \(O(n^{-6})\) remainder. No finite-order numerical fit is used to establish the expansion.

**5. Geometric comparison with the radial defect.** On a unit direction \(v\in S^{n-1}\), the maximum radius allowed by the cylinder inequalities is
\[
 \rho_{C_n}(v)=(1-\min_i v_i^2)^{-1/2}.
\]
Because \(0\le\min_i v_i^2\le1/n\), the body contains the Euclidean unit ball and has maximal radial extent \(\sqrt{n/(n-1)}\), attained exactly in balanced-absolute-coordinate directions. Therefore its maximal radial excess is \(\sqrt{n/(n-1)}-1=1/(2n)+O(n^{-2})\), whereas its normalized volume excess is \(\pi/(2n^2)+O(n^{-3})\).

## Verification

Run the standalone `verify.py` file using Python with `mpmath` and `sympy`. It independently checks the exact series of \(f\), evaluates the one-dimensional quadrature for several dimensions, checks strict descending values, and compares dimensions \(2\), \(3\), \(4\), and \(5\) with independently known exact-volume benchmarks (adjusted from unit-diameter to unit-radius cylinders). It also measures numerical convergence to the two-term asymptotic. Finite numerical tests support the calculation but do not establish the all-dimensional inequalities or asymptotics; those follow from the preceding analytic proof.

## Relationship to prior work

The classical three-dimensional intersection of three perpendicular cylinders (the tricylinder) has volume \(8(2-\sqrt2)\). Hildebrand, Kong, Turner and Uppal's 2012 report and Kong and coauthors' 2013 report investigate *higher-dimensional* intersecting cylinders. Their published tabulations cover the dimension-four and dimension-five volumes, reproduced in OEIS A349579 and A349580. These special cases, and the existence of the cylinder family, are **not** claimed as novel. The full original reports could not be inspected; hence they cannot be characterized as excluding stronger prior results.

The 2012 work of Finch on a hull of two orthogonal disks treats a different three-dimensional convex-hull operation, rather than the intersection of one coordinate cylinder per ambient dimension. A separate published calculation of the intrinsic volumes of the three-disk convex hull likewise identifies the tricylinder as its polar, but supplies a volume formula for the **hull**, not the present normalized all-dimensional intersection. Neither known three-dimensional formula implies the strict comparison of distinct ambient dimensions or the stated quantitative volume-excess expansion. The contribution asserted here is this dimension-to-dimension monotonicity and sharp two-term asymptotic, not the already-studied low-dimensional exact volumes.

## Limitations

The results concern Euclidean cylinders of equal radius whose axes are the coordinate directions in matching ambient dimension. The full 2012 and 2013 Illinois Geometry Lab reports could not be read during source inspection. Their general descriptions concern precisely these higher-dimensional intersections, so historical-priority uncertainty is substantial and independent full-text comparison is warranted, especially concerning possible all-dimensional reductions. Available published summaries and exact low-dimensional tables do not establish that the reports contain the strict normalized-volume monotonicity or the two-term \(n^{-2}\)/\(n^{-4}\)-scale formula. The theorem's correctness is analytical, but its priority has not been independently established.

## References

1. A. J. Hildebrand, L. Kong, A. Turner and A. Uppal, *Applications of n-dimensional Integrals: Random Points, Broken Sticks and Intersecting Cylinders*, Illinois Geometry Lab project report (first public date 11 December 2012), https://conf.math.illinois.edu/igl/Projects-Fall2012/Hildebrand2/report.pdf .
2. L. Kong, L. Lkhamsuren, A. Turner, A. Uppal and A. J. Hildebrand, *Intersecting Cylinders: From Archimedes and Zu Chongzhi to Steinmetz and Beyond*, Illinois Geometry Lab report (25 April 2013), https://faculty.math.illinois.edu/~hildebr/ugresearch/cylinder-spring2013report.pdf .
3. OEIS, A349579 and A349580 (four-dimensional and five-dimensional perpendicular-cylinder intersections, respectively), https://oeis.org/A349579 and https://oeis.org/A349580 .
4. Steven R. Finch, *Convex Hull of Two Orthogonal Disks*, arXiv:1211.4514 (first submitted 19 November 2012), https://arxiv.org/abs/1211.4514 .
5. *Exact intrinsic volumes and boundary decomposition of the orthogonal three-disk hull*, publicly available mathematical research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-intrinsic-volumes-and-boundary-decomposition-of-the-orthog--14663bdfc53a .
