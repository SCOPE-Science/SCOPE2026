# Finite-shape recovery of full Riemann curvature from random short distances

## Finding
For \(n\ge4\), the fourth-order short-radius coefficient of **one scalar population statistic**—the mean squared intrinsic distance between two independent uniform points—recovers the complete Riemann curvature tensor when the sampling neighborhoods vary through normal-coordinate ellipsoids. A generic set of exactly \(N=n^2(n^2-1)/12\) ellipsoid shapes suffices; this count is optimal among fixed scalar coefficient measurements.

For an orthonormal basis \(e_1,\ldots,e_n\) of \(T_pM\), write \(\mathrm{Ric}\) for the Ricci matrix and adopt the curvature convention \(R(u,v,u,v)=K(u,v)(\|u\|^2\|v\|^2-\langle u,v\rangle^2)\) for sectional curvature \(K\). Define
\[
\mathscr R(Q,Q)=\sum_{i,j,k,\ell=1}^n R(e_i,e_k,e_j,e_\ell)Q_{ij}Q_{k\ell}.
\]
The observable coefficient is exactly
\[
\boxed{\mathcal K_p(Q)=\frac{\mathscr R(Q,Q)}{3(n+2)^2}+\frac{2}{3(n+2)(n+4)}\left(\operatorname{tr}(\mathrm{Ric}\,Q^2)-\frac{\operatorname{tr}Q\,\operatorname{tr}(\mathrm{Ric}\,Q)}{n+2}\right).}
\]
This is polynomial in the entries of \(Q\), so its values for positive-definite matrices determine its unique extension to positive-semidefinite matrices.

For each unit tangent vector \(u\), the rank-one limiting shape gives
\[
\boxed{\mathrm{Ric}(u,u)=\frac{3(n+2)^2(n+4)}{2(n+1)}\mathcal K_p(uu^{\mathsf T}).}
\]
For every orthonormal pair \(u,v\), write \(P_{uv}=uu^{\mathsf T}+vv^{\mathsf T}\). Then
\[
\boxed{K(u,v)=\frac{3(n+2)^2}{2}\mathcal K_p(P_{uv})-\frac{n}{n+4}\bigl(\mathrm{Ric}(u,u)+\mathrm{Ric}(v,v)\bigr).}
\]
Thus the full sectional-curvature function, hence the full algebraic curvature tensor, is reconstructed.

## Assumptions and scope
The manifold \((M^n,g)\) is smooth, \(n\ge4\), and \(p\in M\) is an interior point with a fixed known tangent orthonormal frame. For any symmetric positive-definite \(n\times n\) matrix \(Q\) and sufficiently small \(r>0\), put
\[
E_r(Q)=\exp_p\bigl(\{x\in T_pM:x^{\mathsf T}Q^{-1}x<r^2\}\bigr).
\]
The two points \(X_r,Y_r\) are independent and sampled according to normalized Riemannian volume on \(E_r(Q)\). Distances are shortest-path **intrinsic Riemannian distances**, not distances in an ambient embedding. We observe the exact population function of radius \(r\) for each chosen ellipsoid shape, and define
\[
\mathcal K_p(Q)=\lim_{r\downarrow0}\frac{\frac{2r^2}{n+2}\operatorname{tr}Q-\mathbb E[d_g(X_r,Y_r)^2]}{r^4}.
\]
All claims concern the coefficient at a single specified point, not global metric reconstruction or noise robustness.

## Proof
**1. Normal-coordinate and volume expansions.** In normal coordinates at \(p\), uniformly for \(x,y=O(r)\),
\[
d_g(\exp_p x,\exp_p y)^2=\|x-y\|^2-\tfrac13R(x,y,x,y)+O_p(r^5),\quad
J(x)=1-\tfrac16\mathrm{Ric}(x,x)+O_p(r^3).
\]
The convention in the first displayed expansion assigns a negative correction to positive sectional curvature.

**2. Euclidean ellipsoid moments.** Let \(Z\) be uniform on \(r Q^{1/2}B_2^n\) with respect to Euclidean volume. Its second and fourth moments are
\[
\mathbb E_0[Z_iZ_j]=\frac{r^2}{n+2}Q_{ij},\qquad
\mathbb E_0[Z_iZ_jZ_kZ_\ell]=\frac{r^4}{(n+2)(n+4)}(Q_{ij}Q_{k\ell}+Q_{ik}Q_{j\ell}+Q_{i\ell}Q_{jk}).
\]
The normal-coordinate density \(J\), after probability normalization, changes \(\mathbb E\|X\|^2\) at order \(r^4\) by minus one sixth of the Euclidean covariance of \(\|Z\|^2\) and \(\mathrm{Ric}(Z,Z)\). Direct contraction yields
\[
\operatorname{Cov}_0(\|Z\|^2,\mathrm{Ric}(Z,Z))=\frac{2r^4}{(n+2)(n+4)}\left(\operatorname{tr}(\mathrm{Ric}\,Q^2)-\frac{\operatorname{tr}Q\operatorname{tr}(\mathrm{Ric}\,Q)}{n+2}\right).
\]
Because the leading domain is centrally symmetric, the normalized coordinate mean is \(O(r^4)\); its squared norm therefore does not affect the \(r^4\) coefficient. Twice the preceding covariance correction contributes the second term of \(\mathcal K_p(Q)\).

**3. Curved-distance term.** Independence and the Euclidean second-moment identity imply
\[
\mathbb E_0 R(Z,Z',Z,Z')=\frac{r^4}{(n+2)^2}\mathscr R(Q,Q),
\]
where \(Z,Z'\) are independent uniform Euclidean-ellipsoid points. Perturbing their sampling densities affects this already fourth-order term only at higher order. Combining the metric and volume corrections gives the coefficient stated in Finding, with a uniform-in-fixed-\(Q\) error \(O_{p,Q}(r^5)\).

**4. Curvature inversion.** For \(Q=uu^{\mathsf T}\), \(\mathscr R(Q,Q)=0\), \(Q^2=Q\) for unit \(u\), and \(\operatorname{tr}Q=1\). This gives the rank-one inversion formula. For the orthogonal two-plane projector \(Q=P_{uv}\), one has \(\mathscr R(Q,Q)=2K(u,v)\), \(Q^2=Q\), \(\operatorname{tr}Q=2\); the second inversion follows. The rank-one/rank-two evaluations are values of the polynomial **extended by continuity**, not claims that volume sampling on a collapsed ellipsoid is defined. Knowing \(R(u,v,u,v)\) for all vectors \(u,v\) determines \(R\): polarize first in \(u\), then in \(v\), and use the algebraic Bianchi identity to separate the resulting two cross terms. Thus the map \(R\mapsto(Q\mapsto\mathcal K_p(Q))\) is injective.

**5. Generic sharp finite count.** The vector space of algebraic curvature tensors in dimension \(n\) has dimension \(N=n^2(n^2-1)/12\). For each fixed positive-definite \(Q\), evaluation of \(\mathcal K_p(Q)\) is a linear functional on that space. Since all positive-definite evaluations separate curvature tensors, they span the dual, and some \(N\) are independent. The determinant of the associated \(N\times N\) measurement matrix is a nonzero polynomial in the shape entries; hence generic \(N\)-tuples of positive-definite shapes give an invertible system. Any fewer fixed scalar evaluations have a nontrivial kernel. Every algebraic curvature tensor is locally realizable as the curvature jet of a smooth positive Riemannian metric, so this minimality is geometric rather than purely formal.

**6. An invisible Ricci-flat curvature mode.** In dimension four consider the algebraic tensor with diagonal sectional entries \(K_{12}=K_{34}=1\) and \(K_{13}=K_{14}=K_{23}=K_{24}=-1/2\), all mixed four-index terms zero. It obeys curvature symmetries and the Bianchi identity; each Ricci diagonal entry is \(1-1/2-1/2=0\), and all off-diagonals vanish. Therefore \(\mathcal K_p(I)=0\). But at \(Q=\operatorname{diag}(2,2,1,1)\) one computes \(\mathscr R(Q,Q)=2\), so \(\mathcal K_p(Q)=1/54\ne0\). Ellipsoidal averaging detects Weyl curvature invisible to spherical averaging.

## Verification
Run the three accompanying standalone scripts with Python, SymPy, NumPy and SciPy. `check_curvature.py` checks rank-one and orthogonal two-plane recovery formulas exactly in dimensions two and three, including consistency with the round-ball scalar coefficient. `check_rank.py` performs finite-field exact-rank tests of the normalized observation matrices in dimensions two through five (ranks \(1,6,20,50\)); the theoretical generic-rank proof above does not rely on numerical rank. `check_spaceform.py` independently integrates the exact two-sphere exponential-map Jacobian and spherical cosine-law distances for anisotropic ellipsoids, comparing the recovered fourth-order coefficient against the analytic formula. The numerical experiment is only a diagnostic and not a proof of the all-manifold assertion.

## Relationship to prior work
Fefferman, Ivanov, Lassas and Narayanan (2019, arXiv:1905.07182) reconstruct a Riemannian manifold from many noisy, **labeled** intrinsic pairwise distances on a sampled cloud. Fefferman, Ivanov, Lassas, Lu and Narayanan (2021, arXiv:2111.14528) use dense partial distance-vector data to reconstruct local coordinates and metrics. Their measurements and reconstruction theorems do not state that finitely many population means over unlabeled anisotropic neighborhoods recover the whole curvature tensor. A previously established scalar-coefficient identity for **spherical** geodesic balls gives only the scalar trace, while the present theorem recovers anisotropic Ricci and the Weyl component in dimensions at least four. Standard normal-coordinate expansions and polarization are acknowledged as input facts; the new claim is the exact ellipsoid polynomial, inversion, and optimal finite shape count.

## Limitations
The required shape coordinate frame is assumed given. The coefficient is an infinitesimal limit from exact population means: this paper does not provide finite-radius, finite-sample, or noisy stability guarantees, nor a reconstruction of the manifold beyond its curvature tensor at one point. The rank-one and rank-two shapes used for algebraic inversion are polynomial limits, not allowable positive-volume domains. Historical priority remains subject to possible older equivalent constructions in local integral geometry.

## References
1. C. Fefferman, S. Ivanov, M. Lassas, H. Narayanan, *Reconstruction of a Riemannian manifold from noisy intrinsic distances*, arXiv:1905.07182 (first posted 2019-05-17), https://arxiv.org/abs/1905.07182.
2. C. Fefferman, S. Ivanov, M. Lassas, J. Lu, H. Narayanan, *Reconstruction and interpolation of manifolds II: Inverse problems for Riemannian manifolds with partial distance data*, arXiv:2111.14528 (first posted 2021-11-29), https://arxiv.org/abs/2111.14528.
