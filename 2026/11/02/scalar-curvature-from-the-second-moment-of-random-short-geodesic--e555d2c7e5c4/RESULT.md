# Scalar curvature from the second moment of random short geodesic distances

## Finding
Let \(n\ge 2\) and let \((M^n,g)\) be a smooth Riemannian manifold. For an interior point \(p\), choose two independent points \(X_r,Y_r\) according to normalized Riemannian volume on the metric ball \(B_g(p,r)\). Write \(D_r=d_g(X_r,Y_r)\). Then
\[
\mathbb E D_r^2=\frac{2n}{n+2}r^2-\frac{n+8}{3(n+2)^2(n+4)}\operatorname{Scal}_g(p)r^4+O_p(r^5).
\]
In particular, the pointwise scalar curvature is determined by the second moment of the unlabeled distance between two independent volume-uniform points in arbitrarily small balls:
\[
\operatorname{Scal}_g(p)=\frac{3(n+2)^2(n+4)}{n+8}\lim_{r\downarrow0}\frac{\frac{2n}{n+2}r^2-\mathbb E D_r^2}{r^4}.
\]
The signal is negative in a positively curved manifold and positive in a negatively curved manifold. The two correction mechanisms, nonuniform normal-coordinate volume and curvature of geodesic distance, have different dimensional coefficients.

## Assumptions and scope
The manifold and its metric are smooth, \(n\ge2\), and \(p\) is an interior point. Work at radii smaller than a convex normal-neighborhood radius of \(p\), so normal coordinates parameterize the ball by \(\{x\in T_pM:\|x\|<r\}\) and intrinsic minimizing geodesics have the standard uniform expansion. Independence and uniformity mean normalized \(d\operatorname{Vol}_g\) restricted to this ball, not Euclidean coordinate-uniform sampling. The symbol \(\operatorname{Scal}_g\) is the trace of Ricci curvature, with round spheres of sectional curvature \(+1\) having scalar curvature \(n(n-1)\). The remainder constant may depend on the local metric at \(p\).

## Proof
Choose orthonormal coordinates at \(p\) and denote Euclidean vectors in \(T_pM\) by \(x,y\). Uniformly for \(\|x\|,\|y\|\le r\), the normal-coordinate volume Jacobian and squared-distance expansion are
\[
J(x)=1-\frac16\operatorname{Ric}_p(x,x)+O_p(r^3),\qquad
 d_g(\exp_p x,\exp_p y)^2=\|x-y\|^2-\frac13R_p(x,y,y,x)+O_p(r^5).
\]
Here the curvature tensor convention satisfies \(R_p(x,y,y,x)>0\) on orthogonal vectors in a positively curved space form. These normal-coordinate expansions are standard; the distance expansion is also explicitly used in Veronelli's Lemma 9. Their error estimates are uniform on the shrinking product ball, which permits integration.

Let \(U\) be Euclidean-volume-uniform in \(B_{\mathbb R^n}(0,r)\), and write \(\mathbb E_0\) for its expectation. Radial symmetry gives
\[
\mathbb E_0 U=0,\quad \mathbb E_0(U_iU_j)=\frac{r^2}{n+2}\delta_{ij},\quad
\mathbb E_0\|U\|^2=\frac{nr^2}{n+2},\quad
\mathbb E_0\|U\|^4=\frac{nr^4}{n+4}.
\]
With \(\mu_r\) the pullback of normalized Riemannian-volume sampling in the geodesic ball, the Jacobian expansion and quotient normalization yield
\[
\begin{aligned}
\mathbb E_{\mu_r}\|x\|^2
&=\mathbb E_0\|U\|^2
-\frac16\left(\mathbb E_0[\|U\|^2\operatorname{Ric}(U,U)]
-\mathbb E_0\|U\|^2\,\mathbb E_0\operatorname{Ric}(U,U)\right)+O_p(r^5)\\
&=\frac{nr^2}{n+2}-\frac{2\operatorname{Scal}_g(p)}{3(n+4)(n+2)^2}r^4+O_p(r^5).
\end{aligned}
\]
Indeed, rotational symmetry gives the Ricci contraction as \(\operatorname{Scal}_g(p)/n\) times the variance of \(\|U\|^2\), and this variance is \(4nr^4/[(n+4)(n+2)^2]\). The mean normal coordinate under \(\mu_r\) is \(O_p(r^4)\), so its squared magnitude is negligible at the displayed order.

For two independent draws, their Euclidean squared separation therefore contributes
\[
\mathbb E_{\mu_r\otimes\mu_r}\|x-y\|^2
=\frac{2nr^2}{n+2}-\frac{4\operatorname{Scal}_g(p)}{3(n+4)(n+2)^2}r^4+O_p(r^5).
\]
To evaluate the curvature term, replace the perturbed volume measures by Euclidean-volume-uniform measures; this changes the fourth-order integral by \(O_p(r^6)\). By independence, the second-moment tensor identity and contraction of the Riemann curvature tensor,
\[
\mathbb E_0\left[R_p(U,V,V,U)\right]
=\frac{r^4}{(n+2)^2}\sum_{i,j}R_p(e_i,e_j,e_j,e_i)
=\frac{\operatorname{Scal}_g(p)}{(n+2)^2}r^4.
\]
Its contribution to squared distance is \(-\operatorname{Scal}_g(p)r^4/[3(n+2)^2]\). Summation gives
\[
-\frac{4}{3(n+4)(n+2)^2}-\frac{1}{3(n+2)^2}
=-\frac{n+8}{3(n+4)(n+2)^2},
\]
which establishes the asserted expansion and curvature-recovery limit for every integer \(n\ge2\).

## Verification
The accompanying `check_curvature.py` verifies the exact rational combination of the two independent curvature corrections in each of dimensions 2 through 20. It separately integrates the **exact spherical and hyperbolic cosine laws** with their correct polar-volume densities in dimensions two and three, using deterministic Gauss–Legendre quadrature. For both curvature signs and both dimensions the inferred fourth-order coefficient converges numerically toward the proved coefficient as the radius shrinks. Executing `python check_curvature.py` prints `ALL_CHECKS_PASSED` when the finite checks succeed. Neither the finite range nor the quadrature establishes the all-dimensional theorem; that conclusion rests on the displayed normal-coordinate argument.

## Relationship to prior work
Veronelli (2017, arXiv:1710.07178, Theorem 1 and Lemma 9) recovers scalar curvature from the **maximal** averaged pairwise distances among \(n+1\) chosen points (local extent), not from an expectation over two independent volume-uniform points. The metric expansion used here is known, not claimed as novel. Jauregui (2020, arXiv:2009.12394) characterizes scalar curvature through **relative capacity**, building on the classical small-geodesic-ball volume expansion. Hickok and Blumberg (2023, arXiv:2308.02615) give a point-cloud scalar-curvature estimator using **ball-volume growth**, not this pair-distance second-moment formula. The present statement identifies the scalar curvature coefficient for a different normalized two-point observable and requires both the measure-Jacobian and pair-distance curvature corrections. No priority or independent novelty certification is asserted.

## Limitations
The theorem is an infinitesimal population-moment statement for smooth Riemannian manifolds; it does not imply a finite-radius curvature comparison, a finite-sample estimator or noise stability. Dimension is presumed known; the geodesic ball radius is the intrinsic radius. The first non-Euclidean term determines scalar curvature only, not the whole Ricci or Riemann curvature tensor. Possible equivalents under other moment/energy terminology have not been exhaustively ruled out.

## References
1. G. Veronelli, *Scalar curvature via local extent*, arXiv:1710.07178 (first version October 19, 2017), https://arxiv.org/abs/1710.07178. In particular Theorem 1 and Lemma 9.
2. J. L. Jauregui, *Scalar curvature and the relative capacity of geodesic balls*, arXiv:2009.12394 (first version September 25, 2020), https://arxiv.org/abs/2009.12394.
3. A. Hickok and A. J. Blumberg, *An Intrinsic Approach to Scalar-Curvature Estimation for Point Clouds*, arXiv:2308.02615 (first version August 4, 2023), https://arxiv.org/abs/2308.02615.
