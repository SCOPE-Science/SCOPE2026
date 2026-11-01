# Sharp surface-to-volume second-moment bounds for Euclidean ellipsoids

## Finding
Let \(d\ge2\) and let \(E=c+AB_2^d\subset\mathbb R^d\) be a full-dimensional ellipsoid, where \(A\) is invertible. Let \(X,X'\) be independent and uniform by volume on \(E\), and let \(Y,Y'\) be independent and uniform by Euclidean surface area on \(\partial E\). Then
\[
\frac{d+2}{d+1}<
\frac{\mathbb E\|Y-Y'\|^2}{\mathbb E\|X-X'\|^2}
\le\frac{d+2}{d}.
\]
The upper bound is attained if and only if \(E\) is a Euclidean ball. The strict lower constant is optimal but unattained: for the ellipsoids with semiaxes \((\varepsilon,1,\ldots,1)\), the ratio tends to \((d+2)/(d+1)\) as \(\varepsilon\downarrow0\).

There is also an all-direction comparison. If \(\Sigma_{\partial}\) and \(\Sigma_{\mathrm{vol}}\) are the covariance matrices of \(Y\) and \(X\), then
\[
\Sigma_{\partial}\succ\frac{d+2}{d+1}\Sigma_{\mathrm{vol}},
\]
where \(\succ\) means positive-definite difference. The coefficient is optimal simultaneously in every dimension: along any fixed long-axis direction in the above flattening family, the corresponding variance ratio tends to \((d+2)/(d+1)\).

## Assumptions and scope
A full-dimensional ellipsoid is an invertible affine image of the closed Euclidean unit ball. Volume measure means normalized \(d\)-dimensional Lebesgue measure; boundary measure means normalized Euclidean \((d-1)\)-dimensional Hausdorff measure, *not* the pushforward of uniform spherical measure under the affine map. Both pairs consist of independent copies of their respective distributions. The squared Euclidean distance is used, not the unsquared distance or higher powers. The statements are invariant under translation and scaling. No smoothness assumption beyond the ellipsoid parametrization is needed.

## Proof
**1. Reduction and area Jacobian.** Translation and orthogonal coordinate changes do not change distances or covariance eigenvalue comparisons. By singular-value decomposition it suffices to take \(A=\operatorname{diag}(a_1,\ldots,a_d)\), with \(a_i>0\), and \(c=0\). Write \(U\) for a uniformly distributed point on the unit sphere \(S^{d-1}\). Under the boundary parametrization \(u\mapsto Au\), the surface-area Jacobian is
\[
|\det A|\,h(u),\qquad h(u)=\|A^{-1}u\|.
\]
Consequently, for any bounded measurable \(f\),
\[
\mathbb Ef(Y)=\frac{\mathbb E_U[f(AU)h(U)]}{\mathbb E_Uh(U)}.
\]
Both the interior and boundary means equal zero by central symmetry. Since a volume-uniform ball has covariance \(I/(d+2)\),
\[
\Sigma_{\mathrm{vol}}=\frac{A^2}{d+2}.
\]

**2. Exact surface covariance representation.** Let \(G\) be a standard Gaussian in \(\mathbb R^d\), independent of \(U\), and put \(Z=A^{-1}G\). The identity \(\mathbb E|N(0,\sigma^2)|=\sqrt{2/\pi}\,\sigma\) gives
\[
h(u)=\sqrt{\frac\pi2}\,\mathbb E_G|Z\cdot u|.
\]
For every fixed nonzero \(z\in\mathbb R^d\), rotational symmetry and the elementary spherical beta integral give
\[
\frac{\mathbb E_U[UU^{\mathsf T}|z\cdot U|]}{\mathbb E_U|z\cdot U|}
=\frac{I+\widehat z\widehat z^{\mathsf T}}{d+1},
\qquad \widehat z=\frac z{\|z\|}.
\]
Indeed, in the direction \(\widehat z\), the weighted coordinate second moment is \(\mathbb E|U_1|^3/\mathbb E|U_1|=2/(d+1)\); each of the other \(d-1\) coordinates has weighted second moment \(1/(d+1)\). Tonelli's theorem and the two identities yield
\[
\Sigma_{\partial}=\frac{A(I+Q)A}{d+1},\qquad
Q=\frac{\mathbb E[ZZ^{\mathsf T}/\|Z\|]}{\mathbb E\|Z\|}.
\]
The matrix \(Q\) is positive definite: for nonzero \(v\), \(\mathbb E[(v\cdot Z)^2/\|Z\|]>0\). Also \(\operatorname{tr}Q=1\). The off-diagonal entries vanish by coordinate sign symmetry; let \(q_i=Q_{ii}\in(0,1)\), with \(\sum_iq_i=1\). It follows immediately that
\[
\Sigma_{\partial}-\frac{d+2}{d+1}\Sigma_{\mathrm{vol}}
=\frac{AQA}{d+1}\succ0.
\]

**3. Opposite sorting of axis length and Gaussian weights.** Put \(b_i=a_i^{-1}\), \(t_i=\log b_i\), and define
\[
\Phi(t_1,\ldots,t_d)=\log\mathbb E_G\left(\sum_{i=1}^d e^{2t_i}G_i^2\right)^{1/2}.
\]
For almost every fixed Gaussian vector, the logarithm of the integrand is a log-sum-exp function divided by two and is convex; it is strictly convex in every direction not parallel to \((1,\ldots,1)\). Applying Hölder to the pointwise log-convexity shows that \(\Phi\) is symmetric and convex, strictly convex along every such direction. Differentiation under the expectation (dominated locally by a constant times \(\|G\|\)) shows
\[
\frac{\partial\Phi}{\partial t_i}
=\frac{\mathbb E[b_i^2G_i^2/\|Z\|]}{\mathbb E\|Z\|}=q_i.
\]
Interchanging two coordinates in the gradient monotonicity inequality for a symmetric differentiable convex function gives
\[
(t_i-t_j)(q_i-q_j)\ge0,
\]
strictly when \(t_i\ne t_j\). Thus the \(q_i\) are sorted *oppositely* to the squared semiaxis lengths \(a_i^2\). The reverse Chebyshev sum inequality therefore gives
\[
\sum_{i=1}^d a_i^2q_i\le\frac1d\sum_{i=1}^d a_i^2,
\]
with equality exactly when all \(a_i\) are equal. One can also see this directly from
\[
\sum_i a_i^2q_i-\frac1d\sum_i a_i^2
=\frac1d\sum_{i<j}(a_i^2-a_j^2)(q_i-q_j)\le0.
\]

**4. Ratio and equality.** For any random vector \(W\) and an independent copy \(W'\), \(\mathbb E\|W-W'\|^2=2\operatorname{tr}(\operatorname{Cov}W)\). Hence the exact ratio is
\[
\mathcal R(E)=\frac{d+2}{d+1}\left(1+\frac{\sum_i a_i^2q_i}{\sum_i a_i^2}\right).
\]
Because every \(q_i>0\), the lower inequality is strict. The preceding reverse Chebyshev estimate proves the upper inequality, with equality precisely for all equal axes (a ball). At a ball \(q_i=1/d\), so the upper constant is attained.

**5. Sharp lower limit.** Take \(a_1=\varepsilon\) and \(a_i=1\) for \(i\ge2\). Then \(Z=(G_1/\varepsilon,G_2,\ldots,G_d)\), so \(\mathbb E\|Z\|\ge\mathbb E|G_1|/\varepsilon\). For \(i\ge2\),
\[
0<q_i\le\frac{\mathbb E|G_i|}{\mathbb E|G_1|/\varepsilon}=\varepsilon.
\]
Thus \(q_1\to1\), \(\sum_i a_i^2q_i=\varepsilon^2q_1+\sum_{i=2}^dq_i\to0\), whereas \(\sum_i a_i^2\to d-1\). This proves sharpness of the lower ratio. It also shows that in each fixed noncollapsed coordinate direction \(i\ge2\) the covariance ratio \((d+2)(1+q_i)/(d+1)\) tends to the claimed sharp Loewner constant. \(\square\)

## Verification
The standalone `verify.py` computes the surface second moments from deterministic angular quadrature using the exact surface Jacobian, and independently computes the same moments through the Gaussian directional mixture for \(Q\). It checks eight representative nondegenerate ellipsoids in dimensions two and three, including strongly anisotropic cases. The script additionally checks 99 exact spherical angular normalizations in dimensions \(2\) through \(100\), 48 exact ball-equality identities, and 48 strict gap comparisons of the constants. Reproduce using `python verify.py` with Python 3 and NumPy. No finite experiment is used to justify a universal quantifier; the all-dimensional proof is analytic.

## Relationship to prior work
Lotnikov (2026, arXiv:2608.14848, first public posting 2026-08-14) studies the Zaporozhets–Tarasov comparisons of interior and boundary point distances. Its results include planar centrally symmetric bodies and higher-dimensional centrally symmetric counterexamples, but the inspected results do not state the exact surface covariance formula or the sharp all-dimensional ellipsoid squared-distance ratio. Tokmachev (2026, arXiv:2607.08869) proves convex-order domination in the planar matching-centroid case and a class of circumscribed polytopes: these hypotheses do not imply the stated \(d\ge3\) ellipsoid theorem, and they do not determine the sharp ratio or equality cases even for ellipses. An earlier result titled *Exact second-moment boundary gap for arbitrary Euclidean triangles* concerns triangles, not ellipsoids. Rivin (2003, arXiv:math/0306085) estimates ellipsoid surface area and integral mean curvatures; Poelaert–Schniewind–Janssens (2011, arXiv:1104.5145) derive ellipsoid surface Jacobians and curvature. Their inspected material supplies context rather than the covariance and sharp distance-ratio classification. Eriksen (2021) studies rank-two Minkowski *surface-area tensors on outward normals*, a different tensor from the Euclidean-position covariance of uniformly sampled boundary points. Classical spherical beta integrals, area Jacobians and convexity arguments are used as mathematical ingredients, not claimed as new results.

## Limitations
The inequality is about **squared** Euclidean distances and Euclidean **surface-area** boundary sampling for full-dimensional ellipsoids, not general convex bodies, non-Euclidean norms, or arbitrary moments. It gives a sharp scalar ratio and a sharp Loewner lower comparison, not a complete convex-order statement. The lower bound is approached only in a degenerating family and is not attained by any full-dimensional ellipsoid. Historical priority is provisional: despite searches and direct inspection of accessible relevant texts, unlocated equivalent formulas or alternate covariance formulations may exist. One plausible 2026 convex-order preprint was accessible in abstract but its full text was not available during the comparison; its stated hypotheses do not dominate the all-dimensional claim. Independent validation has not been performed.

## References
1. A. S. Lotnikov, *Mean distance between points inside and on the boundary of a convex body*, arXiv:2608.14848 (2026), first submitted 2026-08-14, https://arxiv.org/abs/2608.14848.
2. A. S. Tokmachev, *Inequalities for convex functions of random points inside and on the boundary of convex bodies*, arXiv:2607.08869 (2026), first submitted 2026-07-09, https://arxiv.org/abs/2607.08869.
3. I. Rivin, *Simple estimates for ellipsoid measures*, arXiv:math/0306085 (2003), https://arxiv.org/abs/math/0306085.
4. D. Poelaert, J. Schniewind and F. Janssens, *Surface Area and Curvature of the general Ellipsoid*, arXiv:1104.5145 (2011), https://arxiv.org/abs/1104.5145.
5. *Exact second-moment boundary gap for arbitrary Euclidean triangles*, published mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-second-moment-boundary-gap-for-arbitrary-euclidean-triangl--d886b40f95a8.
6. G. Bonnet, A. Gusakova, C. Thäle and D. Zaporozhets, *Sharp inequalities for the mean distance of random points in convex bodies*, Advances in Mathematics 386 (2021), article 107813, https://doi.org/10.1016/j.aim.2021.107813.
7. R. Eriksen, *Contributions to Integral and Stochastic Geometry: Selected uniqueness problems for integral formulae and Minkowski tensors*, PhD dissertation, Aarhus University (2021), https://data.math.au.dk/publications/phd/2021/math-phd-2021-re.pdf.
