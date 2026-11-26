# Positive dependence and complete joint section–shadow law for ellipsoids

## Finding

Let \(d\ge2\), let \(E\subset\mathbb R^d\) be a centered, full-dimensional ellipsoid with known positive semiaxes \(a_1\le\cdots\le a_d\), and let \(U\) be Haar-uniform on \(S^{d-1}\). Write \(S\) for the \((d-1)\)-volume of \(E\cap U^\perp\) and \(H\) for the \((d-1)\)-volume of the orthogonal projection of \(E\) onto \(U^\perp\). Set \(\lambda_i=a_i^2\), \(C=\kappa_{d-1}\prod_i a_i\), and \(X_i=U_i^2\) in principal-axis coordinates, where \(\kappa_m=\pi^{m/2}/\Gamma(1+m/2)\).

**Theorem.** The following statements hold for every such ellipsoid.

1. The same-direction measurements satisfy
   \[
   S=\frac C{\sqrt{\sum_i\lambda_iX_i}},\qquad
   H=C\sqrt{\sum_iX_i/\lambda_i}.
   \]
   The random pair \((S,H)\) is **associated**: for any bounded coordinatewise nondecreasing Borel functions \(f,g:\mathbb R^2\to\mathbb R\),
   \[
   \operatorname{Cov}(f(S,H),g(S,H))\ge0.
   \]
   In particular \(\mathbb P(S>s,H>h)\ge\mathbb P(S>s)\mathbb P(H>h)\) for all real \(s,h\). Moreover \(\operatorname{Cov}(S,H)>0\) if the ellipsoid is not a ball, and it is zero exactly for balls.
2. The support of \((T,V)=((C/S)^2,(H/C)^2)\) is exactly
   \[
   \operatorname{conv}\{(\lambda_i,\lambda_i^{-1}):1\le i\le d\}.
   \]
   It is a point, a nondegenerate segment, or a two-dimensional polygon according as the number of distinct semiaxis lengths is one, two, or at least three. If exactly two distinct squared lengths \(\alpha<\beta\) occur, the observations lie almost surely on the strictly comonotone positive curve
   \[
   H^2+\frac{C^4}{\alpha\beta S^2}=\frac{C^2(\alpha+\beta)}{\alpha\beta}.
   \]
3. In dimension three, suppose \(0<\lambda_1<\lambda_2<\lambda_3\). Define
   \[
   \Delta=\frac{(\lambda_2-\lambda_1)(\lambda_3-\lambda_1)(\lambda_3-\lambda_2)}{\lambda_1\lambda_2\lambda_3},\qquad
   x_i(t,v)=\frac{\lambda_i(\lambda_j\lambda_kv-\lambda_j-\lambda_k+t)}{(\lambda_i-\lambda_j)(\lambda_i-\lambda_k)},
   \]
   with \(\{i,j,k\}=\{1,2,3\}\). Let \(\mathcal T^\circ\) be the open triangle with vertices \((\lambda_i,\lambda_i^{-1})\). The **complete joint density** of \((T,V)\) is
   \[
   f_{T,V}(t,v)=\frac{1}{2\pi\Delta\sqrt{x_1(t,v)x_2(t,v)x_3(t,v)}}\quad ((t,v)\in\mathcal T^\circ),
   \]
   and zero otherwise. A joint density of \((S,H)\) is
   \[
   f_{S,H}(s,h)=\frac{2h}{\pi\Delta s^3\sqrt{\prod_{i=1}^3 x_i((C/s)^2,(h/C)^2)}}
   \]
   for \(s>0\), \(h>0\), and \(((C/s)^2,(h/C)^2)\in\mathcal T^\circ\); it is zero everywhere else. The observations \((S,H)\) and known semiaxes uniquely recover \((U_1^2,U_2^2,U_3^2)\) by the formulas for \(x_i\). Signs of nonzero coordinates are not determined.

## Assumptions and scope

All hyperplanes are central and normals are sampled by normalized spherical area, not by an affine Crofton measure. The same normal is used for section and projection. Ellipsoid axes are fixed and positive, and known in the direction-reconstruction assertion. The planar density formula in part 3 does not apply in dimension three with repeated semiaxes; then the normalized law is on a segment or a point as in part 2.

## Proof

**Step 1: Exact directional geometry.** In principal-axis coordinates write \(E=AB_2^d\), where \(A=\operatorname{diag}(a_1,\dots,a_d)\) and \(B_2^d\) is the unit Euclidean ball. Let \(Q\) have as columns an orthonormal basis of \(U^\perp\). In those coordinates the section is defined by \(y^{\mathsf T}Q^{\mathsf T}A^{-2}Qy\le1\), while the projection is an ellipsoid with squared shape matrix \(Q^{\mathsf T}A^2Q\). For every positive-definite \(M\), the complementary minor identity in the orthogonal frame \([Q,U]\) gives
\[
\det(Q^{\mathsf T}MQ)=\det(M)\,U^{\mathsf T}M^{-1}U.
\]
Thus the section volume is \(\kappa_{d-1}/\sqrt{\det(Q^{\mathsf T}A^{-2}Q)}\) and the projection volume is \(\kappa_{d-1}\sqrt{\det(Q^{\mathsf T}A^2Q)}\). Substitution proves both formulas in part 1.

**Step 2: Association.** Normalize independent standard Gaussians to obtain \(U\); the normalized squares \(X\) have the \(\operatorname{Dirichlet}(1/2,\dots,1/2)\) law. Put \(P_k=\sum_{i=1}^kX_i\), \(P_d=1\), and \(Z_k=P_k/P_{k+1}\) for \(1\le k<d\). The \(Z_k\) are independent with \(Z_k\sim\operatorname{Beta}(k/2,1/2)\). Indeed, for independent gamma variables of shapes \(1/2\) with common scale, at step \(k\) the ratio of the sum of the first \(k\) variables to the sum of the first \(k+1\) has this beta law and is independent of the latter sum. Induction separates all preceding ratios from the sum and the new ratio. Also \(P_k=\prod_{j=k}^{d-1}Z_j\). Summation by parts yields
\[
\sum_i\lambda_iX_i=\lambda_d-\sum_{k=1}^{d-1}(\lambda_{k+1}-\lambda_k)P_k,\qquad
\sum_i\lambda_i^{-1}X_i=\lambda_d^{-1}+\sum_{k=1}^{d-1}(\lambda_k^{-1}-\lambda_{k+1}^{-1})P_k.
\]
Both \(S\) and \(H\) are therefore coordinatewise nondecreasing functions of the independent \(Z_j\). For scalar independent copies \(Z,Z'\), the product \((f(Z)-f(Z'))(g(Z)-g(Z'))\) is nonnegative for nondecreasing \(f,g\); its expectation is twice their covariance. Conditioning and induction give the same nonnegative covariance for any two bounded coordinatewise nondecreasing functions of independent variables. Composing with \((S,H)\) proves association; choosing upper-tail indicators gives the quadrant inequality.

If \(\lambda_k<\lambda_{k+1}\), both \(S\) and \(H\) strictly increase in \(Z_k\) when the other \(Z_j\) are fixed in \((0,1)\); the displayed \(P_k\) terms are strictly increasing and no other term offsets their effect. The conditional covariance in this single nondegenerate variable is strictly positive, while the covariance of the conditional means is nonnegative by the independent-coordinate argument. Thus the unconditional covariance is positive. If all semiaxes are equal, both volumes are constant.

**Step 3: Support and the two-level identity.** The normalized pair is \((T,V)=\sum_iX_i(\lambda_i,\lambda_i^{-1})\). The Dirichlet law has full support on the closed simplex and this map is continuous, so the support is the stated convex hull. Strict convexity of \(t\mapsto1/t\) on \((0,\infty)\) excludes three collinear points with distinct first coordinates. With just two squared lengths, the relation is \(V=(\alpha+\beta-T)/(\alpha\beta)\), which yields the displayed curve. Both raw volumes vary strictly in the same direction with the common spectral weight.

**Step 4: Triaxial density and direction recovery.** In dimension three, \((X_1,X_2)\) has density \(1/(2\pi\sqrt{X_1X_2X_3})\) for \(X_1,X_2,X_3=1-X_1-X_2>0\). The affine map to \((T,V)\) has columns
\[
(\lambda_1-\lambda_3,\lambda_1^{-1}-\lambda_3^{-1})^{\mathsf T},\qquad
(\lambda_2-\lambda_3,\lambda_2^{-1}-\lambda_3^{-1})^{\mathsf T}.
\]
Its absolute determinant is \(\Delta>0\). The affine functions \(x_i(t,v)\) are its barycentric inverse because \(x_i(\lambda_\ell,\lambda_\ell^{-1})\) equals 1 for \(\ell=i\) and 0 at the other vertices. This change of variables proves \(f_{T,V}\). On the positive quadrant, \((s,h)\mapsto((C/s)^2,(h/C)^2)\) is one-to-one and has absolute Jacobian \(4h/s^3\). It yields \(f_{S,H}\), with zero density outside the positive quadrant. The triangle boundary carries no mass, and its closure is the support of \((T,V)\). The inverse affine formulas recover squared coordinates, including on the boundary; without more observations they do not distinguish reflections in the principal coordinate planes.

## Verification

The standalone `check_joint_ellipsoid.py` uses NumPy. It compares the two area formulas with direct plane-basis determinant calculations in dimension three, checks the triaxial inverse and density Jacobian, and performs reproducible direction-sampling and independent beta-coordinate checks. Those finite checks are consistency tests; the proof establishes the exact law and all-dimensional association.

## Relationship to prior work

The directional geometry and Dirichlet ingredients are classical. Kim–Yaskin–Zvavitch [1] study separate marginal distribution functions for sections and projections. The earlier triaxial paired-measurement record [5] already gives both directional area formulas for the same normal and studies the scalar \((H/S)^2=TV\) to recover shape up to scale and polarity. Here the semiaxes are known for direction recovery, and the claims concern the joint area law and the association of the raw observations. Gusakova–Spodarev–Zaporozhets [4] study ellipsoid intrinsic volumes and spherical integrals; Myroshnychenko–Tatarko–Yaskin [3] study determination by dual volumes, and Hinrichs et al. [2] concern random section circumradii. None of these comparisons establishes exhaustive priority for the paired formulations.

## Limitations

The scope excludes noncentral affine sections, non-Haar normals, nonorthogonal shadows and general convex bodies. Higher-dimensional laws are described by the Dirichlet pushforward and its support, rather than by the elementary triaxial density. Nonzero coordinate signs remain unobserved in triaxial reconstruction. The result does not claim recovery of unknown ellipsoid axes from a single measurement pair.

## References

1. J. Kim, V. Yaskin, A. Zvavitch, *Distribution functions of sections and projections of convex bodies*, https://arxiv.org/abs/1512.07289.
2. A. Hinrichs, D. Krieg, E. Novak, J. Prochno, M. Ullrich, *Random sections of ellipsoids and the power of random information*, https://arxiv.org/abs/1901.06639.
3. S. Myroshnychenko, K. Tatarko, V. Yaskin, *Unique determination of ellipsoids by their dual Steiner polynomial*, https://arxiv.org/abs/2007.08079.
4. J. Gusakova, E. Spodarev, D. Zaporozhets, *Intrinsic volumes of ellipsoids*, https://arxiv.org/abs/2206.14002.
5. *Endpoint tomography from paired sections and shadows of triaxial ellipsoids*, https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-endpoint-tomography-from-paired-sections-and-shadows-of-triaxial--e3183756e2e2/RESULT.md.
