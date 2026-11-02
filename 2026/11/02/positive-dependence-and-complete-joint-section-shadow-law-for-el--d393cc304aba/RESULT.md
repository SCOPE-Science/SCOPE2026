# Positive dependence and complete joint section–shadow law for ellipsoids

## Finding

Let \(d\ge2\), let \(E\subset\mathbb R^d\) be a centered, full-dimensional ellipsoid with known positive semiaxes \(a_1\le\cdots\le a_d\), and let \(U\) be Haar-uniform on \(S^{d-1}\). Write \(S\) for the \((d-1)\)-volume of \(E\cap U^\perp\) and \(H\) for the \((d-1)\)-volume of the orthogonal projection of \(E\) onto \(U^\perp\). Set \(\lambda_i=a_i^2\), \(C=\kappa_{d-1}\prod_i a_i\), and \(X_i=U_i^2\), where \(\kappa_m=\pi^{m/2}/\Gamma(1+m/2)\).

**Theorem.** The following statements hold for every such ellipsoid.

1. The *same-direction* geometric measurements satisfy
   \[
   S=\frac C{\sqrt{\sum_i\lambda_iX_i}},\qquad
   H=C\sqrt{\sum_iX_i/\lambda_i}.
   \]
   The random vector \((S,H)\) is **associated**: for any bounded coordinatewise nondecreasing Borel functions \(f,g:\mathbb R^2\to\mathbb R\),
   \[
   \operatorname{Cov}(f(S,H),g(S,H))\ge0.
   \]
   In particular \(\mathbb P(S>s,H>h)\ge\mathbb P(S>s)\mathbb P(H>h)\) for all real \(s,h\). Moreover \(\operatorname{Cov}(S,H)>0\) if the ellipsoid is not a ball, and it is zero exactly for balls.
2. The support of the normalized pair \((T,V)=((C/S)^2,(H/C)^2)\) is exactly
   \[
   \operatorname{conv}\{(\lambda_i,\lambda_i^{-1}):1\le i\le d\}.
   \]
   It is a point, a nondegenerate line segment, or a two-dimensional polygon according as the number of distinct semiaxis lengths is one, two, or at least three. If exactly two distinct squared lengths \(\alpha<\beta\) occur, the two measurements lie almost surely on the strictly comonotone curve
   \[
   H^2+\frac{C^4}{\alpha\beta S^2}=\frac{C^2(\alpha+\beta)}{\alpha\beta}.
   \]
3. In dimension three, suppose \(0<\lambda_1<\lambda_2<\lambda_3\). Define
   \[
   \Delta=\frac{(\lambda_2-\lambda_1)(\lambda_3-\lambda_1)(\lambda_3-\lambda_2)}{\lambda_1\lambda_2\lambda_3}.
   \]
   For each \((t,v)\) in the open triangle with vertices \((\lambda_i,\lambda_i^{-1})\), define, for \(\{i,j,k\}=\{1,2,3\}\),
   \[
   x_i(t,v)=\frac{\lambda_i(\lambda_j\lambda_kv-\lambda_j-\lambda_k+t)}{(\lambda_i-\lambda_j)(\lambda_i-\lambda_k)}.
   \]
   The **complete joint density** of \((T,V)\) is
   \[
   f_{T,V}(t,v)=\frac{1}{2\pi\Delta\sqrt{x_1(t,v)x_2(t,v)x_3(t,v)}}
   \]
   on that triangle and zero outside (boundary values are immaterial). Equivalently, the density of \((S,H)\) is
   \[
   f_{S,H}(s,h)=\frac{2h}{\pi\Delta s^3\sqrt{\prod_{i=1}^3 x_i((C/s)^2,(h/C)^2)}}
   \]
   whenever \(((C/s)^2,(h/C)^2)\) belongs to the open triangle, and zero otherwise. A measured pair \((S,H)\), together with the known semiaxes, therefore uniquely reconstructs \((U_1^2,U_2^2,U_3^2)\) by the displayed \(x_i\) formulas. The signs of the coordinates are not determined.

## Assumptions and scope

All hyperplanes are central and normal directions are sampled by normalized spherical area, not by an affine Crofton measure. The *same* normal \(U\) is used for section and projection. Ellipsoid axes are fixed, positive, and known for the direction-reconstruction assertion. At repeated-axis limits the two-dimensional density formula does not apply; the correct joint law is supported on the corresponding line segment or point as in part 2.

## Proof

**Step 1: Exact directional geometry.** In principal-axis coordinates write \(E=AB_2^d\), where \(A=\operatorname{diag}(a_1,\dots,a_d)\). Choose a matrix \(V_\perp\in\mathbb R^{d\times(d-1)}\) whose columns form an orthonormal basis of \(U^\perp\). The central section is the ellipsoid
\[
\{V_\perp y:y^{\mathsf T}V_\perp^{\mathsf T}A^{-2}V_\perp y\le1\},
\]
while the projected ellipsoid has squared shape matrix \(V_\perp^{\mathsf T}A^2V_\perp\). For every positive-definite \(M\), Jacobi's complementary minor identity gives
\[
\det(V_\perp^{\mathsf T}MV_\perp)=\det(M)\,U^{\mathsf T}M^{-1}U.
\]
Their volumes are respectively \(\kappa_{d-1}/\sqrt{\det(V_\perp^{\mathsf T}A^{-2}V_\perp)}\) and \(\kappa_{d-1}\sqrt{\det(V_\perp^{\mathsf T}A^2V_\perp)}\). Substitution proves the two formulas in part 1, including all dimensional constants.

**Step 2: A product-coordinate proof of association.** Write \(U_i=G_i/(\sum_jG_j^2)^{1/2}\) with independent standard Gaussians \(G_i\). Then \(X=(X_i)\) has the \(\operatorname{Dirichlet}(1/2,\dots,1/2)\) distribution. Put \(P_k=\sum_{i=1}^kX_i\), \(P_d=1\), and \(Z_k=P_k/P_{k+1}\) for \(1\le k<d\). The gamma-to-beta change of variables shows that the \(Z_k\) are independent and
\[
Z_k\sim\operatorname{Beta}(k/2,1/2),\qquad P_k=\prod_{j=k}^{d-1}Z_j.
\]
For ordered \(\lambda_i\), summation by parts gives
\[
\sum_i\lambda_iX_i=\lambda_d-\sum_{k=1}^{d-1}(\lambda_{k+1}-\lambda_k)P_k,
\]
\[
\sum_i\lambda_i^{-1}X_i=\lambda_d^{-1}+\sum_{k=1}^{d-1}(\lambda_k^{-1}-\lambda_{k+1}^{-1})P_k.
\]
Every \(P_k\) is nondecreasing in every independent \(Z_j\). Consequently *both* \(S\) and \(H\) are coordinatewise nondecreasing functions of \((Z_1,\dots,Z_{d-1})\). For independent scalar variables, the elementary Chebyshev covariance inequality, followed by induction and conditioning, gives nonnegative covariance to any two bounded coordinatewise nondecreasing functions of the variables. Applying it to \(f(S,H)\) and \(g(S,H)\) proves association, and choosing coordinatewise upper-tail indicators proves the quadrant inequality. If some \(\lambda_k<\lambda_{k+1}\), then both \(S\) and \(H\) are strictly increasing in \(Z_k\) with all other \(Z_j\in(0,1)\) held fixed. The one-coordinate conditional covariance is strictly positive; the covariance of the conditional means is nonnegative by association of the remaining independent variables. Hence \(\operatorname{Cov}(S,H)>0\). A ball gives deterministic \(S,H\), and conversely positivity rules out zero covariance for a nonball.

**Step 3: Support and the two-level identity.** Because \(X_i\ge0\) and \(\sum_iX_i=1\),
\[
(T,V)=\sum_iX_i(\lambda_i,\lambda_i^{-1}).
\]
The Dirichlet density is strictly positive in the open probability simplex, so its closed image is exactly the asserted convex hull. Since \(t\mapsto 1/t\) is strictly convex on \((0,\infty)\), three distinct sampled points on this curve are not collinear: the hull has dimension two if and only if at least three different eigenvalues occur. With only \(\alpha\) and \(\beta\), the affine relation \(V=(\alpha+\beta-T)/(\alpha\beta)\) yields the stated deterministic curve. As its common spectral weight varies, both \(S\) and \(H\) vary strictly in the same direction.

**Step 4: Triaxial density and direction recovery.** In \(d=3\), \((X_1,X_2)\) has density \((2\pi\sqrt{X_1X_2X_3})^{-1}\) on \(X_i>0\), \(\sum X_i=1\). The affine map
\[
(X_1,X_2)\longmapsto (T,V)=(\lambda_3,\lambda_3^{-1})+X_1(\lambda_1-\lambda_3,\lambda_1^{-1}-\lambda_3^{-1})+X_2(\lambda_2-\lambda_3,\lambda_2^{-1}-\lambda_3^{-1})
\]
has constant absolute Jacobian \(\Delta>0\). Inverting the linear system \(\sum X_i=1\), \(\sum\lambda_iX_i=T\), \(\sum\lambda_i^{-1}X_i=V\) gives exactly the displayed \(x_i(T,V)\). Change of variables yields \(f_{T,V}\); the final transform \(T=(C/S)^2\), \(V=(H/C)^2\) has absolute Jacobian \(4H/S^3\), giving \(f_{S,H}\). The density integrates to one because it is the bijective pushforward of the normalized Dirichlet density. Its support is the stated open triangle up to its probability-zero boundary. This also proves that the two geometric measurements identify the squared direction coordinates uniquely, but not their signs.

## Verification

The accompanying `check_joint_ellipsoid.py` independently computes the two ellipsoid areas in three dimensions using orthonormal plane bases and determinants, not the closed formulas alone; it checks the triaxial inverse and density Jacobian; and it performs reproducible direction-sampling and independent beta-coordinate checks. Run with `python check_joint_ellipsoid.py` in an environment with NumPy. The finite checks are consistency tests; every distributional and infinite-sample statement above follows from the proof.

## Relationship to prior work

Kim–Yaskin–Zvavitch (arXiv:1512.07289, first public version December 22, 2015) study **separate marginal distribution functions** of section and projection volumes, deriving comparison and identification statements from those marginal laws, but do not study their same-direction joint dependence. Myroshnychenko–Tatarko–Yaskin (arXiv:2007.08079, first public version July 16, 2020) recover ellipsoid semiaxes from collections of *integrated dual volumes*; this concerns shape identification from scalar body invariants, not recovery of a random direction from two same-direction measurements. Gusakova–Spodarev–Zaporozhets (arXiv:2206.14002, first public version June 28, 2022) give intrinsic-volume integrals for ellipsoids, including separate spherical averages; those averages do not determine the joint random pair or its positive dependence. Hinrichs–Krieg–Novak–Prochno–Ullrich (arXiv:1901.06639, first public version January 20, 2019) analyze circumradii of random ellipsoid sections in a different, often high-dimensional, regime, not this paired section-volume/projection-volume law. The elementary geometric and Dirichlet ingredients are classical and are not claimed as novel. The contribution assessed here is their combination into the all-dimensional association theorem and the complete triaxial joint law with exact direction recovery.

## Limitations

The scope excludes noncentral affine sections, non-Haar normals, nonorthogonal shadows, and general convex bodies. The joint-density formula is a \(d=3\), three-distinct-semiaxes formula; higher-dimensional laws remain described by the explicit Dirichlet pushforward and polygonal support, not by a claimed elementary density. Even in three dimensions the normal's coordinate signs remain unobserved. Historic priority of the exact paired formulation remains subject to independently locating earlier equivalent derivations.

## References

1. J. Kim, V. Yaskin, A. Zvavitch, *Distribution functions of sections and projections of convex bodies*, arXiv:1512.07289, first public December 22, 2015. https://arxiv.org/abs/1512.07289
2. A. Hinrichs, D. Krieg, E. Novak, J. Prochno, M. Ullrich, *Random sections of ellipsoids and the power of random information*, arXiv:1901.06639, submitted January 20, 2019. https://arxiv.org/abs/1901.06639
3. S. Myroshnychenko, K. Tatarko, V. Yaskin, *Unique determination of ellipsoids by their dual volumes and the moment problem*, arXiv:2007.08079, submitted July 16, 2020. https://arxiv.org/abs/2007.08079
4. A. Gusakova, E. Spodarev, D. Zaporozhets, *Intrinsic volumes of ellipsoids*, arXiv:2206.14002, submitted June 28, 2022. https://arxiv.org/abs/2206.14002
