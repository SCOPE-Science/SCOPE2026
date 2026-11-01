# Negative sectional and positive mixed bisectional Bergman curvature along the spine of intersected disk bundles

## Finding
For every integer \(n\ge3\) and every \(p_2,\ldots,p_n>0\), consider the bounded complete Reinhardt domain
\[
\Omega_{\boldsymbol p}=\{z\in\mathbb C^n: |z_1|^2+|z_j|^{2p_j}<1\ \text{for all }2\le j\le n\}.
\]
Its Bergman metric has **strictly negative holomorphic sectional curvature in every nonzero tangent direction at every point** of the analytic spine \(\{(a,0,\ldots,0):|a|<1\}\), but **strictly positive holomorphic bisectional curvature for every distinct pair of transverse coordinate directions there**. Thus the two curvature sign conditions separate even within the bounded convex members \(p_j\ge1\) of this family.

At the origin put \(u_j=1/p_j\) and \(T=1+\sum_{j=2}^n u_j\). For the curvature convention in the next section, the nonredundant coordinate components are
\[
\begin{aligned}
g_{1\bar1}&=T+1,&g_{j\bar j}&=\frac{2(T+u_j)}{T},\\
R_{1\bar1 1\bar1}&=-2(T+1),&
R_{1\bar1 j\bar j}&=-\frac{2u_j(T+u_j)}{T},\\
R_{j\bar j j\bar j}&=-\frac{4(T^2+2Tu_j-2u_j^2)}{T^2},&
R_{j\bar j k\bar k}&=\frac{4u_ju_k}{T^2}\quad(j\ne k,\ j,k\ge2).
\end{aligned}
\]
All other components vanish except those obtained by Kähler symmetries. In particular the normalized bisectional curvature between two distinct transverse coordinate lines is exactly
\[
\boxed{\operatorname{Bis}(e_j,e_k)=\frac{u_ju_k}{(T+u_j)(T+u_k)}>0,\qquad 2\le j<k\le n.}
\]
For the convex intersection of quadratic cylinders, \(p_2=\cdots=p_n=1\), this is \(1/(n+1)^2\) for every transverse pair and every spine point.

## Assumptions and scope
The Bergman space is the ordinary unweighted square-integrable holomorphic space with Lebesgue volume on \(\Omega_{\boldsymbol p}\). The Bergman metric is \(g_{i\bar j}=\partial_i\partial_{\bar j}\log K(z,z)\), and curvature is
\[
R_{i\bar j k\bar\ell}=-\partial_i\partial_{\bar j}g_{k\bar\ell}+\sum_{a,b}g^{a\bar b}(\partial_i g_{k\bar b})(\partial_{\bar j}g_{a\bar\ell}).
\]
The holomorphic sectional curvature is \(R(v,\bar v,v,\bar v)/g(v,\bar v)^2\); the bisectional curvature is \(R(v,\bar v,w,\bar w)/(g(v,\bar v)g(w,\bar w))\). No alternate factor-of-two normalization is implicit. All transverse indices are at least two. The strict holomorphic sectional sign is asserted **along the spine only**, not everywhere in the domain.

## Proof
**Monomial norms and kernel jets.** By separate radial integration, for any nonnegative integer multiindex \(\alpha\) and \(u_j=1/p_j\),
\[
\|z^\alpha\|_{L^2(\Omega_{\boldsymbol p})}^2
=\frac{\pi^n}{\prod_{j=2}^n(\alpha_j+1)}
 B\left(\alpha_1+1,1+\sum_{j=2}^n u_j(\alpha_j+1)\right).
\]
The monomials form a complete orthogonal basis by the bounded complete Reinhardt property. Put \(t_\alpha=1+\sum_{j=2}^n u_j(\alpha_j+1)\), so the coefficient of \(\prod_j(z_j\bar w_j)^{\alpha_j}\) in \(\pi^n K(z,w)\) is exactly
\[
 c_\alpha=\frac{\prod_{j=2}^n(\alpha_j+1)}{\alpha_1!}(t_\alpha)_{\alpha_1+1}.
\]
Here \((t)_r=t(t+1)\cdots(t+r-1)\). In particular \(c_0=T\); dividing all coefficients by \(T\), the first- and second-degree coefficients are explicit:
\[
\begin{aligned}
c_{e_1}/T&=T+1,&c_{e_j}/T&=2(T+u_j)/T,\\
c_{2e_1}/T&=(T+1)(T+2)/2,&c_{e_1+e_j}/T&=2(T+u_j)(T+u_j+1)/T,\\
c_{2e_j}/T&=3(T+2u_j)/T,&c_{e_j+e_k}/T&=4(T+u_j+u_k)/T\quad(j\ne k).
\end{aligned}
\]

**Curvature tensor.** Torus invariance makes the metric diagonal at the origin and all its first coordinate derivatives vanish there. With \(x_j=|z_j|^2\), the coefficient of \(x_jx_k\) in \(\log K(z,z)\) is \(c_{e_j+e_k}/T-(c_{e_j}/T)(c_{e_k}/T)\) for \(j\ne k\). For \(x_j^2\), it is \(c_{2e_j}/T-(c_{e_j}/T)^2/2\). Taking the fourth derivatives gives exactly the displayed tensor; the repeated-index differentiation carries the factor four. Independent coordinate rotations ensure no additional components beyond the Kähler permutations.

**All holomorphic sectional directions.** Fix \(v\ne0\) and put \(X_j=|v_j|^2\). Kähler symmetries and the tensor formulas give
\[
\begin{aligned}
R(v,\bar v,v,\bar v)={}&-2(T+1)X_1^2
-\frac8T X_1\sum_{j=2}^n u_j(T+u_j)X_j\\
&-\frac4{T^2}\left[T^2\sum_{j=2}^n X_j^2
+2T\sum_{j=2}^n u_jX_j^2
-2\left(\sum_{j=2}^n u_jX_j\right)^2\right].
\end{aligned}
\]
Since \(\sum_{j=2}^n u_j=T-1\), weighted Cauchy–Schwarz implies
\[
\left(\sum_{j=2}^n u_jX_j\right)^2
\le (T-1)\sum_{j=2}^n u_j X_j^2.
\]
The square-bracketed expression is therefore at least \(T^2\sum_{j=2}^n X_j^2+2\sum_{j=2}^n u_jX_j^2\), strictly positive whenever any transverse component is nonzero. If all transverse components vanish, the first term is strictly negative. As the Bergman metric is positive definite, the normalized holomorphic sectional curvature is strictly negative for every nonzero \(v\).

**Positive mixed pairs and the spine.** For distinct transverse indices \(j,k\), the positive tensor component and diagonal metric immediately give the boxed formula. For any \(|a|<1\), the holomorphic automorphism
\[
 z_1\longmapsto\frac{z_1-a}{1-\bar a z_1},\qquad
 z_j\longmapsto\frac{(1-|a|^2)^{u_j/2}}{(1-\bar a z_1)^{u_j}}z_j
\]
(with the holomorphic branch on the disk) maps \((a,0,\ldots,0)\) to the origin and preserves each defining inequality. Its derivative at that spine point is diagonal. Bergman curvature invariance transfers the strict sectional sign and the normalized transverse bisectional values to every spine point. Finally, for \(p_j\ge1\), each defining inequality is convex on the underlying real vector space, hence their intersection is bounded and convex.

## Verification
The standalone `CHECK.py` independently obtains the relevant low-order coefficients from beta-integral moments using exact rational arithmetic and confirms the tensor formulas in five parameter families (dimensions three through five). It also checks strict holomorphic-sectional negativity for finitely many rational nonnegative squared-component vectors. Running `python CHECK.py` prints its result. These computations are **supplementary**: the universal statements for all dimensions, positive parameters, and vectors follow from the identities and weighted Cauchy–Schwarz proof above, not from finite enumeration.

## Relationship to prior work
Cho and Yuan, arXiv:2004.04637 (first public April 9, 2020), prove global negative holomorphic sectional curvature alongside positive bisectional curvature somewhere on the symmetrized bidisc. That nonconvexifiable two-dimensional domain is different from the present bounded convex intersection examples. Beberok, arXiv:1601.02989 (January 12, 2016), and Park, *J. Math. Anal. Appl.* 504 (2021), 125398, establish explicit Bergman kernels for intersected ellipsoid or cylinder domains; their kernel formulas and monomial framework are fully acknowledged. The geometric sign classification, its all-dimensional tensor and its simultaneous positive transverse/negative sectional characterization are separate consequences requiring fourth-order calculations and an inequality; they are not stated in the inspected portions of those sources. The pre-existing exact kernel formulas make indirect prior coverage a genuine historical-priority risk, not a proof of independent priority.

## Limitations
The theorem does not establish negative sectional curvature away from the analytic spine or any global pinching constant. The positive bisectional conclusion is for distinct coordinate directions transverse to the spine and does not assert positivity for all pairs. The convex cases include nonsmooth boundary points. The result does not claim novelty of the kernel formulas themselves, nor independent mathematical validation; priority beyond the inspected publications and database comparisons is provisional.

## References
- G. Cho and Y. Yuan, *Bergman metric on the symmetrized bidisc and its consequences*, arXiv:2004.04637 (initial version April 9, 2020).
- J.-D. Park, *The Bergman kernel function for intersections of some cylindrical domains and Lauricella's hypergeometric function*, Journal of Mathematical Analysis and Applications **504** (2021), article 125398, DOI: 10.1016/j.jmaa.2021.125398.
- T. Beberok, *The Bergman kernel: explicit formulas, deflation, Lu Qi-Keng problem and Jacobi polynomials*, arXiv:1601.02989 (initial version January 12, 2016), Czechoslovak Mathematical Journal **67** (2017), 537–549.
