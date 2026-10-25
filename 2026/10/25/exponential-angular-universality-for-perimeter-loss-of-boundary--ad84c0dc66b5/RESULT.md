# Exponential angular universality for perimeter loss of boundary-random polygons

## Finding

Let \(P\) be a strictly convex planar polygon with \(m\ge3\) genuine corners, edge lengths \(\ell_1,\ldots,\ell_m>0\), perimeter \(L=\sum_i\ell_i\), and interior angles \(\alpha_i\in(0,\pi)\). Choose \(N\ge3\) independent points uniformly in arclength on its boundary, and denote their convex hull by \(H_N\). Put \(\Delta_N=L-\operatorname{per}(H_N)\). Write

\[
 c_\alpha=\cos(\alpha/2),\qquad
 \Phi(\alpha)=1-\frac{1-c_\alpha^2}{c_\alpha}\operatorname{artanh}(c_\alpha).
\]

**Exponential finite-sample angular universality.** For every such polygon and every integer \(N\ge3\),

\[
 \left|\mathbb E\Delta_N-\frac{L}{N+1}\sum_{i=1}^m\Phi(\alpha_i)\right|
 \le (m+1)L\sum_{i=1}^m\left(1-\frac{\ell_i}{L}\right)^N.
\]

Consequently, with the polygon fixed, the sole algebraic-scale dependence of its expected perimeter deficit on the number of samples is the universal factor \(1/(N+1)\). If two polygons have the same total perimeter and the same multiset of interior angles, their expected perimeter losses differ by at most a quantity exponentially small in \(N\), even if their edge-length sequences differ.

**Non-Gaussian corner limit.** Let \(E_{i,-},E_{i,+}\), for \(1\le i\le m\), be \(2m\) independent mean-one exponential random variables. Define

\[
 F_\alpha(a,b)=a+b-\sqrt{a^2+b^2-2ab\cos\alpha},\qquad
 Z=\sum_{i=1}^m F_{\alpha_i}(E_{i,-},E_{i,+}).
\]

Then \(N\Delta_N/L\) converges in distribution to \(Z\), with convergence of every positive integer moment. The law is nondegenerate and non-Gaussian, and

\[
 \mathbb EZ=\sum_i\Phi(\alpha_i),\qquad
 \operatorname{Var}(Z)=\sum_i\left(6\Phi(\alpha_i)-4c_{\alpha_i}^2-\Phi(\alpha_i)^2\right).
\]

The limiting-exponential construction is compatible with the local Poisson framework in earlier work; the primary distinction of this result is its exact closed-form angular coefficient and finite-sample error bound exponentially small in the sample count.

## Assumptions and scope

Polygons are compact, convex, with nonempty interior and no collinear consecutive edges; thus each listed interior angle is strictly between zero and \(\pi\). Each sample has uniform arclength distribution on the whole boundary. A hull supported on a segment is assigned its standard convex-geometric perimeter (twice its segment length), which only affects exponentially rare edge-omission events. All probabilities and expectations refer to independent samples. The limit holds for each fixed polygon as \(N\to\infty\); no uniformity is asserted as edge lengths degenerate or the number of corners grows. The stated inequalities use Euclidean lengths and angles.

## Proof

**1. Exact perimeter accounting when every edge is hit.** Parametrize \(\partial P\) by cyclic arclength, with corner \(v_i\) at parameter \(s_i\). Let \(A_i\) and \(B_i\) be the forward and backward nearest-sample arclength distances from \(s_i\). If each original edge carries at least one sample, the convex hull consists, in order, of the outermost sampled segment on each edge and one chord connecting the closest samples on the two edges incident to every corner. Removing the two corner-to-sample portions and substituting this chord reduces perimeter by

\[
 F_{\alpha_i}(A_i,B_i)=A_i+B_i-\sqrt{A_i^2+B_i^2-2A_iB_i\cos\alpha_i}.
\]

Therefore, on this full-edge event \(\mathcal E_N\),

\[
 \Delta_N=\sum_i F_{\alpha_i}(A_i,B_i).
\]

No endpoint coincidences arise with positive probability. On the complement, convex-hull perimeter monotonicity gives \(0\le\Delta_N\le L\), while the triangle inequality and \(A_i+B_i\le L\) give \(0\le\sum_iF_{\alpha_i}(A_i,B_i)\le mL\). Consequently the absolute discrepancy between these two quantities is at most \((m+1)L\mathbf 1_{\mathcal E_N^c}\). An individual edge is empty with probability \((1-\ell_i/L)^N\). The union bound proves

\[
 \left|\mathbb E\Delta_N-\mathbb E\sum_i F_{\alpha_i}(A_i,B_i)\right|
 \le (m+1)L\sum_i(1-\ell_i/L)^N.
\]

**2. The exact Dirichlet-spacing mean.** For a deterministic corner and \(N\ge2\), the joint density of nearest forward and backward sample gaps is

\[
 p_N(a,b)=\frac{N(N-1)}{L^2}\left(1-\frac{a+b}{L}\right)^{N-2},\quad a,b>0,\quad a+b<L.
\]

To see this, place one sample in each infinitesimal endpoint interval and require the remaining \(N-2\) to miss the arc of length \(a+b\); the \(N(N-1)\) ordered choices account for the prefactor. Hence \(S=A+B\) and \(U=A/(A+B)\) are independent, with \(U\) uniform on \((0,1)\) and \(\mathbb ES=2L/(N+1)\). By positive homogeneity,

\[
 \mathbb EF_\alpha(A,B)=\frac{2L}{N+1}
 \int_0^1\left[1-\sqrt{1-2(1+\cos\alpha)u(1-u)}\right]du.
\]

Substitute \(u=(1+t)/2\), put \(c=\cos(\alpha/2)\), and integrate \(\sqrt{1-c^2+c^2t^2}\) on \([0,1]\). One obtains precisely \(\mathbb EF_\alpha(A,B)=L\Phi(\alpha)/(N+1)\), proving the first assertion and its exponential bound.

**3. The independent corner limit.** Fix disjoint small boundary arcs around the finitely many vertices. For positive thresholds on the \(2m\) directed gaps, the probability that no uniform sample falls in the union of the corresponding disjoint arcs is \((1-s/N)^N\to e^{-s}\), after each arc length has been scaled by \(L/N\). Inclusion–exclusion gives joint convergence

\[
 \left(\frac N L A_i,\frac N L B_i\right)_{i=1}^m
 \ \Longrightarrow\ (E_{i,+},E_{i,-})_{i=1}^m
\]

with independent mean-one exponential coordinates. The probability of an empty original edge is exponentially small. Continuous mapping applied to the homogeneous, continuous functions \(F_\alpha\) proves the asserted weak limit of \(N\Delta_N/L\).

For convergence of moments, note that each rescaled one-sided gap has tail at most \(e^{-t}\) for \(0\le t\le N\), and is bounded above by \(N\). On the full-edge event, \(N\Delta_N/L\le\sum_i N(A_i+B_i)/L\), whose fixed positive moments are bounded uniformly in \(N\), and indeed all larger fixed moments are bounded. On the exceptional event, \(N\Delta_N/L\le N\) and \(\mathbb P(\mathcal E_N^c)\) decays exponentially. Uniform integrability of every fixed integer power follows.

**4. Explicit limiting moments.** An equivalent representation for each independent corner contribution is \(Gg_\alpha(U)\), where \(G\sim\operatorname{Gamma}(2,1)\), \(U\sim\operatorname{Uniform}(0,1)\), independent, and

\[
 g_\alpha(u)=1-\sqrt{1-4c_\alpha^2u(1-u)}.
\]

Integration gives \(\int_0^1g_\alpha(u)du=\Phi(\alpha)/2\) and \(\int_0^1g_\alpha(u)^2du=\Phi(\alpha)-2c_\alpha^2/3\). Since \(\mathbb EG=2\) and \(\mathbb EG^2=6\), the stated mean and variance follow. Every \(g_\alpha\) is positive on the interior of \((0,1)\), so \(Z\) is nondegenerate and supported on \([0,\infty)\); it therefore cannot have a nondegenerate Gaussian distribution.

## Verification

Run the standalone standard-library Python program \(`python3 verify.py`\). It checks the full-edge chord decomposition against convex-hull perimeter computations for multiple polygons, the closed-form angle integral and variance against independent numerical quadrature, and the leading expected deficit against repeated random samples of a rectangle. These finite tests support reproducibility but do not replace the proof for all polygons and sample counts.

## Relationship to prior work

Reitzner–Schütt–Werner (arXiv:1911.05917, 2019) establish combinatorial and missing-volume asymptotics for random convex hulls of samples on polytope boundaries, not this explicit perimeter-loss formula. Prochno–Schütt–Sonnleitner–Werner (arXiv:2404.02870, 2024) study expected Hausdorff approximation of boundary-random polygons and develop local independent-corner Poisson limits. Those limits furnish a route to the distributional part above, so that aspect alone is not asserted as an independent conceptual innovation. Their computed quantity is a maximum-type Hausdorff error; the finite-sample universal mean, its exact angle function, and exponentially small edge-length remainder instead arise from the complete perimeter accounting and exact gap density here. Smooth-boundary Gaussian results of Turchi–Wespi (arXiv:1706.02944, 2017) concern bodies without polygonal corners and do not imply this corner-dominated law.

## Limitations

The estimate becomes weak for small sample counts or very short edges. It does not assert that finite-sample expected deficits are exactly angle-only, nor that all polygonal shape information disappears; the exponentially small correction can depend on edge lengths. No uniform estimate is claimed under polygon degeneration. The limiting fluctuation law is built from an existing type of local corner Poisson convergence; priority for related perimeter formulas outside the inspected literature is not fully resolved. The analytic proof has not undergone independent validation.

## References

1. M. Reitzner, C. Schütt, E. M. Werner, *The convex hull of random points on the boundary of a simple polytope*, arXiv:1911.05917 (first public version 2019-11-14); DOI:10.1007/s00454-022-00460-2.
2. J. Prochno, C. Schütt, M. Sonnleitner, E. M. Werner, *Random approximation of convex bodies in Hausdorff metric*, arXiv:2404.02870 (first public version 2024-04-03), especially Theorem 1 and the local vertex analysis in Section 2.
3. N. Turchi, F. Wespi, *Limit theorems for random polytopes with vertices on convex surfaces*, arXiv:1706.02944 (first public version 2017-06-09).
