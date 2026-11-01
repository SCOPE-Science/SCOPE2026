# Sharp two-moment ambiguity and three-statistic recovery of spherical latitude zones

## Finding

Let \(S^2\) be the unit Euclidean sphere and consider the latitude zone
\[
K_{m,h}=\{x\in S^2:m-h\le x_3\le m+h\},\qquad 0<h\le1,\quad |m|+h\le1.
\]
Take three independent points \(X_1,X_2,X_3\), each uniform with respect to surface area on this zone. Set \(Q_{ij}=\|X_i-X_j\|^2\) (squared *ambient Euclidean* chord distance) and define the observable moment statistics
\[
M=\mathbb E Q_{12},\qquad V=\operatorname{Var}(Q_{12}),\qquad C=\operatorname{Cov}(Q_{12},Q_{13}).
\]
With \(u=m^2\) and \(z=h^2\), they obey the **exact identities**
\[
\boxed{M=2(1-u),\quad V=2(1-u)^2+4(u-1/3)z+(2/3)z^2,\quad C=(4/3)uz.}
\]
The admissible parameter domain is \(0\le u<1\) and \(0<z\le(1-\sqrt{u})^2\). Reflection in the equator exchanges \(m\) and \(-m\), so at best the zone can be identified up to this isometry.

**Sharp two-moment ambiguity.** The pair \((M,V)\) determines the zone up to reflection whenever \(M\notin(4/3,3/2)\). When \(4/3<M<3/2\), the same two moments can instead arise from **exactly two different zone widths**, and never from more than two. The fold is explicitly
\[
\boxed{V=\frac43-4u^2+\frac23\big(z-(1-3u)\big)^2,\qquad z_*=1-3u.}
\]
It lies in the interior of the admissible width interval if and only if \(1/4<u<1/3\), precisely the displayed ambiguity window in \(M\). For example, setting \(u=3/10\), the distinct widths \(z=3/50\) and \(z=7/50\) both give
\[
M=\frac75,\qquad V=\frac{609}{625},
\]
but their shared-endpoint covariances are respectively \(3/125\) and \(7/125\). The two zones are nondegenerate and not congruent.

**Exact three-statistic recovery.** The triple \((M,V,C)\) uniquely determines \(|m|\) and \(h\), and hence the zone up to reflection, throughout the entire admissible domain. If \(u>0\), already \((M,C)\) suffices, via
\[
\boxed{u=1-M/2,\qquad z=\frac{3C}{4u}.}
\]
If \(u=0\), then \(M=2\) and \(C=0\) for every equator-centered zone, but the remaining statistic recovers its width through
\[
\boxed{z=1-\sqrt{(3V-4)/2}.}
\]
In particular, the shared-endpoint covariance resolves the entire two-branch ambiguity when \(u>0\), while the variance resolves the covariance's equatorial blind spot.

## Assumptions and scope

The sphere has unit radius; surface area, rather than solid angle from a displaced center or latitude angle, defines uniformity. The zone may have one boundary circle (a polar cap), two boundary circles (an ordinary latitude band), or neither (the whole sphere). Positive half-height \(h>0\) is essential. The data involve squared Euclidean lengths rather than great-circle distances. All recovery statements concern exact population moments, not noisy finite-sample estimates. Only congruence classes under sphere isometries are considered.

## Proof

**1. Surface-coordinate law.** Write \(x=(\sqrt{1-t^2}\cos\phi,\sqrt{1-t^2}\sin\phi,t)\), with \(-1\le t\le1\) and \(0\le\phi<2\pi\). The spherical area element is \(dt\,d\phi\); hence for a surface-uniform point in \(K_{m,h}\), \(t\) is uniform on \([m-h,m+h]\), \(\phi\) is uniform on \([0,2\pi)\), and the two coordinates are independent. Therefore
\[
\mathbb E X=(0,0,m),\qquad \mathbb E t^2=m^2+h^2/3=u+z/3,
\]
and its uncentered second-moment matrix is
\[
T=\mathbb E[XX^{\mathsf T}]=\operatorname{diag}\left(\frac{1-u-z/3}{2},\frac{1-u-z/3}{2},u+z/3\right).
\]

**2. Two-point moments.** Independence and \(\|X_i\|=1\) give \(Q_{12}=2-2X_1\cdot X_2\), \(\mathbb E(X_1\cdot X_2)=\|\mathbb E X\|^2=u\), and
\[
\mathbb E[(X_1\cdot X_2)^2]=\operatorname{tr}(T^2).
\]
Consequently \(M=2(1-u)\), and
\[
V=4\big(\operatorname{tr}(T^2)-u^2\big)
=2(1-u)^2+4(u-1/3)z+(2/3)z^2.
\]
Completing the square gives the asserted fold identity with no limiting approximation.

**3. Shared-endpoint covariance.** Conditional on \(X_1\), the random variables \(Q_{12}\) and \(Q_{13}\) are independent, each with conditional mean \(2-2X_1\cdot\mathbb E X=2-2mt_1\). The law of total covariance therefore gives
\[
C=\operatorname{Var}(2-2mt_1)=4m^2\operatorname{Var}(t_1)=4uz/3.
\]
This establishes the formulas even when the zone includes either pole or is the whole sphere.

**4. Exact inverse multiplicity.** At fixed \(M\), \(u=1-M/2\) is fixed and the admissible interval is \(0<z\le z_{\max}=(1-\sqrt u)^2\). The variance is a strictly convex quadratic in \(z\), whose vertex lies at \(z_*=1-3u\). This vertex is strictly inside the physical interval precisely when \(z_*>0\) and \(z_*<z_{\max}\). The first inequality says \(u<1/3\); the second simplifies, for \(u>0\), to \(2\sqrt u<4u\), or \(u>1/4\). When the vertex is outside or on the boundary, \(V\) is one-to-one in \(z\). When it is strictly inside, the values at \(z_*\pm\varepsilon\) coincide for every sufficiently small positive \(\varepsilon\), and no convex quadratic can have more than two inverse values. The parameters \(u=3/10\), \(z=3/50\) and \(7/50\) satisfy \(\sqrt u+\sqrt z<1\) and give the exact witness above. Finally, \(M=2(1-u)\) turns \(1/4<u<1/3\) into \(4/3<M<3/2\).

**5. Complete inversion.** When \(u>0\), the identities for \(M,C\) directly recover \(u,z\). When \(u=0\), the variance identity reduces to \(V=4/3+(2/3)(1-z)^2\); since \(0<z\le1\), the stated square-root inversion is unique. The sign of \(m\) remains unidentifiable because reflection across the equatorial plane preserves every Euclidean chord statistic and maps \(K_{m,h}\) onto \(K_{-m,h}\). Thus the symmetry limitation is unavoidable.

## Verification

The companion file `check_zone_moments.py` requires Python 3 with no additional packages. Run `python3 check_zone_moments.py` in the same directory. It checks the rational fold identity and an exact ambiguous pair, scans the sharp branch threshold, tests the recovery equations and fixed-area ordering, and independently simulates squared chord moments and shared-endpoint covariance for seven surface-uniform latitude zones. Successful output ends with `ALL_CHECKS_PASSED`. The inequalities and identification statements for all admissible real parameters follow from the analytic proof; finite numerical checks are corroborative only.

## Relationship to prior work

Moseeva, Tarasov and Zaporozhets (2020) provide a general geodesic-distance/chord relation for spherical *convex* bodies and a distance density for spherical caps of radius less than a hemisphere. This is the primary literature motivation for identifying precise geometry from random-distance data. An ordinary two-boundary latitude zone is not spherical convex in their line-free-cone sense, and neither their cap density nor their general spherical-convex-body identity states this two-moment inverse fold or shared-endpoint three-point recovery. Sidiropoulos (2014) gives the complete *whole-sphere* Euclidean chord distribution and its moments, furnishing the special benchmark \(M=2\), \(V=4/3\) when \(m=0,h=1\). Neither work is claimed as new here. The present result treats an explicitly parameterized, generally nonconvex family and the inverse multiplicity of its low-order chord statistics.

## Limitations

The result neither determines the entire pairwise distance law for arbitrary zones nor extends to intrinsic geodesic distance without additional analysis. Recovery uses population moments; no finite-sample confidence bounds or robustness under noise are asserted. Historical priority is provisional: specialized earlier literature describing the same zonal inverse fold under different distance-statistic terminology could exist. The proof needs only the elementary surface-coordinate law and second-moment identities, so numerical checks are not evidence of universal correctness by themselves.

## References

1. T. Moseeva, A. Tarasov, D. Zaporozhets, *Random sections of spherical convex bodies*, arXiv:2007.07297v1 (public 14 July 2020), https://arxiv.org/abs/2007.07297 . Sections 1–3, especially Theorem 2.1 and Corollary 2.2.
2. P. Sidiropoulos, *N-sphere chord length distribution*, arXiv:1411.5639v1 (public 20 November 2014), https://arxiv.org/abs/1411.5639 . Sections II–IV, especially whole-sphere moments and dot products.
